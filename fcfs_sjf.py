def main():
    arrivalTime = [0, 1, 2, 3, 4]
    serviceTime = [4, 3, 5, 2, 4]
    FCFS(arrivalTime, serviceTime)
    SJF(arrivalTime, serviceTime)
    print()


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
    print("FCFS")
    sumWholeTime = 0
    sumWeightWholeTime = 0
    for i in wholeTime:
        sumWholeTime += i
    for i in weightWholeTime:
        sumWeightWholeTime += i

    print("sjf")
    print("FINISH TIMES ", exitTime)
    print("WHOLE TIMES ", wholeTime)
    print("WEIGHT WHOLE TIMES", weightWholeTime)
    print("AVG WHOLE TIME", sumWholeTime / len(arrivalTime))
    print("AVG WEIGHT WHOLE TIME", sumWeightWholeTime / len(arrivalTime))

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

    print("SJF")
    print("FINISH TIMES ", exitTime)
    print("WHOLE TIMES ", wholeTime)
    print("WEIGHT WHOLE TIMES", weightWholeTime)
    print("AVG WHOLE TIME", sumWholeTime / len(arrivalTime))
    print("AVG WEIGHT WHOLE TIME", sumWeightWholeTime / len(arrivalTime))


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
