const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    answer = ''
    str = input[0];
    for (i of str){
        if (i === i.toLowerCase()){
            answer += i.toUpperCase()
        }
        else{
            answer += i.toLowerCase()
        }
    }
    console.log(answer)
});