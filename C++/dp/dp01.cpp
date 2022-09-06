// 첫 달에는 새로 태어난 토끼 한 쌍만이 존재한다.
// 두 달 이상이 된 토끼는 번식 가능하다
// 번식 가능한 토끼 한 쌍은 매달 새끼 한쌍을 낳는다
// 토끼는 죽지 않는다
// 각자 1마리씩 낳는 것
// f(n+2) = f(n) + f(n+1) -> fibonacci
// 비둘기 집의 원리(pigeonhole principle) -> 귀류법

//아파트를 각 층별로 파란색 또는 노란색 페인트로 칠하되 다음과 같은 규칙으로 칠하려고 한다.
//노란색은 인접한 두 층에 연속하여 사용할 수 있다
//파란색은 인접한 두 층에 연속하여 사용할 수 없다.
//f(1) = 2, f(2) = 3 이다. f(n)은 얼마인가?
//yellow[n] = yellow[n-1] + Blue[n-1]
//Blue[n] = Yellow[n-1] 점화식
//yellow[1] = 1, Blue[1] = 1
dp[1][0] = dp[1][1] = 1; // 첫번째 배열은 층, 두번째 배열은 마지막 층의 색
for (int i = 2; i <= n; i++){
    dp[i][0] = dp[i-1][0] + dp[i-1][1]; //노랑
    dp[i][1] = dp[i-1][0]; //파랑
}

printf("%d\n", dp[n][0] + dp[n][1])

//메모이제이션 -> dp 의 핵심


//fibonacci using memoization
//memo를 위한 배열을 할당하고, 모두 -1로 초기화(피보나치에는 음수가 없음)
//memo[0]을 0으로 memo[1]는 1로 초기화 한다

//pseudo code
// fibo1(n){
//     if n > 1 & memp[n] = -1
//         memo[n] <- fibo1(n-1) + fibo1(n-2)
//     return memo[n]
// }