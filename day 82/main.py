import sys
import argparse
import time
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', '!': '-.-.--'
}
REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}
COLOR_TITLE = '\033[95m'   
COLOR_CYAN = '\033[96m'    
COLOR_GREEN = '\033[92m'   
COLOR_YELLOW = '\033[93m'  
COLOR_RED = '\033[91m'    
COLOR_RESET = '\033[0m'

def print_header():
    """Prints the application banner."""
    header = f"""
{COLOR_TITLE}=======================================================
 __  __                                 ____          _      
|  \/  |  ___   _ __  ___   ___        / ___|  ___   __| | ___ 
| |\/| | / _ \ | '__|/ __| / _ \      | |     / _ \ / _` |/ _ \\
| |  | || (_) || |   \__ \|  __/      | |___ | (_) | (_| |  __/
|_|  |_| \___/ |_|   |___/ \___|       \____| \___/ \__,_|\___|
                                                               
======================================================={COLOR_RESET}
    """
    print(header)

def text_to_morse(text: str) -> str:
    """Converts standard text to Morse code."""
    text = text.upper()
    words = text.split(' ')
    morse_words = []
    
    for word in words:
        morse_chars = []
        for char in word:
            if char in MORSE_CODE_DICT:
                morse_chars.append(MORSE_CODE_DICT[char])
            else:
                morse_chars.append(char)
        morse_words.append(' '.join(morse_chars))
    return '   '.join(morse_words)

def morse_to_text(morse: str) -> str:
    """Converts Morse code back to text."""
    morse = morse.replace(' / ', '   ')
    words = morse.split('   ')
    text_words = []
    
    for word in words:
        chars = word.split(' ')
        text_chars = []
        for char in chars:
            if not char:
                continue
            if char in REVERSE_MORSE_DICT:
                text_chars.append(REVERSE_MORSE_DICT[char])
            else:
                text_chars.append(char)
        text_words.append(''.join(text_chars))
        
    return ' '.join(text_words)

def play_audio(morse_code: str):
    """Plays Morse code as audio beeps on Windows systems."""
    try:
        import winsound:
        freq = 750  
        dot_duration = 150  
        dash_duration = 450 
        symbol_gap = 0.15 
        letter_gap = 0.35 
        word_gap = 0.8 
        
        print(f"\n{COLOR_CYAN}[Playing Morse Code Audio...]{COLOR_RESET}")
        
        words = morse_code.split('   ')
        for word in words:
            letters = word.split(' ')
            for letter in letters:
                for symbol in letter:
                    if symbol == '.':
                        winsound.Beep(freq, dot_duration)
                    elif symbol == '-':
                        winsound.Beep(freq, dash_duration)
                    time.sleep(symbol_gap)
                time.sleep(letter_gap)
            time.sleep(word_gap)
            
        print(f"{COLOR_GREEN}[Playback finished]{COLOR_RESET}")
    except ImportError:
        print(f"\n{COLOR_RED}[Error] Audio playback requires winsound (Windows only).{COLOR_RESET}")
    except Exception as e:
        print(f"\n{COLOR_RED}[Error] Playback failed: {e}{COLOR_RESET}")

def interactive_mode():
    """Runs the interactive console translator."""
    print_header()
    print(f"{COLOR_CYAN}Welcome to the Morse Code Translator!{COLOR_RESET}")
    print("Commands:")
    print(f"  {COLOR_YELLOW}/t{COLOR_RESET} - Switch to: Text -> Morse")
    print(f"  {COLOR_YELLOW}/m{COLOR_RESET} - Switch to: Morse -> Text")
    print(f"  {COLOR_YELLOW}/q{COLOR_RESET} - Quit the program")
    print("-" * 55)
    
    current_mode = 'text_to_morse'
    
    while True:
        mode_name = "Text to Morse" if current_mode == 'text_to_morse' else "Morse to Text"
        prompt = f"\n{COLOR_CYAN}[{mode_name}]{COLOR_RESET} Enter input:\n>> "
        
        try:
            user_input = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{COLOR_YELLOW}Exiting Morse Code Translator. Goodbye!{COLOR_RESET}")
            break
            
        if not user_input:
            continue
            
        if user_input.lower() == '/q':
            print(f"{COLOR_YELLOW}Exiting Morse Code Translator. Goodbye!{COLOR_RESET}")
            break
        elif user_input.lower() == '/t':
            current_mode = 'text_to_morse'
            print(f"{COLOR_GREEN}Switched to Text to Morse mode.{COLOR_RESET}")
            continue
        elif user_input.lower() == '/m':
            current_mode = 'morse_to_text'
            print(f"{COLOR_GREEN}Switched to Morse to Text mode.{COLOR_RESET}")
            continue
            
        if current_mode == 'text_to_morse':
            translated = text_to_morse(user_input)
            print(f"\n{COLOR_GREEN}Morse Code:{COLOR_RESET}")
            print(f"{COLOR_YELLOW}{translated}{COLOR_RESET}")
            
            # Interactive audio prompt for Windows users
            if sys.platform == 'win32':
                play_choice = input(f"\nPlay audio beep sequence? (y/N): ").strip().lower()
                if play_choice == 'y':
                    play_audio(translated)
        else:
            translated = morse_to_text(user_input)
            print(f"\n{COLOR_GREEN}Decoded Text:{COLOR_RESET}")
            print(f"{COLOR_YELLOW}{translated}{COLOR_RESET}")

def main():
    parser = argparse.ArgumentParser(
        description="Translate text to Morse code and vice-versa, with optional audio playback on Windows."
    )
    parser.add_argument(
        'input_string', 
        type=str, 
        nargs='?', 
        help="Input text or Morse code string to translate. If omitted, starts interactive mode."
    )
    parser.add_argument(
        '-r', '--reverse', 
        action='store_true', 
        help="Reverse translation: Morse code to plain text."
    )
    parser.add_argument(
        '-p', '--play', 
        action='store_true', 
        help="Play translated Morse code as audio (Windows only)."
    )
    
    args = parser.parse_args()
    if sys.platform == 'win32':
        import os
        os.system('')
        
    if args.input_string is None:
        interactive_mode()
    else:
        if args.reverse:
            result = morse_to_text(args.input_string)
            print(result)
        else:
            result = text_to_morse(args.input_string)
            print(result)
            if args.play:
                play_audio(result)

if __name__ == '__main__':
    main()
