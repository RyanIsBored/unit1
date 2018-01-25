#Ryan Jones
#1/24/18

priceOfMeal = float(input('Price of the meal (in dollars): '))
tip = int(input('% of tip: '))
ans = round(priceOfMeal*tip/100,2)
print("You should tip",(ans),"dollars")