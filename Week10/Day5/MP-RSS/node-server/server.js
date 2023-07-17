const rssUrl = "https://thefactfile.org/feed/";
const express = require("express");
const cors = require("cors");
const app = express();
const path = require("path");
app.use(express.static('public'));

app.listen(3000, ()=> console.log("server.js on port 3000"))

let Parser = require('rss-parser');
let parser = new Parser();

(async () => {

  let feed = await parser.parseURL(rssUrl);
  // console.log(feed.title);

  feed.items.forEach(item => {
    // console.log(item.title + ':' + item.link)
  });

})();

// ejs

app.set("view engine", "ejs");


app.get("/", async (req, res) => {
  try {
    const feed = await parser.parseURL(rssUrl);
    res.render("pages/index", { posts: feed.items });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving facts from RSS feed");
  }
});

app.get("/search", (req, res) => {
  res.render("pages/search", {posts: []})
});

app.post("/search/title", (req, res) => {
  const searchTtitle = req.body.title;
  const filteredPosts = feed.filter(
    post => post.title.toLowerCase().includes(searchTitle.tolowerCase())
  );
  res.render("pages/search", {posts: filteredPosts});
});

