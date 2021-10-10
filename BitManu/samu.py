t = int(input())

for test in range(t):
    n, k = map(int, input().split())
    selectedDishes = []
    for _ in range(n):
        dish = input()
        selectedDishes.append(dish)
    selectedDishes = list(map(lambda x: int(x, 2), selectedDishes))
    result = k
    for i in range(1, 2 ** k):
        suitableString = True
        for j in range(n):
            if selectedDishes[j] & i == 0:
                suitableString = False
        
        if suitableString:
            # count 1 of i
            temp = i
            count = 0
            while temp:
                if temp % 2 == 1:
                    count += 1
                temp = temp >> 1
            result = min(result, count)
    
    print(result)