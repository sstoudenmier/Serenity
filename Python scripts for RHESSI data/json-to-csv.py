import json

with open("rhessi-flare-list.json") as infile:
    contents = json.load(infile)
    headers = list(contents.keys())
    with open("rhessi-flare-list.csv", "w") as outfile:
        outfile.write(", ".join(headers) + "\n")
        for i in range(len(contents[headers[0]])):
            temp = []
            for title in headers:
                temp.append(contents[title][i])
            outfile.write(", ".join(temp) + "\n")
