#Code by bigmohammad
#---------------------
#Youtube: bigmohammad
#---------------------
#Instagram: bigmohammad.official

from art import *

def text_to_art(text):
    result = text2art(text)
    print(result)

while True:
    text = input("Enter a word : ")
    if text.lower() == '-----_@exit_----': #>>>>="If you type this, the program will close"
        break
    text_to_art(text)
