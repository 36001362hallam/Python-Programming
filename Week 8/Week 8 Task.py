from random import *
names = ["Al","Bruce","Casper","Dave","Ed"]
shuffle(names)
string = ""
for name in names:
    if(name == names[-1]):
        string = f"{string}and {name}"
    else:
        string = f"{string}{name}, "
string = f"{string}."
print(string)
