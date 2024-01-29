function solution(my_string) {
    var answer = 0;
    for (n of my_string){
       if( 47<n.charCodeAt() && n.charCodeAt() < 58){
           answer += Number(n)
       }
    }
    return answer;
}