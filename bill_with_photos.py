# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


low_name_1 = name1.lower()
low_name_2 = name2.lower()

t =  low_name_1.count('t')
t1 = low_name_2.count('t')
r = low_name_1.count('r')
r1 =low_name_2.count('r')
u = low_name_1.count('u')
u1 =low_name_2.count('u')
e = low_name_1.count('e')
e1 =low_name_2.count('e')

counting_true = (t + t1) + (r + r1) + (u + u1) + (e + e1)


l = low_name_1.count('l')
l1 = low_name_2.count('l')
o = low_name_1.count('o')
o1 =low_name_2.count('o')
v = low_name_1.count('v')
v1 =low_name_2.count('v')
e = low_name_1.count('e')
e1 =low_name_2.count('e')

counting_love = (l + l1) + (o + o1) + (v + v1) + (e + e1)

res =  str(counting_true) + str(counting_love)

if int(res) < 10 or int(res) > 90:
    print(f"Your score is {res}, you go together like coke and mentos.")

elif int(res) >= 40 and int(res) <= 50:
    print(f"Your score is {res}, you are alright together.")

else:
    print(f"Your score is {res}.")







