function performAddition() {
    var num1 = parseInt(document.getElementById("num1").value);
    var num2 = parseInt(document.getElementById("num2").value);
    var result = num1 + num2;
    document.getElementById("result").innerHTML = "Result: " + result;
}
function performSubtraction() {
    var num1 = parseInt(document.getElementById("num1").value);
    var num2 = parseInt(document.getElementById("num2").value);
    var result = num1 - num2;
    document.getElementById("result").innerHTML = "Result: " + result;
}
function performMultiplication() {
    var num1 = parseInt(document.getElementById("num1").value);
    var num2 = parseInt(document.getElementById("num2").value);
    var result = num1 * num2;
    document.getElementById("result").innerHTML = "Result: " + result;
}
function performDivision() {
    var num1 = parseInt(document.getElementById("num1").value);
    var num2 = parseInt(document.getElementById("num2").value);
    var result = num1 / num2;
    document.getElementById("result").innerHTML = "Result: " + result;
}
