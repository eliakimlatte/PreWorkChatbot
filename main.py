name = input("Please enter your name: ")
age = input("Please enter your age: ")
options = [
    "1. Hobbies and Interests",
    "2. Travel Experiences",
    "3. Book Recommendations",
    "4. End Discussion"
]
for option in options:
    print(option)
choice = input(f"please {name}, inter a number of Discussion ")
print (f"hell0 {name} nice to meet you , How can I help you today? ")

if choice == "1":
    hobbies = input("What are some of your hobbies or interests? ")
    print(f"That sounds great! I’d love to hear more about your hobbies: {hobbies}.")
elif choice == "2":
    travel = input("What’s one of your favorite travel experiences? ")
    print(f"That sounds amazing! Traveling is always a great adventure: {travel}.")
elif choice == "3":
    book = input("What’s a book you would recommend? ")
    print(f"Thanks for the recommendation! I’ll check out: {book}.")
elif choice == "4":
    print("Thank you for chatting! Have a great day!")
else:
    print("Sorry, that’s not a valid option.")

