$(document).ready(function () {
    $("#bugs").load("Data.txt .calculator")
    let str = "";
    $(".Zero").click(function () {
        if (str === "") {
            str = "0";
        }
        else {
            str += "0"
        }
        document.getElementById("InValue").innerText = str;
    });
    $(".One").click(function () {
        if (str === "0") {
            str = "";
        }
        str += "1"
        document.getElementById("InValue").innerText = str;
    });
    $(".Two").click(function () {
        if (str === "0") {
            str = "";
        }
        str += "2"
        document.getElementById("InValue").innerText = str;
    });
    $(".Three").click(function () {
        if (str === "0") {
            str = "";
        }
        str += "3"
        document.getElementById("InValue").innerText = str;
    });
    $(".Four").click(function () {
        if (str === "0") {
            str = "";
        }
        str += "4"
        document.getElementById("InValue").innerText = str;
    });
    $(".Five").click(function () {
        if (str === "0") {
            str = "";
        }
        str += "5"
        document.getElementById("InValue").innerText = str;
    });
    $(".Six").click(function () {
        if (str === "0") {
            str = "";
        }
        str += "6"
        document.getElementById("InValue").innerText = str;
    });
    $(".Seven").click(function () {
        if (str === "0") {
            str = "";
        }
        str += "7"
        document.getElementById("InValue").innerText = str;
    });
    $(".Eight").click(function () {
        if (str === "0") {
            str = "";
        }
        str += "8"
        document.getElementById("InValue").innerText = str;
    });
    $(".Nine").click(function () {
        if (str === "0") {
            str = "";
        }
        str += "9"
        document.getElementById("InValue").innerText = str;
    });
    //---------------------------- v OPERATIONS v ----------------------------

    $(".Division").click(function () {
        if (str === "0") {
            str = "0";
        } else if (str[str.length - 1] !== "/" && str[str.length - 1] !== "*" && str[str.length - 1] !== "-" && str[str.length - 1] !== "+") {
            str += "/";
        }
        document.getElementById("InValue").innerText = str;
    });

    $(".Comma").click(function () {
        if (str[str.length - 1] === ".") {
            return;
        } else {
            str += ".";
        }
        document.getElementById("InValue").innerText = str;
    });

    $(".Multiply").click(function () {
        if (str === "0") {
            str = "0";
        } else if (str[str.length - 1] !== "/" && str[str.length - 1] !== "*" && str[str.length - 1] !== "-" && str[str.length - 1] !== "+") {
            str += "*";
        }
        document.getElementById("InValue").innerText = str;
    });

    $(".Addition").click(function () {
        if (str === "0") {
            str = "0";
        } else if (str[str.length - 1] !== "/" && str[str.length - 1] !== "*" && str[str.length - 1] !== "-" && str[str.length - 1] !== "+") {
            str += "+";
        }
        document.getElementById("InValue").innerText = str;
    });

    $(".Substraction").click(function () {
        if (str === "0") {
            str = "0";
        } else if (str[str.length - 1] !== "/" && str[str.length - 1] !== "*" && str[str.length - 1] !== "-" && str[str.length - 1] !== "+") {
            str += "-";
        }
        document.getElementById("InValue").innerText = str;
    });
    $(".ParantheseClose").click(function () {
        if (str === "0") {
            str = "";
        }
        str += ")"
        document.getElementById("InValue").innerText = str;
    });
    $(".ParantheseOpen").click(function () {
        if (str === "0") {
            str = "";
        }
        str += "("
        document.getElementById("InValue").innerText = str;
    });

    //---------------------------- ^ OPERATIONS ^ ----------------------------
    $(".C-Pad").click(function () {
        str = ""
        document.getElementById("InValue").innerText = "0";
        document.getElementById("OutValue").innerText = "";
    });
    $(".CE-Pad").click(function () {
        str = ""
        document.getElementById("InValue").innerText = "0";
        document.getElementById("OutValue").innerText = "";
    });
    $(".Erase").click(function () {
        let temp;
        if (parseInt(str) > 10) {
            temp = str;
            str = "";
            for (let i = 0; i < temp.length - 1; i++) {
                str += temp[i];
            }
        } else {
            str = "0";
        }
        document.getElementById("InValue").innerText = str;
    });
    // Arithmetical Operations
    $(".Equals").click(function () {

        document.getElementById("OutValue").innerHTML = evaluatePostfix(infix_to_postfix(str));
        if (str === "0") {
            str = "";
        }
        str = "0"
        document.getElementById("InValue").innerText = str;

        function infix_to_postfix(infix) {
            let Stack = [];
            let postFix = [];
            let temp = "";

            for (let i = 0; i < infix.length; i++) {
                let char = infix[i];

                switch (char) {
                    case '+':
                    case '-':
                    case '/':
                    case '*':
                    case '(':
                        if (temp !== "") {
                            postFix.push(temp);
                            temp = "";
                        }
                        Stack.push(char);
                        break;

                    case ')':
                        if (temp !== "") {
                            postFix.push(temp);
                            temp = "";
                        }
                        while (Stack[Stack.length - 1] !== '(') {
                            postFix.push(Stack[Stack.length - 1]);
                            Stack.pop();
                        }
                        Stack.pop();
                        break;

                    default:
                        temp += char;
                        break;
                }
            }
            if (temp !== "") {
                postFix.push(temp);

            }
            while (Stack.length > 0) {
                postFix.push(Stack[Stack.length - 1])
                Stack.pop();
            }
            let retPostfix = "";
            for (let i = 0; i < postFix.length; i++) {
                retPostfix += " " + postFix[i];
            }
            return retPostfix
        }

        function evaluatePostfix(exp) {
            // create a stack
            let stack = [];

            // Scan all characters one by one
            for (let i = 0; i < exp.length; i++) {
                let c = exp[i];

                if (c === ' ') {

                }

                    // If the scanned character is an
                    // operand (number here),extract
                // the number. Push it to the stack.
                else if (c >= '0' && c <= '9') {
                    let n = 0;

                    // extract the characters and
                    // store it in num
                    while (c >= '0' && c <= '9') {
                        n = n * 10 + (c - '0');
                        i++;
                        c = exp[i];
                    }
                    i--;

                    // push the number in stack
                    stack.push(n);
                }

                    // If the scanned character is
                    // an operator, pop two elements
                // from stack apply the operator
                else {
                    let val1 = stack.pop();
                    let val2 = stack.pop();

                    switch (c) {
                        case '+':
                            stack.push(val2 + val1);
                            break;

                        case '-':
                            stack.push(val2 - val1);
                            break;

                        case '/':
                            stack.push(parseInt(val2 / val1, 10));
                            break;

                        case '*':
                            stack.push(val2 * val1);
                            break;
                    }
                }
            }
            return stack.pop();
        }
    });

});