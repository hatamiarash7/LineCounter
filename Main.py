import glob
from Counter import Counter

file_list = glob.glob("*.py")

c =  Counter(file_list)

print(str(c.count()))