ans = []
num = [-1, 0, 1, 2, -1, -4]
num.sort()  # [-4, -1, -1, 0, 1, 2]

for k in range(len(num) - 2):
    # 1. Skip duplicate outer values (k)
    if k > 0 and num[k] == num[k - 1]:
        continue

    # 2. Only search elements AFTER index k
    i = k + 1
    j = len(num) - 1
    target = 0 - num[k]

    while i < j:
        x = num[i] + num[j]

        if x == target:
            ans.append([num[k], num[i], num[j]])

            # 3. Skip duplicate left values (i)
            while i < j and num[i] == num[i + 1]:
                i += 1
            # 4. Skip duplicate right values (j)
            while i < j and num[j] == num[j - 1]:
                j -= 1

            i += 1
            j -= 1
        elif x > target:
            j -= 1
        else:
            i += 1

print("ans:", ans)