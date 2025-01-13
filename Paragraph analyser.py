import tkinter as tk
from ttkbootstrap import Style
from PIL import Image, ImageTk


def analyze_paragraph():
    entered_paragraph = entry.get()
    display_paragraph.config(text=f"Entered Paragraph: {entered_paragraph}")

    word_count = len(entered_paragraph.split())
    display_word_count.config(text=f"Total Number of words: {word_count}")

    counts = dict()
    words = entered_paragraph.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    display_word_counts.config(text="Word Counts:")
    for word, count in counts.items():
        display_word_counts.config(text=f"{display_word_counts.cget('text')}\n{word}: {count}")

def search_word():
    entered_paragraph = entry.get()
    search_word = search_entry.get()
    result = entered_paragraph.find(search_word)
    if result != -1:
        search_result.config(text=f"{search_word} found", font="Calibri 18 bold")
    else:
        search_result.config(text=f"{search_word} not found", font="Calibri 18 bold")

# Create the main window
root = tk.Tk()
root.minsize(600,400)
root.resizable(False, False)
root.title("Paragraph Analyzer")

# Load and convert image
image = Image.open('bg3.jpg')
image = ImageTk.PhotoImage(image)

# Create label and configure as background
background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place widgets
style = Style(theme="darkly")  # Change "darkly" to your preferred theme

entry_label = tk.Label(master=root, text="Enter a paragraph:", font="Calibri 22 bold")
entry_label.pack()

entry = tk.Entry(root, width=50, font="Calibri 18 bold")
entry.pack()

analyze_button = tk.Button(root, text="Analyze", font="Calibri 18 bold", command=analyze_paragraph)
analyze_button.pack()

buffer_1 = tk.Label(root)
buffer_1.pack()


display_paragraph = tk.Label(root, text="Entered Paragraph: ", font="Calibri 18 bold")
display_paragraph.pack()

buffer_3 = tk.Label(root)
buffer_3.pack()

display_word_count = tk.Label(root, text="Total Number of words: ", font="Calibri 18 bold")
display_word_count.pack()

display_word_counts = tk.Label(root, text="Word Counts:", font="Calibri 18 bold")
display_word_counts.pack()

buffer_2 = tk.Label(root)
buffer_2.pack()

search_label = tk.Label(root, text="Enter the word to search:", font="Calibri 18 bold")
search_label.pack()

search_entry = tk.Entry(root, width=30, font="Calibri 18 bold")
search_entry.pack()

search_button = tk.Button(root, text="Search", font="Calibri 18 bold", command=search_word)
search_button.pack()

# Configure button style to set the background color
style.configure("TButton", background="blue")

search_result = tk.Label(root, text="", font="Calibri 16 bold")
search_result.pack()

# Run the main loop
root.mainloop()
