length = int(input())
tides = input().split()
for tide in range(len(tides)):
    tides[tide] = int(tides[tide])
tides.sort()

middle = int(length/2)
low_tide = tides[:middle]
high_tide = tides[middle:]
low_tide.sort(reverse=True)

low_value = True
current_val = low_tide[0]
counter = 0
print(low_tide[counter], end=" ")
while True:
    if low_value:
        low_value = False
        print(high_tide[counter], end=" ")
        counter += 1
        current_val = low_tide[counter]
    else:
        low_value = True
        print(low_tide[counter], end=" ")
        current_val = high_tide[counter]
    if current_val == tides[-1]:
        print(current_val, end=" ")
        break