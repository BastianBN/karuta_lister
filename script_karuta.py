import argparse
text = ''
text = '\n'.join(iter(input, text))

lines = text.split("\n")

for line in lines:
    splitted_line = line.split(" · ")
    anime = splitted_line[4]
    print(line[2:9], end="")
    print(anime)
