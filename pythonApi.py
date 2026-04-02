import requests
from datetime import datetime


def get_price(coin):
    try:
        url = f"https://api.coinbase.com/v2/prices/{coin}-USD/spot"
        response = requests.get(url)
        data = response.json()
        price = data["data"]["amount"]
        return price
    except:
        return "Invalid Coin"


def menu():
    while True:
        print("==== Crypto Price Checker ====")
        print("1. Check price")
        print("2. Save price to file")
        print("3. View history")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            coin = input("Enter coin symbol (BTC, ETH...): ")
            print(get_price(coin))
        elif choice == "2":
            coin = input("Enter coin symbol (BTC, ETH...): ")
            price = get_price(coin)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("saved_prices.txt", "a") as f:
                f.write(f"{timestamp} | {coin}: ${price}\n")
            print("Price saved!")
            
        elif choice == "3":

            coin = input("Enter coin symbol: ")
            price = get_price(coin)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                with open("saved_prices.txt", "r") as f:
                    history = f.read()
                print (history)
            except FileNotFoundError:
                print ( "File not found")

        elif choice == "4":
            print("See you soon!")
            break
        else:
            print("Invalid choice")


menu()