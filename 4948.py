'''
    No: 4948
    Title: 베르트랑 공준
    Problem:
        베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
        이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
        예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
        자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

        - 1 ≤ n ≤ 123,456
    Input:
        입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
        입력의 마지막에는 0이 주어진다.
    Output:
        각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
    Lang:
        Python 3
    Explanation:
        브루트포스 알고리즘으로 시간복잡도 O(N)에 처리하는 것보다 에라토스테네스의 체를 이용해 시간복잡도 O(logN)으로 효율적인 처리가 가능하다.
        에라토스테네스의 체를 통해 소수 필터링이 된 결과를 배열에 저장해두면 공간복잡도 O(1)로 해결 할 수 있다.
'''

arr = [True]*(123456*2+1) # 에라토스테네스의 체를 적용하여 소수를 필터링하기 위한 리스트
checked = 0 # 배수 필터링이 된 마지막 소수
while True: # 테스트케이스 반복
    N = int(input()) # 표준 입력 처리
    if N == 0: # N이 0이면 종료
        break
    cnt = 0 # 소수 개수
    for i in range(2, N*2+1): # i를 2부터 N*2까지 1씩 증가
        if arr[i]: # arr[i]가 True(소수)이면 하위 작업 수행
            if checked < i: # 이미 배수 필터링이 완료된 소수인지 검사
                checked = i # 배수 필터링이 된 마지막 소수 업데이트
                for j in range(2, 123456*2//i+1): # 소수의 배수 필터링 작업
                    arr[i*j] = False
            if N < i: # i가 범위 내의 소수인지 확인하고, 참이면 소수 개수를 1 증가
                cnt += 1
    print(cnt) # 주어진 N ~ 2N 범위 내의 소수 개수 출력