import random
import pickle


data = []

for i in range(100):
    this_dice = {random.randint(1,6), random.randint(1,6)}
    data.append(this_dice)

random_dices_file = open("competition", "wb")
pickle.dump(data, random_dices_file)
random_dices_file.close()
    