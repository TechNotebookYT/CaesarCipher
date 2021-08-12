# https://youtube.com/technotebook
from tkinter import *
from tkinter import messagebox as mb

# English Alphabet List
eng_alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
'x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x',
'y','z']

# Encrypter Function
def encrypter(a, p, s, f):
    # This Function's purpose is to encrypt a string in the Caesar Cipher format (https://www.dcode.fr/caesar-cipher)
    # a - alphabet, p - phrase, s - shift, f - final list
    while True:
        if int(s) > 26:
            s -= 26
        elif int(s) <= 26:
            break
    
    for letter in p:
        index = 0
        for alpha in a:
            if letter == " ":
                f.append(" ")
                break
            elif letter == alpha:
                index += int(s)
                f.append(a[index])
                break
            elif letter != alpha:
                index += 1

def decrypter(a, p, s, f):
    # This Function's purpose is to decrypt a string in the Caesar Cipher format (https://www.dcode.fr/caesar-cipher)
    # a - alphabet, p - phrase, s - shift, f - final list
    while True:
        if int(s) > 26:
            s -= 26
        elif int(s) <= 26:
            break
    for letter in p:
        indexvar = 26
        for alpha in a:
            if letter == " ":
                f.append(" ")
                break
            elif letter == alpha:
                indexvar -= int(s)
                indexvar = int(indexvar)
                f.append(a[indexvar])
                break
            else:
                indexvar += 1

# GetEntry Function
def getEntryEncrypt():
    # Final List to temporarily store value
    final = []
    
    # Collects Data From fields
    phrase = phrase_entry.get().lower()
    shift = shift_entry.get().lower()
    
    ## DEBUG<>:
    #print(phrase)
    #print(shift)
    # Debug<>
    
    # Runs the Encrypter Function
    encrypter(eng_alpha_list, phrase, shift, final)
    def listToString(list_to_convert):
        separator = ""
        return (separator.join(list_to_convert))
    
    # Execute list_to_string
    finalString = listToString(final)
    
    # Creates a messagebox with the final string
    mb.showinfo("Result: ", str(finalString))

def getEntryDecrypt():
    # Final List to temporarily store value
    final = []
    
    # Collects Data From fields
    phrase = phrase_entry.get().lower()
    shift = shift_entry.get().lower()
    
    ## DEBUG<>:
    #print(phrase)
    #print(shift)
    # Debug<>
    
    # Runs the Decrypter Function
    decrypter(eng_alpha_list, phrase, shift, final)
    def listToString(list_to_convert):
        separator = ""
        return (separator.join(list_to_convert))
    
    # Execute list_to_string
    finalString = listToString(final)
    
    # Creates a messagebox with the final string
    mb.showinfo("Result: ", str(finalString))

# Creating Window
root = Tk()
root.title("Caesar Cipher Solver")
root.geometry("300x180")

# Defining Fields
phrase_label = Label(text = "Phrase", fg = "red")
phrase_entry = Entry(root, text = "Phrase to Encrypt/Decrypt")

shift_label = Label(text = "Shift", fg = "red")
shift_entry = Entry(root, text = "Shift")

EncryptButton = Button(text = "Encrypt", bg = "green", command = getEntryEncrypt)
DecryptButton = Button(text = "Decrypt", bg = "orange", command = getEntryDecrypt)

bottom_infocard = Label(text="Pranav Bala")
youtube = Label(text="https://youtube.com/technotebook", fg='red')

# Pack Fields
phrase_label.pack(fill = "x", side = "top")
phrase_entry.pack(fill = "x", side = "top")

shift_label.pack(fill = "x", side = "top")
shift_entry.pack(fill = "x", side = "top")

youtube.pack(fill="x", side="bottom")
bottom_infocard.pack(fill="x", side="bottom")

DecryptButton.pack(fill = "x", side = "bottom")
EncryptButton.pack(fill = "x", side = "bottom")


# Window Mainloop
root.mainloop()
