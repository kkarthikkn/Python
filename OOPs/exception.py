# Instead of letting your program crash when an error occurs,
# you can catch the error and handle it.

try:
    num = int(input("enter num to divide: "))         # give input() inside try block, which allows it to catch invalid inputs (like strings)
    div=1/num

except ZeroDivisionError:
    print("**** You cant divide by zero ****")

except ValueError:      # This will be raised if the user provides input that can't be converted into an integer
    print("**** Enter the number ****")

except Exception:       # it doesn't specify the exception(not recommended)
    print("Something went wrong!")

finally:
    print("Done")