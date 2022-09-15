# 먼저 매장 내 N개의 부품을 번호를 기준으로 정렬한 후 M개의 찾고자 하는 부품이 각각 매장에 존재하는지 검사하면 된다.
# 이때 매장의 부품들은 정렬이 되어 있기 때문에 이진 탐색을 수행하여 찾을 수 있다.

# 이진 탐색 소스코드 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid

        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None


# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort()
# M 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')