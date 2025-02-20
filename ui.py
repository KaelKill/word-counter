import tkinter as tk
from tkinter import filedialog
from count_words import count_words


def on_button_click(entry, label):
    text = entry.get()
    word_count = count_words(text)
    label.config(text=f"Word count: {word_count}")

def upload_file(entry, label):
    filename = filedialog.askopenfilename()
    with open(filename, 'r') as f:
        text = f.read()
    if not text:
        label.config(text="No text in file.")
        return
    else:
        entry.insert(0, text)
        word_count = count_words(text)
        label.config(text=f"Word count: {word_count}")

def create_gui():
    root = tk.Tk()
    root.geometry("300x200")
    root.title("Word Counter")

    label = tk.Label(root, text="Enter text:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Count words", command=lambda: on_button_click(entry, result_label))
    button.pack()

    upload_button = tk.Button(root, text="Upload file", command=lambda: upload_file(entry, result_label))
    upload_button.pack()

    result_label = tk.Label(root, text="Word count: 0")
    result_label.pack()

    root.mainloop()

if __name__ == '__main__':
    create_gui()