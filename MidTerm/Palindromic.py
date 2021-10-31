dic = {
    '0': 'a',
    '1': 'b',
    '2': 'c',
    '3': 'd',
    '4': 'e',
    '5': 'f',
    '6': 'g',
    '7': 'h',
    '8': 'i',
    '9': 'j',
}
def par(b):
    i = 0
    j = len(b) - 1
    while i <= j:
        if b[i] != b[j]:
            return 'NO'
            break
        else:
            i += 1
            j -= 1
    return 'YES'
t = int(input())
for _ in range(t):
    n = input()
    string = ''
    sum = 0
    for i in n:
        string += dic[i]
        sum += int(i)
    # print(sum)
    # print(string)
    b = ''
    for i in range(1,sum+1):
        j = i % len(string)
        b += string[j -1]
    # print(b)
    print(par(b))
