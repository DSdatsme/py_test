def validate(userInput):
    pwscore = 0
    output = "Your password needs: \n"
    if len(userInput) > 5:
        pwscore += 1
    else:
        output += "add more characters \n"

    if len(userInput) < 13:
        pwscore += 1
    else:
        output += "remove characters \n"

    if any(x.isupper() for x in userInput):
        pwscore += 1
    else:
        output += "Add capital letters\n"

    if any(x.islower() for x in userInput):
        pwscore += 1
    else:
        output += "Add lowercase letters\n"

    if any(x.isdigit() for x in userInput):
        pwscore += 1
    else:
        output += "Add numbers\n"

    if ("@" in userInput or "#" in userInput or "$" in userInput):
        pwscore += 1
    else:
        output += "Add symbols\n"

    if pwscore == 6:
        return True
    else:
        print(output)
        return False


def main():
    isValidated = False
    while not (isValidated):
        isValidated = validate(raw_input("Enter a password: "))

    print("Password accepted")


if __name__ == "__main__":
    main()
