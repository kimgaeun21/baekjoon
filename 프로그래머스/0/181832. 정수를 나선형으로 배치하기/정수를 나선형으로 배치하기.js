function solution(n) {
    var answer = [];

    for(let i = 0 ; i < n; i ++){
        var arr = [];
        for(let j = 0 ; j < n ; j ++){
            arr.push(0)
        }
        answer.push(arr)
    }
    
    dic = {
        0: [1, 0], 
        1: [0, 1],
        2: [-1, 0],
        3: [0, -1]
    }
    go = 0; x = 0; y= 0;
    
    for (let i = 1; i <= n**2; i ++){
        answer[y][x] = i
        if(go == 0 && x < n){
            if (answer[y][x+1] == 0){
                x ++
            }
            else{
                go = 1
                y ++
            }
            continue
        }
        
        if (go == 1 && y < n){
            if (y != n-1 && answer[y+1][x] == 0){
                y ++
            }
            else{
                go = 2
                x --
            }
            continue
        }
        
        if (go ==2 && x > -1){
            if (x != 0 && answer[y][x-1] == 0){
                x --
            }
            else{
                go = 3
                y --
            }
            continue
        }
        
        if (go == 3 && y > -1){
            
            if (y != 0 && answer[y-1][x] == 0){
                y --
            }
            else{
                go = 0
                x++
            }
            continue
        }
    }

    return answer;
}