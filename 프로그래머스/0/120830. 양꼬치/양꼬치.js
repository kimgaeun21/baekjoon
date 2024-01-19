function solution(n, k) {
    var answer = 0;
    
    answer += n*12000;
    k = k- (parseInt(n/10))
    answer += k * 2000

    return answer;
}