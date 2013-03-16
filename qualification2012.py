def comparewords(text):
	finalresult = ""
	googlerese = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
	english = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
	for letter in range(len(text)):
		for exactletter in range(len(googlerese)):
			if (googlerese[exactletter] == text[letter]):
				finalresult = finalresult + english[exactletter]
				break
	return finalresult
