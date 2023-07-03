// XP1

function compareToTen(num) {
    return new Promise((resolve, reject) => {
        if (num <= 10) {
            resolve("success");
        } else {
            reject("failure");
        }
    })
};

compareToTen(15)
  .then(result => console.log(result))
  .catch(error => console.log(error));

compareToTen(8)
  .then(result => console.log(result))
  .catch(error => console.log(error));

// XP2
// Create a promise that resolves itself in 4 seconds and returns a “success” string.

const fourPromise = new Promise((resolve, reject) => {
    setTimeout(
        () => resolve("success"), 4000
    )
});

fourPromise.then(console.log);

// XP3
// Use Promise.resolve(value) to create a promise that will resolve itself with a value of 3.
// Use Promise.reject(error) to create a promise that will reject itself with the string “Boo!”

const resolvePromise = Promise.resolve(3);

resolvePromise.then((result) => {
  console.log(result);
});

const rejectPromise = Promise.reject("Boo!");

rejectPromise.catch((result) => {
    console.log(result)
});