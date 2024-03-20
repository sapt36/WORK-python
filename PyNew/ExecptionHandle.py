# exception = events detected during exe that interrupt program
#!!! 先"try"錯誤的執行一次 例如:下方程式除0時出錯
# ->得到ZeroDivisionError: division by zero的錯誤代碼

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator /denominator
except ZeroDivisionError:
    print("You can't divide by zero! Idiot!")
except ValueError as e:
    print(e)
    # ValueError: invalid literal for int() with base 10: 'p'
    # compiler auto gegnerate error prompt
    print("Enter number plz :)")
except Exception as e:
    print(e) #一般來說 用這個就好 不用多打下面那行
    print("something went wrong :(")
else: # try all expect pass then print result
    print(result)
finally: # whether or not catch the exception
    print("This will always exe!")