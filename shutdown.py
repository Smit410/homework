def shutdown(input_user):
    input_user = input_user.lower()
    
    if input_user == "yes":
        print("Shutting down")
    elif input_user == "no":
        print("Abort shut down")
    else:
        print("Sorry")
user_choice = input("Do you want to shut down? (Yes/No): ")
shutdown(user_choice)