from comp_choice import comp_choice
def quote_generator():
    while True:
        print("-"*20,"WELCOME","-"*20)
        print("\nHow many quotes you want?")
        print("1. One")
        print("2. Two")
        print("3. Three")
        print("4. Four")
        choice=int(input("Enter your choice: "))
        if choice ==1:
            print(comp_choice())
            break
        elif choice ==2:
            print(comp_choice())
            print(comp_choice())
            break
        elif choice==3:
            print(comp_choice())
            print(comp_choice())
            print(comp_choice())
            break
        elif choice ==4:
            print(comp_choice())
            print(comp_choice())
            print(comp_choice())
            print(comp_choice())
            break
        else:
            print("Enter a valid choice!!")
            break

quote_generator()