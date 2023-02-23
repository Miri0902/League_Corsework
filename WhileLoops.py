# using while loop to repeatedly execute the condition

count = 1
while count <= 5:
    print (count)
    count = count + 1  # in while loop we need to increment 1 to stop the loop otherwise it will run indefinitely
print("Done")

count = 1
while count <= 5:
    print ('*' * count)
    count = count + 1
print("Done")

secret_number = 9
guess_count =0  #  represents the number of guesses. if we right click on the variable, Refactor we
                     # can change it's name

guess_limit = 3
while guess_count < guess_limit:   # while loops can have optional else part
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed!')

# CAR GAME

#help, start, stop, quit
command = ""
while True: # command.lower() can be modified in input to stop repeating ourselves
    command = input(">").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command =="help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")

# rewrite the same code,but after entering start or stop it wont allow the same twice
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        print("Car started...")
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif command =="help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")








#  represents the number of guesses. if we right click on the variable, Refactor we
                     # can change it's name
