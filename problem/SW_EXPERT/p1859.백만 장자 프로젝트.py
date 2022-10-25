"""
[1859.백만 장자 프로젝트]
뒤에 오는 가장 큰 숫자가 이전의 숫자의 차를 추가해나가면 되는 문제
거꾸로 접근하면 쉽게 풀 수 있다

T : 테스트케이스
N : 오는 숫자의 수
M : 숫자의 리스트
value : 차를 더한 값(결과값)
max_num : 리스트에서 큰 값(뒤에서부터 접근하였을 때)
"""

T = int(input())
for t in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    value = 0
    #max_num의 초기값은 리스트의 맨 마지막 값으로 설정
    max_num = M[-1]

    #뒤에서부터 접근하여 max_num의 값보다 크다면 값을 바꿔주고,
    #작다면 max_num과의 차를 value에 더해준다
    for m in range(len(M)-2, -1, -1):
        if max_num > M[m]:
            value += max_num - M[m]
        else:
            max_num = M[m]
    print('#{} {}'.format(t, value))