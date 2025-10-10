import pandas as pd
import random
fNames = ["tom", "danny", "chris", "matt", "mathew", "gorbino", "donald", "benedict", "richard", "andrew", "joe", "john", "james", "noah", "owen", "dave", "maddy", "angelina", "jenny", "madson", "patty", "marge"]
lNames = ["putman", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "li", "gi", "smith", "smells", "like", "handover", "riso", "wisseaux", "jacqueline", "dav", "lamar", "smithers", "elvis", "presley", "president", "king", "cobain", "kurt", "jackson", "friedmann", "fripp"]
names = []
for i in range(20):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")
fishmanData = {
    "names": names,
    "worried": [random.randint(1, 10) for _ in names],
    "sympathetic": [random.randint(1, 10) for _ in names],
    "moxieAndGusto": [random.randint(1, 10) for _ in names],
    "numFishmen": [random.randint(0, 2) for _ in names],
    "squimbleAndGwibble": [random.randint(1, 10) for _ in names],
    "trustworthy": [random.randint(1, 10) for _ in names],
    "phLevel": [random.randint(1, 10) for _ in names],
}
fishmanDataFrame = pd.DataFrame(fishmanData)
fishmanDataFrame.to_csv('dataFrame.csv', index=False)