print("Secret Message")

message = (input("Enter your secret party message: "))
guest = (input("Enter the guest's name: "))
cleaned_message = message.strip()
print("What would you like to see?")
print("1) Uppercase message")
print("2) Reversed message")
print("3) Number of characters")

def secret_message():
    select = int(input("Pick from 1 to 3: "))
    if select == 1:
        return cleaned_message.upper()
    elif select == 2:
        return cleaned_message[::-1]
    else:
        return len(cleaned_message)
   
print(f" Hey {guest}, here's your secret code: {secret_message()}")