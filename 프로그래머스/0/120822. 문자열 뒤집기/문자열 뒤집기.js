function solution(my_string) {
    var answer = '';
    arr = my_string.split("")
    reversestr = arr.reverse()
    answer = reversestr.join("")
    return answer;
}