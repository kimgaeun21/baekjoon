function solution(babbling) {
    var answer = 0;
    for (i of babbling){
        check = 0
        
        if (i.includes('aya')){
            check += 3;
        }
        
        if (i.includes('ye')){
            check += 2
        }
        
        if (i.includes('woo')){
            check+= 3
        }
        
        if (i.includes('ma')){
            check += 2
        }
        
        if (check == i.length){
            answer += 1
        }
    }
    return answer;
}