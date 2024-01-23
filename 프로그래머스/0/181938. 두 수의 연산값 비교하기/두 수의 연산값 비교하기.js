function solution(a, b) {
    var answer = 0;
    answer = Number(String(a)+ String(b)) >= 2* a* b ? Number(String(a)+ String(b)) : 2* a* b
    return answer;
}