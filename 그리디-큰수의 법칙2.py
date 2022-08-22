# 위 문제를 좀 더 간단하게 푸는 방법
# 가장 큰 수와 두 번째로 큰 수가 더해길 때는 특정한 수열 형태로 일정하게 반복해서 더해지는 특징이 있다.
# 반복되는 수열의 길이는 (K+1)
# 따라서 M을 (K+1)로 나눈 몫이 수열이 반복되는 횟수가 된다. 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.
# 이때 M이 (K+1)로 나누어떨어지지 않는 경우도 고려해야 한다.
# 그럴 때는 M을 (K+1)로 나눈 나머지만큼 가장 큰 수가 추가로 더해지므로 이를 고려해주어야 한다.
# 즉, 가장 큰 수가 더해지는 횟수는 다음과 같다.
# int(M / (K+1)) * K + M % (K+1)

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)