import random

# Predefined list of 5 words
word_list = ['apple', 'tiger', 'house', 'chair', 'plant']
word = random.choice(word_list)  # Randomly pick one word

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Reveal the first letter
first_letter = word[0]
guessed_letters.append(first_letter)

# Create display word showing only the first letter
display_word = [first_letter if word[i] == first_letter else '_' for i in range(len(word))]

print("=== Welcome to Hangman ===")
print("Hint: The first letter is revealed to help you guess!")
print("You have 6 chances to make a wrong guess.")

while incorrect_guesses < max_guesses and '_' in display_word:
    print("\nWord: ", ' '.join(display_word))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_guesses - incorrect_guesses} guesses left.")

# Game Result
if '_' not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The correct word was:", word)
