from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os


def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)


def play_music():
    music = playlist.get(ACTIVE)
    print(music[:])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()


root = Tk()
root.title("Music Player")
root.geometry("900x700")
root.configure(bg="black")
root.resizable(False, False)

mixer.init()

image_icon = PhotoImage(file="C:\\Users\\HP\\Desktop\\logo.png")
root.iconphoto(False, image_icon)

logo = PhotoImage(file="C:\\Users\\HP\\Desktop\\logo.png")
Label(root, image=logo, bg="cyan").place(x=0, y=0)

play_button = Button(root, text="Play", font="arial 20", fg="black", bg="green", command=play_music)
play_button.place(x=230, y=550, width="60", height="40")

pause_button = Button(root, text="Pause", font="arial 20", fg="black", bg="yellow", command=mixer.music.pause)
pause_button.place(x=120, y=550, width="80", height="40")

resume_button = Button(root, text="Resume", font="arial 20", fg="white", bg="blue", command=mixer.music.unpause)
resume_button.place(x=320, y=550, width="110", height="40")

stop_button = Button(root, text="Stop", font="arial 20", fg="white", bg="red", command=mixer.music.stop)
stop_button.place(x=230, y=610, width="60", height="40")

open_button = Button(root, text="Open Music Folder", font="arial 10 bold", fg="black", bg="cyan", command=open_folder)
open_button.place(x=550, y=100, width="140", height="40")

menu = Label(root, text="Music Playlist", font="arial 20", fg="white", bg="blue")
menu.place(x=620, y=20)

menu_frame = Frame(root, bd=2, relief="solid")
menu_frame.place(x=550, y=150, width="320", height="450")


scroll = Scrollbar(menu_frame)
playlist = Listbox(menu_frame, width=100, font="arial 10", fg="white", bg="grey", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
