#FINALS PROJECT ITCS102
#BY Jasmine D. Ebreo

import os
name = input("Please Enter your name ----> ")
name = name.title()
print ("Hi! " + name )
tuloy = True
while tuloy == True:
    
    print()
    print("|====================================================================|")
    print("|                                 PROJECT MENU                       |")
    print("|====================================================================|")
    print("|                           ACTIVITIES (1-25)                        |")
    print("|————————————————————————————————————————————————————————————————————|")
    print("|    1. Activity1.py             21. Activity21.py                   |")
    print("|    2. Activity2.py             22. Activity22.py                   |")
    print("|    3. Activity3.py             23. Activity23.py                   |")
    print("|    4. Activity4.py             24. Activity24.py (WIP)             |")
    print("|    5. Activity5.py             25. Activity25.py (WIP)             |")
    print("|    6. Activity6.py                                                 |")
    print("|    7. Activity7.py                                                 |")
    print("|    8. Activity8.py                                                 |")
    print("|    9. Activity9.py                                                 |")
    print("|    10. Activity10.py                                               |")
    print("|    11. Activity11.py                                               |")
    print("|    12. Activity12.py                                               |")
    print("|    13. Activity13.py                                               |")
    print("|    14. Activity14.py                                               |")
    print("|    15. Activity15.py                                               |")
    print("|    16. Activity16.py                                               |")
    print("|    17. Activity17.py                                               |")
    print("|    18. Activity18.py                                               |")
    print("|    19. Activity19.py(WIP)                                          |")
    print("|    20. Activity20.py (WIP)                                         |")
    print("|————————————————————————————————————————————————————————————————————|")
    print("|                          CODE CHALLENGES (1-15)                    |")
    print("|————————————————————————————————————————————————————————————————————|")
    print("|    1. Code Challenge 1            9. Code Challenge 9              |")
    print("|    2. Code Challenge 2            10. Code Challenge 10            |")
    print("|    3. Code Challenge 3            11. Code Challenge 11            |")
    print("|    4. Code Challenge 4            12. Code Challenge 12            |")
    print("|    5. Code Challenge 5            13. Code Challenge 13            |")
    print("|    6. Code Challenge 6  (WIP)     14. Code Challenge 14            |")
    print("|    7. Code Challenge 7            15. Code Challenge 15 (WIP)      |")
    print("|    8. Code Challenge 8                                             |")
    print("|————————————————————————————————————————————————————————————————————|")
    
    print("|    PS: (WIP) means Work In Progress/Not Implemented.               |")
    print("|————————————————————————————————————————————————————————————————————|")
    print("||   0. to back/exit                                                ||")
    print("|————————————————————————————————————————————————————————————————————|")
    
    try:
        choice_type = int(input("\nDo you want to run a ACTIVITY [1] or a CODE CHALLENGE [2]? (Type 1 or 2, or 0 to exit)--->"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        input("Press Enter to continue...")
        continue
        
    if choice_type == 0:
        b = 0 
    
    elif choice_type == 1:
        try:
            b = int(input("Enter Activity number (1-25)---> "))
            if b < 1 or b > 25:
                print("Invalid Activity number please enter a number between (1-25)")
                input("Press Enter to continue....")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            input("Press Enter to continue....")
            continue
            
    elif choice_type == 2:
        try:
            c = int(input("Enter Code Challenge number (1-15)---> "))
            if c < 1 or c > 15:
                print("Invalid Code Challenge number. Please enter a number between (1-15)")
                input("Press Enter to continue....")
                continue
            
            b = c + 25 
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")
            continue
            
    else:
        print("Invalid Choice, Please try again.")
        input("Press Enter to continue...") 
        continue
    
    # Activity 1
    if b == 1:
        os.system("cls")
        def Activity1(): 
            print('Hello world')
            
        Activity1() 
        input("Press Enter to continue...")
        continue

    # Activity 2
    elif b == 2:
        os.system("cls")
        def Activity2(): 
            N = input("Enter your Name?")
            print("Hi" , N , "Welcome to my github account")
            
        Activity2() 
        input("Press Enter to continue...")
        continue

    # Activity 3
    elif b == 3:
        os.system("cls")
        def Activity3(): 
            # Note: \r (Carriage return) will overwrite the start of the line in the terminal.
            print("Good Morning!\n\tBSIT-1C Python Class-->", "\t||Moves to a New Line")
            print("file path: C:\\Users\\Student\\Files-->", "\t||Double backlashes")
            print("\rHello Everyone!-->", "\t\t\t||Carriage return")
            print("First Line-->\t\t\t\t||FORM A FEED \fSecond Line\fThird Line ")
            
        Activity3()
        input("Press Enter to continue...")
        continue
    
    # Activity 4
    elif b == 4:
        os.system("cls")
        def Activity4():
            name = input("Enter a name --> ")
            name = name.capitalize()
            print("Welcome to the matrix", name)
            print("Your name has", len(name), "characters")
                    
        Activity4() 
        input("Press Enter to continue...")
        continue

    # Activity 5    
    elif b == 5:
        os.system("cls")
        def Activity5(): 
            x = eval(input("Type something... "))
            print("The data type is", type(x))
                
        Activity5()
        input("Press Enter to continue...")
        continue
    
    # Activity 6    
    elif b == 6:
        os.system("cls")
        def Activity6(): 
            no1 = eval(input("Enter a number---> "))
            no2 = eval(input("Enter another number ----> "))
            ans1 = (no1 + no2)
            ans2 = (no1 - no2)
            ans3 = (no1 * no2)
            ans6 = (no1 ** no2)
            
            if no2 != 0:
                ans4 = (no1 / no2)
                ans5 = (no1 % no2)
                ans7 = (no1 // no2)
            else:
                ans4 = "Undefined (Div/0)"
                ans5 = "Undefined (Mod/0)"
                ans7 = "Undefined (FloorDiv/0)"

            print("\nthe sum of", no1 ,"and", no2 ,"is", ans1 ,)
            print("the difference of", no1 ," and", no2 ,"is", ans2 ,)
            print("the product of", no1 ,"and", no2 ,"is", ans3 ,)
            print("the qoutient of", no1 ,"and", no2 ,"is", ans4 ,)
            print("the remainder of", no1 ,"and", no2 ,"is", ans5 ,)
            print("the exponent of", no1 ,"and", no2 ,"is", ans6 ,)
            print("the floor division of", no1 ,"and", no2 ,"is", ans7 ,)

        Activity6()
        input("Press Enter to continue...")
        continue

    # Activity 7    
    elif b == 7:
        os.system("cls")
        def Activity7(): 
            Ammount = 5
            print("The amount of chromosomes the you had", Ammount)

            Ammount += 5
            print("The amount that you want is", Ammount)

            Ammount += 60
            Ammount *= 2
            print("Your current money right now", Ammount)

        Activity7()
        input("Press Enter to continue...")
        continue

    # Activity 8
    elif b == 8:
        os.system("cls")
        def Activity8():
            a = 3
            b = 5

            print( a < b )

            name1 = "Jasmine"
            name2 = "Jasmine"

            print( name1 != name2 )

        Activity8()
        input("Press Enter to continue...") 
        continue

    # Activity 9
    elif b == 9:
        os.system("cls")
        def Activity9(): 
            username = 'Cuteporato'
            password = 'friesandicecream'

            print("USER LOGIN")
            print( (username == 'cutepotato') and ( password == 'friesandicecream' ) )
                
        Activity9()
        input("Press Enter to continue...")
        continue
            
    # Activity 10
    elif b == 10:
        os.system("cls")
        def Activity10():
            username = 'cutepotato'
            password = 'friesandicecream'

            u = input("USERNAME --> ")
            p = input("PASSWORD --> ")

            if (u == username) and (p == password):
                print("Access granted")
            else:
                print("Acces Denied")
            
        Activity10()
        input("Press Enter to continue...")
        continue
        
    # Activity 11
    elif b == 11:
        os.system("cls")
        def Activity11():
            temp = eval(input("Enter temperature --> "))

            if temp >= 1 and temp <= 20:
                print("The temperature is considered extremely cold")
            elif temp >= 21 and temp <= 30 :
                print("The temperature is moderately cold")
            elif temp >= 31 and temp<= 37: 
                print("The temperature is normal")
            elif temp >= 38 and temp <= 45:
                print("The temperature is hot")
            elif temp > 45 and temp <= 50:
                print("The temperature is boiling hot") 
            elif temp > 50: 
                print("The temperature is dangerous")
            else: 
                print("The temperature is invalid")
                            
        Activity11()
        input("Press Enter to continue...")
        continue
                    
    # Activity 12
    elif b == 12:
        os.system("cls")
        def Activity12(): 
            for cycle in range(1,11,1):
                print("BSIT 1C")
                print("Magandang hapon")
                
        Activity12()
        input("Press Enter to continue...")
        continue
            
    # Activity 13
    elif b == 13:
        os.system("cls")
        def Activity13(): 
            sum = 0
            for x in range(1,11,1):
                print(x)
                number = eval(input("Enter any number:"))
                sum += number
                
            print("\n\tThe sum of all numbers is", sum) 
            
        Activity13()
        input("Press Enter to continue...")
        continue

    # Activity 14
    elif b == 14:
        os.system("cls")
        def Activity14(): 
            for i in range(20,0,-1):
                print(i)
        
        Activity14()
        input("Press Enter to continue...")
        continue

    # Activity 15
    elif b == 15:
        os.system("cls")
        def Activity15():
            for i in range(1,11,1):
                for x in range(1,11,1):
                    print(x, end=" ")
                print(i)
                    
        Activity15()
        input("Press Enter to continue...")
        continue

    # Activity 16
    elif b == 16:
        os.system("cls")
        def Activity16(): 
            for i in range(1,11,1):
                for x in range(1,i,1):
                    print(x, end=" ")
                print() 
            
        Activity16()
        input("Press Enter to continue...")
        continue
    
    # Activity 17
    elif b == 17:
        os.system("cls")
        def Activity17(): 
            for i in range(11, 1, -1):
                for x in range(1, i, 1):
                    print("*", end=" ")
                print()
        
        Activity17()
        input("Press Enter to continue...")
        continue
    
    # Activity 18
    elif b == 18:
        os.system("cls")
        def Activity18(): 
            for i in range(1, 11, 1):
                for x in range(11, i, -1):
                    print(" ", end=" ")
                for y in range(1, i, 1):
                    print("*", end=" ")
                print() 

        Activity18()
        input("Press Enter to continue...")
        continue
    
    # # Activity 19 (WIP)
    # elif b == 19:
    #     os.system("cls")


    #     input("Press Enter to continue...")
    #     continue

    # # Activity 20 (WIP)
    # elif b == 20:
    #     os.system("cls")


    #     input("Press Enter to continue...")
    #     continue
    
    # Activity 21
    elif b == 21:
        os.system("cls")
        def Activity21(): 
            import random

            print("NUMBER GUESSING GAME")
            print("_______________________")

            random_value = random.randint(1, 5)
            tries = 0 
            tuloy = True

            while tuloy == True:
                try:
                    num = int(input("Guess the number from 1 to 5 --> "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                    
                tries += 1
                if num == random_value:
                    print("WINNER!!!")
                    break
                else:
                    print("Mali ang hula mo boi")
                    continue

            print(f" Hi, your guess is correct. The number of tries {tries}")
        
        Activity21()
        input("Press Enter to continue...")
        continue

    # Activity 22
    elif b == 22:
        os.system("cls")
        def Activity22(): 
            isDirty = True

            while isDirty == True:
                washing = input("Continue washing cloths?: (yes/no)").lower()

                if washing == "yes":
                    print("Washing cloths now....")
                    continue
                else:
                    print("Stopped washing cloths...")
                    break
        
        Activity22()
        input("Press Enter to continue...")
        continue
    
    # Activity 23
    elif b == 23:
        os.system("cls")
        def Activity23(): 
            months = ['Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun' , 'Jul']

            for month in months:
                print(f"Month of {month}")
            
            months.reverse()
            print("\nReversed list:", months)
        
        Activity23()
        input("Press Enter to continue...")
        continue

    # Activity 24 (WIP)
    elif b == 24:
        os.system("cls")
        print("Activity 24 is currently under construction/not implemented.")
        input("Press Enter to continue...")
        continue

    # Activity 25 (WIP)
    elif b == 25:
        os.system("cls")
        print("Activity 25 is currently under construction/not implemented.")
        input("Press Enter to continue...")
        continue
        
    
    #----------------------------------------------Code Challenge (from 1-15 to 26-40)--------------------------------------------------------------------
   
    
    # Code Challenge 1 
    elif b == 26: 
        os.system("cls")
        def code_challenge1():
            print("\t\t\t  *\n\t\t      *\t      *\n\t\t  *\t\t  *\n\t      * \tHi\t      *\n\t  *\t\tJasmine\t          *\n\t      *\t\t\t"
            "      *\n\t\t  *\t\t  *\n\t\t       *\t      *\n\t\t\t  *")
            
        code_challenge1()
        input("Press Enter to continue...")
        continue

    # Code Challenge 2
    elif b == 27:
        os.system("cls")
        def code_challenge2():
            try:
                amount = int(input("Enter amount to deposit (integer only): "))
            except ValueError:
                print("Invalid input. Please enter a whole number.")
                return

            print ("Here is a breakdown of your deposit: ")

            thou = amount // 1000
            tc = amount % 1000
            
            fh = tc // 500 
            fhc = tc % 500

            th = fhc // 200 
            thc = fhc % 200

            oneh = thc // 100
            onehc = thc % 100

            fifty = onehc // 50
            fifty_change = onehc % 50

            twenty = fifty_change // 20
            twch = fifty_change % 20

            tens = twch // 10 
            tch = twch % 10

            fives = tch // 5 
            fc = tch % 5 

            ones = fc // 1 
            onec = fc % 1

            print (f"{thou} - 1000s")
            print (f"{fh} - 500s")
            print (f"{th} - 200s")
            print (f"{oneh} - 100s")
            print (f"{fifty} - 50s")
            print (f"{twenty} - 20s")
            print (f"{tens} - 10s")
            print (f"{fives} - 5s")
            print (f"{ones} - 1s")

        code_challenge2()
        input("Press Enter to continue...") 
        continue

    # Code Challenge 3
    elif b == 28:
        os.system("cls")
        def code_challenge3():
            name = input("Enter your name ---->")

            try:
                fare = float(input("How much is your fare --->"))
            except ValueError:
                print("Invalid fare amount.")
                return
                
            student = input("Are you a Student (Yes/No)?")
            
            if student.lower() == 'yes':
                disc = 0.20
                disc_amoount = fare * disc
                disc_fare = fare - disc_amoount
                print(f"\nHello, {name}")
                print(f"The original fare is: ₱{fare:.2f}")
                print(f"The student discount amount is: ₱{disc_amoount:.2f}")
                print(f"The discounted fare is: ₱{ disc_fare:.2f}")
                
            else:
                print(f"\nHello, {name}")
                print(f"You are not eligible for a student discount.")
                print(f"The regular fare is: ₱{fare:.2f}")

            print("\nThank you for using my program")
        
        code_challenge3()
        input("Press Enter to continue...") 
        continue
        
    # Code Challenge 4
    elif b == 29:
        os.system("cls")
        def code_challenge4():
            print("Welcome to the manga recommendator")
            genre = input("What genre o manga would you like? (Action/Romance/Horror)?  ").capitalize()

            if genre in ["Action", "Romance", "Horror"]:
                a = input("Nice! What do you prefer Short, Medium, Long?  ").capitalize()
                
                if a in ["Short", "Medium", "Long"]:
                    b_decade = input("What decade do you want (2000, 2010)?  ") 

                    if genre == "Action":
                        if a == "Long" and b_decade == "2000":
                            print("I recommend you read (One Piece)")
                        elif a == "Medium" and b_decade == "2010":
                            print("I recommend (Attack on Titan)")
                        elif a == "Short" and b_decade == "2010":
                            print("I recommend (Zero two)")
                        else:
                            print("Try (Clover)")


                    elif genre == "Romance":
                        if a == "Short" and b_decade == "2000":
                            print("I recommend (ball room)")
                        elif a == "Medium" and b_decade == "2010":
                            print("I recommend (Ao Haru Ride)")
                        elif a == "Long" and b_decade == "2010":
                            print("I recommend (Kimi ni Todoke)")
                        else:
                            print("Try (Horimiya)")

                    elif genre == "Horror":
                        if a == "Short" and b_decade == "2000":
                            print("I recommend (Mononoke)")
                        elif a == "Medium" and b_decade == "2010":
                            print("I recommend (Tokyo Ghoul)")
                        elif a == "Long" and b_decade == "2000":
                            print("I recommend (Hellsing)")
                        else:
                            print("Try (Parasyte)")
                else:
                    print("Invalid length input. Please type Short, Medium, or Long.")
            else:
                print("Invalid Genre. Please choose from Action, Romance, or Horror.")

        code_challenge4()
        input("Press Enter to continue...") 
        continue
        

    # Code Challenge 5
    elif b == 30:
        os.system("cls")
        def code_challenge5():
            factor = 1
            try:
                a = int(input("Enter your number: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                return

            if a < 0:
                print("Factorial is not defined for negative numbers.")
            elif a == 0:
                print("The factorial of 0 is 1.")
            else:
                for i in range (a,0,-1):
                    factor *= i 

                print("The factorial of the number", a, " is ", factor)

                
        code_challenge5()
        input("Press Enter to continue...") 
        continue
            
    
    # # Code Challenge 6 
    # elif b == 31:
    #     os.system("cls")


    #     input("Press Enter to continue...")
    #     continue
    
    # Code Challenge 7 
    elif b == 32:
        os.system("cls")
        def code_challenge7():
            print("ODD NUMBERS ACCUMULATOR")
            print("Enter 10 numbers. We'll help you sum only the odd ones!\n")

            odd_sum = 0

            for i in range(1, 11):
                try:
                    num = int(input(f"Enter number {i}: "))
                    if num % 2 != 0:
                        odd_sum += num
                except ValueError:
                    print("Invalid input, skipping this entry.")
                    continue

            print(f"\n Sum of all odd numbers: {odd_sum}")
                
        code_challenge7()
        input("Press Enter to continue...") 
        continue

    # Code Challenge 8 
    elif b == 33:
        os.system("cls")
        def code_challenge8():
            print("MULTIPLICATION TABLE CREATOR")

            try:
                num = int(input("Enter a number: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                return

            print(f"\nMultiplication table for {num}:")

            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")
                
        code_challenge8()
        input("Press Enter to continue...") 
        continue
    
    # Code Challenge 9 
    elif b == 34:
        os.system("cls")
        def code_challenge9(): 
            print("SPACESHIP COUNTDOWN TIMER")

            try:
                start_num = int(input("Enter the starting number for countdown: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                return

            print("\nCountdown started:")

            for i in range(start_num, 0, -1):
                print(i)

            print("Liftoff!")
        
        code_challenge9()
        input("Press Enter to continue...") 
        continue

    # Code Challenge 10 
    elif b == 35:
        os.system("cls")
        def code_challenge10():
            
            for i in range(11,0,-1):
                for x in range(1,i,1):
                    print("*", end=" ") 
                print()
            
        code_challenge10()
        input("Press Enter to continue...") 
        continue

    # Code Challenge 11
    elif b == 36:
        os.system("cls")
        def code_challenge11():
            
            for i in range(1, 11):
                print(" " * (11 - i), end="")
                print("*" * (2 * i - 1))
                
            
            for i in range(9, 0, -1):
                print(" " * (11 - i), end="")
                print("*" * (2 * i - 1))

        code_challenge11()
        input("Press Enter to continue...") 
        continue
    
    # Code Challenge 12 
    elif b == 37:
        os.system("cls")
        def code_challenge12():
            # Number Pyramid Pattern
            for i in range(1, 7, 1):
                for x in range(7, i, -1):
                    print(" ",end=" ")
                for y in range(i, 0, -1):
                    print(y, end=" ")
                for z in range(2, i + 1):
                    print(z, end=" ")
                print()

        
        code_challenge12()
        input("Press Enter to continue...") 
        continue

    # Code Challenge 13 
    elif b == 38:
        os.system("cls")
        def code_challenge13():
                    name = input("Enter your name: ")
        print("ODD NUMBER SELECTOR")

        odd = ""
        sum = 0
        uneven = True
        while uneven == True:
            number = eval(input("Enter an odd number: "))

            if number % 2 == 1:  
                print("ODD NUMBER DETECTED")
                sum += number
                odd += str(number) + " "
                continue
            elif number== 0:
                print("LOOP TERMINATED")
                break
            else:
                if number % 2 == 0:
                    print("EVEN NUMBER DETECTED")
                else:
                    print("Invalid number / input")
                continue

        print(f"Hi {name}, the sum of all odd numbers is {sum}")
        print(f"ODD NUMBERS include the ff --> {odd}")
                
        code_challenge13()
        input("Press Enter to continue...") 
        continue

    # Code Challenge 14 
    elif b == 39:
        os.system("cls")
        def code_challenge14():
            anime_list = [ ]

            arayko = True
            while arayko == True:
                a_list = input("Enter an anime (or type \"exit\" to stop): ").strip() 
                
                if a_list.lower() == "exit": 
                    print("You have exited the anime entry program")
                    break
                elif a_list: 
                    anime_list.append(a_list)
                    continue
                else:
                    print("Please enter a valid anime name.")

            print("\nHere is the list of animes you typed: ")
            for a in anime_list:
                print(f"-{a}")
                
        code_challenge14()
        input("Press Enter to continue...") 
        continue

    # # Code Challenge 15 
    # elif b == 40:
    #     os.system("cls")
        

    #     input("Press Enter to continue...")
    #     continue

    # ----------------------------------------------------------------------Exit & Invalid Choice--------------------------------------------------------
    elif b == 0:
        os.system("cls")
        def Exit0():
            print("\nProgram terminated, Thank you for checking my Program.\n")
            print("Thankyou")
        print('''by Jasmine D. Ebreo BSIT 1-C''')
        Exit0()
        break
        
    else:
        print("Invalid Choice, Please try again.")
        input("Press Enter to continue...") 
        continue