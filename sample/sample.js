var anwser;

document.addEventListener("DOMContentLoaded", function() {
    var operation = generateSimpleOperation();    
    anwser = operation['anwser'];
    setPrompt(operation.operation); // lmao
    
});

function getRandomNumber(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
}

function getRandomOperand() {
    var operands = ["*", "-", "+", "/"];
    var index = getRandomNumber(0,4);
    return operands[index];
}

function generateSimpleOperation(operation) {
    var simpleOperation = {};



    var operand  = getRandomOperand();
    
    //generate nice numbers 
    if (operand == "/") {
	// hack
	firstTerm = 32;
	lastTerm = 2;
    } else {
	var firstTerm = getRandomNumber(1,101);
	var lastTerm = getRandomNumber(1,101);	
    }
 
    simpleOperation['operation'] = firstTerm + " " + operand + " " + lastTerm;
    simpleOperation['anwser'] = eval(simpleOperation['operation']);

    return simpleOperation;
}

function setPrompt(prompt) {
    document.getElementById('prompt').innerHTML = prompt;
}

function getInput() {
    return document.getElementById('inputBox').value;
}

function checkAnwser(userInput) {
    var label = document.getElementById('passLabel');
    label.style.display = "block";
    if (userInput == anwser)
	label.innerHTML = "Correct";
    else
	label.innerHTML = "Wrong";
}
