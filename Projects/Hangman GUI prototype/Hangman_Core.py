import random
from tkinter import *

guess = []
images = []
fail = 0

def Choose_Movie():
    movie_list = open("Files/Movies.txt", 'r')
    data = [line.strip() for line in movie_list]        #line.strip remove \n while reading the data
    list_size = (len(data))
    Movie_name = data[random.randint(0, (list_size-1))]
    movie_list.close()
    return Movie_name.upper()

def draw_noose(hang, Drawing_Area):
    if hang == 1:
        Drawing = PhotoImage(file="Pics/Noose/H0.png")
    elif hang == 2:
        Drawing = PhotoImage(file="Pics/Noose/H1.png")
    elif hang == 3:
        Drawing = PhotoImage(file="Pics/Noose/H2.png")
    elif hang == 4:
        Drawing = PhotoImage(file="Pics/Noose/H3.png")
    elif hang == 5:
        Drawing = PhotoImage(file="Pics/Noose/H4.png")
    elif hang == 6:
        Drawing = PhotoImage(file="Pics/Noose/H5.png")
    elif hang == 7:
        Drawing = PhotoImage(file="Pics/Noose/H6.png")
    elif hang == 8:
        Drawing = PhotoImage(file="Pics/Noose/H7.png")
    elif hang == 9:
        Drawing = PhotoImage(file="Pics/Noose/H8.png")
    elif hang == 10:
        Drawing = PhotoImage(file="Pics/Noose/Victory.png")
    else:
        Drawing = PhotoImage(file="Pics/Noose/Game Over.png")
    images.append(Drawing)          # preventing garbage collector from destroying it
    Drawing_Area.config(image=Drawing)

def push_entry(my_movie, progress, Drawing_Area, Letter_entry, Total_Tries, Submit, Progress_So_Far_Label, Total_Tries_Left, Words_Used_Text):
    global fail
    Playerguessword = Letter_entry.get()
    print(progress)

    if len(Playerguessword) > 0:
        player_char = Playerguessword[0].upper()
        guess.append(player_char)
        Letter_entry.delete(0, 'end')
        
        if player_char in my_movie:
            progress = print_progress(guess, my_movie, Progress_So_Far_Label)
            Words_Used_Text.config(text = ' '.join(guess))
        else:
            fail += 1
            Words_Used_Text.config(text = ' '.join(guess))
        
            triesLeft = Total_Tries - fail
            Total_Tries_Left.config(text="Tries left: " + str(triesLeft))
            draw_noose(triesLeft, Drawing_Area)

        if my_movie == progress:            # need fixing
            draw_noose(10, Drawing_Area)
        elif fail == Total_Tries:
            draw_noose(0, Drawing_Area)
            Words_Used_Text.config(text = ' '.join(guess))
            Submit.config(state=DISABLED)
            print("Game Over (x_x)")
            Progress_So_Far_Label.config(text="Movie was: " + my_movie)
    

def print_progress(words, movie, Progress_So_Far_Label):
    progress_so_far = []
    for char in movie:
        if char in words:
            progress_so_far.append(char + ' ')
        elif char == ' ':
            progress_so_far.append('  ')
        else:
            progress_so_far.append('_ ')
    Progress_So_Far_Label.config(text=''.join(progress_so_far))
    return ''.join(progress_so_far)
    
def validate(P):
    if len(P) == 0:
        return True
    elif len(P) == 1:
        return True
    else:
        return False

def StartGame(Total_Tries, root, my_movie):
    
    global guess
    
    Total_Tries_Left = Label(root,text="Tries left: " + str(Total_Tries), background="#dffddf", font=("Comic Sans MS", 20, 'italic'), compound=CENTER)
    Total_Tries_Left.place(x = 50, y = 50, width=200, height=50)

    Progress_So_Far_Label = Label(root, background="#dffddf", font=("Comic Sans MS", 35, 'bold'))
    Progress_So_Far_Label.place(x = 75, y = 520, width=930, height=150)
    progress = print_progress(guess, my_movie, Progress_So_Far_Label)

    Input_Board = Label(root, background="#dffddf", font=("Comic Sans MS", 15, 'bold'))
    Input_Board.place(x = 50, y = 130, width=200, height=350)

    vcmd = (root.register(validate), '%P')
    Letter_entry = Entry(Input_Board,validate="key", validatecommand=vcmd, font=("ariel", 75, "bold"))
    Letter_entry.place(x = 50, y = 120, width=100, height=100)

    Submit = Button(Input_Board, text="Submit a Letter", command=lambda: push_entry(my_movie, progress, Drawing_Area, Letter_entry, Total_Tries, Submit, Progress_So_Far_Label, Total_Tries_Left, Words_Used_Text))
    Submit.place(x= 50, y = 235, width=100, height= 30)

    Drawing_Area = Label(root, background="#dffddf")
    Drawing_Area.place(x = 300, y = 50, width=430, height=430)
    draw_noose(Total_Tries, Drawing_Area)

    Words_Used_Board = Label(root, background="#dffddf")
    Words_Used_Board.place(x = 780, y = 50, width=250, height=430)

    Words_Used_Text_1 = Label(Words_Used_Board, text="Words used: ", background="#dffddf", font=("Papyrus", 30, "bold"), compound=TOP)
    Words_Used_Text_1.place(y=10)

    Words_Used_Text = Label(Words_Used_Board, background="#dffddf", font=("Ink Free", 30, "bold"), wraplength=200)
    Words_Used_Text.place(y=70, x= 10, height = 350)