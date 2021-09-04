import tkinter as tk
from tkinter import filedialog, mainloop
from tkinter.constants import CENTER
from tkinter import messagebox
from os.path import join
root = tk.Tk()
root.geometry("400x400")
root.title('Upload File')


def readFile(filename):
    file = open(filename)
    counter = dict()
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

    filteredItems = dict(sorted(counter.items(), key=lambda x: x[1]))
    outputpath = "/Users/rawscripter/Desktop/"
    outputFileName = 'words.txt'

    newFile = open(join(outputpath, outputFileName), 'w')
    newFile.write(str(filteredItems))
    newFile.close()
    file.close()
    messagebox.showinfo("File converted successfully",
                        "Please check your file current folder to get the output file.")


def getLocalFile():
    root = tk.Tk()

    root.withdraw()

    filePath = filedialog.askopenfilename()
    # print('File path：', filePath)
    # return filePath
    readFile(filePath)


fileUploadButton = tk.Button(
    text="Upload File", padx=20, pady=20, command=getLocalFile)

fileUploadButton.pack()
fileUploadButton.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()