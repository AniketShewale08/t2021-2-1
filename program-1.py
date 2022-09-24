class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def substaction(self):
        return abs(self.a - self.b)

    def multiplication(self):
        return self.a * self.b 

    def division(self):
        return self.a / self.b
    

if __name__ == "__main__":
    
    a = float(input("Enter a value of a: "))
    b = float(input("Enter a value of b: "))
    operation = str(input("Enter the opertaion which you want to perform(+, -, *, /): "))

    s = Calc(a,b)
    if operation == "+":
        print(s.addition())
    elif operation == "-":
        print(s.substaction())
    elif operation == "*":
         print(s.multiplication())
    elif operation == "/":
        print(s.division())
    else:
        print("Please enter a valid option(+, -, *, /)")