for _ in range(int(input())):
    n, k = map(int, input().split()) # number of buyers, books available to sell
    arr1 = list(map(int, input().split())) # max no. of books that can be bought respectively
    arr2 = list(map(int, input().split())) # money offered to buy arr1[i] books
    arrr = [arr2[i] / arr1[i] for i in range(n)] # cost of 1 book offered
    arr = list(zip(arrr, arr2, arr1)) # nested list
    arr.sort(reverse=True) # sorting in descending order giving priority to "cost of 1 book" then "money offered" and priority of arr1 doesn't matter
    sum = 0
    number = 0
    for j in range(n):
        if number + arr[j][2] <= k: # conditional check
            sum += arr[j][1]
            number += arr[j][2]
        else:
            sum += arr[j][0] * (k - number) # adding the cost of "incomplete" books that can be sold
            break
    print(int(sum))