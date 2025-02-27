import os
import time
from PIL import Image

def show_intro():
    os.system("clear")
    print("\033[1;36m")
    print("  ╔══════════════════════════════════════════╗")
    print("  ║               🔹 StegX 🔹                ║")
    print("  ║                                          ║")
    print("  ║  👤 Author: Plotter Lyta                 ║")
    print("  ║  🔗 GitHub: github.com/plotterlyta-dev   ║")
    print("  ║  🎦 YouTube: @techy_tricks_plotterlyta   ║")  
    print("  ║  📨 Contact: plotterlyta@gmail.com       ║")
    print("  ╚══════════════════════════════════════════╝")
    
    print("\n\033[1;32m🔍 What is StegX?")
    print("\033[1;37mStegX is a steganography tool that allows you to hide secret messages inside images.")
    print("You can use it to encode a message into an image and later extract it whenever needed.")
    print("\n✅ Features:")
    print("   - Hide any text message inside an image without changing its appearance.")
    print("   - Extract hidden messages from images encoded with this tool.")
    
    input("\n\033[1;34m🔹 Press Enter to continue...\033[1;37m")

def show_menu():
    os.system("clear")
    print("\033[1;32m")
    print("╭━━━┳╮╱╱╱╭╮╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮")
    print("┃╭━╮┃┃╱╱╭╯╰┳╯╰╮╱╱╱╱╱┃┃╱╱╱╱╱╭╯╰╮")
    print("┃╰━╯┃┃╭━┻╮╭┻╮╭╋━━┳━╮┃┃╱╱╭╮╱┣╮╭╋━━╮")
    print("┃╭━━┫┃┃╭╮┃┃╱┃┃┃┃━┫╭╯┃┃╱╭┫┃╱┃┃┃┃╭╮┃")
    print("┃┃╱╱┃╰┫╰╯┃╰╮┃╰┫┃━┫┃╱┃╰━╯┃╰━╯┃╰┫╭╮┃")
    print("╰╯╱╱╰━┻━━┻━╯╰━┻━━┻╯╱╰━━━┻━╮╭┻━┻╯╰╯")
    print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃")
    print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯")

    print("\033[1;36m")
    print("  ╔══════════════════════════════════════════╗")
    print("  ║               🔹 StegX 🔹                ║")
    print("  ╚══════════════════════════════════════════╝")
    print("\033[1;32m  [1] Hide Message in Image")
    print("  [2] Extract Hidden Message")
    print("  [3] Exit")
    print("\033[1;37m")

def loading_effect(duration=2):
    print("\033[1;34mProcessing", end="", flush=True)
    for _ in range(duration):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n\033[1;37m")

def encode_image():
    input_image = input("\n\033[1;33m📂 Enter the path of the input image: \033[1;37m").strip()
    message = input("\033[1;33m📝 Enter the secret message: \033[1;37m").strip()
    output_image = input("\033[1;33m💾 Enter the output image filename (e.g., lyta.png): \033[1;37m").strip()

    loading_effect()

    try:
        img = Image.open(input_image)
        img = img.convert("RGB")
        pixels = img.load()

        message += chr(0) 
        binary_message = ''.join(format(ord(c), '08b') for c in message)

        if len(binary_message) > img.width * img.height:
            raise ValueError("❌ Message is too large to hide in the image.")

        data_index = 0
        for y in range(img.height):
            for x in range(img.width):
                if data_index < len(binary_message):
                    r, g, b = pixels[x, y]
                    new_r = (r & 0xFE) | int(binary_message[data_index])
                    pixels[x, y] = (new_r, g, b)
                    data_index += 1
                else:
                    break
            if data_index >= len(binary_message):
                break

        img.save(output_image)
        print(f"\n\033[1;32m✅ Message successfully encoded and saved as '{output_image}'\033[1;37m")

    except FileNotFoundError:
        print("\n\033[1;31m❌ Error: The input image file was not found! Check the path.\033[1;37m")

    input("\n\033[1;34mPress Enter to return to the menu...\033[1;37m")

def decode_image():
    input_image = input("\n\033[1;33m📂 Enter the path of the image to decode: \033[1;37m").strip()

    loading_effect()

    try:
        img = Image.open(input_image)
        img = img.convert("RGB")
        pixels = img.load()

        binary_message = ""
        for y in range(img.height):
            for x in range(img.width):
                r, _, _ = pixels[x, y]
                binary_message += str(r & 1)

        message = ""
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            if len(byte) < 8:
                break
            char = chr(int(byte, 2))
            if char == chr(0):
                break
            message += char

        if message:
            print(f"\n\033[1;32m✅ Hidden message extracted: '{message}'\033[1;37m")
        else:
            print("\n\033[1;31m⚠️ No hidden message found in the image.\033[1;37m")

    except FileNotFoundError:
        print("\n\033[1;31m❌ Error: The image file was not found! Check the path.\033[1;37m")

    input("\n\033[1;34mPress Enter to return to the menu...\033[1;37m")

if __name__ == "__main__":
    show_intro()  # Display introduction before menu
    while True:
        show_menu()
        choice = input("\n\033[1;35m🎯 Select an option: \033[1;37m").strip()

        if choice == "1":
            encode_image()
        elif choice == "2":
            decode_image()
        elif choice == "3":
            print("\n\033[1;31m🚪 Exiting... Have a great day!\033[1;37m")
            time.sleep(1)
            break
        else:
            print("\n\033[1;31m❌ Invalid option! Try again.\033[1;37m")
            time.sleep(1)