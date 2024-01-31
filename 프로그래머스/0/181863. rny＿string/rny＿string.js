function solution(rny_string) {
    var answer = '';
    for (i of rny_string){
        if(i === 'm'){
            answer += 'rn'
        }
        else{
            answer += i
        }
    }
    return answer;
}