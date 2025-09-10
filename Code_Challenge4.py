print("Welcome to the manga recommendator")
genre = input("What genre o manga would you like? (Action/Romance/Horror)?  ")

if genre ("Action, Romance, Horror"): 
    a = input("Nice! What do you prefer Short,Mmedium, Long?  ")

if a ("Short, Medium, Long"):
    b = input("What decade do you want (2000,2010,2020)?  ") 

if genre == "Action":
    if a  == "long" and b == "2000":
        print("I recommend you read (One Piece).")
    elif a == "medium" and b == "2010":
        print("I recommend (Attack on Titan).")
    elif a == "short" and b == "2010":
        print("I recommend (Zero two).")
    else:
        print("Try (Clover).")


elif genre == "Romance":
    if a == "short" and b == "2000":
        print("I recommend (ball room).")
    elif a == "medium" and b == "2010":
        print("I recommend (Ao Haru Ride).")
    elif a == "long" and b == "2010":
        print("I recommend (Kimi ni Todoke).")
    else:
        print("Try *Horimiya*.")

elif genre == "Horror":
    if a == "short" and b == "2000":
        print("I recommend (Mononoke)")
    elif a == "medium" and b == "2010":
        print("I recommend (Tokyo Ghoul).")
    elif a == "long" and b == "2000":
        print("I recommend (Hellsing).")
    else:
        print("Try *Parasyte*.")

