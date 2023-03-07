# start page which allows a user to select a language of choice
print("Hitamo ururimi/choice of language/Lungha/choix de la langue:")
print("1. Kinyarwanda")
print("2. English")
print("3. Kiswahili")
print("4. French")

# user's choice of language
language = int(input("Enter your choice (1-4): "))

# output for the user

if language == 1:
    print("komeza.")
elif language == 2:
    print("continue.")
elif language == 3:
    print("endelea.")
elif language == 4:
    print("continuer.")
else:
    print("Invalid choice. Please select a number between 1 and 4.")
