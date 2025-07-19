def format_text(text, width=50):
    # Bold text using ANSI escape codes
    bold_text = f"\033[1m{text}\033[0m"
    
    # Center justify the bold text within the width
    justified = bold_text.center(width)
    
    return justified

if __name__ == "__main__":
    message = "NRE A KUNO NRE...PARA NI"
    print(format_text(message))
import random

def play_game():
    number_to_guess = random.randint(1, 100)
    max_guesses = 15
    guess_count = 0

    print("\n🎯 de 1 r pe 100 r vitrt nmbr eta vabek.")
    print(f"tuhak {max_guesses} bar chnch dm vbba...para jdi vbi uilo!")

    while guess_count < max_guesses:
        try:
            if guess_count == 0:
                guess = int(input(f"\nchnch no {guess_count + 1 } de ko: "))
            else:
                guess = int(input(f"\nei {guess_count + 1} bar hl a...para ni! de ko aro😏 "))
            if guess_count == 4:
                guess = int(input(f"\nei {guess_count + 1 }bar hl a....nhbo a haka tr darai..ko holio aro: "))
            
            guess_count += 1

            if guess < number_to_guess:
                print("🔻 besi xoru hy gl haka!")
            elif guess > number_to_guess:
                print("🔺 besi vbsa😒!")
            else:
                print(f"✅ amr eao sb janne njna ktha ni haka.... {guess_count} bar t holio miloisi.")
                break
        except ValueError:
            print("kiba koli kiba kra...buji npo nki bl")
    else:
        print(f"\n😢 nlge ja khelba....ghume thk {number_to_guess}bar dlu a kba.")

def main():
    while True:
        play_game()
        again = input("\n🔁 khlbi na ki aro? (yes/no): ").lower()
        if again not in ('yes', 'y'):
            print("👋 ja hb ja kam ni")
            break

if __name__ == "__main__":
    main()