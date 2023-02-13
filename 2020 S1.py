value = input()

measurement = []
distances = []
for a in range(int(value)):
    measurement.append(input().split())
    measurement[-1][0] = int(measurement[-1][0])
    measurement[-1][1] = int(measurement[-1][1])
    distances.append([measurement[-1][0]])
    distances.sort()

for a in range(len(distances)):
    for b in measurement:
        if distances[a][0] == b[0]:
            distances[a].append(b[1])
            break

highest_speed = 0
for c in range(len(distances)-1):
    if (abs(distances[c+1][1]-distances[c][1])/(distances[c+1][0]-distances[c][0])) > highest_speed:
        highest_speed = abs(distances[c+1][1]-distances[c][1])/abs(distances[c+1][0]-distances[c][0])

print(highest_speed)