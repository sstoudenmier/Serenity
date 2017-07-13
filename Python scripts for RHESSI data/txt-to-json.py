import json

header = True
contents = {}

with open("flare-list.txt") as infile:
    for line in infile:
        if header:
            for title in line.split():
                contents[title] = []
            header = False
            print(contents)
        else:
            counter = 0
            line = line.split()
            for title in contents:
                if title == "Start_Time":
                    contents[title].append("___".join(line[counter:counter+2]))
                    counter+=2
                    continue
                if title == "Flags":
                    contents[title].append(" ".join(line[counter:]))
                    continue
                contents[title].append(line[counter])
                counter+=1

with open("rhessi-flare-list.json", "w") as outfile:
    outfile.write(json.dumps(contents))
