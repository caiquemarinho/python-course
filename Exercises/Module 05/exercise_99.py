"""

To calculate the attack of a player in Tibia


Formula:

PS: This formula is based in values observed.

Max damage:
 Where:

0.85*d*x*y + lvl/5

 x = Weapon Attack
 y = Player Skill
 lvl = Player Level
 d =  Posture
Let's take an example of a  80 level player, using a  50 attack weapon, skills 85 and with attack posture.
0.085*1*50*85+80/5 = 377.25 (377 rounding)

"""


print('Please insert your weapon attack')
x = int(input())

print('Please insert your player skill')
y = int(input())

print('Please insert your player level')
lvl = int(input())

print('Please insert your posture')
d = int(input())

h = round(0.085*d*x*y + (lvl/5))

print(f'Your highest attack is: {h}')
