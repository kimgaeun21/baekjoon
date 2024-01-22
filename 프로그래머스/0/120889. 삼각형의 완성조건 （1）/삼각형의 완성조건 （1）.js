function solution(sides) {
    var answer = 0;
    maxi = Math.max(...sides)
    sum = sides.reduce((a, b) => a + b, 0);
    if (sum - maxi > maxi){
        answer = 1
    }
    else{
        answer =2
    }
    return answer;
}