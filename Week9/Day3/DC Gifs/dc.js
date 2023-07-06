const addGif = async (event) => {
    event.preventDefault(); 
  
    const data = new FormData(event.target);
    const objBody = {
      method: "GET",
      headers: { "Content-type": "application/json; charset=UTF-8" },
    };
    const tag = data.get("tag"); // Use get() method to retrieve the value of the "tag" field
  
    try {
      const response = await fetch(
        `https://api.giphy.com/v1/gifs/random?api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&tag=${tag}&limit=1`,
        objBody
      );
      if (response.status === 400) {
        throw new Error("Bad gif");
      } else {
        console.log("response", response);
        const responseData = await response.json();
        console.log("data", responseData);
        displayGif(responseData);
      }
    } catch (error) {
      console.log(error);
    }
};

const displayGif = responseData => {
    let gif = document.createElement('img');
    gif.setAttribute('src', responseData['data']['embed_url']);
    console.log(responseData['data']['url'])
    document.body.appendChild(gif)
}
  

  
const formArticle = document.querySelector("form");
formArticle.addEventListener("submit", addGif);

  