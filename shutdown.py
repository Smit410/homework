def shutdown(input_data):
    if input_data == "Yes":
        print("Shutting down")
    elif input_data == "No":
        print("Abort shut down")
    else:
        print("Sorry")

choice = input("Do you want to shut down? (Yes/No): ")

shutdown(choice)