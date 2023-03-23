# DOCUMENTATION
# Window Resolution: 1280x720
# More in README.md

# Library Imports
from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from time import sleep
from random import randint as rand

# Global Variables
LEFT_KEY = "A"
RIGHT_KEY = "D"

SCORE = 0
NAME = "unnamed"
LIVES = 5
SHIELDS = 0
SPECIAL_WEAPON = False
SPECIAL_WEAPON_FRAMES = 0
SCORE_BOOST = False
SCORE_BOOST_FRAMES = 0
GAME_PAUSE = 0

IN_BOSS_WINDOW = False

MOVE_LEFT = False
MOVING_LEFT_1 = False
MOVING_LEFT_2 = False
MOVING_LEFT_3 = False
MOVE_RIGHT = False
MOVING_RIGHT_1 = False
MOVING_RIGHT_2 = False
MOVING_RIGHT_3 = False

LEADERBOARD_SCORE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LEADERBOARD_NAMES = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
LEADERBOARD_INDEX = 0
LOADED_GAME = False
RESET_HOWTO = False

GAME_FRAMES = 0

# Leaderboard Import
scores = open("Files/leaderboard_score.txt", "r")
names = open("Files/leaderboard_names.txt", "r")

while True:
    score = scores.readline()
    name = names.readline()
    if not score and not name:
        break
    LEADERBOARD_SCORE[LEADERBOARD_INDEX] = score.strip()
    LEADERBOARD_NAMES[LEADERBOARD_INDEX] = name.strip()
    LEADERBOARD_INDEX += 1

# Create Root
root = Tk()
root.title("Galaxy Attack")
root.iconbitmap('Assets/game_icon.ico')
w = 1280
h = 720
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y-50))
canvas = Canvas(root, width= 1280, height=720, relief='ridge', highlightthickness=0)
root.wm_attributes('-transparentcolor', '#ab23ff')
#root.wm_attributes('-fullscreen', 'True') # change for showcase
canvas.pack()

# Canvas-dependent Global Variables
LEFT_INPUT = StringVar()
RIGHT_INPUT = StringVar()
GET_NAME = StringVar()

# Image Imports
boss_img = ImageTk.PhotoImage(Image.open("Assets/bosskey.png"))
player_img = PhotoImage(file="Assets/playershadow.png")
player_left1_img = PhotoImage(file="Assets/playerleft1shadow.png")
player_left2_img = PhotoImage(file="Assets/playerleft2shadow.png")
player_right1_img = PhotoImage(file="Assets/playerright1shadow.png")
player_right2_img = PhotoImage(file="Assets/playerright2shadow.png")

enemy1_img = PhotoImage(file="Assets/enemy1.png")
enemy2_img = PhotoImage(file="Assets/enemy2.png")
enemy3_img = PhotoImage(file="Assets/enemy3.png")

powerup1_img = PhotoImage(file="Assets/powerup1.png")
powerup2_img = PhotoImage(file="Assets/powerup2.png")
powerup3_img = PhotoImage(file="Assets/powerup3.png")
powerup4_img = PhotoImage(file="Assets/powerup4.png")
powerup5_img = PhotoImage(file="Assets/powerup5.png")

projectile_img = PhotoImage(file="Assets/projectile.png")
adv_projectile_img = PhotoImage(file="Assets/adv_projectile.png")
energy_shield_img = PhotoImage(file="Assets/energyshield.png")
reward_img = PhotoImage(file="Assets/reward.png")

exhaust_skin1 = PhotoImage(file="Assets/exhaust1.png")
exhaust_skin2 = PhotoImage(file="Assets/exhaust2.png")
exhaust_skin3 = PhotoImage(file="Assets/exhaust3.png")
exhaust_skin4 = PhotoImage(file="Assets/exhaust4.png")
exhaust_skin5 = PhotoImage(file="Assets/exhaust5.png")
exhaust_skin6 = PhotoImage(file="Assets/exhaust6.png")

playbutton_img = PhotoImage(file="Assets/playbutton.png")
loadbutton_img = PhotoImage(file="Assets/loadbutton.png")
howtobutton_img = PhotoImage(file="Assets/howtobutton.png")
quitbutton_img = PhotoImage(file="Assets/quitbutton.png")
resetbutton_img = PhotoImage(file="Assets/resetbutton.png")
pausebutton_img = PhotoImage(file="Assets/pausebutton.png")
returntomenu_img = PhotoImage(file="Assets/returntomenubutton.png")

updatenamebutton_img = PhotoImage(file="Assets/updatename.png")
updateleft_img = PhotoImage(file="Assets/updateleft.png")
updateright_img = PhotoImage(file="Assets/updateright.png")

back_button = PhotoImage(file="Assets/backbutton.png")
slot1button_img = PhotoImage(file="Assets/slot1_button.png")
slot2button_img = PhotoImage(file="Assets/slot2_button.png")
slot3button_img = PhotoImage(file="Assets/slot3_button.png")
erase_img = PhotoImage(file="Assets/erasebutton.png")
exitbutton_img = PhotoImage(file="Assets/exitbutton.png")
savebutton_img = PhotoImage(file="Assets/savebutton.png")
resumebutton_img = PhotoImage(file="Assets/resumebutton.png")

background_img = ImageTk.PhotoImage(Image.open("Assets/background.png"))
in_game_bg_img = ImageTk.PhotoImage(Image.open("Assets/in_game_bg.png"))
menu_bg_img = ImageTk.PhotoImage(Image.open("Assets/background_menu.png"))
howto_bg_img = ImageTk.PhotoImage(Image.open("Assets/howto_bg.png"))
load_bg_img = ImageTk.PhotoImage(Image.open("Assets/load_bg2.png"))
pause_bg_img = ImageTk.PhotoImage(Image.open("Assets/pause_bg.png"))
save_bg_img = ImageTk.PhotoImage(Image.open("Assets/save_bg.png"))
gameover_bg_img = ImageTk.PhotoImage(Image.open("Assets/gameover_bg.png"))

ini_name_img = Image.open("Assets/name.png")
name_img = ImageTk.PhotoImage(ini_name_img)
ini_controls_img = Image.open("Assets/controls.png")
controls_img = ImageTk.PhotoImage(ini_name_img)

def create_background():
    canvas.create_image(0, 0, image= background_img, anchor=NW)
def create_in_game_bg():
    canvas.create_image(0, 0, image= in_game_bg_img, anchor=NW)
def create_menu_bg():
    canvas.create_image(0, 0, image= menu_bg_img, anchor=NW)
def create_howto_bg():
    canvas.create_image(0, 0, image= howto_bg_img, anchor=NW)
def create_load_bg():
    canvas.create_image(0, 0, image= load_bg_img, anchor=NW) 
def create_gameover_bg():
    canvas.create_image(0, 0, image= gameover_bg_img, anchor=NW) 
    
