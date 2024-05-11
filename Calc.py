import sqlite3 as sq

TrueFlag = True

def MinusNum(a, b):
    if a > b:
        return a - b
    else: 
        return b - a

def PlusNum(a, b):
    return a + b

def DivNum(a, b):
    return a / b

def MultNum(a, b):
    return a * b

def WhoWork():
    work = str(input("Что делаем(+,-,*,/)?: "))
    return work

# Запись в БД
def AppendExbd(num1, num2, work, result):
    cur.execute(f""" INSERT INTO ResultCalc (FirstNum, SecondNum, Work, Result) VALUES ({num1}, {num2}, "{work}", {result})""")
    print(f"Результат: {result}")

while TrueFlag:

    with sq.connect("dbcalc.db") as db:
        cur = db.cursor()

        cur.execute(""" CREATE TABLE IF NOT EXISTS ResultCalc (
                    FirstNum INTEGER NOT NULL ,
                    SecondNum INTEGER,
                    Work TEXT,
                    Result INTEGER
        )""")

        try:
            num1 = int(input("Первое число?: "))
        except ValueError:
            print("Вы ввели не число !")
            break    

        try:
            num2 = int(input("Второе число?: "))
        except ValueError:
            print("Вы ввели не число !")
            break

        work = WhoWork()

        if work == "+":
            NumResultPlus = PlusNum(num1, num2)
            AppendExbd(num1, num2, work, NumResultPlus)
        elif work == "-":
            NumResultMinus = MinusNum(num1, num2)
            AppendExbd(num1, num2, work, NumResultMinus)
        elif work == "*":
            NumResultMult = MultNum(num1, num2)
            AppendExbd(num1, num2, work, NumResultMult)
        elif work == "/":
            NumResultDiv = DivNum(num1, num2)
            AppendExbd(num1, num2, work, NumResultDiv)
        elif work.lower() == "c":
            print("Конец!")
            break
        else: 
            print("Нету такого действия !")
            