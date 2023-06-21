let str = "";
for (let i = 1; i < 7; i++) {
    str += "* ";
    console.log(str)
}

pattern = "";
for (let i = 1; i < 7; i++) {
    for (let j = 1; j <= i; j++) {
      pattern += "* ";
    }
    pattern += "\n";
  }