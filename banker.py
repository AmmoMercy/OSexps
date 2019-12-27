import copy


def main():
    while True:
        print("==========================银行家算法==========================")
        max = [
            [7, 5, 3],
            [3, 2, 2],
            [9, 0, 2],
            [2, 2, 2],
            [4, 3, 3]
        ]
        alloc = [
            [0, 1, 0],
            [2, 0, 0],
            [3, 0, 2],
            [2, 1, 1],
            [0, 0, 2]
        ]
        need = [
            [7, 4, 3],
            [1, 2, 2],
            [6, 0, 0],
            [0, 1, 1],
            [4, 3, 1]
        ]
        available = [3, 3, 2]
        requestList = [3, 3, 0]
        input("请按回车开始")
        print("    Max    Allocaton  Need" )
        for i in range(len(max)):
            print(max[i],alloc[i],need[i])

        banker(copy.copy(max), copy.copy(alloc), copy.copy(need), copy.copy(available))
        request(0, requestList, alloc, need, available)
        banker(copy.copy(max), copy.copy(alloc), copy.copy(need), copy.copy(available))


def request(pid, requestList, alloc, need, available):
    print("在pid=", pid, "的进程发出", requestList, "请求后，", end="")
    for i in range(len(alloc[pid])):
        alloc[pid][i] += requestList[i]
        need[pid][i] -  = requestList[i]
        available[i] -= requestList[i]


def banker(max, alloc, need, available):
    finished = []
    while (True):
        safe = True
        for i in range(len(max)):
            if i not in finished and isEnough(need[i], available):
                available = releaseSource(alloc[i], available)
                finished.append(i)
                break
            else:
                if i == len(max) - 1:
                    safe = False
        if (safe == False):
            print("不安全！\n")
            break
        if (len(finished) == len(max)):
            print("安全序列:", end="")
            print(finished)
            break


def isEnough(needVector, availableVector):
    for a, b in zip(needVector, availableVector):
        if b < a:
            return False
    return True


def releaseSource(alloc, available):
    for i in range(len(alloc)):
        available[i] += alloc[i]
    return available


if __name__ == '__main__':
    main()
