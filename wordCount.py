import sys
import re

in_file = sys.argv[1]
out_file = sys.argv[2]

word_count = {}

with open(in_file, 'r') as f:
    data = f.read()
f.close()

data = data.lower()
data = re.sub(r'[^\w\s]', ' ', data)
data = data.split()

for word in data:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

f = open(out_file, "w")
for key, value in sorted(word_count.items()):
    f.write(f"{key} {value}\n")
f.close()
