var answer;

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('inputBox').value = "";
    var operation = generateSimpleOperation();
    answer = operation['anwser'];
    setPrompt(operation.operation); // lmao
    setAnswer(answer);
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
    

    var firstTerm = getRandomNumber(1,101);
    var lastTerm = getRandomNumber(1,101);	

 
    simpleOperation['operation'] = firstTerm + " " + operand + " " + lastTerm;
    simpleOperation['anwser'] = eval(simpleOperation['operation']);

    return simpleOperation;
}

function setPrompt(prompt) {
    document.getElementById('prompt').innerHTML = prompt;
}

function setAnswer() {
    document.getElementById('answer-label').innerHTML = answer;
}

function getInput() {
    return document.getElementById('inputBox').value;
}

function checkAnswer(userInput) {
    var label = document.getElementById('passLabel');
    label.style.display = "block";
    if (userInput == answer)
	label.innerHTML = "Correct";
    else
	label.innerHTML = "Wrong";
}
