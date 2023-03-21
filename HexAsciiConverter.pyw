# -----------------------------------------------------
# | Hex/ASCII Converter     |   Created by Ea    v. 1 |
# -----------------------------------------------------
# | Date:               21.03.2023                    |
# -----------------------------------------------------

from tkinter import *
# from time import sleep


class Application():
    def HexToAscii(self, event):
        hexStr = self.hexBox.get(1.0, END)
        if (hexStr != ''):
            #   Write in cmd hex string
            # print('Hex: {}'.format(hexStr))
            #   Decode hex to ascii
            asciiTxt = bytes.fromhex(hexStr).decode('utf-8')
            #   Write in cmd decoded ascii string
            # print('Ascii: {}'.format(asciiTxt))
            #   Clear txt box
            self.txtBox.delete(1.0, END)
            #   Insert decoded
            self.txtBox.insert(END, asciiTxt)
        else:
            pass

    def AsciiToHex(self, event):
        txtStr = self.txtBox.get(1.0, END)
        #   if doesn't work xd
        if (txtStr != ''):
            #   Write in cmd hex string
            # print('Ascii: {}'.format(txtStr))
            #   Decode hex to ascii
            hexTxt = txtStr.encode('utf-8').hex()
            #   Write in cmd decoded ascii string
            # print('Hex: {}'.format(hexTxt))
            #   Clear txt box
            self.hexBox.delete(1.0, END)
            #   Insert decoded
            self.hexBox.insert(END, hexTxt)
        else:
            pass

    def Application_custom_title(self, main):
        #   Create custom title Application frame
        titleFrame = Frame(main, width=app_w,
                           height=30)
        titleFrame.pack(side=TOP)
        titleFrame.pack_propagate(0)
        #   Change custom title bg color
        titleFrame.configure(bg='#0A150B')
        #   Add label
        Label(titleFrame, text='   HEX/ASCII Converter    v. 1', foreground='#2BFF00', bg='#0A150B', font='Times 18',
              height=20, border=0).pack(side=LEFT)
        #   Create custom buttons
        Label(titleFrame, text='    ', bg='#0A150B',
              height=20, border=0).pack(side=RIGHT)
        hexBtn = Button(titleFrame, text='  X  ',
                        background='#0A150B', font='Times 18', foreground='#00FF1A', height=1, width=1, command=quit, border=0)
        hexBtn.pack(side=RIGHT)
        Label(titleFrame, text='    ', bg='#0A150B',
              height=20, border=0).pack(side=RIGHT)
        hexBtn = Button(titleFrame, text='  —  ',
                        background='#0A150B', font='Times 18', foreground='#00FF1A', height=1, width=1, command=quit, border=0)
        hexBtn.pack(side=RIGHT)

    def Application_Frames(self, main):
        #   Create custom title
        self.Application_custom_title(main)

        #   Create main Application frame
        labelsFrame = Frame(main, width=app_w,
                            height=60)
        labelsFrame.pack(side=TOP)
        labelsFrame.pack_propagate(0)

        #   Frame for `hex` label
        hexFrame = Frame(labelsFrame, bg='#0A150B', width=app_w //
                         2, height=60)
        hexFrame.pack(side=LEFT)
        hexFrame.pack_propagate(0)

        #   Frame for `txt` label
        txtFrame = Frame(labelsFrame, bg='#0A150B', width=app_w //
                         2, height=60)
        txtFrame.pack(side=LEFT)
        txtFrame.pack_propagate(0)

        #   Create `hex` and `txt` labels
        Label(hexFrame, text='   HEX', foreground='#2BFF00', bg='#0A150B', font='Times 23',
              height=60, border=0).pack(side=LEFT)
        Label(txtFrame, text='   ASCII', foreground='#2BFF00', bg='#0A150B', font='Times 23',
              height=60, border=0).pack(side=LEFT)

        #   Create buttons
        hexBtn = Button(hexFrame, text='Convert',
                        background='#363636', font='Times 15', foreground='#00FF1A', height=1, width=6)
        hexBtn.pack(side=RIGHT)
        txtBtn = Button(txtFrame, text='Convert',
                        background='#363636', font='Times 15', foreground='#00FF1A', height=1, width=6)
        txtBtn.pack(side=RIGHT)

        #   Frame for `hex` box
        hexBoxFrame = Frame(main, bg='#363636', width=app_w //
                            2, height=app_h-60, )
        hexBoxFrame.pack(side=LEFT)
        hexBoxFrame.pack_propagate(0)

        #   Frame for `hex` box
        txtBoxFrame = Frame(main, bg='#363636', width=app_w //
                            2, height=app_h-60,)
        txtBoxFrame.pack(side=LEFT)
        txtBoxFrame.pack_propagate(0)

        #   Create `hex` and `txt` boxes
        self.hexBox = Text(hexBoxFrame, bg='#363636',
                           fg='white', font="Courier 14")
        self.hexBox.pack(side=LEFT)
        self.txtBox = Text(txtBoxFrame, bg='#363636',
                           fg='white', font="Courier 14")
        self.txtBox.pack(side=LEFT)

        #   Add events to buttons and boxes
        hexBtn.bind("<Button-1>", self.HexToAscii)
        txtBtn.bind("<Button-1>", self.AsciiToHex)

    def Application_window(self, main):
        #   Window size
        global app_w
        global app_h
        app_w = 720
        app_h = 380
        #   Coords to centre the window
        width_to_centre = main.winfo_screenwidth()//2 - app_w//2
        height_to_centre = main.winfo_screenheight()//2 - app_h//2
        #
        main.geometry("{}x{}+{}+{}".format(app_w, app_h,
                      width_to_centre, height_to_centre))
        #   Rename title of window
        main.title('Hex/ASCII Converter')
        #   Change background color of window
        main.configure(bg='#1E1E1E')
        main.resizable(False, False)

    #    Called when Application was run
    def __init__(self):
        #   Create Tk
        main = Tk()
        main.overrideredirect(1)
        #   Call def to create window
        self.Application_window(main)
        #   Show ...
        self.Application_Frames(main)

        #   Start main loop
        main.mainloop()


#   Run app
try:
    #   Call app class
    Application()

#   Catch error
except NameError:
    # print('Error name: ' + NameError)
    pass
