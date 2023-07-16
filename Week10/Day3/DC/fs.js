const fs = require("fs");
const data = fs.readFileSync("RightLeft.txt", 'utf-8').split("");

// part 1
let step = 0;
for (const i of data) {
    if (i === ">") {
        step ++;
    } else if (i === "<") {
        step --;
    }
};
console.log(step);

// part 2
let step2 = 0;
for (const i in data) {
    if (data[i] === ">") {
        step2 ++;
    } else if (data[i] === "<") {
        step2 --;
    };
    if (step2 === -1) {
        console.log(`to get to -1 you need ${i} steps`);
        return
    };
};