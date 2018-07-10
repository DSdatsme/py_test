import logging as logger

REQUIRED_SYMBOLS = "$#@"


def validate(s):
    print(len(s))
    if 5 < len(s):
        logger.debug('Length lowerbound verified: %s', s)
        if len(s) < 13:
            logger.debug("checked length upper bound %s", s)

            if lambda x: any(x.isupper() for x in s):
                logger.debug("password contains uppercase")

                if lambda x: any(x.islower() for x in s):
                    logger.debug("password contains lowercase")

                    if lambda x: any(x.isdigit() for x in s):
                        logger.debug("password has a number")
                    else:
                        print("add a number and try again")
                        return False

                else:
                    print("add a lowercase character, try again")
                    return False
            else:
                print("add uppercase character and try again")
                return False
        else:
            print("length of your password is too large, try again")
            return False
    else:
        print("length of your password is too small, try again")
        return False











    for i in [REQUIRED_SYMBOLS][0]:
        if i in s:
            print('symbol found')
            break
        print("Add Symbols to your password and try again")
        return False

    return True

def main():
    isVerified = False
    while not(isVerified):


        s = raw_input("enter password")
        isVerified = validate(s)
    print("Password set sucessfully")

if __name__== "__main__":
    #s = raw_input("Enter a password: ")
    main()