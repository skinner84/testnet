count = 0

f = open("comments.txt", "r")
for line in f.readlines():
    words = line.split()
    for word in words:
        if str(word).lower() == "telcoin":
            count += 1
            print (word)
print (count)

