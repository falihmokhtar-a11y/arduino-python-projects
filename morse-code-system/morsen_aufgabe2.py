#Morse-Buchstaben werden durch Leerzeichen getrennt
# Wörter werden durch / getrennt

abc = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e',
       '..-.':'f','--.':'g','....':'h','..':'i','.---':'j',
       '-.-':'k','.-..':'l','--':'m','-.':'n','---':'o',
       '.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t',
       '..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y',
       '--..':'z','/':' ','.-.-':'ä','..--':'ü','.-.-.-':'.',
       '---.':'ö','----':'ch','-.-.--':'!','.-..-.':'"',
       '.----':'1','..---':'2','...--':'3','....-':'4','.....':'5',
       '-....':'6','--...':'7','---..':'8','----.':'9','-----':'0',
       '':'','---...':':','--..--':',','..--..':'?','-..-.':'/',
       '-....-':'-','-.--.':'(','-.--.-':')','-.-.-.':';','.----.':"'",
       '-...-':'\n'}

def decode(morse_code):
     # Ich entferne überflüssige Leerzeichen am Anfang und Ende
    words = morse_code.strip()
    # Ich trenne den Morsecode in einzelne Wörter (getrennt durch " / ")
    wordds = words.split(" / ")
    # Ich erstelle eine Liste für die dekodierte Nachricht
    decoded_message = []
    # Ich dekodiere jedes Wort einzeln
    for word in wordds:
        decoded_word = ''
        letters = word.split(" ") # Ich trenne die Buchstaben eines Wortes
        # Ich übersetze jeden Morsebuchstaben in einen normalen Buchstaben
        for letter in letters:
            if letter in abc:
                decoded_word += abc[letter]
        decoded_message.append(decoded_word)
    # Ich verbinde alle Wörter zu einem Text
    return ' '.join(decoded_message)

def encode(text):
    # Ich wandle den Text in Kleinbuchstaben um
    text = text.lower()
    encoded_message = []
    reverse_abc = {v: k for k, v in abc.items()} # Ich erstelle ein umgekehrtes Wörterbuch (Buchstabe → Morsecode)
    words = text.split(" ")
    # Ich kodiere jedes Wort einzeln
    for word in words: 
        encoded_word = ""
        # Ich kodiere jeden Buchstaben in Morsecode
        for char in word:
            if char in reverse_abc:
                encoded_word += reverse_abc[char] + " "
        encoded_message.append(encoded_word.strip()) # Ich füge das kodierte Wort zur Nachricht hinzu
    return " / ".join(encoded_message) # Ich trenne Wörter mit " / "

if __name__ == "__main__":
    # Hauptprogramm: Ich lasse den Benutzer auswählen, was er tun möchte
    while True:
        choice = input("Möchten Sie kodieren (e) oder dekodieren (d)? (q zum Beenden): ").lower()
        if choice == 'e': # Ich kodiere normalen Text in Morsecode
            text = input("Geben Sie den Text ein: ")
            encoded_message = encode(text)
            print("Morsecode:", encoded_message)
            continue
        elif choice == 'q': # Ich beende das Programm
            break
        elif choice == 'd': # Ich dekodiere Morsecode in normalen Text
            morse_code = input("Geben Sie den Morsecode ein: ")
            decoded_message = decode(morse_code)
            print("Entschlüsselter Text:", decoded_message)
            continue
        elif choice == 'q': #programm wird beendet
            break
        else:
            print("(?) Ungültige Eingabe. Bitte versuchen Sie es erneut.") # Ungültige Eingabe
            continue
                               