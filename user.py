prices = [10, 25, 5, 50, 100]
discounted_prices = []

for p in prices :
    if p > 20 :
        print (f"Good you can get up to 10% off ")
        price = p - 10
        discounted_prices.append (price)

    print (discounted_prices )