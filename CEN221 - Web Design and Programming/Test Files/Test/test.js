$(document).ready(function () {
    $("#PushButton").click(function () {

        let infix = document.getElementById("infixExp").value;

        //  Conversion Infix to Postfix
        function infix_to_postfix() {
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
                        if (temp != "") {
                            postFix.push(temp);
                            temp = "";
                        }
                        Stack.push(char);
                        break;

                    case ')':
                        if (temp != "") {
                            postFix.push(temp);
                            temp = "";
                        }
                        while (Stack[Stack.length - 1] != '(') {
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
            if (temp != "") {
                postFix.push(temp);
                temp = "";
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

        document.getElementById("TextField").value = evaluatePostfix(infix_to_postfix(infix));

        //    Arithmetic Operation Part!

        function evaluatePostfix(exp) {
            // create a stack
            let stack = [];

            // Scan all characters one by one
            for (let i = 0; i < exp.length; i++) {
                let c = exp[i];

                if (c == ' ') {
                    continue;
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
