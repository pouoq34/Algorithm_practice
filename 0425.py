#1. 그리디_거스름 돈 갯수 구하기!

n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인

coin_types = [500,100,50,10]

for coin in coin_types:
    count += n //coin
    n%=coin

print(count)

#2. 그리디_큰 수의 법칙(version 1)

#k는 연속해서 더해질 수 있는 갯수, #m은 더해지는 횟수, #n은 배열의 크기

n,m,k = map(int,input().split())
#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))
data.sort()

biggest = data[-1]
second = data[-2]
result = 0

while True:
    for i in range(k): #가장 큰 수를 k번 더하기
        if m == 0: #m이 0이라면 반복문 탈출
            break
        result += biggest
        m -=1 #더할 때마다 1씩 빼기

    if m ==0:  #m이 0이라면 반복문 탈출
        break
    result += second # 두번째로 큰 수를 한 번 더하기
    m -=1 #더할 때마다 1씩 빼기

print(result)

#2. 그리디_큰 수의 법칙(version 2)

n,m,k = map(int,input().split())
#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))
data.sort()
biggest = data[-1]
second = data[-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count)* biggest #가장 큰 수 더하기
result += (m - count) * second #두 번째로 큰 수 더하기
print(result)