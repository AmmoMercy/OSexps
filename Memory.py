import copy
def main():
    while (True):
        print("==========================动态分区==========================")
        choose = int(input("选择算法\n1-首次适应\n2-循环首次适应\n3-最佳适应\n4-最坏适应\n"))
        # memory = [16, 16, 8, 32, 64, 32, 8, 16, 64]
        # processNeed = [7, 18, 9, 20, 35, 8, ]
        memory = [int(i) for i in input("请输入内存空间\n").split()]
        processNeed = [int(i) for i in input("请输入进程需求\n").split()]
        print("分区情况如下\n")
        if choose == 1:
            firstPartion(copy.copy(memory), processNeed)
        elif choose == 2:
            cycleFirstPartion(copy.copy(memory), processNeed)
        elif choose == 3:
            bestPartition(copy.copy(memory), processNeed)
        elif choose == 4:
            worstPartition(copy.copy(memory), processNeed)


def firstPartion(memory, processNeed):
    for pid in range(len(processNeed)):
        for addr in range(len(memory)):
            if isinstance(memory[addr], int) and memory[addr] > processNeed[pid]:
                if addr != len(memory) - 1:
                    memory.insert(addr + 1, memory[addr] - processNeed[pid])
                else:
                    memory.append(memory[addr] - processNeed[pid])
                memory[addr] = chr(65 + pid)
                break
            elif isinstance(memory[addr], int) and memory[addr] == processNeed[pid]:
                memory[addr] = chr(65 + pid)
                break

    print(memory)


def cycleFirstPartion(memory, processNeed):
    pid = 0
    while (True):
        addr = 0
        while (addr != len(memory)):
            if isinstance(memory[addr], int) and memory[addr] > processNeed[pid]:
                if addr != len(memory) - 1:
                    memory.insert(addr + 1, memory[addr] - processNeed[pid])
                else:
                    memory.append(memory[addr] - processNeed[pid])
                memory[addr] = chr(65 + pid)
                addr += 1
                pid += 1
                if pid == len(processNeed): break
            elif isinstance(memory[addr], int) and memory[addr] == processNeed[pid]:
                memory[addr] = chr(65 + pid)
                pid += 1
                if pid == len(processNeed): break
            addr += 1
        if (pid == len(processNeed)): break
    print(memory)


def bestPartition(memory, processNeed):
    for pid in range(len(processNeed)):
        bestIndex = -1
        bestSize = float("inf")
        for addr in range(len(memory)):
            if isinstance(memory[addr], int) and memory[addr] >= processNeed[pid] and memory[addr] < bestSize:
                bestIndex = addr
                bestSize = memory[addr]
        if bestIndex != -1:
            if memory[bestIndex] > processNeed[pid]:
                if bestIndex != len(memory) - 1:
                    memory.insert(bestIndex + 1, memory[bestIndex] - processNeed[pid])
                else:
                    memory.append(memory[bestIndex] - processNeed[pid])
                memory[bestIndex] = chr(65 + pid)
                if pid != len(processNeed) - 1:
                    pid += 1
                else:
                    break

            elif memory[bestIndex] == processNeed[pid]:
                memory[bestIndex] = chr(65 + pid)
                if pid != len(processNeed) - 1:
                    pid += 1
                else:
                    break
        else:
            print("内存不足")
    print(memory)


def worstPartition(memory, processNeed):
    for pid in range(len(processNeed)):
        worstIndex = -1
        worstSize = 0
        for addr in range(len(memory)):
            if isinstance(memory[addr], int) and memory[addr] >= processNeed[pid] and memory[addr] > worstSize:
                worstIndex = addr
                worstSize = memory[addr]
        if worstIndex != -1:
            if memory[worstIndex] > processNeed[pid]:
                if worstIndex != len(memory) - 1:
                    memory.insert(worstIndex + 1, memory[worstIndex] - processNeed[pid])
                else:
                    memory.append(memory[worstIndex] - processNeed[pid])
                memory[worstIndex] = chr(65 + pid)
                if pid != len(processNeed) - 1:
                    pid += 1
                else:
                    break

            elif memory[worstIndex] == processNeed[pid]:
                memory[worstIndex] = chr(65 + pid)
                if pid != len(processNeed) - 1:
                    pid += 1
                else:
                    break
        else:
            print("内存不足")
    print(memory)


if __name__ == '__main__':
    main()
