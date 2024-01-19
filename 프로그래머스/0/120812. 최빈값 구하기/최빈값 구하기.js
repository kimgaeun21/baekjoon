function solution(array) {
    var answer = -1;
    var check={}
    
    for (let i of array){
        if (check[i] >= 1){
            check[i] += 1
        }
        else{
            check[i] = 1
        }
    }
    
    M=Math.max(...Object.values(check))
    
    for (let j in check){
        if ( check[j] == M && answer == -1){
            answer = j
        }
        else if (check[j] == M && answer != -1){
            answer = -1
        }
    }
    return Number(answer);
}