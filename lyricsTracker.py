from tkinter import *
from win32api import GetSystemMetrics
import os


class LyricsTracker:

    # def __init__(self, screenWidth, screenHeight):
    #     self.screenWidth = GetSystemMetrics(0)
    #     self.screenHeight = GetSystemMetrics(1)
    screenWidth = GetSystemMetrics(0)
    screenHeight = GetSystemMetrics(1)

    def startProgram():

        def onFrameConfigure(canvas):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))

        def onMouseWheel(event):
            # Adjust the scrolling of the canvas when the mouse wheel is scrolled
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            #canvas.configure(scrollregion=canvas.bbox("all"))

        class BackButton:
            def __init__(self, win):
                self.win = win
            def backButtonPressed(self):
                self.win.destroy()
                LyricsTracker.startProgram()

        lyrics, songTitle = LyricsTracker.getWords()
        songTitle = songTitle.replace("_"," ").title()


        # init window
        win = Tk()

        # size and font
        win.geometry(str(int(LyricsTracker.screenWidth * 0.4)) + "x" + str(int(LyricsTracker.screenHeight * 0.6)))
        #win.option_add("*Label.Font", "helvetica 20 bold")

        # create and pack label at the top
        # title = Label(win, text="Lyrics for " + songTitle)
        # title.pack()

        # init parts of the window
        win.title("Lyrics for " + songTitle)
        canvas = Canvas(win, borderwidth=0, background="#FBFAF5")
        frame = Frame(canvas, background="#FBFAF5")
        scrollbar = Scrollbar(win, width=20, orient = "vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)


        # packing items
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4,4),window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
        win.bind_all("<MouseWheel>", onMouseWheel)

        # create text widget and pack it
        tt = Text(frame, height=60, width=180,background="#FBFAF5")
        tt.pack()
        tt.config(font=("Yu Mincho Demibold", 22))

        # inserts text into the text item
        tt.insert('end', lyrics)
        tt.config(state=DISABLED)

        # pins the window to the top of the desktop
        win.attributes('-topmost', True)

        # back button pressed destroy window make call CreateWindow again
        bb = BackButton(win)
        backButton = Button(win, text="<-", command=bb.backButtonPressed)
        backButton.pack()

        win.mainloop()

    def getWords():
        class LabelSelector:
            def __init__(self, win, titles):
                self.win = win
                self.titles = titles
                self.selected_title = None

            def label_click(self, event):
                # Set the instance variable 'selected_text' to the text of the clicked label
                self.selected_title = event.widget.cget("text")
                self.win.destroy()  # Close the Tkinter window

        # creates a list of song titles without .txt
        titles = [file_name[:-4] for file_name in os.listdir("..\\Lyrics_Tracker\\savedSongs") if file_name.endswith(".txt")]
        
        # create a window 
        win = Tk()
        win.geometry(str(int(LyricsTracker.screenWidth * 0.4)) + "x" + str(int(LyricsTracker.screenHeight * 0.6)))
        
        # creates a label selector object that takes the current window and list of titles
        label_selector = LabelSelector(win, titles)

        # creates and packs a label for each song in the folder
        for i in range(len(titles)):
            label = Label(win, text = titles[i], cursor = "hand2")
            label.pack(pady=15)
            label.config(font="arial 16", state=DISABLED)

            label.bind("<Button-1>", label_selector.label_click)

        win.mainloop()

        # assigns the selected title to a variable
        title = label_selector.selected_title

        # testing with a hard coded file path
        # later create a window to select a song from the folder of saved songs
        try:
            filePath = f"..\\Lyrics_Tracker\\savedSongs\\{title}.txt"
            lyrics = ""
            with open(filePath, 'r', encoding = 'utf-8') as file:
                lines = file.readlines()

                for line in lines:
                    lyrics += str(line)
            
            file.close
        except:
            print("TESTING ")
        return lyrics, title
