import random

again: bool = True
die1 : int = random.randint(1,6)
die2 : int = random.randint(1,6)

while again:
    print(f"Dic 1 = {die1} \nDic 2 = {die2}")
    another_roll : str = input("Want to roll the dic again(y/n): ")
    if another_roll.lower() == 'y':
        continue
    else:
        break