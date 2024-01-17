function GCD(num1,num2){
     while(num2 > 0){
        let r = num1 % num2;
        num1 = num2;
        num2 = r;
    } 
    
    return num1
}
function solution(numer1, denom1, numer2, denom2) {
    let answer = [];
    let denom = denom1* denom2;
    let numer = numer1 * denom2 + numer2* denom1;
    let gcd = GCD(numer,denom)
    
    answer.push(parseInt(numer/gcd))
    answer.push(parseInt(denom/gcd))
    return answer;
}