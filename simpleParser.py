# A really simple expression evaluator supporting the
# four basic math functions, parentheses, and variables.
# Adapted from https://nerdparadise.com/programming/parsemathexpr

import math

class Parser:
    def __init__(self, string, vars={}):
        self.string = string
        self.index = 0
        self.vars = {
            'pi' : math.pi,
            'e' : math.e
            }
        for var in vars.keys():
            if self.vars.get(var) != None:
                raise Exception("Cannot redefine the value of " + var)
            self.vars[var] = vars[var]
    
    def getValue(self):
        value = self.parseExpression()
        self.skipWhitespace()
        if self.hasNext():
            raise Exception(
                "Unexpected character found: '" +
                self.peek() +
                "' at index " +
                str(self.index))
        return value
    
    def peek(self):
        return self.string[self.index:self.index + 1]
    
    def hasNext(self):
        return self.index < len(self.string)
    
    def skipWhitespace(self):
        while self.hasNext():
            if self.peek() in ' \t\n\r':
                self.index += 1
            else:
                return
    
    def parseExpression(self):
        return self.parseAddition()
    
    def parseAddition(self):
        values = [self.parseMultiplication()]
        while True:
            self.skipWhitespace()
            char = self.peek()
            if char == '+':
                self.index += 1
                values.append(self.parseMultiplication())
            elif char == '-':
                self.index += 1
                values.append(-1 * self.parseMultiplication())
            else:
                break
        return sum(values)
    
    def parseMultiplication(self):
        values = [self.parseParenthesis()]
        while True:
            self.skipWhitespace()
            char = self.peek()
            if char == '*':
                self.index += 1
                values.append(self.parseParenthesis())
            elif char == '/':
                div_index = self.index
                self.index += 1
                denominator = self.parseParenthesis()
                if denominator == 0:
                    raise Exception(
                        "Division by 0 kills baby whales (occured at index " +
                        str(div_index) +
                        ")")
                values.append(1.0 / denominator)
            else:
                break
        value = 1.0
        for factor in values:
            value *= factor
        return value

    
    def parseParenthesis(self):
        self.skipWhitespace()
        char = self.peek()
        if char == '(':
            self.index += 1
            value = self.parseExpression()
            self.skipWhitespace()
            if self.peek() != ')':
                raise Exception(
                    "No closing parenthesis found at character "
                    + str(self.index))
            self.index += 1
            return value
        else:
            return self.parseNegative()
    
    def parseNegative(self):
        self.skipWhitespace()
        char = self.peek()
        if char == '-':
            self.index += 1
            return -1 * self.parseParenthesis()
        else:
            return self.parseValue()
    
    def parseValue(self):
        self.skipWhitespace()
        char = self.peek()
        if char in '0123456789.':
            return self.parseNumber()
        else:
            return self.parseVariable()

    def parseMathFunc(self, funcType):
        mathFunSubStr = self.string[self.index + 1:]
        closingPths = mathFunSubStr.find(")") 

    
    def parseVariable(self):
        self.skipWhitespace()
        var = ''
        while self.hasNext():
            char = self.peek()
            if char.lower() in '_abcdefghijklmnopqrstuvwxyz0123456789':
                var += char
                self.index += 1
            else:
                break
        value = self.vars.get(var, None)
        
        if var == 'sin':
            return math.sin(self.parseMultiplication())
        elif var == 'tan':
            return math.tan(self.parseMultiplication())
        elif var == 'cos':
            return math.cos(self.parseMultiplication())
        elif var == 'ln':
            return math.log(self.parseMultiplication())
        elif value == None:
            raise Exception(
                "Unrecognized variable: '" +
                var +
                "'")
        return float(value)
    
    def parseNumber(self):
        self.skipWhitespace()
        strValue = ''
        decimal_found = False
        char = ''
        
        while self.hasNext():
            char = self.peek()            
            if char == '.':
                if decimal_found:
                    raise Exception(
                        "Found an extra period in a number at character " +
                        str(self.index) +
                        ". Are you European?")
                decimal_found = True
                strValue += '.'
            elif char in '0123456789':
                strValue += char
            else:
                break
            self.index += 1
        
        if len(strValue) == 0:
            if char == '':
                raise Exception("Unexpected end found")
            else:
                raise Exception(
                    "I was expecting to find a number at character " +
                    str(self.index) +
                    " but instead I found a '" +
                    char +
                    "'. What's up with that?")
    
        return float(strValue)
        
def evaluate(expression, vars={}):
    try:
        p = Parser(expression, vars)
        value = p.getValue()
    except Exception as ex:
        print(ex)
        return
        # will return NoneType
        #msg = ex.message
        #raise Exception(msg)
    
    # Return an integer type if the answer is an integer
    if int(value) == value:
        return int(value)
    
    # If Python made some silly precision error
    # like x.99999999999996, just return x + 1 as an integer
    epsilon = 0.0000000001
    if int(value + epsilon) != int(value):
        return int(value + epsilon)
    elif int(value - epsilon) != int(value):
        return int(value)
    
    return value

print(evaluate("-5.78 + -(4 - 2.23) + sin(0) * cos(1) / 1 + tan(2 * ln(-3 + 2 * (1.23 + 99.111)))"))