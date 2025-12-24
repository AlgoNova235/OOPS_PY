from converter import CurrencyConverter

API_KEY = "K3NS5f5tx4C57MsE3Msik2dmyqK8JK"

def main():
    cc = CurrencyConverter()
    #created teh object from the class

    while True:
        print("\n=== Currency Converter ===")
        print("1. View all currencies")
        print("2. Convert currency")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            cc.show_all_currencies()

        elif choice == "2":
            from_cur = input("From currency code: ").upper()
            to_cur = input("To currency code: ").upper()
            amount = float(input("Amount: "))

            if not cc.is_valid(from_cur):
                print("Invalid FROM currency.")
                continue

            if not cc.is_valid(to_cur):
                print("Invalid TO currency.")
                continue

            result = cc.convert(from_cur, to_cur, amount)
            print(f"\n{amount} {from_cur} = {result} {to_cur}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
