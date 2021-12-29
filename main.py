print('-' * 90)
def search_number(left, right):

    # Counter variable
    cnt = 1
    # User input
    ans_from_user = ''

    while True:
        mid = (left+right) // 2

        if cnt != 10:
            print("Numbers of tries: ", cnt)
            print("It's your number", mid, '?')
            ans_from_user = input("Your answer: ")
            if ans_from_user == "yes":
                print()
                return ["Number is", str(mid), "If it's not, then you wanted to trick me and you changed it !\n""Number of tries: ", str(cnt)]
            print()

        if cnt == 10:
            return ["Number is", str(mid), "If it's not, then you lied during the quetions or you wanted to trick me and you changed it!\n""Number of tries: ", str(cnt)]

        else:
            if ans_from_user == "bigger":
                left = mid + 1

            elif ans_from_user == "smaller":
                right = mid - 1

        cnt += 1

print()
print("Think at a number between 0 and 1000 and i will guess it in no more than 10 tries: ", end = ' ')
print()
print("You will answer: \"bigger\" if your number is higher than what program shows and \"smaller\" if your number is lower or \"yes\" if the program guessed it earlier")
print()
print()

print(' '.join(search_number(1, 1000)))

print('-' * 90)