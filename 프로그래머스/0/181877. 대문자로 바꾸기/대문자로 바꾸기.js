function solution(myString) {
    var answer = '';
    for (a of myString){
        answer += a.toUpperCase()
    }
    return answer;
}