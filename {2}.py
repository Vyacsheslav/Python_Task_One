def TaxiAndSpacing(ValueS, Const, Const_0): #Функция для вычисления стоимости поездки на такси
    ValueS = int(ValueS)
    ValueS *= 1000
    ValueS1 = ValueS // 140; 
    ValueM = Const+(ValueS1 * Const_0)
    print("Итоговая сумма оплаты такси составляет ($): ", ValueM)
print("\tОплата такси\n*Услуга такси, тариф составляет: $4,00, где плюс $0,25 за каждые 140 метров*\n") #Выводит на консоль название программы. Описание тарифа
Const = 4.00 #Константа базового тарифа
Const_0 = 0.25 #Константа плавающей ставки
ValueS = input("Введите пройденное расстояние в километрах: "); #Ввод значения (ValueS) 
if (ValueS.isdigit() == True): #Проверка оператора. Является ли значения (ValueS) числом
    TaxiAndSpacing(ValueS, Const, Const_0) #Введенное значение являются числом. Вызов функции 
else: #Введенное значение (ValueS) является словом 
    print("Введенное расстояние неверное!!!")