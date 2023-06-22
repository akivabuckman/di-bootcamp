function getComputerNumber() {
    let computerNumber = Math.round(Math.random() * 10);
    console.log(computerNumber)
    return computerNumber
}

function getUserNumber(playCount) {
    userNum = prompt('Enter number between 0 and 10:');
        if (isNaN(userNum)) {
            alert('Sorry Not a number, Goodbye');
            return
        } else if (0 > userNum || 10 < userNum) {
            alert("Sorry that's not a good number, Goodbye")
            return
        } else {
            return userNum
        }
}

function compareNumbers(userNumber, computerNumber, playCount) {
    if (userNumber == computerNumber) {
        alert('WINNER')
    } else if (userNumber > computerNumber) {
        if (playCount == 2) {
            alert('Out of chances')
            return 
        } else {
            alert("Your number is bigger than the computer's. Guess again");
            return 1;
        }
    } else if (userNumber < computerNumber) {
        if (playCount == 2) {
            alert('Out of chances')
            return 
        } else {
            alert("Your number is lower than the computer's. Guess again");
            return 1;
        }
    }
}

function playTheGame() {
    response = confirm("Play?");
    if (response != true) {
        alert("No problem, Goodbye");
        return;
    } else {
        computerNum = getComputerNumber()
        playCount = 0;
        do {
            playCount += compareNumbers(getUserNumber(), computerNum, playCount);
        }
        while (playCount <= 2)
    }
}