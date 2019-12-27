def main():
    while (True):
        choose = input("选择算法\n1-FCFS\n2-SJF\n")
        if choose == "1" or choose == "2":
            break
        else:
            print("重新输入")
    # arrivalTimeStr = input("请输入到达时间数组\n")
    # arrivalTime = [0, 1, 2, 3, 4]
    arrivalTime = [int(n) for n in input("请输入到达时间数组:\n").split()]
    serviceTimeStr = input("请输入服务时间数组:\n")
    serviceTime = [int(n) for n in serviceTimeStr.split()]
    # serviceTime = [4, 3, 5, 2, 4]
    if choose == '1':
        FCFS(arrivalTime, serviceTime)
    elif choose == '2':
        SJF(arrivalTime, serviceTime)


def FCFS(arrivalTime, serviceTime):
    currentTime = 0
    exitTime = []
    wholeTime = []
    weightWholeTime = []
    for jobID in range(len(arrivalTime)):
        if (arrivalTime[jobID] <= currentTime):
            currentTime += serviceTime[jobID]
            exitTime.append(currentTime)
            wholeTime.append(currentTime - arrivalTime[jobID])
            weightWholeTime.append(wholeTime[jobID] / serviceTime[jobID])
        else:
            print("waitforjobs")
            currentTime += 1
    sumWholeTime = 0
    sumWeightWholeTime = 0
    for i in wholeTime:
        sumWholeTime += i
    for i in weightWholeTime:
        sumWeightWholeTime += i
    print("结束时间:", exitTime)
    print("周转时间:", wholeTime)
    print("带权周转时间:", weightWholeTime)
    print("平均周转时间:", sumWholeTime / len(arrivalTime))
    print("平均带权周转时间:", sumWeightWholeTime / len(arrivalTime))


def SJF(arrivalTime, serviceTime):
    currentTime = 0
    exitTime = []
    wholeTime = [0 for _ in arrivalTime]
    weightWholeTime = [0 for _ in arrivalTime]
    status = [False for _ in arrivalTime]
    while (True):
        jobID = shortJobID(status, arrivalTime, serviceTime, currentTime)
        if jobID == -1: break
        currentTime += serviceTime[jobID]
        exitTime.append(currentTime)
        wholeTime[jobID] = currentTime - arrivalTime[jobID]
        weightWholeTime[jobID] = wholeTime[jobID] / serviceTime[jobID]
        status[jobID] = True
    sumWholeTime = 0
    sumWeightWholeTime = 0
    for i in wholeTime:
        sumWholeTime += i
    for i in weightWholeTime:
        sumWeightWholeTime += i

    print("结束时间:", exitTime)
    print("周转时间:", wholeTime)
    print("带权周转时间:", weightWholeTime)
    print("平均周转时间:", sumWholeTime / len(arrivalTime))
    print("平均带权周转时间:", sumWeightWholeTime / len(arrivalTime))


def shortJobID(status, arrivalTime, serviceTime, currentTime):
    flag = False
    jobID = 0
    shortTime = 65535
    for i in range(len(serviceTime)):
        if serviceTime[i] < shortTime and arrivalTime[i] <= currentTime and status[i] == False:
            jobID = i
            shortTime = serviceTime[i]
            flag = True
    if flag == True:
        return jobID
    else:
        return -1


if __name__ == '__main__':
    main()
