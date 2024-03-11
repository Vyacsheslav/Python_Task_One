class MathFunc():
    def Pifagor(a, b):
        import math
        a = int(a)
        b = int(b)
        c = math.sqrt(a^2 + b^2)
        print("Гипотенуза треугольника: ", c)
        
class Event():
    def NoCondition():
        print("Введены не верные значения!")

print("\tВычисление длины гипотенузы")
a = input("Введите первую длину катета: ")
b = input("Введите вторую длину катета: ")
if (a.isdigit() and b.isdigit() == True): #Является ли и строка числом
    MathFunc.Pifagor(a, b)
else:
    Event.NoCondition()