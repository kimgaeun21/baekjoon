function solution(lines) {
    var arr = new Array(200).fill(0)
    for (i of lines){
        for(;i[0]<i[1];i[0]++){
            arr[i[0]+100]++
        }
    }
    return arr.reduce((a,c)=> c>1 ? a+1 : a ,0)
}