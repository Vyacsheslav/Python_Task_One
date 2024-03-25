def PriceDelivery(OrderProduct): #Функция которая вычисляет сумму доставки
    OrderProduct = int(OrderProduct)
    Total = 10.95 + 2.95 * (OrderProduct - 1)
    print("Сумма доставки составляет ($): ", Total) 
print("\tРачет стоимости доставки\n*Интернет-магазин предоставляет услугу экспресс-доставки для части своих товаров по цене $10,95 за первый товар в заказе и $2,95 - за все последующие")
OrderProduct = input("Введите кол-во товаров заказе: ") #Ввод значения (OrderProduct)
if (OrderProduct.isdigit() == True): #Проверка оператора. Является ли значения (OrderProduct) числом
    PriceDelivery(OrderProduct) #Введенное значение являются числом. Вызов функции 
else: #Введенное значение (OrderProduct) является словом 
    print("Введенное расстояние неверное!!!")