let usernum = parseInt(prompt('Number:'));

let j = 1
let i=usernum;

do {
    if (i > j) {
        console.log(`${i} bottles of beer on the wall`);
        console.log(`${i} bottles of beer`);
        console.log(`Take ${j} down, pass ${j==1 ? 'it' : 'them'} around`)
        if (i-j == 1) {
            console.log(`Now you got ${i-j} bottle of beer on the wall`)
        } else {
            console.log(`Now you got ${i-j} bottles of beer on the wall`)
        }
        i -= j
        j += 1
    }
}

while (i > j);
if (i == 1){
    console.log('1 bottle of beer on the wall');
    console.log('1 bottle of beer');
    console.log('take it down, pass it around');
    console.log('now go buy some more beer')
} else {
    console.log(`${i} bottles of beer on the wall`);
    console.log(`${i} bottles of beer`);
    console.log('take them down, pass them around');
    console.log('now go buy some more beer')
}