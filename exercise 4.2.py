# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

no_of_names = int(len(names))

i = random.randint(0, no_of_names - 1)

bill_paying_person = names[i]

print(f"The person who has to pay the bill is {bill_paying_person}")
