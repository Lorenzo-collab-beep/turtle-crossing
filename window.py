from tkinter import PhotoImage
from turtle import Screen
import threading
import pygame
import globals
import sys
import os


# local methods
def __get_assets_path(filename):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, filename)

def __setup_icon(screen):
    root = screen.getcanvas().winfo_toplevel()
    root.resizable(False, False)
    icon_path = __get_assets_path(globals.CROSSING_ICON)
    if os.path.exists(icon_path):
        icon = PhotoImage(file=icon_path)
        root.iconphoto(True, icon)

# def __setup_music():
#     pygame.mixer.init()
#     music_path = __get_assets_path(globals.GAME_MP3)
#     if os.path.exists(music_path):
#         pygame.mixer.music.load(music_path)
#         pygame.mixer.music.play(-1)
#         pygame.mixer.music.set_volume(globals.VOLUME)

def __setup_music():
    def play_music():
        pygame.mixer.init()
        music_path = __get_assets_path(globals.GAME_MP3)
        if os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(globals.VOLUME)

    threading.Thread(target=play_music, daemon=True).start()

def __game_over_sound():
    sound_path = __get_assets_path(globals.GAME_OVER_SOUND)
    if os.path.exists(sound_path):
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

def __stop_music():
    pygame.mixer.music.stop()

def __quit_music():
    pygame.mixer.quit()

# window function
def setup_window():
    __setup_music()
    screen = Screen()
    screen.title("Turtle Crossing")
    screen.setup(width=globals.SCREEN_W, height=globals.SCREEN_H)
    screen.tracer(0)
    __setup_icon(screen)
    return screen

def window_game_over():
    __stop_music()
    __game_over_sound()

def window_quit():
    __quit_music()