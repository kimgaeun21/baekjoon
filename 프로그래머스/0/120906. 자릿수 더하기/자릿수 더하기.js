function solution(n) {
    var answer = 0;
    for (i of String(n)){
        answer += Number(i)
    }
    return answer;
}