from queue import Queue
import copy


def main():
    while True:
        print("==========================时间片轮转调度==========================")
        # jobs = [{"name": "A", "arrivalTime": 0, "serviceTime": 4},
        #         {"name": "B", "arrivalTime": 1, "serviceTime": 3},
        #         {"name": "C", "arrivalTime": 2, "serviceTime": 5},
        #         {"name": "D", "arrivalTime": 3, "serviceTime": 2},
        #         {"name": "E", "arrivalTime": 4, "serviceTime": 4}, ]
        jobs = [{} for i in range(int(input("请输入任务数量:\n")))]
        nameArr = [i for i in input("请输入任务名称:\n").split()]
        arrivalTimeArr = [int(i) for i in input("请输入到达时间:\n").split()]
        serviceTimeArr = [int(i) for i in input("请输入服务时间:\n").split()]
        for i in range(len(nameArr)):
            jobs[i]["name"] = nameArr[i]
            jobs[i]["arrivalTime"] = arrivalTimeArr[i]
            jobs[i]["serviceTime"] = serviceTimeArr[i]
        q = int(input("请输入时间片大小:\n"))
        RR(jobs, q)


def RR(_job, q):
    jobs = copy.deepcopy(_job)
    currentTime = 0
    jobQueue = Queue()
    currentJob = {}
    round = 0
    while (True):

        for job in jobs:
            if job["arrivalTime"] == currentTime:
                jobQueue.put(job)
                break

        if round == 0:
            if currentJob != {}:
                jobQueue.put(currentJob)
            currentJob = jobQueue.get()

        currentJob["serviceTime"] -= 1
        currentTime += 1
        round += 1

        if (currentJob["serviceTime"] == 0):
            round = 0
            for oldjob in _job:
                if oldjob["name"] == currentJob["name"]:
                    oldjob["finishTime"] = currentTime
                    break
            currentJob = {}

        if round == q:
            round = 0

        if jobQueue.empty() and currentJob == {}:
            break
    sumOfWholeTime = 0
    sumOfWeightWholeTime = 0
    for job in _job:
        job["wholeTime"] = job["finishTime"] - job["arrivalTime"]
        sumOfWholeTime += job["wholeTime"]
        job["weightWholeTime"] = job["wholeTime"] / job["serviceTime"]
        sumOfWeightWholeTime += job["weightWholeTime"]
        print(job)
    print("平均周转时间", sumOfWholeTime / len(_job))
    print("平均带权周转时间", sumOfWeightWholeTime / len(_job))


if __name__ == '__main__':
    main()