# Main function
def menu(event):
    global NAME
    global LIVES
    global SHIELDS
    global SPECIAL_WEAPON
    global SPECIAL_WEAPON_FRAMES
    global SCORE_BOOST
    global SCORE_BOOST_FRAMES
    global GET_NAME
    global LEFT_KEY
    global RIGHT_KEY
    global LOADED_GAME
    global current_lives
    
    GET_NAME.set("")
    
    for stuff in canvas.winfo_children():
            stuff.destroy()
    canvas.delete('all')
    
    # place background
    create_menu_bg()
    
    # Reset data
    if not LOADED_GAME:
        NAME = 'unnamed'
        LEFT_KEY = 'A'
        RIGHT_KEY = 'D'
        LIVES = 5
        SHIELDS = 0
        SPECIAL_WEAPON = False
        SPECIAL_WEAPON_FRAMES = 0
        SCORE_BOOST = False
        SCORE_BOOST_FRAMES = 0 
        current_lives = 5
    #TESTING: 
    print(NAME, LEFT_KEY, RIGHT_KEY, LIVES, SHIELDS, SPECIAL_WEAPON, SPECIAL_WEAPON_FRAMES, SCORE_BOOST, SCORE_BOOST_FRAMES)
    # play button
    play_button = canvas.create_image(38, 122, image=playbutton_img)
    canvas.moveto(play_button, 305, 330)
    canvas.tag_bind(play_button, '<Button-1>', lambda event: start_game('<event>'))
    
    # load button
    load_button = canvas.create_image(38, 122, image=loadbutton_img)
    canvas.moveto(load_button, 305, 380)
    canvas.tag_bind(load_button, '<Button-1>', lambda event: load_screen('<event>'))
    
    # input current name 
    label_nameEntry = Label(canvas, image=name_img, borderwidth=0, text = f"{NAME}", font="PIXSPACE-DEMO 16", fg="#47d4f9", bg="#161f28", activebackground="#161f28", compound=tk.CENTER)
    label_nameEntry.place(x= 490, y= 325, height= 100, width=170)
    
    entry_nameEntry = Entry(canvas, textvariable= GET_NAME, background="#141414", foreground="#47d4f9", font="PIXSPACE-DEMO 13", justify=tk.CENTER)
    entry_nameEntry.place(x= 550, y= 395, height= 25, width= 45)
    
    submit_name = canvas.create_image(38, 122, image=updatenamebutton_img)
    canvas.moveto(submit_name, 513, 425)
    canvas.tag_bind(submit_name, '<Button-1>', lambda event: update_name('<event>'))
    
    # reset game data 
    reset_button = canvas.create_image(38, 122, image=resetbutton_img)
    canvas.moveto(reset_button, 305, 480)
    canvas.tag_bind(reset_button, '<Button-1>', lambda event: reset_game('<event>'))
    
    # how to button
    howto_button = canvas.create_image(38, 122, image=howtobutton_img)
    canvas.moveto(howto_button, 305, 430)
    canvas.tag_bind(howto_button, '<Button-1>', lambda event: how_to('<event>'))
    
    # Quit button
    quit_button = canvas.create_image(38, 122, image=quitbutton_img)
    canvas.moveto(quit_button, 305, 530)
    canvas.tag_bind(quit_button, '<Button-1>', lambda event: quit('<event>'))
    
    # leaderboard 
    def write_leaderboard(): 
        global score
        global name
        
        canvas.create_text(925, 350, text="Leaderboard", fill="#47d4f9", font=('PIXSPACE-DEMO 18'))
        data_x = 953
        data_y = 392
        # import leaderboard scores
        leaderboard_score = open("Files/leaderboard_score.txt", "r")
        leaderboard_names = open("Files/leaderboard_names.txt", "r")
        while True: 
            score = leaderboard_score.readline()
            name = leaderboard_names.readline()
            if not score and not name:
                break
            canvas.create_text(data_x-50, data_y, text = f"{name}", fill= "white", font=('PIXSPACE-DEMO 13'))
            canvas.create_text(data_x, data_y, text = f"{score}", fill= "white", font=('PIXSPACE-DEMO 13'))
            data_y += 20
            
    write_leaderboard()
    
    #keybinds
    controls_label = Label(canvas, text = f"Left - {LEFT_KEY} | Right - {RIGHT_KEY}", image=controls_img, borderwidth=0, font="PIXSPACE-DEMO 11", fg="#47d4f9", bg="#161f28",activebackground="#161f28", compound=tk.CENTER)
    controls_label.place(x=490, y=460, height=60, width=170)
    
    # buttons for entry of left input 
    entry_moveLeft = Entry(canvas, textvariable= LEFT_INPUT, background="#141414", foreground="#47d4f9", font="PIXSPACE-DEMO 10", justify=tk.CENTER)
    entry_moveLeft.place(x=523, y= 507, height= 20, width= 30)
    
    submit_left_button = canvas.create_image(36, 70, image=updateleft_img)
    canvas.moveto(submit_left_button, 503, 532)
    canvas.tag_bind(submit_left_button, '<Button-1>', lambda event: update_controls('<event>', 1))
    
    # buttons for entry of right input
    entryMoveRight = Entry(canvas, textvariable= RIGHT_INPUT, background="#141414", foreground="#47d4f9", font="PIXSPACE-DEMO 10", justify=tk.CENTER)
    entryMoveRight.place(x= 596, y= 507, height= 20, width= 30)
    
    submit_left_button = canvas.create_image(36, 70, image=updateleft_img)
    canvas.moveto(submit_left_button, 576, 532)
    canvas.tag_bind(submit_left_button, '<Button-1>', lambda event: update_controls('<event>', 2))
    
    def clear_frame():
        for stuff in canvas.winfo_children():
            stuff.destroy()
        canvas.delete('all')
    
    def load_screen(event):
        for stuff in canvas.winfo_children():
            stuff.destroy()
        create_load_bg()
        
        save_slot1_btn = canvas.create_image(38, 122, image=loadbutton_img)
        canvas.moveto(save_slot1_btn, 163, 498)
        canvas.tag_bind(save_slot1_btn, '<Button-1>', lambda event: load_slot1('<event>'))
        
        save_slot2_btn = canvas.create_image(38, 122, image=loadbutton_img)
        canvas.moveto(save_slot2_btn, 515, 498)
        canvas.tag_bind(save_slot2_btn, '<Button-1>', lambda event: load_slot2('<event>'))
        
        save_slot3_btn = canvas.create_image(38, 122, image=loadbutton_img)
        canvas.moveto(save_slot3_btn, 870, 498)
        canvas.tag_bind(save_slot3_btn, '<Button-1>', lambda event: load_slot3('<event>'))
        
        delete_slot1_btn = canvas.create_image(38, 122, image=erase_img)
        canvas.moveto(delete_slot1_btn, 290, 498)
        canvas.tag_bind(delete_slot1_btn, '<Button-1>', lambda event: delete_slot1('<event>'))
        
        delete_slot2_btn = canvas.create_image(38, 122, image=erase_img)
        canvas.moveto(delete_slot2_btn, 642, 498)
        canvas.tag_bind(delete_slot2_btn, '<Button-1>', lambda event: delete_slot2('<event>'))
        
        delete_slot3_btn = canvas.create_image(38, 122, image=erase_img)
        canvas.moveto(delete_slot3_btn, 997, 498)
        canvas.tag_bind(delete_slot3_btn, '<Button-1>', lambda event: delete_slot3('<event>'))
        
        load_back_btn = canvas.create_image(38, 122, image=back_button)
        canvas.moveto(load_back_btn, 100, 630)
        canvas.tag_bind(load_back_btn, '<Button-1>', lambda event: back_to_game('<event>'))
        
        def back_to_game(event):
            for stuff in canvas.winfo_children():
                stuff.destroy()
            canvas.delete('all')
            menu('<event>')
        
        def load_slot1(event):
            global LOADED_GAME
            global LIVES
            global SCORE
            global SHIELDS
            global SPECIAL_WEAPON
            global SPECIAL_WEAPON_FRAMES
            global SCORE_BOOST
            global SCORE_BOOST_FRAMES
            global LEFT_KEY
            global RIGHT_KEY
            global NAME
            global current_lives
            
            LOADED_GAME = True
            with open("Files/save_slot1.txt", 'r') as save_file1:
                left_key_local = save_file1.readline().strip()
                if left_key_local == '':
                    messagebox.showerror("Error", "Save Slot 1 is empty.")
                    LIVES = 5
                    SCORE = 0
                    SHIELDS = 0
                    SPECIAL_WEAPON = False
                    SPECIAL_WEAPON_FRAMES = 0
                    SCORE_BOOST = False
                    SCORE_BOOST_FRAMES = 0
                    return
                LEFT_KEY = left_key_local
                RIGHT_KEY = save_file1.readline().strip()
                SCORE = int(save_file1.readline().strip())
                NAME = save_file1.readline().strip()
                LIVES = int(save_file1.readline().strip())
                current_lives = LIVES
                SHIELDS = int(save_file1.readline().strip())
                
                weapon_frames = save_file1.readline().strip().lower()           
                if weapon_frames == 'true':
                    SPECIAL_WEAPON = True
                elif weapon_frames == 'false':
                    SPECIAL_WEAPON = False
                    
                SPECIAL_WEAPON_FRAMES = int(save_file1.readline().strip())

                score_frames = save_file1.readline().strip().lower()           
                if score_frames == 'true':
                    SCORE_BOOST = True
                elif score_frames == 'false':
                    SCORE_BOOST = False
                
                SCORE_BOOST_FRAMES = int(save_file1.readline().strip())   
            messagebox.showinfo("Update", "Game loaded succesfully.")
        def load_slot2(event):
            global LOADED_GAME
            global LIVES
            global SCORE
            global SHIELDS
            global SPECIAL_WEAPON
            global SPECIAL_WEAPON_FRAMES
            global SCORE_BOOST
            global SCORE_BOOST_FRAMES
            global LEFT_KEY
            global RIGHT_KEY
            global NAME
            global current_lives
            
            LOADED_GAME = True
            with open("Files/save_slot2.txt", 'r') as save_file1:
                left_key_local = save_file1.readline().strip()
                if left_key_local == '':
                    messagebox.showerror("Error", "Save Slot 2 is empty.")
                    LIVES = 5
                    SCORE = 0
                    SHIELDS = 0
                    SPECIAL_WEAPON = False
                    SPECIAL_WEAPON_FRAMES = 0
                    SCORE_BOOST = False
                    SCORE_BOOST_FRAMES = 0
                    return
                LEFT_KEY = left_key_local
                RIGHT_KEY = save_file1.readline().strip()
                SCORE = int(save_file1.readline().strip())
                NAME = save_file1.readline().strip()
                LIVES = int(save_file1.readline().strip())
                current_lives = LIVES
                SHIELDS = int(save_file1.readline().strip())
                
                weapon_frames = save_file1.readline().strip().lower()           
                if weapon_frames == 'true':
                    SPECIAL_WEAPON = True
                elif weapon_frames == 'false':
                    SPECIAL_WEAPON = False
                    
                SPECIAL_WEAPON_FRAMES = int(save_file1.readline().strip())

                score_frames = save_file1.readline().strip().lower()           
                if score_frames == 'true':
                    SCORE_BOOST = True
                elif score_frames == 'false':
                    SCORE_BOOST = False
                
                SCORE_BOOST_FRAMES = int(save_file1.readline().strip())   
            messagebox.showinfo("Update", "Game loaded succesfully.")
        def load_slot3(event):
            global LOADED_GAME
            global LIVES
            global SCORE
            global SHIELDS
            global SPECIAL_WEAPON
            global SPECIAL_WEAPON_FRAMES
            global SCORE_BOOST
            global SCORE_BOOST_FRAMES
            global LEFT_KEY
            global RIGHT_KEY
            global NAME
            global current_lives
            
            LOADED_GAME = True
            with open("Files/save_slot3.txt", 'r') as save_file1:
                left_key_local = save_file1.readline().strip()
                if left_key_local == '':
                    messagebox.showerror("Error", "Save Slot 3 is empty.")
                    LIVES = 5
                    SCORE = 0
                    SHIELDS = 0
                    SPECIAL_WEAPON = False
                    SPECIAL_WEAPON_FRAMES = 0
                    SCORE_BOOST = False
                    SCORE_BOOST_FRAMES = 0
                    return
                LEFT_KEY = left_key_local
                RIGHT_KEY = save_file1.readline().strip()
                SCORE = int(save_file1.readline().strip())
                NAME = save_file1.readline().strip()
                LIVES = int(save_file1.readline().strip())
                current_lives = LIVES
                SHIELDS = int(save_file1.readline().strip())
                
                weapon_frames = save_file1.readline().strip().lower()           
                if weapon_frames == 'true':
                    SPECIAL_WEAPON = True
                elif weapon_frames == 'false':
                    SPECIAL_WEAPON = False
                    
                SPECIAL_WEAPON_FRAMES = int(save_file1.readline().strip())

                score_frames = save_file1.readline().strip().lower()           
                if score_frames == 'true':
                    SCORE_BOOST = True
                elif score_frames == 'false':
                    SCORE_BOOST = False
                
                SCORE_BOOST_FRAMES = int(save_file1.readline().strip())   
            messagebox.showinfo("Update", "Game loaded succesfully.")
   
        def delete_slot1(event):
            with open("Files/save_slot1.txt", 'w') as save_file1:
                save_file1.truncate()
                messagebox.showinfo("Update", "Save File 1 deleted succesfully.")
                
        def delete_slot2(event):
            with open("Files/save_slot2.txt", 'w') as save_file1:
                save_file1.truncate()
                messagebox.showinfo("Update", "Save File 2 deleted succesfully.")
                
        def delete_slot3(event):
            with open("Files/save_slot3.txt", 'w') as save_file1:
                save_file1.truncate()
                messagebox.showinfo("Update", "Save File 3 deleted succesfully.")
            
    def quit(event):
        root.destroy()          
            
    def reset_game(event):
        global LEADERBOARD_NAMES
        global LEADERBOARD_SCORE
        global LOADED_GAME
        global LIVES
        global RESET_HOWTO
        global SCORE
        global current_lives
        
        LOADED_GAME = True
        LIVES = current_lives
        current_lives = LIVES
        SCORE = 0
        
        with open("Files/leaderboard_score.txt", "w") as score_file:
            score_file.truncate()
            for i in range(10):
                score_file.write("0\n")
                
        with open("Files/leaderboard_names.txt", "w") as name_file:
            name_file.truncate()
            for i in range(10):
                name_file.write("N/A\n")
                
        LEADERBOARD_SCORE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        LEADERBOARD_NAMES = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
        messagebox.showinfo("Update", "The leaderboard has been reset.") 
        
        menu('<event>')
    
    def game_over():
        global SCORE
        global LEADERBOARD_INDEX
        global LEADERBOARD_SCORE
        global LIVES
        global SHIELDS
        global SPECIAL_WEAPON
        global SPECIAL_WEAPON_FRAMES
        global SCORE_BOOST
        global SCORE_BOOST_FRAMES
        
        for stuff in canvas.winfo_children():
            stuff.destroy()
        canvas.delete('all')
        create_gameover_bg()
        
        return_to_menu_button = canvas.create_image(38, 122, image=returntomenu_img)
        canvas.moveto(return_to_menu_button, 550, 550)
        canvas.tag_bind(return_to_menu_button, '<Button-1>', lambda event: menu('<event>'))
        
        canvas.create_text(645, 350, text=f"Your score was: {SCORE}", font="PIXSPACE-DEMO 25", fill="#47d4f9")
        
        # Insert current score in leaderboard list if it is in top 10
        for i in range(10):
            if SCORE > int(LEADERBOARD_SCORE[i]):
                LEADERBOARD_SCORE.insert(i, SCORE)
                LEADERBOARD_NAMES.insert(i, NAME)
                break
            
        # update leaderboard files
        with open("Files/leaderboard_score.txt", "w") as score_file:
            score_file.truncate()
            for i in range(10):
                score_file.write(f"{str(LEADERBOARD_SCORE[i])}\n")      
                     
        with open("Files/leaderboard_names.txt", "w") as name_file:
            name_file.truncate()
            for i in range(10):
                name_file.write(f"{LEADERBOARD_NAMES[i]}\n")
                
        LIVES = 5
        SCORE = 0
        SHIELDS = 0
        SPECIAL_WEAPON = False
        SPECIAL_WEAPON_FRAMES = 0
        SCORE_BOOST = False
        SCORE_BOOST_FRAMES = 0
    # get current player's name
    def update_name(event):
        global NAME
        global GET_NAME
        
        if GET_NAME.get() != "" and len(GET_NAME.get()) == 3 and (GET_NAME.get().isalpha()):
            NAME = GET_NAME.get()
        elif len(GET_NAME.get()) != 3:
            messagebox.showwarning("Warning", "You must enter a three-digit name.")
        elif GET_NAME.get().isalpha() == False:
            messagebox.showwarning("Warning", "You can only enter alphabetical characters.")
        GET_NAME.set("")
        
        label_nameEntry.config(text = f"{NAME}")
                
    def update_controls(event, direction):
        global LEFT_KEY
        global RIGHT_KEY
        
        if direction == 1:
            if LEFT_INPUT.get() != 'j' and LEFT_INPUT.get() != 'J' and LEFT_INPUT.get() != 'k' and LEFT_INPUT.get() != 'K' and LEFT_INPUT.get() != 'l'  and LEFT_INPUT.get() != 'L' and LEFT_INPUT.get() != 'i'  and LEFT_INPUT.get() != 'I' and LEFT_INPUT.get() != 'o'  and LEFT_INPUT.get() != 'O' and LEFT_INPUT.get() != 'b'  and LEFT_INPUT.get() != 'B' and LEFT_INPUT.get() != ' ' and len(LEFT_INPUT.get()) == 1:  
                LEFT_KEY = LEFT_INPUT.get()
                LEFT_KEY = LEFT_KEY.upper()
                LEFT_INPUT.set("")
                if LEFT_KEY == RIGHT_KEY:
                    messagebox.showwarning("Warning", "You have unbound the key for moving to the right.")
                    RIGHT_KEY = ""
            elif len(LEFT_INPUT.get()) != 1:
                messagebox.showerror("Error", "Please input a single keybind.")
                LEFT_INPUT.set("")
            else:
                messagebox.showerror("Error", "Please select a different key.")
                LEFT_INPUT.set("")
                
        elif direction == 2:
            if RIGHT_INPUT.get() != 'j' and RIGHT_INPUT.get() != 'J' and RIGHT_INPUT.get() != 'k' and RIGHT_INPUT.get() != 'K' and RIGHT_INPUT.get() != 'l'  and RIGHT_INPUT.get() != 'L' and RIGHT_INPUT.get() != 'i'  and RIGHT_INPUT.get() != 'I' and RIGHT_INPUT.get() != 'o'  and RIGHT_INPUT.get() != 'O' and RIGHT_INPUT.get() != 'b'  and RIGHT_INPUT.get() != 'B' and RIGHT_INPUT.get() != ' '   and len(RIGHT_INPUT.get()) == 1:  
                RIGHT_KEY = RIGHT_INPUT.get()
                RIGHT_KEY = RIGHT_KEY.upper()
                RIGHT_INPUT.set("")
                if RIGHT_KEY == LEFT_KEY:
                    messagebox.showwarning("Warning", "You have unbound the key for moving to the left.")
                    LEFT_KEY = ""
            elif len(RIGHT_INPUT.get()) != 1:
                messagebox.showerror("Error", "Please input a single keybind.")
                RIGHT_INPUT.set("")
            else:
                messagebox.showerror("Error", "Please select a different key.")
                RIGHT_INPUT.set("")
                
        controls_label.config(text = f"Left - {LEFT_KEY} | Right - {RIGHT_KEY}")

    def how_to(event):
        global LEFT_KEY
        global RIGHT_KEY
        global LOADED_GAME
        global current_lives
        global LIVES
        
        LOADED_GAME = True
        LIVES = current_lives
        current_lives = LIVES
        
        for stuff in canvas.winfo_children():
            stuff.destroy()
        canvas.delete('all')
        
        create_howto_bg()

        # back to menu button
        howto_back_button = canvas.create_image(38, 122, image=back_button)
        canvas.moveto(howto_back_button, 110, 620)
        canvas.tag_bind(howto_back_button, '<Button-1>', lambda event: menu('<event>'))
        # keybinds
        left_keybind = canvas.create_text(160, 455, text=f"{LEFT_KEY}", fill="#47d4f9", font="PIXSPACE-DEMO 21")
        right_keybind = canvas.create_text(160, 479, text=f"{RIGHT_KEY}", fill="#47d4f9", font="PIXSPACE-DEMO 21")
        
        
    def start_game(event):
        global LOADED_GAME
        global LIVES
        global SHIELDS
        global SCORE
        global LEFT_KEY
        global RIGHT_KEY
        global NAME
        global GAME_FRAMES
        global MOVE_LEFT
        global SPECIAL_WEAPON
        global SPECIAL_WEAPON_FRAMES
        global SCORE_BOOST
        global SCORE_BOOST_FRAMES
        
        GAME_FRAMES = 0
        
        #check if keybinds are ok
        if len(LEFT_KEY) != 1 or len(RIGHT_KEY) != 1:
            messagebox.showerror("Error", "You do not have a keybind for each type of movement.")
            menu('<event>')
            return
        
        if NAME == "unnamed":
            messagebox.showerror("Error", "You must enter a player name.")
            menu('<event>')
            return
        
        if LOADED_GAME:
            LOADED_GAME = False
        elif not LOADED_GAME:
            LIVES = 5
            SCORE = 0
            SHIELDS = 0
            SPECIAL_WEAPON = False
            SPECIAL_WEAPON_FRAMES = 0
            SCORE_BOOST = False
            SCORE_BOOST_FRAMES = 0
            
        clear_frame()
        create_in_game_bg()
        
        #create player
        player = canvas.create_image(128, 128, image=player_img)
        exhaust = canvas.create_image(128,128, image= exhaust_skin1)
        canvas.moveto(player, 580, 600)
        canvas.moveto(exhaust, canvas.coords(player)[0], 600)

        # player movement
        def move_left(event):
            global LIVES, MOVE_LEFT
            MOVE_LEFT = True
            if LIVES != 999 and LIVES != 998 and canvas.coords(player)[0]>32:
                canvas.move(player, -30, 0)
                
        def move_right(event):
            global LIVES, MOVE_RIGHT
            MOVE_RIGHT = True
            if LIVES != 999 and LIVES != 998 and canvas.coords(player)[0]<1252:
                canvas.move(player, 30, 0)
                
        root.bind(f"<{LEFT_KEY.lower()}>", move_left)
        root.bind(f"<{RIGHT_KEY.lower()}>", move_right)

        # scores
        score_label = Label(canvas, text=f"Score: {SCORE}", font="PIXSPACE-DEMO 14", fg="#47d4f9", bg="black", border=1, borderwidth=1, compound=tk.CENTER)
        score_label.place(x = 55, y = 100)

        # lives
        lives_label = Label(canvas, text = f"Lives: {LIVES}", font="PIXSPACE-DEMO 14", fg="#47d4f9", bg="black", border=1, borderwidth=1, compound=tk.CENTER)
        lives_label.place(x= 55, y= 50)
        
        # shields
        shields_label = Label(canvas, text = f"Shields: {SHIELDS}", font="PIXSPACE-DEMO 14", fg="#47d4f9", bg="black", border=1, borderwidth=1, compound=tk.CENTER)
        shields_label.place(x=55, y = 75)
        
        # enemies
        enemies = []
        for i in range(5):
            enemies.append(canvas.create_image(128, 128, image=enemy1_img))
            canvas.moveto(enemies[i], rand(10, 1260), rand(10, 400))
        for i in range(5,10):
            enemies.append(canvas.create_image(128, 128, image=enemy2_img))
            canvas.moveto(enemies[i], rand(10, 1260), rand(10, 400))
        for i in range(10,15):
            enemies.append(canvas.create_image(128, 128, image=enemy3_img))
            canvas.moveto(enemies[i], rand(10, 1260), rand(10, 400))
            
        # projectiles
        projectiles = []
        # basic projectiles
        projectiles.append(canvas.create_image(128, 128, image=projectile_img))
        projectiles.append(canvas.create_image(128, 128, image=projectile_img))
        projectiles.append(canvas.create_image(128, 128, image=projectile_img))
        canvas.moveto(projectiles[0], canvas.coords(player)[0], 435)
        canvas.moveto(projectiles[1], canvas.coords(player)[0], 290)
        canvas.moveto(projectiles[2], canvas.coords(player)[0], 145)
        # advanced projectiles
        projectiles.append(canvas.create_image(128, 128, image=adv_projectile_img))
        projectiles.append(canvas.create_image(128, 128, image=adv_projectile_img))
        projectiles.append(canvas.create_image(128, 128, image=adv_projectile_img))
        canvas.moveto(projectiles[3], canvas.coords(player)[0]+3000, 435)
        canvas.moveto(projectiles[4], canvas.coords(player)[0]+3000, 290)
        canvas.moveto(projectiles[5], canvas.coords(player)[0]+3000, 145)
        canvas.pack()
        
        # powerups
        powerups = []
        for i in range(3): #lives
            powerups.append(canvas.create_image(128, 128, image=powerup3_img))
            canvas.moveto(powerups[i], rand(10, 1260), rand(-500, 0))
        for i in range(3,6): #shields
            powerups.append(canvas.create_image(128, 128, image=powerup5_img))
            canvas.moveto(powerups[i], rand(10, 1260), rand(-500, 0))
        for i in range(6,8): #scoreboost
            powerups.append(canvas.create_image(128, 128, image=powerup2_img))
            canvas.moveto(powerups[i], rand(10, 1260), rand(-500, 0))
        for i in range(8,10): #superlaser
            powerups.append(canvas.create_image(128, 128, image=powerup4_img))
            canvas.moveto(powerups[i], rand(10, 1260), rand(-500, 0))
        
        # energy shield
        energy_shield = canvas.create_image(128, 128, image=energy_shield_img)
        
        # rewards
        rewards = []
        for i in range(7):
            rewards.append(canvas.create_image(128, 128, image=reward_img))
            canvas.moveto(rewards[i], rand(10, 1260), rand(-500, 0))
        
        def start_projectiles():
            global SPECIAL_WEAPON
            global SPECIAL_WEAPON_FRAMES
            
            if SPECIAL_WEAPON:
                for i in range(3):
                    if canvas.coords(projectiles[i])[1] <= 150:
                        canvas.moveto(projectiles[i], canvas.coords(player)[0]+3000, 585)
                    canvas.move(projectiles[i], 0, -10)
                for i in range(3, 6):
                    if canvas.coords(projectiles[i])[1] <= 150:
                        canvas.moveto(projectiles[i], canvas.coords(player)[0]-20, 585)
                    canvas.move(projectiles[i], 0, -10)
                    root.update()
                SPECIAL_WEAPON_FRAMES += 1
            elif not SPECIAL_WEAPON:
                for i in range(3):
                    if canvas.coords(projectiles[i])[1] <= 150:
                        canvas.moveto(projectiles[i], canvas.coords(player)[0]-4, 585)
                    canvas.move(projectiles[i], 0, -10)
                for i in range(3, 6):
                    if canvas.coords(projectiles[i])[1] <= 150:
                        canvas.moveto(projectiles[i], canvas.coords(player)[0]+3000, 585)
                    canvas.move(projectiles[i], 0, -10)
                    root.update()

        def start_npc():
            global SCORE
            global LIVES
            global GAME_FRAMES
            global SHIELDS
            global SPECIAL_WEAPON_FRAMES
            global SPECIAL_WEAPON
            global SCORE_BOOST
            global SCORE_BOOST_FRAMES
            
            #enemies collisions
            for i in range(len(enemies)):
                canvas.move(enemies[i], 0, 2)
                
                # out of frame collision
                if canvas.coords(enemies[i])[1] > 700:
                    canvas.moveto(enemies[i], rand(10, 1260), 0)
                    
                # player collision
                elif canvas.coords(enemies[i])[0] <= canvas.coords(player)[0]+50 and canvas.coords(enemies[i])[0] >= canvas.coords(player)[0]-50 and canvas.coords(enemies[i])[1] >= 601 and canvas.coords(enemies[i])[1] <= 700:
                    if SHIELDS > 0:
                        SHIELDS -= 1
                    else:
                        LIVES -= 1
                    canvas.moveto(enemies[i], rand(10, 1260), 0)
                    
                # projectile collision
                elif canvas.coords(projectiles[0])[0] <= canvas.coords(enemies[i])[0]+20 and canvas.coords(projectiles[0])[0] >= canvas.coords(enemies[i])[0]-20  and canvas.coords(projectiles[0])[1] <= canvas.coords(enemies[i])[1]:
                    canvas.moveto(enemies[i], rand(10, 1260), 0)
                elif canvas.coords(projectiles[1])[0] <= canvas.coords(enemies[i])[0]+20  and canvas.coords(projectiles[1])[0] >= canvas.coords(enemies[i])[0]-20   and canvas.coords(projectiles[1])[1] <= canvas.coords(enemies[i])[1]:
                    canvas.moveto(enemies[i], rand(10, 1260), 0)
                elif canvas.coords(projectiles[2])[0] <= canvas.coords(enemies[i])[0]+20  and canvas.coords(projectiles[2])[0] >= canvas.coords(enemies[i])[0]-20   and canvas.coords(projectiles[2])[1] <= canvas.coords(enemies[i])[1]:
                    canvas.moveto(enemies[i], rand(10, 1260), 0)
                elif canvas.coords(projectiles[3])[0] <= canvas.coords(enemies[i])[0]+40 and canvas.coords(projectiles[3])[0] >= canvas.coords(enemies[i])[0]-40  and canvas.coords(projectiles[3])[1] <= canvas.coords(enemies[i])[1]:
                    canvas.moveto(enemies[i], rand(10, 1260), 0)
                elif canvas.coords(projectiles[4])[0] <= canvas.coords(enemies[i])[0]+40  and canvas.coords(projectiles[4])[0] >= canvas.coords(enemies[i])[0]-40   and canvas.coords(projectiles[4])[1] <= canvas.coords(enemies[i])[1]:
                    canvas.moveto(enemies[i], rand(10, 1260), 0)
                elif canvas.coords(projectiles[5])[0] <= canvas.coords(enemies[i])[0]+40  and canvas.coords(projectiles[5])[0] >= canvas.coords(enemies[i])[0]-40   and canvas.coords(projectiles[5])[1] <= canvas.coords(enemies[i])[1]:
                    canvas.moveto(enemies[i], rand(10, 1260), 0)
                    
                root.update()
                
            # powerups collisions
            for i in range(len(powerups)):
                canvas.move(powerups[i], 0, 1)
                
                # out of frame collision
                if canvas.coords(powerups[i])[1] > 710:
                    canvas.moveto(powerups[i], rand(10, 1260), rand(-500, 0))
                    
                # player collision
                elif canvas.coords(powerups[i])[0] <= canvas.coords(player)[0]+30 and canvas.coords(powerups[i])[0] >= canvas.coords(player)[0]-80 and canvas.coords(powerups[i])[1] >= 601 and canvas.coords(powerups[i])[1] <= 700:
                    
                    # determine which powerup is activated
                    if i == 6 or i == 7:
                        # score boost powerup
                        SCORE_BOOST = True
                        SCORE_BOOST_FRAMES = 0
                    elif i == 0 or i == 1 or i == 2:
                        # regenerate life powerup
                        if LIVES <= 4:
                            LIVES += 1
                    elif i == 8 or i == 9:
                        # special weapon
                        SPECIAL_WEAPON = True
                        SPECIAL_WEAPON_FRAMES = 0
                    elif i == 3 or i == 4 or i == 5:
                        # shields
                        if SHIELDS <= 2:
                            SHIELDS += 1
                        
                    canvas.moveto(powerups[i], rand(10, 1260), rand(-500, 0))
                    
                root.update()
            
            # rewards collision
            for i in range(len(rewards)):
                canvas.move(rewards[i], 0, 4)
                
                # out of frame collision
                if canvas.coords(rewards[i])[1] > 710:
                    canvas.moveto(rewards[i], rand(10, 1260), rand(-500, 0))
                    
                # player collision
                elif canvas.coords(rewards[i])[0] <= canvas.coords(player)[0]+55 and canvas.coords(rewards[i])[0] >= canvas.coords(player)[0]-55 and canvas.coords(rewards[i])[1] >= 601 and canvas.coords(rewards[i])[1] <= 700:
                    canvas.moveto(rewards[i], rand(10, 1260), rand(-500, 0))
                    if SHIELDS > 0:
                        SHIELDS = 0
                    elif SHIELDS == 0:
                        LIVES = 0
                        
                # projectile collision
                for j in range(3):
                    if canvas.coords(projectiles[j])[0] <= canvas.coords(rewards[i])[0]+40 and canvas.coords(projectiles[j])[0] >= canvas.coords(rewards[i])[0]-40  and canvas.coords(projectiles[j])[1] <= canvas.coords(rewards[i])[1]:
                        canvas.moveto(rewards[i], rand(10, 1260), rand(-500, 0))
                        if SCORE_BOOST:
                            SCORE += 20
                        else:
                            SCORE += 10
                for j in range(3,6):
                    if canvas.coords(projectiles[j])[0] <= canvas.coords(rewards[i])[0]+60 and canvas.coords(projectiles[j])[0] >= canvas.coords(rewards[i])[0]-60  and canvas.coords(projectiles[j])[1] <= canvas.coords(rewards[i])[1]:
                        canvas.moveto(rewards[i], rand(10, 1260), rand(-500, 0))
                        if SCORE_BOOST:
                            SCORE += 20
                        else:
                            SCORE += 10
                            
                root.update()

            if SCORE_BOOST:
                SCORE_BOOST_FRAMES += 1
            GAME_FRAMES += 1
            sleep(0.00000000001)
        
        def move_energy_shield():
            if SHIELDS > 0:
                canvas.moveto(energy_shield, canvas.coords(player)[0]-32, canvas.coords(player)[1]-30)
            else:
                canvas.moveto(energy_shield, canvas.coords(player)[0]+3000, canvas.coords(player)[1]-30)
                
        current_lives = 0
        pause_bg = 0
        exit_button = 0
        resume_button = 0
        save_button = 0

        # pause function
        def pause_press(event):
            global pause_bg
            global exit_button
            global resume_button
            global save_button
            global current_lives
            global LIVES
            
            # pause background
            pause_bg = Label(canvas, image=pause_bg_img, borderwidth=0, border=0)
            pause_bg.place(x=0, y=0) 
            
            # pause menu buttons
            exit_button = Button(canvas, image=exitbutton_img, borderwidth=0, bg="#161f28", activebackground="#161f28", command= lambda: exit_key("<event>"))
            resume_button = Button(canvas, image=resumebutton_img, borderwidth=0, bg="#161f28", activebackground="#161f28", command= lambda: unpause_press("<event>"))
            save_button = Button(canvas, image=savebutton_img, borderwidth=0, bg="#161f28", activebackground="#161f28", command= lambda: save_screen("<event>"))
            
            exit_button.place(x=580, y=550)
            resume_button.place(x=580, y=382)
            save_button.place(x=580, y=465)
            
            current_lives = LIVES
            LIVES = 999
            
        def unpause_press(event):
            global pause_bg
            global exit_button
            global resume_button
            global save_button
            global LIVES
            global current_lives
            
            pause_bg.destroy()
            exit_button.destroy()
            save_button.destroy()
            resume_button.destroy()
            
            LIVES = current_lives
            current_lives = LIVES
            
            do_game()
            
        def pause():
            return
        
        # save screen
        def save_screen(event):
            # create buttons
            background = Label(canvas, image= save_bg_img, borderwidth=0, border=0)
            save_slot1 = Button(canvas, image=savebutton_img, borderwidth=0, bg="#161f28", activebackground="#161f28", command= lambda: write_slot1())
            save_slot2 = Button(canvas, image=savebutton_img, borderwidth=0, bg="#161f28", activebackground="#161f28", command= lambda: write_slot2())
            save_slot3 = Button(canvas, image=savebutton_img, borderwidth=0, bg="#161f28", activebackground="#161f28", command= lambda: write_slot3())
           
            background.place(x=0, y=0)
            save_slot1.place(x=226, y=498)
            save_slot2.place(x=577, y=498)
            save_slot3.place(x=933, y=498)
            
            # back to pause screen button
            back_btn = Button(canvas, image=back_button, borderwidth=0, bg="#161f28", activebackground="#161f28", command= lambda: back_to_game())
            back_btn.place(x=577, y=605)
            
            def back_to_game():
                background.destroy()
                save_slot1.destroy()
                save_slot2.destroy()
                save_slot3.destroy()
                back_btn.destroy()
                
            def write_slot1():
                global LEFT_KEY
                global RIGHT_KEY
                global SCORE
                global NAME
                global current_lives
                global SHIELDS
                global SPECIAL_WEAPON
                global SPECIAL_WEAPON_FRAMES
                global SCORE_BOOST
                global SCORE_BOOST_FRAMES
                
                with open("Files/save_slot1.txt", 'w') as save_file1:
                    save_file1.truncate()
                    save_file1.write(f"{LEFT_KEY}\n")
                    save_file1.write(f"{RIGHT_KEY}\n")
                    save_file1.write(f"{SCORE}\n")
                    save_file1.write(f"{NAME}\n")
                    save_file1.write(f"{current_lives}\n")
                    save_file1.write(f"{SHIELDS}\n")
                    save_file1.write(f"{SPECIAL_WEAPON}\n")
                    save_file1.write(f"{SPECIAL_WEAPON_FRAMES}\n")
                    save_file1.write(f"{SCORE_BOOST}\n")
                    save_file1.write(f"{SCORE_BOOST_FRAMES}\n")
                messagebox.showinfo("Update", "Game saved succesfully.")
                
            def write_slot2():
                global LEFT_KEY
                global RIGHT_KEY
                global SCORE
                global NAME
                global current_lives
                global SHIELDS
                global SPECIAL_WEAPON
                global SPECIAL_WEAPON_FRAMES
                global SCORE_BOOST
                global SCORE_BOOST_FRAMES
                
                with open("Files/save_slot2.txt", 'w') as save_file1:
                    save_file1.truncate()
                    save_file1.write(f"{LEFT_KEY}\n")
                    save_file1.write(f"{RIGHT_KEY}\n")
                    save_file1.write(f"{SCORE}\n")
                    save_file1.write(f"{NAME}\n")
                    save_file1.write(f"{current_lives}\n")
                    save_file1.write(f"{SHIELDS}\n")
                    save_file1.write(f"{SPECIAL_WEAPON}\n")
                    save_file1.write(f"{SPECIAL_WEAPON_FRAMES}\n")
                    save_file1.write(f"{SCORE_BOOST}\n")
                    save_file1.write(f"{SCORE_BOOST_FRAMES}\n")
                messagebox.showinfo("Update", "Game saved succesfully.")
                
            def write_slot3():
                global LEFT_KEY
                global RIGHT_KEY
                global SCORE
                global NAME
                global current_lives
                global SHIELDS
                global SPECIAL_WEAPON
                global SPECIAL_WEAPON_FRAMES
                global SCORE_BOOST
                global SCORE_BOOST_FRAMES
                
                with open("Files/save_slot3.txt", 'w') as save_file1:
                    save_file1.truncate()
                    save_file1.write(f"{LEFT_KEY}\n")
                    save_file1.write(f"{RIGHT_KEY}\n")
                    save_file1.write(f"{SCORE}\n")
                    save_file1.write(f"{NAME}\n")
                    save_file1.write(f"{current_lives}\n")
                    save_file1.write(f"{SHIELDS}\n")
                    save_file1.write(f"{SPECIAL_WEAPON}\n")
                    save_file1.write(f"{SPECIAL_WEAPON_FRAMES}\n")
                    save_file1.write(f"{SCORE_BOOST}\n")
                    save_file1.write(f"{SCORE_BOOST_FRAMES}\n")
                messagebox.showinfo("Update", "Game saved succesfully.")
            
        # cheat codes
        def cheat_code1(event):
            global LIVES
            LIVES = 100
        def cheat_code2(event):
            global SCORE
            SCORE += 200
            
        # boss key
        boss_label = Label(canvas, image= boss_img)
        
        def boss_key(event):
            global IN_BOSS_WINDOW
            global LIVES
            global current_lives
            
            # check current boss key state
            if IN_BOSS_WINDOW == True:
                return
            IN_BOSS_WINDOW = True
            boss_label.place(x=0, y=0)
            
            # pause game
            current_lives = LIVES
            LIVES = 998
            
        def unboss_key(event):
            global LIVES
            global SCORE
            global IN_BOSS_WINDOW
            global current_lives
            
            # check current boss key state
            if IN_BOSS_WINDOW == False:
                return
            IN_BOSS_WINDOW = False
            
            # destroy boss image
            boss_label.place_forget()
            
            # unpause game
            LIVES = current_lives
            current_lives = LIVES
                       
            do_game()
        
        # key to exit to main menu
        def exit_key(event):
            menu('<event>')
        
        #keybinds     
        root.bind("<j><k><l>", cheat_code1)
        root.bind("<i><o>", cheat_code2)
        root.bind("<b>", boss_key)
        root.bind("<b><b>", unboss_key)
        
        # frames for special projectile duration manipulation
        def special_proj_frames():
            global SPECIAL_WEAPON_FRAMES
            global SPECIAL_WEAPON
            
            if SPECIAL_WEAPON_FRAMES == 600:
                SPECIAL_WEAPON_FRAMES = 0
                SPECIAL_WEAPON = False
        
        # frames for score booster duration manipulation
        def score_boost_frames():
            global SCORE_BOOST
            global SCORE_BOOST_FRAMES
            
            if SCORE_BOOST_FRAMES == 600:
                SCORE_BOOST_FRAMES = 0
                SCORE_BOOST = False                      

        # frames function for animation manipulation and game state manipulation
        def frames():
            global GAME_FRAMES
            global MOVE_LEFT
            global MOVING_LEFT_1
            global MOVING_LEFT_2
            global MOVING_LEFT_3
            global MOVE_RIGHT
            global MOVING_RIGHT_1
            global MOVING_RIGHT_2
            global MOVING_RIGHT_3
            
            # game cycle for costume update
            if GAME_FRAMES == 0:
                # player move left costumes
                if MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2 and MOVING_LEFT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_LEFT = False
                    MOVING_LEFT_1 = False
                    MOVING_LEFT_2 = False
                    MOVING_LEFT_3 = False
                elif MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_3 = True         
                elif MOVE_LEFT and MOVING_LEFT_1:
                    canvas.itemconfig(player, image= player_left2_img)
                    MOVING_LEFT_2 = True  
                elif MOVE_LEFT:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_1 = True 
                # player move right costumes
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2 and MOVING_RIGHT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_RIGHT = False
                    MOVING_RIGHT_1 = False
                    MOVING_RIGHT_2 = False
                    MOVING_RIGHT_3 = False
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_3 = True 
                elif MOVE_RIGHT and MOVING_RIGHT_1:
                    canvas.itemconfig(player, image= player_right2_img)
                    MOVING_RIGHT_2 = True  
                elif MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_1 = True 
                # no move player costumes                        
                elif not MOVE_LEFT and not MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_img)
                # exhaust costumes
                canvas.itemconfig(exhaust, image= exhaust_skin1)
                canvas.moveto(exhaust, canvas.coords(player)[0]-12, 648)
            elif GAME_FRAMES == 2:
                # player move left costumes
                if MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2 and MOVING_LEFT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_LEFT = False
                    MOVING_LEFT_1 = False
                    MOVING_LEFT_2 = False
                    MOVING_LEFT_3 = False
                elif MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_3 = True         
                elif MOVE_LEFT and MOVING_LEFT_1:
                    canvas.itemconfig(player, image= player_left2_img)
                    MOVING_LEFT_2 = True  
                elif MOVE_LEFT:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_1 = True 
                # player move right costumes
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2 and MOVING_RIGHT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_RIGHT = False
                    MOVING_RIGHT_1 = False
                    MOVING_RIGHT_2 = False
                    MOVING_RIGHT_3 = False
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_3 = True 
                elif MOVE_RIGHT and MOVING_RIGHT_1:
                    canvas.itemconfig(player, image= player_right2_img)
                    MOVING_RIGHT_2 = True  
                elif MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_1 = True
                # no move player costumes                        
                elif not MOVE_LEFT and not MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_img)
                #exhaust costumes
                canvas.itemconfig(exhaust, image= exhaust_skin2)
                canvas.moveto(exhaust, canvas.coords(player)[0]-10, 650)
            elif GAME_FRAMES == 4:
                # player move left costumes
                if MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2 and MOVING_LEFT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_LEFT = False
                    MOVING_LEFT_1 = False
                    MOVING_LEFT_2 = False
                    MOVING_LEFT_3 = False
                elif MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_3 = True         
                elif MOVE_LEFT and MOVING_LEFT_1:
                    canvas.itemconfig(player, image= player_left2_img)
                    MOVING_LEFT_2 = True  
                elif MOVE_LEFT:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_1 = True 
                # player move right costumes
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2 and MOVING_RIGHT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_RIGHT = False
                    MOVING_RIGHT_1 = False
                    MOVING_RIGHT_2 = False
                    MOVING_RIGHT_3 = False
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_3 = True 
                elif MOVE_RIGHT and MOVING_RIGHT_1:
                    canvas.itemconfig(player, image= player_right2_img)
                    MOVING_RIGHT_2 = True  
                elif MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_1 = True
                # no move player costumes                        
                elif not MOVE_LEFT and not MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_img)
                # exhaust costumes
                canvas.itemconfig(exhaust, image= exhaust_skin3)
                canvas.moveto(exhaust, canvas.coords(player)[0]-7, 655)
            elif GAME_FRAMES == 6:
                # player move left costumes
                if MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2 and MOVING_LEFT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_LEFT = False
                    MOVING_LEFT_1 = False
                    MOVING_LEFT_2 = False
                    MOVING_LEFT_3 = False
                elif MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_3 = True         
                elif MOVE_LEFT and MOVING_LEFT_1:
                    canvas.itemconfig(player, image= player_left2_img)
                    MOVING_LEFT_2 = True  
                elif MOVE_LEFT:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_1 = True 
                # player move right costumes
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2 and MOVING_RIGHT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_RIGHT = False
                    MOVING_RIGHT_1 = False
                    MOVING_RIGHT_2 = False
                    MOVING_RIGHT_3 = False
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_3 = True 
                elif MOVE_RIGHT and MOVING_RIGHT_1:
                    canvas.itemconfig(player, image= player_right2_img)
                    MOVING_RIGHT_2 = True  
                elif MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_1 = True
                # no move player costumes                        
                elif not MOVE_LEFT and not MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_img)
                # exhaust costumes
                canvas.itemconfig(exhaust, image= exhaust_skin4)
                canvas.moveto(exhaust, canvas.coords(player)[0]-12, 650)
            elif GAME_FRAMES == 8:
                # player move left costumes
                if MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2 and MOVING_LEFT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_LEFT = False
                    MOVING_LEFT_1 = False
                    MOVING_LEFT_2 = False
                    MOVING_LEFT_3 = False
                elif MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_3 = True         
                elif MOVE_LEFT and MOVING_LEFT_1:
                    canvas.itemconfig(player, image= player_left2_img)
                    MOVING_LEFT_2 = True  
                elif MOVE_LEFT:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_1 = True 
                # player move right costumes
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2 and MOVING_RIGHT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_RIGHT = False
                    MOVING_RIGHT_1 = False
                    MOVING_RIGHT_2 = False
                    MOVING_RIGHT_3 = False
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_3 = True 
                elif MOVE_RIGHT and MOVING_RIGHT_1:
                    canvas.itemconfig(player, image= player_right2_img)
                    MOVING_RIGHT_2 = True  
                elif MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_1 = True
                # no move player costumes                        
                elif not MOVE_LEFT and not MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_img)
                # exhaust costumes
                canvas.itemconfig(exhaust, image= exhaust_skin5)
                canvas.moveto(exhaust, canvas.coords(player)[0]-10, 650)
            elif GAME_FRAMES == 10:
                # player move left costumes
                if MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2 and MOVING_LEFT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_LEFT = False
                    MOVING_LEFT_1 = False
                    MOVING_LEFT_2 = False
                    MOVING_LEFT_3 = False
                elif MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_3 = True         
                elif MOVE_LEFT and MOVING_LEFT_1:
                    canvas.itemconfig(player, image= player_left2_img)
                    MOVING_LEFT_2 = True  
                elif MOVE_LEFT:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_1 = True 
                # player move right costumes
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2 and MOVING_RIGHT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_RIGHT = False
                    MOVING_RIGHT_1 = False
                    MOVING_RIGHT_2 = False
                    MOVING_RIGHT_3 = False
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_3 = True 
                elif MOVE_RIGHT and MOVING_RIGHT_1:
                    canvas.itemconfig(player, image= player_right2_img)
                    MOVING_RIGHT_2 = True  
                elif MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_1 = True
                # no move player costumes                        
                elif not MOVE_LEFT and not MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_img)
                # exhaust costumes
                canvas.itemconfig(exhaust, image= exhaust_skin6)
                canvas.moveto(exhaust, canvas.coords(player)[0]-7, 655)
            elif GAME_FRAMES == 12:
                # player move left costumes
                if MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2 and MOVING_LEFT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_LEFT = False
                    MOVING_LEFT_1 = False
                    MOVING_LEFT_2 = False
                    MOVING_LEFT_3 = False
                elif MOVE_LEFT and MOVING_LEFT_1 and MOVING_LEFT_2:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_3 = True         
                elif MOVE_LEFT and MOVING_LEFT_1:
                    canvas.itemconfig(player, image= player_left2_img)
                    MOVING_LEFT_2 = True  
                elif MOVE_LEFT:
                    canvas.itemconfig(player, image= player_left1_img)
                    MOVING_LEFT_1 = True 
                # player move right costumes
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2 and MOVING_RIGHT_3:
                    canvas.itemconfig(player, image= player_img)
                    MOVE_RIGHT = False
                    MOVING_RIGHT_1 = False
                    MOVING_RIGHT_2 = False
                    MOVING_RIGHT_3 = False
                elif MOVE_RIGHT and MOVING_RIGHT_1 and MOVING_RIGHT_2:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_3 = True 
                elif MOVE_RIGHT and MOVING_RIGHT_1:
                    canvas.itemconfig(player, image= player_right2_img)
                    MOVING_RIGHT_2 = True  
                elif MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_right1_img)
                    MOVING_RIGHT_1 = True
                # no move player costumes                        
                elif not MOVE_LEFT and not MOVE_RIGHT:
                    canvas.itemconfig(player, image= player_img)
                # exhaust costumes
                canvas.itemconfig(exhaust, image= exhaust_skin1)
                canvas.moveto(exhaust, canvas.coords(player)[0]-12, 648)
                GAME_FRAMES = 2
        
        # continuous game run    
        def do_game():
            global LEFT_KEY
            global RIGHT_KEY
            global LIVES
            global SCORE
            global SHIELDS
            global current_lives
            
            # pause button in_game
            pause_btn = canvas.create_image(38, 122, image=pausebutton_img)
            canvas.moveto(pause_btn, 1100, 55)
            canvas.tag_bind(pause_btn, '<Button-1>', lambda event: pause_press('<event>'))
            
            root.update()
      
            while LIVES > 0:            
                frames()
                move_energy_shield()
                
                score_boost_frames()
                special_proj_frames()

                start_projectiles()
                start_npc()
                if LIVES == 999:
                    pause()
                    break
                elif LIVES == 998:
                    break
                current_lives = LIVES
                lives_label.config(text = f"Lives: {LIVES}") 
                score_label.config(text = f"Score: {SCORE}") 
                shields_label.config(text = f"Shields: {SHIELDS}")

            if LIVES <= 0:
                game_over()
         
        do_game()
                
menu('<event>')
root.mainloop()