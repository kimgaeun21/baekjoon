function solution(arr) {
    var answer = [];
    for (i of arr){
        for (var j = 0 ; j<i; j++){
            answer.push(i)
        }
    }
    return answer;
}