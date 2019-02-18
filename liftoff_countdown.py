#this is me asking myself how long to lift off?
user_input = int(input("Houston, what's estimated time to lift off? "))

# this is just incase someone puts a million and we all die waiting
if user_input > 20:
    print("Thats too long to wait...")

#looping the count down, and look at that "import time" part cool hun?
while user_input > 0 and user_input <= 20:
    print(user_input)
    user_input = user_input -1
    import time
    time.sleep(1)

#once the clock runs out we have lift off! 🚀
if user_input == 0:
    print("IGNITION")
    time.sleep(1)
    print("Houston, we have lift off!")
