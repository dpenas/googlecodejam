def comparewords(text, i):
	finalresult = ""
	googlerese = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq"
	english = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz"
	for letter in range(len(text)):
		for exactletter in range(len(googlerese)):
			if (googlerese[exactletter] == text[letter]):
				finalresult = finalresult + english[exactletter]
				break
	print finalresult
	f = open("fileout.txt", 'a')
	f.write("Case #" + str(i) + ": " + finalresult + "\n")

def readFile(nameFile):
	i = 0
	f = open(nameFile, 'r')
	filetext = f.readline()
	while filetext:
		i +=1
		filetext = f.readline()
		print(filetext)
		if (filetext != "\n"):
			comparewords(filetext, i)
	f.close()
