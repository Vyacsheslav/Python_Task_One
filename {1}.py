def Pifagor(a, b): #Функция принимающая два значения и получая третье значение (c)
    import math
    a = int(a)
    b = int(b)
    c = math.sqrt(a**2 + b**2)
    print("Гипотенуза треугольника: ", c)
def NoCondition(): #Функция преставляющая ввиде ошибки ввода одного или двух значений (Exception)
    print("Введены не верные значения!")
print("\tВычисление длины гипотенузы") #Вывод на консоле название кода
a = input("Введите первую длину катета: ") #Ввод первого значения (a)
b = input("Введите вторую длину катета: ") #Ввод второго значения (b)
if ((a.isdigit() == True and b.isdigit() == True)): #Проверка оператора. Является ли два значения (a, b) числом
    Pifagor(a, b) #Введенные значения являются числами. Вызов функции 
else: #Введенные значения (a, b), один или двое являются не числами, а словами 
    NoCondition() #Вывоз функции в виде исключения
