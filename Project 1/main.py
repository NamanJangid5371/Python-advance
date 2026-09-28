import math


def scientific_calculator():
    while True:
        print("\n" + "=" * 40)
        print("       SCIENTIFIC CALCULATOR")
        print("=" * 40)

        print("""
1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  Power (x^y)
6.  Square Root
7.  Sine
8.  Cosine
9.  Tangent
10. Logarithm (base 10)
11. Natural Log (ln)
12. Factorial
13. Percentage
14. Pi (π)
15. Euler's Number (e)
0. Exit
""")

        choice = input("Enter your choice: ")

        try:
            if choice == "0":
                print("Calculator closed.")
                break

            elif choice == "1":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a + b)

            elif choice == "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a - b)

            elif choice == "3":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a * b)

            elif choice == "4":
                a = float(input("Enter numerator: "))
                b = float(input("Enter denominator: "))

                if b == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print("Result:", a / b)

            elif choice == "5":
                a = float(input("Enter base: "))
                b = float(input("Enter exponent: "))
                print("Result:", a ** b)

            elif choice == "6":
                a = float(input("Enter number: "))

                if a < 0:
                    print("Error: Cannot calculate square root of a negative number.")
                else:
                    print("Result:", math.sqrt(a))

            elif choice == "7":
                angle = float(input("Enter angle in degrees: "))
                print("Result:", math.sin(math.radians(angle)))

            elif choice == "8":
                angle = float(input("Enter angle in degrees: "))
                print("Result:", math.cos(math.radians(angle)))

            elif choice == "9":
                angle = float(input("Enter angle in degrees: "))
                print("Result:", math.tan(math.radians(angle)))

            elif choice == "10":
                a = float(input("Enter number: "))

                if a <= 0:
                    print("Error: Number must be greater than 0.")
                else:
                    print("Result:", math.log10(a))

            elif choice == "11":
                a = float(input("Enter number: "))

                if a <= 0:
                    print("Error: Number must be greater than 0.")
                else:
                    print("Result:", math.log(a))

            elif choice == "12":
                a = int(input("Enter a non-negative integer: "))

                if a < 0:
                    print("Error: Factorial is not defined for negative numbers.")
                else:
                    print("Result:", math.factorial(a))

            elif choice == "13":
                value = float(input("Enter value: "))
                percentage = float(input("Enter percentage: "))
                print("Result:", (value * percentage) / 100)

            elif choice == "14":
                print("π =", math.pi)

            elif choice == "15":
                print("e =", math.e)

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Error: Please enter a valid number.")

        except OverflowError:
            print("Error: Result is too large.")

        input("\nPress Enter to continue...")


scientific_calculator()