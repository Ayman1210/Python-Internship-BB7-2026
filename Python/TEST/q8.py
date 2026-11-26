try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Invalid input.")
#Runtime Error (ValueError and ZeroDivisionError).
except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)