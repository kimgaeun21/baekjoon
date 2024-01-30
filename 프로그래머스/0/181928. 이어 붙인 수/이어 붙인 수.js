function solution(num_list) {
    var answer = 0;
    let a = ''
    let b = ''
    for (i of num_list){
        if (i%2 == 0){
            a += String(i)
        }
        else{
            b += String(i)
        }
    }
    answer = Number(a)+ Number(b)
    return answer;
}