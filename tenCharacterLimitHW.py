f = open("input.txt","r+")
fo = open("output.txt","w")

eachLines = f.readlines()

for line in eachLines:
	actual = len(line)
	leftOver = actual - 10
	if actual >= 11:
		line = line[:-leftOver]
		fo.write(line + "\n")
	else:
		fo.write(line)