prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
average_price = sum(prices) / len(prices)
above_average = [price for price in prices if price > average_price]

print(average_price)  
print(above_average)  