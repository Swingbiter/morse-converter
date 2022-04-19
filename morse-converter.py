morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

def phrase_to_morse(phrase):
    
    morse_phrase = "";

    words = phrase.split(" ")

    for word in words:
        converted_word = "";
        for letter in word:
            if letter.lower() in morse.keys():
                converted_word += morse[letter.lower()] + "_"
        morse_phrase += converted_word + " "
    
    return morse_phrase.strip()


def morse_to_phrase(morse_phrase):
    phrase = "";
    words = morse_phrase.split(" ")

    for word in words:
        converted_word = "";
        letters = word.split("_")
        for letter in letters:
            if letter in morse.values():
                # flip keys and values in morse dict
                morse_to_text = {morse[l]: l for l in morse.keys()}
                converted_word += morse_to_text[letter]
        phrase += converted_word + " "
    
    return phrase.strip()


def run_converter():
    while True:
        
        user_input = input("Enter 1 for Text To Morse\n2 for Morse To Text: ")

        if user_input == "1":
            user_input = input("Enter phrase: ")
            print(phrase_to_morse(user_input))
        elif user_input == "2":
            user_input = input("Enter morse: ")
            print(morse_to_phrase(user_input))
        else:
            print("Invalid option selected. Please try again.")
        

        user_input = input("Would you like to continue? y / n : ")
        if user_input.lower() != "y":
            break;

if __name__ == "__main__":
    run_converter()
