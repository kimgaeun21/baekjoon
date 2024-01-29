function solution(myString) {
    var answer = '';
    for(n of myString){
        answer += n.toLowerCase()
    }
    return answer;
}