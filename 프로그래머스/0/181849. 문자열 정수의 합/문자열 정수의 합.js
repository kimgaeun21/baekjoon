function solution(num_str) {
    var answer = 0;
    for (n of num_str){
        answer += Number(n)
    }
    return answer;
}