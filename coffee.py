flavor = ["Latte", "Americano", "Cappuccino", "Mocha"]


def main():
    index = 0
    for f in flavor:
        index += 1
        print(str(index) + " " + f)

    choice = input("\nwhich flavor do you want? ")

    try:
        if len(flavor) >= int(choice) >= 1:
            make_coffee(int(choice)-1)
        else:
            print("wrong choice")
    except ValueError:
        print("invalid choice")


def make_coffee(choice):
    print("\n")
    print("grinding beans")
    print("making your coffee, please wait")
    print(f"your {flavor[choice]} is ready, enjoy!")


if "__name__" == "__main__":
    main()
