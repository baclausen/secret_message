# This is the SECRET MESSAGE portion of the exercise
message = input("Enter your secret party message: ")
recipient = input("Enter the guest's name: ")
cleaned_message = message.strip()
print("")
print("What would you like to see?")
print("1) Uppercase message")
print("2) Reversed message")
print("3) Number of characters \n")

choice = int(input("Enter a number 1, 2, or 3: "))
# User selects output option
def user_option(option):
    if option == 1:
        return cleaned_message.upper()
    if option == 2:
        return cleaned_message[::-1]
    if option == 3:
        return len(cleaned_message)
    else:
        return "unavailable because you can't follow rules."

# Combine inputs
print(f"Hey {recipient}, here's your secret unbreakable code: {user_option(choice)}")

