import queue

class Train:
    def __init__(self, start, end, side):
        self.start = start
        self.end = end
        self.side = side

t = int(input())
for _ in range(1, t+1):
    n = int(input())

    na, nb = map(int, input().split())
    tripList = []

    pqa = queue.PriorityQueue()
    pqb = queue.PriorityQueue()
    # print(pqb.queue[0])

    for i in range(na):
        start, end = input().split()
        hourS, minuteS = map(int, start.split(':'))
        convertS = hourS * 60 + minuteS
        hourE, minuteE = map(int, end.split(':'))
        convertE = hourE * 60 + minuteE
        tripList.append(Train(convertS, convertE, 0))
    for i in range(nb):
        start, end = input().split()
        hourS, minuteS = map(int, start.split(':'))
        convertS = hourS * 60 + minuteS
        hourE, minuteE = map(int, end.split(':'))
        convertE = hourE * 60 + minuteE
        tripList.append(Train(convertS, convertE, 1))

    tripList.sort(key=lambda trip: trip.start)

    countA = 0
    countB = 0

    for trip in tripList:
        if trip.side == 0:
            if not pqa.empty() and pqa.queue[0] <= trip.start:
                pqa.get()
            else:
                countA += 1
            pqb.put(trip.end + n)
        else:
            if not pqb.empty() and pqb.queue[0] <= trip.start:
                pqb.get()
            else:
                countB += 1
            pqa.put(trip.end + n)

    print(f'Case #{_}: {countA} {countB}')