# 문제51 : merge sort를 만들어보자

# 병합정렬(merge sort)은 대표적인 정렬 알고리즘 중 하나로 다음과 같이 동작합니다.

# 1. 리스트의 길이가 0 또는 1이면 이미 정렬된 것으로 본다. 그렇지 않은 경우에는
# 2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
# 3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
# 4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.

# 다음 코드의 빈칸을 채워 병합정렬을 완성해 봅시다.

def merge_sort(a):
    n = len(a) 
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
    if n <= 1:
        return a
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정 
    mid = n // 2 # 중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(a[:mid]) # 재귀 호출로 첫 번째 그룹을 정렬
    g2 = merge_sort(a[mid:]) # 재귀 호출로 두 번째 그룹을 정렬
    # 두 그룹을 하나로 병합
    result = [] # 두 그룹을 합쳐 만들 최종 결과
    while g1 and g2: # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]: # 두 그룹의 맨 앞 자료 값을 비교
            # g1의 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g1.pop(0))
        else:
            # g2의 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g2.pop(0))
    # 아직 남아 있는 자료들을 결과에 추가
    # g1과 g2 중 이미 빈 것은 while을 바로 지나감
    while g1:
        result.append(g1.pop(0)) 
    while g2:
        result.append(g2.pop(0)) 
    return result

a = [180, 145, 165, 45, 170, 175, 173, 171]
print(merge_sort(a))

# Reference
# https://stricky.tistory.com/184

# 답안
#병합 정렬
def 병합정렬(입력리스트):
    입력리스트길이 = len(입력리스트)
    if 입력리스트길이 <= 1:
        return 입력리스트
    중간값 = 입력리스트길이 // 2
    그룹_하나 = 병합정렬(입력리스트[:중간값])
    그룹_둘 = 병합정렬(입력리스트[중간값:])
    결과값 = []

    while 그룹_하나 and 그룹_둘:
        if 그룹_하나[0] < 그룹_둘[0]:
            결과값.append(그룹_하나.pop(0))
        else:
            결과값.append(그룹_둘.pop(0))

    while 그룹_하나:
        결과값.append(그룹_하나.pop(0))
    while 그룹_둘:
        결과값.append(그룹_둘.pop(0))
    return 결과값

주어진리스트 = input().split(' ')
주어진리스트 = [int(i) for i in 주어진리스트]

print(병합정렬(주어진리스트))