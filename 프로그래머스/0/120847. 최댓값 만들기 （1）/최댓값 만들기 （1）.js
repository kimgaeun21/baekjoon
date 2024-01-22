function solution(numbers) {
    var answer = 0;
    numbers.sort((a, b)=> a-b)
    numbers.reverse()
    answer = numbers[0] * numbers[1]
    return answer;
}