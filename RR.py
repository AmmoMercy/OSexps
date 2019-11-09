from queue import Queue
import copy


def main():
    jobs = [{"name": "A", "arrivalTime": 0, "serviceTime": 4},
            {"name": "B", "arrivalTime": 1, "serviceTime": 3},
            {"name": "C", "arrivalTime": 2, "serviceTime": 5},
            {"name": "D", "arrivalTime": 3, "serviceTime": 2},
            {"name": "E", "arrivalTime": 4, "serviceTime": 4}, ]
    RR(jobs, 1)
    RR(jobs, 4)


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

        print(jobQueue)
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
