'''

Functions:

1. Even or Odd      -
2. Factorial      -

Conditional Statements:

1. Grading System      -
2. Leap Year Checker      -
3. Maximum of Three Numbers      -
4. Positive/Negative/Zero      -
5. BMI Calculator      -

Input and Output Statements:

1. User Name Greeting      -
2. Simple Calculator      -
3. Temperature Converter      -

'''

def main():
    number = int(input("Enter an integer to find even/odd: "))
    EvenOdd(number)
    
    temp_num = int(input("Enter an expression to find the factorial: ").rstrip("!"))
    print(f"The factorial of number {temp_num} is :",factorial(temp_num))
    
    grade = int(input("Enter your CP: "))
    GradingSys(grade)
    
    year = int(input("Enter Year to find the leap year: "))
    leapYear(year)
    
    length3()
    
    numberinput = int(input("Enter a number to find its nature: "))
    nature(numberinput)
    
    weight = int(input("Enter your weight in kilograms: "))
    height = int(input("Enter your Height in meters: "))
    BMI(weight,height)
    
    name = input("Enter your name: ")
    greet(name)
    
    calculating()
    
    choice = int(input("Press '1' to convert Farhenhiet into Celcius\nPress '2' to convert Celcius into Farhenhiet\n"))
    if choice == 1:
        Unit = float(input("Farhenhiet: "))
        F_C(Unit)
    elif choice == 2:
        Unit = float(input("Celcius: "))
        C_F(Unit)
    else:
        print("Invalid")

    
def EvenOdd(number):
    if number % 2 == 0:
        print(f"The {number} is even")
    else:
        print(f"The {number} is odd")

        
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def GradingSys(m):
    if m >= 90:
        print("Your grade is A")
    elif m>=80:
       print("Your grade is B")     
    elif m>=70:
       print("Your grade is C")       
    else:
        print("Your grade is F")


def leapYear(y):
    if y%4 == 0 and y % 100 != 0:
        print(f"{y} is a leap year")
    elif y%400 == 0 and y%100 == 0:
        print(f"{y} is a leap year")
    else:
        print(f"{y} is not leap year")


def length3():
    number = input("Enter digit of Maximum 3: ")
    l = len(number)
    if l == 3:
        print(f"The number is 3-digit: {l}")
    if l != 3:
        print("Enter a number within 3-digits")
        return length3()


def nature(n):
    if n == 0:
        print("The number is 0")
    elif n > 0:
        print("The number is positive")
    else:
        print("The number is negative")


def BMI(h,w):
    bmi = w / h*h
    if bmi > 40:
        print("BMI = Severe Overweight")      
    elif 39.9 < bmi > 25.0:
        print("BMI = Overweight")      
    elif 24.9 < bmi > 18.5 :
        print("BMI = Normal Weight")      
    else:
        print("BMI = Underweight")  


def greet(n):
    print(f"Hello {n}")   


def calculating():
    expression = input("Enter an expression: ").rstrip("").lstrip("")
    n1,char,n2 = expression
    if char == "+":
        print("Sum is :",int(n1) + int(n2)) 
    elif char == "-":
        print("Subtraction is :",int(n1) - int(n2))
    elif char == "/":
        print("Division is :",int(n1) / int(n2))
    elif char == "*":
        print("Multiplication is :",int(n1) * int(n2))
    else: 
        print("Invalid")


def C_F(u):
    temp = (9/5 * u) + 32
    print(f"Farhenhiet:{temp}")

    
def F_C(u):
    temp = (5/9 * u)+32
    print(f"Celcius:{temp}")


main()