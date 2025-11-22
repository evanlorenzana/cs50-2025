greeting = input("Greeting: ")

ng = greeting.strip().lower()

if ng.startswith("hello"):

    print("$0")

elif ng.startswith("h"):

    print("$20")

else:
    
    print("$100")