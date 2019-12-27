import sys
import copy


def main():
    while(True):
        print("==========================虚拟内存调度==========================")
        choose = int(input("请选择调页算法:\n1-FIFO \n2-OPI\n3-LRU\n"))
        pageNum = int(input("请输入页面个数:\n"))
        #pageOrder = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
        pageOrder = [int(i) for i in input("请输入页面序号序列:\n").split()]
        if choose==1:
            FIFO(copy.deepcopy(pageNum), copy.deepcopy(pageOrder))
        elif choose==2:
            Optimal(copy.deepcopy(pageNum), copy.deepcopy(pageOrder))
        elif choose==3:
            LRU(copy.deepcopy(pageNum), copy.deepcopy(pageOrder))


def Optimal(pageNum, pageOrder):
    VM = [-1 for i in range(pageNum)]
    lackPageTime = 0
    for i in range(len(pageOrder)):
        if pageOrder[i] not in VM:
            lackPageTime += 1
            if -1 in VM:
                VM[VM.index(-1)] = pageOrder[i]
            else:
                VM[findOptimal(VM, pageOrder, i)] = pageOrder[i]
            print(pageOrder[i], VM)
        else:
            print(pageOrder[i], " ")
    print("OPI缺页次数:", lackPageTime," 缺页率:",lackPageTime/len(pageOrder)*100,"%\n")


def findOptimal(VM, pageOrder, index):
    nextUseTime = []
    for page in VM:
        temp = index
        while (True):
            temp += 1
            if temp == len(pageOrder):
                nextUseTime.append(sys.maxsize)
                break
            if (pageOrder[temp] == page):
                nextUseTime.append(temp - index)
                break

    return nextUseTime.index(max(nextUseTime))


def FIFO(pageNum, pageOrder):
    VM = [-1 for i in range(pageNum)]
    lackPageTime = 0
    loadTime = [-1 for i in range(pageNum)]
    for i in range(len(pageOrder)):
        if pageOrder[i] not in VM:
            lackPageTime += 1
            if -1 in VM:
                addr = VM.index(-1)
                VM[addr] = pageOrder[i]
                loadTime[addr] = i
            else:
                addr = findOld(loadTime)
                VM[addr] = pageOrder[i]
                loadTime[addr] = i
            print(pageOrder[i], VM)

        else:
            print(pageOrder[i], " ")
    print("FIFO缺页次数:", lackPageTime," 缺页率:",lackPageTime/len(pageOrder)*100,"%\n")


def findOld(loadTime):
    return loadTime.index(min(loadTime))


def LRU(pageNum, pageOrder):
    VM = [-1 for i in range(pageNum)]
    lackPageTime = 0
    lastAccess = [-1 for i in range(pageNum)]
    for i in range(len(pageOrder)):
        if pageOrder[i] not in VM:
            lackPageTime += 1
            if -1 in VM:
                addr = VM.index(-1)
                VM[addr] = pageOrder[i]
                lastAccess[addr] = i
            else:
                addr = findRecentlyUse(lastAccess)
                VM[addr] = pageOrder[i]
                lastAccess[addr] = i
            print(pageOrder[i], VM)

        else:
            lastAccess[VM.index(pageOrder[i])]=i
            print(pageOrder[i], " ")
    print("LRU缺页次数:", lackPageTime," 缺页率:",lackPageTime/len(pageOrder)*100,"%\n")
def findRecentlyUse(lastAccess):
    return lastAccess.index(min(lastAccess))

if __name__ == '__main__':
    main()
