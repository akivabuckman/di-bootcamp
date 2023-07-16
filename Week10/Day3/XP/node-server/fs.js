// XP1
const fs = require("fs/promises");

fs.readFile("./xp1_1.txt", {encoding: "utf8"})
    .then(res => console.log(res))
    .catch(console.error);

// XP2_2
async function fileEdit () {
    try {
        await fs.writeFile("xp1_2.txt", "this is XP2");
        await fs.appendFile("xp1_2.txt", `\nthis is continued`)

        // XP2_3
        await fs.unlink("xp1_2.txt")
    } catch (err) {
        console.error(err)
    };
};
fileEdit();
