count = 0
max_num = 1000
for i in range(max_num):
    if i < 2:
        continue
    limit = int(i / 2) + 1
    for j in range(2, limit):
        if i % j == 0:
            break
    else:
        count += 1
        if (count == 29):
            print(count, ":", i)
            break
