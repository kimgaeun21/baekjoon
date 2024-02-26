function solution(arr1, arr2) {
    var answer = 0;
    if (arr1.length > arr2.length){
        answer = 1
    }
    else if (arr2.length > arr1.length){
        answer = -1
    }
    else{
        sum_a = arr1.reduce((a, b) => a + b, 0)
        sum_b = arr2.reduce((a, b)=> a+b, 0)
        
        if (sum_a > sum_b){
            answer = 1
        }else if (sum_a < sum_b){
            answer = -1
        }
        
    }
    return answer;
}