while True:
    registeredno = [8273714900, 9837617560, 9456000666, 6437356890,7906254591,1234567890]
    ask = int(input("What is your registered number: "))
    if ask not in registeredno:
         print("Invalid no")
         break
    if ask in registeredno:
        print("Valid no!You can procced!")
        name = input("Please tell your name: ")
        print(f"Hello {name.upper()} !")
        election = ["BJP = 1", "CONGRESS = 2", "SP = 3", "BSP = 4", "ASP = 5", "OTHER = 6"]
        print(f"Here is the list of parties: {election}")
        vote = int(input("Choose the party to whom you want to vote: "))
        if vote == 1:
            print("You voted BJP!")
            print("Results will be announced in 2 months.")
            break
        if vote == 2:
            print("You voted CONGRESS!")
            print("Results will be announced in 2 months.")
            break
        if vote == 3:
            print("You voted SP!")
            print("Results will be announced in 2 months.")
            break
        if vote == 4:
            print("You voted BSP!")
            print("Results will be announced in 2 months.")
            break
        if vote == 5:
            print("You voted ASP!")
            print("Results will be announced in 2 months.")
            break
        if vote == 6:
            print("You voted OTHER!")
            print("Results will be announced in 2 months.")
            break
