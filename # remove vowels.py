# remove vowels

VOWElS = ("a","e","i","o","u")

message = input("enter you message : ")

new_message = ""

for letter in message:
    if letter not in VOWElS:
        new_message += letter

print(new_message)