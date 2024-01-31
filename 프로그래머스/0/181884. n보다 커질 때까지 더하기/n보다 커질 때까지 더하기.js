function solution(numbers, n) {
    var answer = 0;
    for(a of numbers){
        answer += a
        if (answer > n){
            return answer
        }
    }
}