MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}
def morse_to_text(morse_code):
    text = ''
    for code in morse_code.split(' '):
        if code in REVERSE_MORSE_CODE_DICT:
            text += REVERSE_MORSE_CODE_DICT[code]
        elif code == '':
            text += ' '
        else:
            print(f"Kode morse {code} tidak dikenal, kode morse ini akan diabaikan")
    return text

def text_to_morse(text):
    morse_code= []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        elif char == ' ':
            morse_code.append(' ')
        else:
            print(f"Karakter {char} tidak dikenal, karakter ini akan diabaikan")
    return ' '.join(morse_code)

while True:
    choice = input("Pilih konversi yang ingin dilakukan (1. Text ke Morse, 2. Morse ke Text) : ")
    if choice == '1':
        text = input("Masukkan teks yang ingin dikonversi ke Morse: ")
        print(f"Hasil konversi: {text_to_morse(text)}")
    elif choice == '2':
        morse_code = input("Masukkan kode morse yang ingin dikonversi ke teks: ")
        print(f"Hasil konversi: {morse_to_text(morse_code)}")
    else:
        print("Pilihan tidak valid")

    another_conversion = input("Apakah ingin melakukan konversi lagi? (y/n): ")
    if another_conversion.lower() != 'y':
        break