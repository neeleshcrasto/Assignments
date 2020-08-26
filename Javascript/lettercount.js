//Counts the number of letters in string
letternos = 0;
function countChar(string, letter) {
	for (counter=0; counter<string.length; counter++) {
		if (string[counter]==letter) letternos++;
	}
	return letternos;
}

document.write(countChar("kakerlak", "k"))
