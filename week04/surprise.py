# surprise.py
# A fake "crash" prank that turns into a mind-reading trick.
# Libraries:
#   random -> random fake errors/percentages and a shuffled card order
#   time   -> delays that build the tension
#   os     -> clears the screen

import os
import random
import time

CARD_COUNT = 6  # 6 cards cover every number from 1 to 63 (2 ** 6 = 64)


def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, delay=0.03):
  # Prints a text letter by letter, like a typewriter.
  for character in text:
    print(character, end="", flush=True)
    time.sleep(delay)
  print()


def ask_yes_no(question):
  # Keeps asking until the user answers yes or no. Returns True for yes.
  while True:
    answer = input(question).strip().lower()
    if answer in ["yes", "y"]:
      return True
    if answer in ["no", "n"]:
      return False
    print("Please answer with yes or no.")


def fake_crash(name):
  # Nothing is really deleted here. Everything is just text on the screen.
  print()
  slow_print(f"Starting the mind reader for {name}...")
  time.sleep(1)
  slow_print("Loading brain module...", 0.05)
  time.sleep(0.8)

  errors = [
      "ERROR: brain.dll not found",
      "WARNING: too many thoughts detected",
      "ERROR: imagination is out of memory",
      "FATAL: cannot divide by zero... again",
  ]
  for _ in range(4):
    print(random.choice(errors))
    time.sleep(random.uniform(0.3, 0.8))

  print()
  slow_print("Deleting homework.py ...")
  percent = 0
  while percent < 87:
    percent = min(87, percent + random.randint(3, 11))
    print(f"\rDeleting... {percent}%", end="", flush=True)
    time.sleep(0.15)
  print()
  time.sleep(1)

  print("CRITICAL ERROR!!! SYSTEM FAILURE!!!")
  for seconds in range(3, 0, -1):
    print(f"Shutting down in {seconds}...")
    time.sleep(1)

  clear_screen()
  slow_print("Just kidding :)")
  slow_print("Nothing was deleted. homework.py is safe.")
  time.sleep(1.5)
  slow_print("But since you are here, let me read your mind.")
  time.sleep(1.5)


def numbers_on_card(bit):
  # A number is on this card if its binary digit at position "bit" is 1.
  # (number // 2**bit) % 2 gives exactly that digit.
  size = 2 ** bit
  text = ""
  count = 0
  for number in range(1, 64):
    if (number // size) % 2 == 1:
      text += f"{number:3d}"
      count += 1
      if count % 8 == 0:
        text += "\n"
  return text.rstrip("\n")


def play_round(name):
  slow_print(f"{name}, think of a number between 1 and 63. Don't tell me!")
  input("Press Enter when you are ready...")

  # The cards are shown in random order, but the trick still works.
  order = list(range(CARD_COUNT))
  random.shuffle(order)

  total = 0
  for card_number, bit in enumerate(order, start=1):
    clear_screen()
    print(f"CARD {card_number} of {CARD_COUNT}\n")
    print(numbers_on_card(bit))
    print()
    if ask_yes_no("Is your number on this card? (yes/no): "):
      total += 2 ** bit  # the first number on a card is 1, 2, 4, 8, 16 or 32

  # Reveal
  clear_screen()
  slow_print("Reading your mind", 0.05)
  for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(1)
  print()

  if total == 0:
    print("You said no to every card. That number is not between 1 and 63...")
    print("Are you trying to trick me, " + name + "? :)")
    return

  slow_print(f"Your number is {total}!", 0.08)
  time.sleep(1.5)

  # The secret: it is not magic, it is binary numbers.
  secret = ""
  for bit in range(CARD_COUNT - 1, -1, -1):
    if (total // 2 ** bit) % 2 == 1:
      if secret != "":
        secret += " + "
      secret += str(2 ** bit)
  print()
  print("It's not magic, it's binary numbers.")
  print("The first numbers on the cards are 1, 2, 4, 8, 16 and 32.")
  print(f"I just added the cards you said yes to: {secret} = {total}")


def main():
  name = input("What is your name? ").strip()
  if name == "":
    name = "stranger"

  fake_crash(name)

  while True:
    play_round(name)
    if not ask_yes_no("\nPlay again? (yes/no): "):
      break

  print("Goodbye!")


if __name__ == "__main__":
  main()
