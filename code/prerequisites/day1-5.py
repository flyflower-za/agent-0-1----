

from random import choice
def add(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b
def div(a,b): 
    if b == 0:
        return "Error: Division by zero"
    return a / b

while True:
    print("\n---简易计算器---")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("q. 退出")
    choice = input("请输入您的选择: ")
    
    if choice == "q":
        print("感谢使用，再见！")
        break
    
    if choice in ["1","2","3","4"]:
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        if choice == "1":
            print("结果: ", add(num1, num2))
        elif choice == "2":
            print("结果: ", sub(num1, num2))
        elif choice == "3":
            print("结果: ", mul(num1, num2))
        elif choice == "4":
            print("结果: ", div(num1, num2))
    else:
        print("输入错误")