
print("             HEALTH MANAGEMENT SYSTEM             \n")

def gettime():
    import datetime
    return datetime.datetime.now()

def diet_plain_Waqas():
    with open("Waqas_Diet.txt","a") as wd:
        wd.write(str(gettime())+" "+input("Enter Diet Here: "))
        print("\nDiet Plained Successfuly")

def diet_plain_Rohit():
    with open("Rohit_Diet.txt","a") as rd:
        rd.write(str(gettime())+" "+input("Enter Diet Here: "))
        print("\nDiet Plained Successfuly")

def diet_plain_Saqib():
    with open("Saqib_Diet.txt","a") as sd:
        sd.write(str(gettime())+" "+input("Enter Diet Here: "))
        print("\nDiet Plained Successfuly")

def exer_plain_Waqas():
    with open("Waqas_Exer.txt","a") as we:
        we.write(str(gettime())+" "+input("Enter Exercise Here: "))
        print("\nExercise Plained Successfuly")

def exer_plain_Rohit():
    with open("Rohit_Exer.txt","a") as re:
        re.write(str(gettime())+" "+input("Enter Exercise Here: "))
        print("\nExercise Plained Successfuly")

def exer_plain_Saqib():
    with open("Saqib_Exer.txt","a") as se:
        se.write(str(gettime())+" "+input("Enter Exercise Here: "))
        print("\nExercise Plained Successfuly")

def diet_ret_Waqas():
    with open("Waqas_Diet.txt","r") as wr:
        print(wr.read())
        print("\nDiet Retrived Successfuly")

def diet_ret_Rohit():
    with open("Rohit_Diet.txt","r") as rr:
        print(rr.read())
        print("\nDiet Retrived Successfuly")

def diet_ret_Saqib():
    with open("Saqib_Diet.txt","r") as sr:
        print(sr.read())
        print("\nDiet Retrived Successfuly")


def exer_ret_Waqas():
    with open("Waqas_Exer.txt", "r") as wr:
        print(wr.read())
        print("\nExercise Retrived Successfuly")


def exer_ret_Rohit():
    with open("Rohit_Exer.txt", "r") as rr:
        print(rr.read())
        print("\nExercise Retrived Successfuly")


def exer_ret_Saqib():
    with open("Saqib_Exer.txt", "r") as sr:
        print(sr.read())
        print("\nExercise Retrived Successfuly")




lock = int(input("What do you want? \n1 for Plain Diet or Exercise\n2 for Retrive Diet or Exercise\n"))
if lock == 1:
    plain = int(input("\nWhat do you want to plain? \n1 for Diet\n2 for Exercise\n"))
    if plain == 1:
        name = int(input("\nFor whom you want to plain Diet?\n1 for Waqas\n2 for Rohit\n3 for Saqib\n"))
        if name == 1:
            diet_plain_Waqas()
        elif name == 2:
            diet_plain_Rohit()
        elif name == 3:
            diet_plain_Saqib()
        else:
            print("\nInvalid input")

    else:
        name = int(input("\nFor whom you want to plain Exercise?\n1 for Waqas\n2 for Rohit\n3 for Saqib\n"))
        if name == 1:
            exer_plain_Waqas()
        elif name == 2:
            exer_plain_Rohit()
        elif name == 3:
            exer_plain_Saqib()
        else:
            print("\nInvalid input")
else:
    plain = int(input("\nWhat do you want to retrive? \n1 for Diet\n2 for Exercise\n"))
    if plain == 1:
        name = int(input("\nWhose data you want to retrive Diet?\n1 for Waqas\n2 for Rohit\n3 for Saqib\n"))
        if name == 1:
            diet_ret_Waqas()
        elif name == 2:
            diet_ret_Rohit()
        elif name == 3:
            diet_ret_Saqib()
        else:
            print("\nInvalid input")
    else:
        name = int(input("\nWhose data you want to retrive Exercise?\n1 for Waqas\n2 for Rohit\n3 for Saqib\n\n"))
        if name == 1:
            exer_ret_Waqas()
        elif name == 2:
            exer_ret_Rohit()
        elif name == 3:
            exer_ret_Saqib()
        else:
            print("Invalid input")

