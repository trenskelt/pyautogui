import pyautogui
import time

answer = pyautogui.confirm(
    text="This will open Gmail and send an email to Michael Sekol. Continue?",
    title="PyAutoGUI Email",
    buttons=["Send it", "Cancel"],
)
if answer != "Send it":
    print("Cancelled.")
    raise SystemExit

pyautogui.FAILSAFE = True  # Move the mouse to any screen corner to abort.
pyautogui.PAUSE = 0.5  # Wait half a second after every PyAutoGUI call.

print("Screen size:", pyautogui.size())
print("Mouse is at:", pyautogui.position())

# Give yourself 3 seconds to get your hands off the keyboard.
time.sleep(3)

# Open the Windows Run box and launch Chrome at Gmail.
pyautogui.hotkey("win", "r")
pyautogui.write("chrome https://mail.google.com")
pyautogui.press("enter")

# Gmail takes a few seconds to load.
time.sleep(6)

# Focus the Gmail window, then press c to compose.
pyautogui.click(pyautogui.size().width // 2, pyautogui.size().height // 2)
pyautogui.press("c")
time.sleep(2)

# The cursor starts in the To box.
pyautogui.write("michael.sekol@mahoningctc.com", interval=0.03)
pyautogui.press("tab")

# Enter the subject and body.
pyautogui.press("tab")
pyautogui.write("Hi Mr. Sekol,", interval=0.03)
pyautogui.press("enter", presses=2)
pyautogui.write("Happy Birthday!", interval=0.03) 
pyautogui.press("enter")
pyautogui.write("I didnt know that you could just make it write your emails like this.", interval=0.03)
pyautogui.press("enter")
pyautogui.write("I didnt think it would be this easy as well.", interval=0.03)

# Send the email.
pyautogui.hotkey("ctrl", "enter")
print("Email sent.")
