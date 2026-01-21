# 1 - import random module
import random
"""
# 2 - create subjects

subjects =["Anant Ambani",
           "Virat Kohli",
           "Nirmala Sitaraman",
           "A mumbai cat",
           "A group of monkeys",
           "Prime Ministor Modi",
           "Auto Rickshaw Driver from Delhi"
           ]

actions = ["lanches",
           "cancels",
           "dance",
           "eats",
           "Declares war on",
           "orders",
           "celebrates"
           ]
places_or_things = ["at Red Fort",
                   "in Mumbai Local Train",
                   "a plate of Samosa",
                   "inside Parliament",
                   "at Circus",
                   "during IPL Match",
                   "At India Gate"
                   ]


# 3 - start the headline generation loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    Place = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {Place}"
    print("\n"+ headline)

    user_input = input("\n Do you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

#print goodbye message

print("\n Thanks for using the Fake Headline generator. Have a fun day")
"""

print("Enter subjects (enter 'done' after completion on separate new line)")
while True:
    sub = input("> ").strip()
    if sub.lower()=="done":
        break
    subjects.append(sub)

print("Enter Action after comma in single line")
act = input(act.split(",").strip())


print("Enter new subjects")
sub = input()
act = input()
place= input()

while True:
    print("Do you want another headline?(yes/no)")
    n = input()
    if n == "no":
         break
""""""