function solution(s1, s2) {
    var answer = 0;
    for(i of s1){
        for (j of s2){
            if (i == j){
                answer +=1
            }
        }
    }
    return answer;
}