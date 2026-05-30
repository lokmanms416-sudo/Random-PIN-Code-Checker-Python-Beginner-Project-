import random
#الطلب من المستخدم ادخال اربع ارقام
pin_code = (input("Enter a 4-digit PIN code: "))
#اختيار الكومبيوتر للاربع ارقام
pin_code_computer = str(random.randint(1000,9999))
#التحقق من ان المستخدم ادخل 4 ارقام
if len(pin_code) == 4:
    #التحقق من تساوي الارقام
    if pin_code == pin_code_computer:
        print("congratulation")
    else:
        print("failure! PIN code did not match")
        print(f"the computer generated this PIN: {pin_code_computer}")
else:
    print("please Enter 4 digits")
