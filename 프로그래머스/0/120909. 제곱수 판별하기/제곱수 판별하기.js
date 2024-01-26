function solution(n) {
    var answer = 2;
    check = Math.sqrt(n)
    if (check % 1 == 0){
        answer =1
    }
    
    return answer;
}