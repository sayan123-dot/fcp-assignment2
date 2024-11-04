import random
#Opening the file without encoding="utf-8" results in an error for some reason.
print(random.choice(open("fortune.txt", encoding="utf-8").read().split("\n%\n")))
