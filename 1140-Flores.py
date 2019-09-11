while True:
	gay = input().lower().split()
	letter = gay[0][0]

	if letter == "*":
		break

	print(all(word[0] == letter for word in gay) and "Y" or "N")