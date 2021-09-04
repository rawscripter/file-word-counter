import tkinter as tk
from tkinter import filedialog, mainloop
from tkinter.constants import CENTER
from tkinter import messagebox
from os.path import join
from tkinter.filedialog import asksaveasfile
import json

root = tk.Tk()
root.geometry("400x400")
root.title('Word Counter App')


# ask user where to save the file
def save(data):
    file = asksaveasfile(mode='w', defaultextension=".json")
    if file is None:
        return
    file.write(str(data))
    file.close()


# read file and save it as json file
def readFile(filename):
    file = open(filename)
    counter = dict()
    # loop every line from file
    lines = file.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                word = word.replace(',', '')
                word = word.replace('.', '')
                counter[word] = 1
    file.close()
    # sort to ascending order
    outPutData = dict(sorted(counter.items(), key=lambda x: x[1]))
    json_object = json.dumps(outPutData, indent=4)
    # save as json object
    save(json_object)


# upload file
def getLocalFile():
    root = tk.Tk()
    root.withdraw()
    filePath = filedialog.askopenfilename()
    readFile(filePath)


# file upload button
fileUploadButton = tk.Button(
    text="Upload File", padx=20, pady=20, command=getLocalFile)

fileUploadButton.pack()
fileUploadButton.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()
