class Calculator:
    
    def Addition(self, number1, number2):
        return number1 + number2
    
    def Subtraction(self, number1, number2):
        return number1 - number2
    
    def Multiplication(self, number1, number2):
        return number1 * number2
    
    def Division(self, number1, number2):
        if number2 == 0:
            raise ZeroDivisionError('Number2 cannot be Zaro, as Denominator cannot be Zero')
        
        return number1 / number2

        
    
calculator = Calculator()
print("Input 'exit' or '0' to quit the loop.")
while True:
    exp = input("Enter expression: ")
    if exp.lower() == 'exit' or exp == '0':
        break
    variables = exp.split(" ")

    if len(variables) == 3:
        
        number1, operator, number2 = variables
        try:
            number1 = int(number1)
            number2 = int(number2)

            
        except ValueError as v:
            print("INVALID INPUT!!, Numbers should be interger or float")

        else:
            if operator == '+':
                    result = calculator.Addition(number1, number2)
                    print(f"{number1} {operator} {number2} = {result}")
            elif operator == '-':
                result = calculator.Subtraction(number1, number2)
                print(f"{number1} {operator} {number2} = {result}")
            elif operator == '*':
                result = calculator.Multiplication(number1, number2)
                print(f"{number1} {operator} {number2} = {result}")
            elif operator == '/':
                try: 
                    result = calculator.Division(number1, number2)
                except ZeroDivisionError as z:
                    print(z)
                else:
                    print(f"{number1} {operator} {number2} = {result}")

    else:
        print("INVALID INPUT!!, try again!")