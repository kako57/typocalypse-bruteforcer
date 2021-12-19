import keyboard
from time import sleep

PAUSE_FLAG = True
EXIT_FLAG = False
SLEEP_INTERVAL = 0.1 # in milliseconds
WORDLIST = []
WORDLIST_INDEX = 0
with open("wordlist.txt", "r") as f:
  WORDLIST = f.readlines()
WORDLIST_LENGTH = len(WORDLIST)

def on_press_action(event):
  global EXIT_FLAG, PAUSE_FLAG
  if event.name == 'tab':
    PAUSE_FLAG = not PAUSE_FLAG
    if PAUSE_FLAG:
      print("\rpaused ", end="")
    else:
      print("\rrunning", end="")
  elif event.name == '`':
    EXIT_FLAG = True

def type_word_from_wordlist():
  global WORDLIST, WORDLIST_INDEX
  keyboard.write(WORDLIST[WORDLIST_INDEX].strip());
  keyboard.press_and_release('ctrl+a')
  WORDLIST_INDEX += 1
  if WORDLIST_INDEX >= WORDLIST_LENGTH:
    WORDLIST_INDEX = 0
  sleep(SLEEP_INTERVAL)

keyboard.on_press(on_press_action, suppress=True)

while True:
  if EXIT_FLAG:
    break
  if not PAUSE_FLAG:
    type_word_from_wordlist()
