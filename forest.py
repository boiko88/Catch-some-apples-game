from tkinter import *
import time
import random
import winsound

game_on = True
apples_count = 0
hearts_count = 4

# UI
window = Tk()
window.title('Forest')
WIDTH = 300
HEIGHT = 500
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='white')

# Text
score_line = StringVar()
label = Label(window, textvariable=score_line, font=(
    "Helvetica", 24), bg='grey', fg='white')
score_line.set(f'Score: 0')
label.pack(side=TOP)
canvas.pack()

# Functions


def game_status(apples_count, hearts_count):
    global game_on
    if apples_count >= 20:
        print("Congratulations! You won!")
        window.configure(bg='pink')
        canvas.create_image(0, 0, anchor=NW, image=forest_img)
        forest_img.configure(file='you_win.png')
        game_on = False
    if apples_count <= -1 or hearts_count == 0:
        print("You lose!")
        window.configure(bg='grey')
        canvas.create_image(0, 0, anchor=NW, image=forest_img)
        forest_img.configure(file='you_lose.png')
        game_on = False


def moving(event):
    coords = canvas.coords(player)
    if event.keysym == 'Left' and coords[0] > 25:
        canvas.move(player, -5, 0)
    if event.keysym == 'Right' and coords[0] < WIDTH - 25:
        canvas.move(player, 5, 0)


def check_bomb(bombs):
    for bomb in str(bombs):
        global apples_count
        global hearts_count
        bomb_coords = canvas.coords(bomb)
        basket_coords = canvas.coords(player)
        if bomb_coords[0] - 12 > basket_coords[0] - 40 and bomb_coords[0] + 12 < basket_coords[0] + 40:
            if bomb_coords[1] + 12 > basket_coords[1] - 25:
                apples_count -= 1
                hearts_count -= 1
                x = random.randint(13, WIDTH - 13)
                y = -25
                canvas.coords(bomb, x, y)
                winsound.PlaySound('boom_sound.wav', winsound.SND_ASYNC)
                score_line.set(f"Score: {apples_count}")
                print(f"your hearts count is {hearts_count}")


def check_apples(apples):
    for apple in apples:
        global apples_count
        apple_coords = canvas.coords(apple)
        basket_coords = canvas.coords(player)
        if apple_coords[0] - 12 > basket_coords[0] - 40 and apple_coords[0] + 12 < basket_coords[0] + 40:
            if apple_coords[1] + 12 > basket_coords[1] - 25:
                apples_count += 1
                x = random.randint(13, WIDTH - 13)
                y = -25
                canvas.coords(apple, x, y)
                winsound.PlaySound('score.wav', winsound.SND_ASYNC)
                score_line.set(f"Score: {apples_count}")


def check_heart(hearts):
    global hearts_count
    for heart in str(hearts):
        heart_coords = canvas.coords(heart)
        basket_coords = canvas.coords(player)
        if heart_coords[0] - 12 > basket_coords[0] - 40 and heart_coords[0] + 12 < basket_coords[0] + 40:
            if heart_coords[1] + 12 > basket_coords[1] - 25:
                print("You got a heart")
                x = random.randint(13, WIDTH - 13)
                y = -25
                canvas.coords(heart, x, y)
                winsound.PlaySound('heart.wav', winsound.SND_ASYNC)
                if hearts_count < 4:
                    hearts_count += 1
                print(f"Your heart count is {hearts_count}")


# Images and Engine

forest_img = PhotoImage(file='forest.png')
canvas.create_image(0, 0, anchor=NW, image=forest_img)
basket_img = PhotoImage(file='basket.png')
player = canvas.create_image(WIDTH / 2, HEIGHT, anchor=S, image=basket_img)
canvas.bind_all("<Key>", moving)
apple_img = PhotoImage(file='apple.png')
bomb_img = PhotoImage(file='bomb.png')
heart_img = PhotoImage(file='heart.png')

x = random.randint(13, WIDTH - 13)
y = 25
apple1 = canvas.create_image(x, y, anchor=CENTER, image=apple_img)

x = random.randint(13, WIDTH - 13)
apple2 = canvas.create_image(x, y, anchor=CENTER, image=apple_img)

x = random.randint(13, WIDTH - 13)
apple3 = canvas.create_image(x, y, anchor=CENTER, image=apple_img)

x = random.randint(13, WIDTH - 13)
bomb = canvas.create_image(x, y, image=bomb_img)
heart = canvas.create_image(x, y, image=heart_img)

while game_on:
    canvas.move(apple1, 0, 0.7)
    canvas.move(apple2, 0, 1)
    canvas.move(apple3, 0, 1.5)
    canvas.move(bomb, 0, 1.8)
    canvas.move(heart, 0, 1.8)
    window.update()
    time.sleep(0.006)

    apple1_coords = canvas.coords(apple1)
    if apple1_coords[1] > HEIGHT:
        x = random.randint(13, WIDTH - 13)
        y = -25
        canvas.coords(apple1, x, y)

    apple2_coords = canvas.coords(apple2)
    if apple2_coords[1] > HEIGHT:
        x = random.randint(13, WIDTH - 13)
        y = -25
        canvas.coords(apple2, x, y)

    apple3_coords = canvas.coords(apple3)
    if apple3_coords[1] > HEIGHT:
        x = random.randint(13, WIDTH - 13)
        y = -25
        canvas.coords(apple3, x, y)

    bomb_coords = canvas.coords(bomb)
    if bomb_coords[1] > HEIGHT:
        x = random.randint(13, WIDTH - 13)
        y = -25
        canvas.coords(bomb, x, y)

    heart_coords = canvas.coords(heart)
    if heart_coords[1] > HEIGHT:
        x = random.randint(13, WIDTH - 13)
        y = -25
        canvas.coords(heart, x, y)

    check_apples((apple1, apple2, apple3))
    check_bomb(bomb)
    check_heart(heart)
    game_status(apples_count, hearts_count)


# Do we actually need this?
window.mainloop()
