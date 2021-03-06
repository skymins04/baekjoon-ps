'''
    No: 2748
    Title: 피보나치 수 2
    Problem:
        피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
        이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
        n=17일때 까지 피보나치 수를 써보면 다음과 같다.
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
        n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
    Input:
        첫째 줄에 n이 주어진다. n은 90보다 작거나 같은 자연수이다.
    Output:
        첫째 줄에 n번째 피보나치 수를 출력한다.
    Lang:
        Python 3
    Explanation:
        Bottom-Up Dynamic Programing을 통해 CallStack Overflow를 방지하고 시간복잡도를 줄여야한다.
'''

N = int(input()) # 표준 입력 처리
arr = [0, 1] # DP memoization을 위한 리스트 - 0번째, 1번째 피보나치 수는 각각 0, 1이다.
arr.extend([-1] * (N-1)) # N번째까지 -1을 채움
if N > 1: # 0번째, 1번재 피보나치 수가 아닌 경우 DP 작업 수행
    for i in range(2, N+1): # N번째 피보나치 수까지 DP 작업 수행
        arr[i] = arr[i-1] + arr[i-2] # Fn() = Fn-1() + Fn-2()
print(arr[N]) # N번째 피보나치 수 출력