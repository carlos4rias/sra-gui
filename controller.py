import tkinter as tk

import config
from Configuration.configuration import Configuration
from main import Main
from Run.run import Run
from Training.train import Train
from YoloMark.yoloMark import YoloMark

class Controller( tk.Tk ):

    def __init__( self, *args, **kwargs ):
        tk.Tk.__init__( self, *args, **kwargs )

        self.config = config

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.show_frame( 'Main' )

    def show_frame( self, page_name_show ):
        '''Show a frame for the given page name'''
        for F in ( YoloMark, Main, Configuration, Train, Run ):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        frame = self.frames[page_name_show]
        frame.tkraise()

if __name__ == "__main__" :
    app = Controller()
    app.mainloop()