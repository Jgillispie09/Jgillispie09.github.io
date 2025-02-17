let diceButton = document.getElementById("dice-button");
let diceInput = document.getElementById("dice-num");

diceButton.addEventListener("click", function() {
    let numDice = parseInt(document.getElementById("dice-num").value);

    let diceSelect = document.getElementById("dice-selector").value;

    diceSelect = parseInt(diceSelect);

    let totalResult = 0;

    for (let i=0; i < numDice; i++) {
        let diceRoll = Math.floor(Math.random() * diceSelect)  + 1;
        totalResult += diceRoll;
    }

    let rollResult = document.getElementById("roll-result");

    rollResult.innerText = totalResult;
})

diceInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        diceButton.click();
    }
})