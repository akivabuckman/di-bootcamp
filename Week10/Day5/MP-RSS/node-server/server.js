const rssUrl = "https://thefactfile.org/feed/";
const express = require("express");
const cors = require("cors");
const app = express();
const path = require("path");
app.use(express.static('public'));
app.use(express.json())
app.listen(3000, ()=> console.log("server.js on port 3000"))

let Parser = require('rss-parser');
let parser = new Parser();

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

app.post("/search/title", async (req, res) => {
  const searchTitle = req.body.searchInput;
  const feed = await parser.parseURL(rssUrl);
  const filteredPosts = filterFeed(feed.items, searchTitle);
  res.json(filteredPosts);
});

const filterFeed = (feed, searchTitle) => {
  const filteredFeed = feed.filter((item) => item.title.toLowerCase().includes(searchTitle.toLowerCase()));
  return filteredFeed;
};

app.post("/search/category", async (req, res) => {
  const searchCategory = req.body.searchInput;
  const feed = await parser.parseURL(rssUrl);
  const filteredPosts = filterCategory(feed.items, searchCategory);
  res.json(filteredPosts);
});

const filterCategory = (feed, searchTitle) => {
  const query = searchTitle.charAt(0).toUpperCase() + searchTitle.slice(1).toLowerCase();
  const filteredFeed = feed.filter((item) => item.categories.includes(query));
  return filteredFeed;
};