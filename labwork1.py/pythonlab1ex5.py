colors= ["Red", "Green", "Blue", "Yellow", "Purple"]
ask = input("What is your favorite color? ")
if ask in colors:
    index = colors.index(ask)
    print(f"Your color is at index {index} in my list")
else:
    print ("Sorry, I could not find your color")