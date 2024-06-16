import random

fail = 0
guess = []

def Choose_Movie():
    movie_list = open("D:/Studies/My Python/Hang Man/Files/Movies.txt", 'r')
    data = [line.strip() for line in movie_list]        #line.strip remove \n while reading the data
    list_size = (len(data))
    Movie_name = data[random.randint(0, (list_size-1))]
    movie_list.close()
    return Movie_name

def set_level(a):
    if a == 1:
        b = 9
    elif a == 3:
        b = 4
    else:
        b = 6
        print("As you have selected invalid option, the level is set to 2.")
    return b

def draw_noose(hang):
    if hang == 1:
        print("  _______\n |     |\n |   (x_X)\n |    /|\\\n |    / \\\n |      \n_|_")
    elif hang == 2:
        print("  _______\n |     |\n |   (O_O)\n |    /|\\\n |    / \\\n |      \n_|_")
    elif hang == 3:
        print("  _______\n |     |\n |   (-_-)\n |    /|\\\n |    / \\\n |      \n_|_")
    elif hang == 4:
        print("  _______\n |     |\n |   (-_-)\n |    /|\\\n |    / \n |      \n_|_")
    elif hang == 5:
        print(" _______\n |     |\n |   (-_-)\n |    /|\\\n |      \n |      \n_|_")
    elif hang == 6:
        print("  _______\n |     |\n |   (-_-)\n |    /|\n |      \n |      \n_|_")
    elif hang == 7:
        print("  _______\n |     |\n |   (-_-)\n |     |\n |      \n |      \n_|_")
    elif hang == 8:
        print("  _______\n |     |\n |   (-_-)\n |      \n |      \n |      \n_|_")
    elif hang == 9:
        print("  _______\n |     |\n |     \n |      \n |      \n |      \n_|_")
    else:
        print("Invalid hang value.")

def print_progress(words, movie):
    progress_so_far = []
    for char in movie:
        if char in words:
            progress_so_far.append(char)
            print(char, end='')
        elif char == ' ':
            progress_so_far.append(' ')
            print(' ', end='')
        else:
            progress_so_far.append('_')
            print('_', end='')
    
    print()  # To move to the next line after printing the progress
    return ''.join(progress_so_far)


totalTries = set_level(int(input("\n\nLet's play Hangman.\nEnter a level: 1 to 3.\n[Higher the number, lower the tries]: ")))
my_movie = Choose_Movie().upper()           # print(my_movie) # Cheat

while True:
    triesLeft = totalTries - fail 
    draw_noose(triesLeft)
    progress = print_progress(guess, my_movie)
    print("\nRemaining tries are: ", triesLeft)
    print("words used so far: ", guess)
    if my_movie == progress:
        print("\nCongratulations.!! You've guessed it in time.\nYou have scored ", (triesLeft*100.00)/ totalTries, "\n\n")
        break
    else:
        Playerguessword = input("Enter a letter..\n")
        player_char = Playerguessword[0].upper()
        guess.append(player_char)
    if player_char in my_movie:
        print(player_char, " - exists\n")
    else:
        fail += 1
        if fail == totalTries:
            print("\nGame Over (x_x)\n   The Movie was: ", my_movie, "\n\n")
            break
        else:
            print(player_char + " - Does not exist.")

# over





