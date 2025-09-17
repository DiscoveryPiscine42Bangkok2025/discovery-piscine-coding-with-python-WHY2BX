def greetings(name):
    if name:
        try:
            int(name)
            print("Error! It was not a name.")
        except ValueError:
            print("Hello,", name)
    else:
        print("Hello,","noble stranger.")

greetings(input())