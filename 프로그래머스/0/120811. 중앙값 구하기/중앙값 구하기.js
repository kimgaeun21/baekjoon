function solution(array) {
    var answer = 0;
    let sort = array.sort((a, b) => a - b)
    answer = sort[(array.length+1)/2-1]
    return answer;
}