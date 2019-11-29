n = int(input("Enter n: "))
k = []

k = input("Enter list: ")

if (len(k) + 1) / 2 == n * n:
    k = k.split()
    lst = []
    t = 0
    for i in range(0,n):
        lst.append(k[t:t+n])
        t += n
    print(lst)
    ss = 0
    for i in range(n):
        for j in range(0,n):
            if lst[i][j] != lst[j][i]:
                i = 0
            else:
                ss += 1
    if ss == n * n:
        print("Yes")
    else :
        print("No")

else:
    print ("Error")

