def NumeralList(Value): #Функция переводящая с целого число в строковое слово 
    List = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth", ""]
    for i in range(len(List)): #Цикл подбора чисел из списка
        if (Value == i): #Оператор условия где введенное число сопадает с его нумерации списка
            i-=1
            print("Числительное:",List[i]) #Вывод на консоле строкового числа
print("\tПеревод целых чисел в числительные") #Вывод на консоле название программы
Value = int(input("Введите целое число: ")) #Ввод целого числа
for i in range(1,13): #Цикл для подбора чисел из диапозона [1;12]
    if (Value == i): #Оператор условия где введенное чилсо совападает с диапозоном
        NumeralList(Value) #Вызов функции