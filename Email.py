end = False
def email_splicer():
    email = input("\nEnter the email you would like to slice: ")
    if email.find("@") == -1:
        print("\nNot a valid e-mail address")
    else:
        print("\nThe domain name is: ", email[(email.find("@")+1):len(email)])
        print("\nThe username is: ", email[0:(email.find("@"))])

while end == False:
    email_splicer()
    if input("\nDo you want to go again? (n=no): ") == "n":
        end == True
        break