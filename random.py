import webbrowser
user_inp = input("enter a website: ").replace(" ", "+")
webbrowser.open("https://www.google.com/search?q=" + user_inp)

