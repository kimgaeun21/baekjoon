function solution(my_string, is_suffix) {
    var answer = 0;
    if (is_suffix === my_string.slice(my_string.length-is_suffix.length)){
        answer = 1
    }
    return answer;
}