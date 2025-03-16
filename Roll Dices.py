import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

dice_art ={
    1:("┌───────────┐",
       "│           │",
       "│     ●     │",
       "│           │",
       "└───────────┘",),
    2:("┌───────────┐",
       "│   ●       │",
       "│           │",
       "│        ●  │",
       "└───────────┘",),
    3:("┌───────────┐",
       "│     ●     │",
       "│     ●     │",
       "│     ●     │",
       "└───────────┘",),
    4:("┌───────────┐",
       "│  ●     ●  │",
       "│           │",
       "│  ●     ●  │",
       "└───────────┘",),
    5:("┌───────────┐",
       "│  ●     ●  │",
       "│     ●     │",
       "│  ●     ●  │",
       "└───────────┘",)
            }

dice = []
total = 0
number_dice =int(input("Enter number of dices"))

for die in range(number_dice):
    dice.append(random.randint(1,6))

# for die in range(number_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)
print(dice)
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()

for die in dice:
    total+=die

print(total)




