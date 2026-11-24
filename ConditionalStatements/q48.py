# Q48. Print language choice using match case (Python 3.10+).
language = input("Choose language (English/Marathi/Hindi): ").lower()
match language:
    case "english":
        print("You selected English")
    case "marathi":
        print("You selected Marathi")
    case "hindi":
        print("You selected Hindi")
    case _:
        print("Language not available")
