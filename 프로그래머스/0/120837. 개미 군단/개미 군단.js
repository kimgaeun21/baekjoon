function solution(hp) {
    var answer = 0;
    var ant = [5,3,1]
    for (i of ant){
        answer += parseInt(hp/i)
        hp %= i
    }
    return answer;
}