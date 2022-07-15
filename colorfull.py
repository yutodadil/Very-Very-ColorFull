from colorama import Fore as f
import random

while True: 

    Test3 = random.randrange(0, 255, 2)
    Test = random.randrange(0, 255, 2)
    Test4 = random.randrange(0, 255, 2)
    randcolor = f"\x1b[38;2;{Test};{Test3};{Test4}m"
    print(randcolor + "カラフル～～～!!" + f.RESET)
