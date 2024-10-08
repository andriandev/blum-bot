from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
from termcolor import colored
import keyboard
import random
from pynput.mouse import Button, Controller

mouse = Controller()
time.sleep(0.5)

putih = '\033[1;97m'
merah = '\033[1;91m'
hijau = '\033[1;92m'
kuning = '\033[1m\033[93m'
biru = '\033[1;94m'
reset = '\033[0m'
putihmerah = '\033[97m\033[41m'
putihhijau = '\033[97m\033[42m'
merahhijau = '\033[1;91m\033[42m'

print()
print(f" {putihhijau}*** Author: AndrianDev ***{reset}")
print(f" {putihhijau}*** Blum Bot Auto Click ***{reset}")
print()
print(colored("  ...:::: CHOOSE LANGUAGE ::::...", 'light_cyan'))
print(colored("  [", 'white') + colored("1", 'light_green') + colored("] ", 'white') + colored("English", 'light_yellow'))
print(colored("  [", 'white') + colored("2", 'light_green') + colored("] ", 'white') + colored("Bahasa Indonesia", 'light_yellow'))

while True:
    try:
        language_choice = int(input(f"\n  {putih}blum.bot@main:~# {reset}"))
        if language_choice in [1, 2]:
            break
        else:
            print(f"  {merah}Yo bro wrong choose. You can input {kuning}1 {merah}or {kuning}2{merah}.{reset}")
    except ValueError:
        print(f"  {merah}What??? your input not valid. Please enter number {kuning}1 {merah}or {kuning}2 {merah}bro.{reset}")

if language_choice == 1:
    window_input = f"\n{putih} [?] | Enter Window : {reset}"
    window_not_found = f"{putih} [>] | Your Window - {{}} {kuning}not found!{reset}"
    window_found = f"{hijau} [>] | Window found - {{}}\n {hijau}Now bot working...\n {putih}Press {kuning}'S' {putih}to start or pause.\n Press {kuning}'Q' {putih}to stop bot.\n Press {kuning}'Space' {putih}to play again blum game.{reset}"
    pause_message = f" {biru}Bot paused...{reset}"
    continue_message = f" {biru}Bot running...{reset}"
    close_message = f" {merah}Program closing...{reset}"
elif language_choice == 2:
    window_input = f"\n{putih} [?] | Masukin Window nya : {reset}"
    window_not_found = f"{putih} [>] | Window - {{}} {kuning}tidak tersedia!{reset}"
    window_found = f"{hijau} [>] | Window ditemukan - {{}}\n {hijau}Sekarang bot aktif...\n {putih}Tekan {kuning}'S' {putih}untuk mulai atau jeda.\n Tekan {kuning}'Q' {putih}untuk stop bot.\n Tekan {kuning}'Spasi' {putih}untuk main ulang blum game.{reset}"
    pause_message = f" {biru}Bot terjeda...{reset}"
    continue_message = f" {biru}Bot berjalan...{reset}"
    close_message = f" {merah}Menutup program...{reset}"

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)
    
def get_pixel_color_under_cursor():
    # Mengambil warna pixel di bawah posisi kursor
    x, y = pyautogui.position()  # Mendapatkan posisi kursor
    screenshot = pyautogui.screenshot()  # Mengambil screenshot penuh layar
    pixel_color = screenshot.getpixel((x, y))  # Mendapatkan warna pixel di posisi kursor
    return x, y, pixel_color

window_name = input(window_input)

window_check = gw.getWindowsWithTitle(window_name)

if not window_check:
    print(window_not_found.format(window_name))
    if language_choice == 1:
        print(f"\n   {putihmerah}EN:{reset}\n   {putihmerah}Make sure you use the TelegramDesktop application (not Telegram Web).{reset}\n   {putihmerah}And have opened the Blum bot on your TelegramDesktop.{reset}\n   {putihmerah}Until the Blum window is available{reset}")
    elif language_choice == 2:
        print(f"\n   {putihmerah}ID:{reset}\n   {putihmerah}Pastikan kamu menggunakan aplikasi TelegramDesktop (bukan Telegram Web).{reset}\n   {putihmerah}Dan telah membuka Blum bot di TelegramDesktop kamu.{reset}\n   {putihmerah}Hingga tersedia window Blum nya{reset}")
else:
    print(window_found.format(window_name))
    telegram_window = window_check[0]
    paused = True
    play_again = False

    while True:
        if keyboard.is_pressed('S'):
            paused = not paused
            if paused:
                print(pause_message)
            else:
                print(continue_message)
            time.sleep(0.2)
            
        if keyboard.is_pressed('Q'):
            print(close_message)
            exit() 
            
        if keyboard.is_pressed('space'):
            play_again = True
            print(f" {hijau}Play Again...{reset}")
            click(1603, 900)
            time.sleep(0.2)
            
        if keyboard.is_pressed('1'):
            x, y, pixel_color = get_pixel_color_under_cursor()  # Memanggil fungsi untuk mengambil warna pixel dan posisi
            print(f" {kuning}Color : {pixel_color}{reset} \n {kuning}Position : ({x}, {y}){reset}")
            time.sleep(0.2)  # Menunggu sebentar agar tidak terus-menerus mendeteksi saat tombol ditekan
        
        if play_again:
            play_again = False
            continue

        if paused:
            continue

        window_rect = (
            telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
        )

        if telegram_window != []:
            try:
                telegram_window.activate()
            except:
                telegram_window.minimize()
                telegram_window.restore()

        scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

        width, height = scrn.size
        pixel_found = False
        if pixel_found:
            break

        for x in range(0, width, 15):
            for y in range(0, height, 15):
                r, g, b = scrn.getpixel((x, y))
                if (b in range(0, 80)) and (r in range(150, 233)) and (g in range(215, 255)):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 2, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    break