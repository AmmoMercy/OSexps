import copy
import sys


def main():
    trackOrder = [55, 58, 39, 18, 90, 160, 150, 38, 184]
    currentTrack = 100
    # True for outer and False for inner
    direction = True
    FCFS(copy.deepcopy(trackOrder), copy.deepcopy(currentTrack))
    SSTF(copy.deepcopy(trackOrder), copy.deepcopy(currentTrack))
    Scan(copy.deepcopy(trackOrder), copy.deepcopy(currentTrack), direction)
    CScan(copy.deepcopy(trackOrder), copy.deepcopy(currentTrack),direction)


def FCFS(trackOrder, currentTrack):
    currentMoveDistance = 0
    totalMoveDistance=0
    for i in range(len(trackOrder)):
        currentMoveDistance = abs(currentTrack - trackOrder[i])
        totalMoveDistance+=currentMoveDistance
        currentTrack = trackOrder[i]
        print(currentTrack, currentMoveDistance)
    print("FCFS",totalMoveDistance/len(trackOrder),end="\n\n")
    return currentTrack


def SSTF(trackOrder, currentTrack):
    lenth=len(trackOrder)
    TotalMoveDistance = 0
    while (len(trackOrder) != 0):
        recentTrackIndex = findRecentTrack(trackOrder, currentTrack)
        print(trackOrder[recentTrackIndex], end=" ")
        distance = abs(trackOrder[recentTrackIndex] - currentTrack)
        TotalMoveDistance+=distance
        print(distance)
        currentTrack = trackOrder[recentTrackIndex]
        del trackOrder[recentTrackIndex]
    print("SSTF",TotalMoveDistance/lenth,end="\n\n")


def findRecentTrack(trackOrder, currentTrack):
    recentDistance = sys.maxsize
    recentTrackIndex = -1
    for i in range(len(trackOrder)):
        if (abs(currentTrack - trackOrder[i]) < recentDistance):
            recentDistance = abs(currentTrack - trackOrder[i])
            recentTrackIndex = i
    return recentTrackIndex


def Scan(trackOrder, currentTrack, direction):
    trackOrder.sort()
    totalMoveDistance=0
    trackPieceOne = []
    trackPieceTwo = []
    if direction == True:
        nextIndex = GoOuter(trackOrder, currentTrack)
        for i in range(len(trackOrder)):
            if i < nextIndex:
                trackPieceOne.append(trackOrder[i])
            else:
                trackPieceTwo.append(trackOrder[i])
        trackPieceOne.reverse()
    else:
        nextIndex = GoInner(trackOrder, currentTrack)
        for i in range(len(trackOrder)):
            if i < nextIndex:
                trackPieceOne.append(trackOrder[i])
            else:
                trackPieceTwo.append(trackOrder[i])
        trackPieceOne.reverse()
    print("SCAN",Serve(trackPieceTwo+trackPieceOne,currentTrack)/len(trackOrder),end="\n\n")

def GoOuter(trackOrder, currentTrack):
    if currentTrack > max(trackOrder):
        return -1
    recentOuterTrack = min((track for track in trackOrder if track > currentTrack), key=lambda x: abs(x - currentTrack))
    return trackOrder.index(recentOuterTrack)


def GoInner(trackOrder, currentTrack):
    if currentTrack < min(trackOrder):
        return -1
    recentInnerTrack = min((track for track in trackOrder if track < currentTrack), key=lambda x: abs(x - currentTrack))
    return trackOrder.index(recentInnerTrack)


def CScan(trackOrder, currentTrack, direction):
    trackOrder.sort()
    trackPieceOne = []
    trackPieceTwo = []
    if direction == True:
        nextIndex = GoOuter(trackOrder, currentTrack)
        for i in range(len(trackOrder)):
            if i < nextIndex:
                trackPieceOne.append(trackOrder[i])
            else:
                trackPieceTwo.append(trackOrder[i])
    else:
        nextIndex = GoInner(trackOrder, currentTrack)
        for i in range(len(trackOrder)):
            if i < nextIndex:
                trackPieceOne.append(trackOrder[i])
            else:
                trackPieceTwo.append(trackOrder[i])
    print("SCAN", Serve(trackPieceTwo + trackPieceOne, currentTrack) / len(trackOrder),end="\n\n")


def Serve(trackOrder, currentTrack):
    currentMoveDistance = 0
    totalMoveDistance=0
    for i in range(len(trackOrder)):
        currentMoveDistance = abs(currentTrack - trackOrder[i])
        totalMoveDistance+=currentMoveDistance
        currentTrack = trackOrder[i]
        print(currentTrack, currentMoveDistance)
    return totalMoveDistance
if __name__ == '__main__':
    main()
