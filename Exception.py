try:
    a = int(input("ENTER NUMBER A = "))
    b = int(input("ENTER NUMBER B = "))
    result = a / b
    print("Result", result)
except ZeroDivisionError:
    print("Error: can not divide by zero")
except ValueError:
    print("Error: Enter valid numbers")
finally:
    print("Program Ended")
