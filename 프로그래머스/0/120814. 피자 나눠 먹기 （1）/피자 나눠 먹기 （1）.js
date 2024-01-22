function solution(n) {
    var answer = 0;
    answer  = parseInt(n/7) +1
    if (n%7 == 0){
        answer -= 1
    }
    return answer;
}