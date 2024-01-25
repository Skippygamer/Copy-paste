import pyperclip
import keyboard

def type_paste():
    # Simulate CTRL + B
    keyboard.press_and_release('ctrl+b')

def main():
    last_clipboard = pyperclip.paste()

    try:
        while True:
            current_clipboard = pyperclip.paste()

            # Check if 'CTRL + B' is pressed
            if keyboard.is_pressed('ctrl+b'):
                print("CTRL + B pressed")

                # Type the copied letters
                type_paste()
                keyboard.write(current_clipboard)

                # Uncomment the next line if you want to clear the clipboard after typing
                # pyperclip.copy('')

            # No delay for instant response
            # Adjust the delay if needed

    except KeyboardInterrupt:
        print("Script terminated by user.")

if __name__ == "__main__":
    main()
