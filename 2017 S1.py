length = int(input())
swiftRuns = input().split()
semaphoresRuns = input().split()

swiftsum = 0
semaphoresum = 0
K = 0
day = 1

for item in range(length):
    swiftsum += int(swiftRuns[item])
    semaphoresum += int(semaphoresRuns[item])

    if swiftsum == semaphoresum:
        K = day
    day += 1
print(K)