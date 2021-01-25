const { type } = require('os')
const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const horseShoe = (arr) => {
    let c = 0,
        nArr = [...arr]

    arr.map((val, ind) => {
        nArr.shift()
        if (nArr.indexOf(val) !== -1) c += 1
    })

    return c
}

rl.on('line', (input) => {
    input = input.trim().split(' ')
    console.log(horseShoe(input))
    input = input.map(num => parseInt(num))
    rl.close()
})