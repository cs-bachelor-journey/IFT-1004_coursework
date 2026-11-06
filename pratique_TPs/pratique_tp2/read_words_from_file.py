
ACCENTS = {
    "à": "a", "â": "a", "ä": "a",
    "é": "e", "è": "e", "ê": "e", "ë": "e",
    "î": "i", "ï": "i",
    "ô": "o", "ö": "o",
    "ù": "u", "û": "u", "ü": "u",
    "ç": "c",
}

def correct_format(word):
    
    new_word = word.strip()
    newest_word = ""
    
    for letter in new_word:
        
        if letter in ACCENTS:
            letter = ACCENTS[letter]
        
        newest_word += letter
    
    return newest_word

with open("word.txt", "r", encoding="utf-8") as fichier:
    count = 0
    
    for ligne in fichier:
        if ligne != "":
            count += 1
            print(f"{count} - Without accents: {correct_format(ligne)}. With accents: {ligne}")