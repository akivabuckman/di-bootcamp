class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

    watch() {
        console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`)
    }
}

let a = new Video('vidvid', 'akiva', 5);
a.watch();

let b = new Video('another vid', 'michael', 33333);
let c = a;
let d = b;
let e = d;
let videos = [a, b, c, d, e];
let videoInfo = [];
for (let video of videos) {
    videoInfo.push(video)
};

for (let i of videos) {
    i.watch()
};