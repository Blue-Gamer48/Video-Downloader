import time
from tkinter import *
from moviepy.editor import *
import tkinter as tk
import getpass
from pytube import YouTube
from tkinter import filedialog, messagebox
from tkinter.messagebox import showinfo
username = getpass.getuser()


def createWidgets():
    link_label = Label(root, text="YouTube URL:", bg="#03c9ff")
    link_label.pack(pady=10)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.pack(pady=10)

    browse_but = Button(root, text="Browse", command=browse, width=25, bg="#00ff04")
    browse_but.pack(pady=10)

    downloadmp4_but = Button(root, text="Download Video", command=mp4, width=25, bg="#00ff04")
    downloadmp4_but.pack(pady=10)

    downloadmp3_but = Button(root, text="Download Audio", command=mp3, width=25, bg="#00ff04")
    downloadmp3_but.pack(pady=10)

def browse():
    download_dir = filedialog.askdirectory(initialdir="your Directory Path")
    download_path.set(download_dir)

def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: Blue_Gamer48\n\
Datum: 10.06.23\n\
Version: 0.1\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")


def mp4():
    url = video_link.get()
    folder = f"C:\\Users\\{username}\\Videos"
    file_path = filedialog.asksaveasfilename(initialdir=folder, defaultextension=".mp4",
                                            filetypes=(("MP4 Dateien", "*.mp4"), ("Alle Dateien", "*.*")))

    if file_path:
        # Herunterladen der Video-Datei unter dem angegebenen Dateinamen
        get_video = YouTube(url)
        get_stream = get_video.streams.get_highest_resolution()
        get_stream.download(output_path=os.path.dirname(file_path), filename=os.path.basename(file_path))

        messagebox.showinfo("Erfolgreich Abgeschlossen", "Der Download wurde Erfolgreich Abgeschlossen. Du findest dein Video in\n" + os.path.dirname(file_path))


def mp3():
    url = video_link.get()
    username = getpass.getuser()
    folder_mp3 = f"C:\\Users\\{username}\\Music"
    video = YouTube(url)
    get_stream = video.streams.get_highest_resolution()
    mp4_file = get_stream.download(output_path=folder_mp3)

    if mp4_file:
        mp4_path = os.path.join(folder_mp3, mp4_file)

        # Dialog zum Speichern der MP3-Datei anzeigen
        mp3_file = filedialog.asksaveasfilename(initialdir=folder_mp3, defaultextension=".mp3",
                                                filetypes=(("MP3 Dateien", "*.mp3"), ("Alle Dateien", "*.*")))
        if mp3_file:
            # Konvertiere MP4 in MP3
            video_clip = VideoFileClip(mp4_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(mp3_file)

            # Video- und Audioclip schließen
            video_clip.close()
            audio_clip.close()

            # Alte MP4-Datei löschen
            os.remove(mp4_path)

            messagebox.showinfo("Erfolgreich Abgeschlossen",
                                "Der Download wurde Erfolgreich Abgeschlossen. Du findest deine Audio in\n" + folder_mp3)
        else:
            messagebox.showinfo("Abgebrochen", "Der Vorgang wurde abgebrochen.")

root = tk.Tk()
root.geometry("920x690")
root.resizable(True, True)
root.title("Youtube Downloader")
root.config(background="#03c9ff")
menuleiste = Menu(root)
menu = Menu(menuleiste, tearoff=0)
menu.add_command(label="Exit", command=root.quit)
menu.add_command(label="Infos zum Programm", command=action_get_info_dialog)
menuleiste.add_cascade(label="Menü",menu=menu)
video_link = StringVar()
download_path = StringVar()

# Zentriere das Widget im Fenster
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
widget_width = 400
widget_height = 300
x_pos = (window_width - widget_width) // 2
y_pos = (window_height - widget_height) // 2
root.geometry(f"{widget_width}x{widget_height}+{x_pos}+{y_pos}")

createWidgets()
root.config(menu=menuleiste)
root.mainloop()


print("Der Youtube Downloader wurde beendet")
