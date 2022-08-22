# As per task from codechick.io/challenges:
# Equation should be input in a format x + 6 = 12. Symbols: "+" or "-"

class WrongFormatError(BaseException):

    def __init__(self):
        self.message = 'Wrong input format\n'

    def __str__(self):
        return self.message


def solve(equation: list) -> float:
    global x
    match equation[1]:
        case '+':
            x = float(equation[4]) - float(equation[2])
        case '-':
            x = float(equation[4]) + float(equation[2])
    return x


def input_equation() -> list:
    try:
        user_input = input('''Input equation:
    - "x" should be first
    - use space between operands and symbols
Your input: ''')
        splitted_input = user_input.split(' ')
        if len(splitted_input) != 5:
            raise WrongFormatError
        if splitted_input[0] != 'x':
            raise WrongFormatError
        if not splitted_input[1] in ['+', '-']:
            raise WrongFormatError
        if not (splitted_input[2].isdigit() and splitted_input[4].isdigit()):
            raise WrongFormatError
        if splitted_input[3] != '=':
            raise WrongFormatError
        return splitted_input
    except WrongFormatError as error:
        print(error)
        input_equation()


print(solve(input_equation()))
