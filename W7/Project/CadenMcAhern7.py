from tkinter import *
from functional import *

def main():

    #Power tests
    print(power(2, 3)) #should be 8
    print(power(-2, 3))     #should be -8
    print(power(1, 5)) #should be 1


    #Alien Ears tests
    print(alien_ears(1))        #should be 3
    print(alien_ears(2))        #should be 5
    print(alien_ears(4))        #should be 10


    #Flood fill tests
    image2 = [["red", "red", "red", "white", "red"],
              ["white", "red", "red", "red", "white"],
              ["red", "white", "red", "red", "white"],
              ["red", "red", "white", "white", "white"],
              ["red", "white", "white", "red", "white"]]

    # Perform first flood fill test
    start_row, start_col, newColor = 1, 2, "blue"
    imageCopy = copy.deepcopy(image2)
    result1 = flood_fill(start_row, start_col, newColor, imageCopy)

    window = Tk()
    window.title('Flood Fill start vs result')
    window.geometry('300x350')
    window.resizable(False, False)
    Gui(window, image2, result1)
    window.mainloop()

    # Perform 2nd flood fill test
    start_row, start_col, newColor = 2, 4, "green"
    imageCopy2 = copy.deepcopy(imageCopy)
    result2 = flood_fill(start_row, start_col, newColor, imageCopy2)

    window = Tk()
    window.title('Flood Fill start vs result')
    window.geometry('300x350')
    window.resizable(False, False)
    Gui(window, result1, result2)
    window.mainloop()

class Gui:
    def create_image(self, whichCanvas, whichImage):
        rect = {}
        fillVal = "black"
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column * self.cellWidth
                y1 = row * self.cellHeight
                x2 = x1 + self.cellWidth
                y2 = y1 + self.cellHeight
                fillVal = whichImage[row][column]
                rect[row, column] = whichCanvas.create_rectangle(x1, y1, x2, y2, fill=fillVal, tags="rect")

    def __init__(self, window, initial, final):
        self.window = window

        self.frame_one = Frame(self.window)
        self.initTitle = Label(self.frame_one, text='Initial Grid')
        self.initTitle.pack(side="top")
        self.canvas = Canvas(self.frame_one, width=150, height=150, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both")
        self.rows = 5
        self.columns = 5
        self.cellWidth = 25
        self.cellHeight = 25
        self.create_image(self.canvas, initial)
        self.frame_one.pack()

        self.frame_two = Frame(self.window)
        self.newTitle = Label(self.frame_two, text='New Grid')
        self.newTitle.pack(side="top")
        self.canvas2 = Canvas(self.frame_two, width=150, height=150, borderwidth=0, highlightthickness=0)
        self.canvas2.pack(side="top", fill="both")
        self.create_image(self.canvas2, final)
        self.frame_two.pack()

        #self.frame_one.pack()

if __name__ == "__main__":
    main()













