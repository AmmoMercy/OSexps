import sys
import copy


def main():
    pageNum = 3
    pageOrder = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    Optimal(copy.deepcopy(pageNum), copy.deepcopy(pageOrder))
    FIFO(copy.deepcopy(pageNum), copy.deepcopy(pageOrder))
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
