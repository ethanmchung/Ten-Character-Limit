f = open("input.txt","r")
fo = open("output.txt","w")

eachLines = f.readlines()
f.close()

for line in eachLines:
	actual = len(line)
	leftOver = actual - 10 #leftOver is the left over characters that exceed the limited 10
	if actual > 10:
		line = line[:-leftOver]
		fo.write(line + "\n")
	else:
		fo.write(line)

fo.close()