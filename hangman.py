import random
from string import ascii_lowercase
print('H A N G M A N')
start = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
again = ["play", "results", "exit"]
i=0
j=0
while start in again:

    if start == "play":
        word = random.choice(['python', 'java', 'swift', 'javascript'])
        s = set()
        w = set()
        lives = 8
        while lives > 0:
            print()
            for k in word:
                if k in s:
                    print(k, end='')
                else:
                    print('-', end='')
            print()
            print('Input a letter: ', end='')
            n = input()
            if n not in word and n not in w and n in ascii_lowercase:
                print("That letter doesn't appear in the word.")
                lives -= 1
                w.add(n)
            elif n in w:
                print("You've already guessed this letter.")
                lives -= 0
            elif n in s:
                print("You've already guessed this letter.")
                lives -= 0
            elif len(n) > 1:
                print("Please, input a single letter.")
                lives -= 0
            elif n not in ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
                lives -= 0
            elif n == "":
                print("Please, input a single letter.")
                lives -= 0
            else:
                s.add(n)
            if set(word) == s:
                j += 1
                print('You guessed the word ' + word +'!\nYou survived!')
                
                break
                start = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if lives == 0:
            i +=1
            print("You lost!")
            
        start = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if start == "play":
        continue
    if start == "results":
        print(f'You lost: {i} times')
        print(f'You won: {j} times')
        start = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if start == "exit":
        break


