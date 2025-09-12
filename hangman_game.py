import random
words = (
    "apple", "orange", "banana", "coconut", "pineapple", "grape", "melon", "cherry", "pear", "peach",
    "dog", "cat", "lion", "tiger", "elephant", "giraffe", "zebra", "monkey", "horse", "rabbit",
    "car", "bus", "train", "bicycle", "motorcycle", "truck", "airplane", "helicopter", "boat", "ship",
    "table", "chair", "sofa", "bed", "lamp", "desk", "mirror", "carpet", "shelf", "door",
    "house", "apartment", "castle", "hut", "palace", "cabin", "tent", "skyscraper", "farm", "garage",
    "book", "pen", "pencil", "paper", "notebook", "eraser", "marker", "ruler", "calculator", "folder",
    "computer", "laptop", "keyboard", "mouse", "monitor", "printer", "phone", "tablet", "camera", "television",
    "paris", "london", "berlin", "madrid", "rome", "vienna", "prague", "tokyo", "beijing", "sydney",
    "happy", "sad", "angry", "tired", "excited", "calm", "brave", "scared", "kind", "friendly",
    "run", "walk", "jump", "swim", "fly", "read", "write", "sing", "dance", "play",
    "football", "basketball", "tennis", "golf", "baseball", "cricket", "rugby", "hockey", "boxing", "cycling",
    "red", "blue", "green", "yellow", "purple", "orange", "black", "white", "brown", "pink",
    "sun", "moon", "star", "planet", "galaxy", "universe", "cloud", "rain", "snow", "wind",
    "water", "fire", "earth", "air", "metal", "wood", "stone", "sand", "glass", "gold",
    "music", "art", "science", "history", "math", "language", "physics", "chemistry", "biology", "geography"
)

hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\",
                  "   "),
               5:(" o ",
                  "/|\\",
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \ ")}

def display_man(wrong_guesses):
    print("************")
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer =  random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess =  input("Enter a letter: ").lower()

        if len(guess) !=1 or guess.isalpha()==False:
            print("Invalid input")
            continue


        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False

        elif wrong_guesses>=len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()