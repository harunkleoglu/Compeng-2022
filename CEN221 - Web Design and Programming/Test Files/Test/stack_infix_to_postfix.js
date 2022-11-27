$(document).ready(function () {
    $("#PushButton").click(function () {
        let infix = document.getElementById("infixExp");

        function infix_to_postfix(infix) {
            let operand_stack = [];
            let postfix_stack = [];
            let postfix = "";
            let temp = "";

            for (let i = 0; i < infix.length; i++) {
                let char = infix[i];

                switch (char) {
                    case '+':
                        operand_stack.push('+');
                        postfix += temp;
                        break;
                    case '-':
                        operand_stack.push('-');
                        postfix += temp;
                        break;
                    case '*':
                        operand_stack.push('*');
                        postfix += temp;
                        break;
                    case '/':
                        operand_stack.push('/');
                        postfix += temp;
                        break;
                    case '(':
                        operand_stack.push('(');
                        break;
                    case ')':
                        while (operand_stack.top() != '(') {
                            let operator = operand_stack.top;
                            operand_stack.pop();
                            postfix += operator;
                        }
                        break;

                    default :
                        temp += char;
                        break;
                }
            }
            return postfix_stack;
        }

        const arr = infix_to_postfix(infix);
        document.getElementById("TextField").value = arr;

    });

});