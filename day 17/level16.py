# 1) კომენტარის სახით ახსენით რაში გვჭირდება elif.
# elif - გამოიყენება if/else და ის გვჭირდება იმისთვის რომ შევქმნათ კიდევ ერთი პირობა

#2) for loop-ის გამოყენებით გამოიტანეთ ყველა კენტი რიცხვი 20-დან 100-მდე.
for i in range(20, 100, 2):
    print(i)

#3) შექმენით password ცვლადი სადაც შეინახავთ რაიმე პაროლს, შემდეგ მომხმარებელს შემოატანინეთ პაროლი, სანამ  პაროლები არ დაემთხვევა გამოიტანეთ: "incorrect password" და თავიდან შემოაყვანინეთ პაროლი. , ხოლო თუ  დაემთხვევა გამოიტანეთ: "password is correct".  გამოიყენეთ  while loop  და if/elif/else.

password = "my_secret_password"
user_input = ""

while user_input != password:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("password is correct")
    else:
        print("incorrect password")


#4) while loop-ის დახმარებით გამოიტანეთ ყველა ლუწი რიცხვი 100-დან 20-მდე.
num = 100
 while num <= 20:
    print(num)
    num  = num - 2
