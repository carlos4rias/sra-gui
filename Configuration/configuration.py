
import tkinter as tk
from tkinter import filedialog
import os


class Configuration( tk.Frame ):

    DARKNET = 'darknet'
    YOLOMARK = 'yolomark'

    def __init__( self, parent, controller ):
        tk.Frame.__init__( self, parent )
        self.controller = controller

        frame = tk.LabelFrame(self, text = "Rutas Darknet & YoloMark", padx = 10, pady = 10)

        # variables to path
        self.path_darknet = ''
        self.path_yolo_mark = ''


        # Path for Darknet
        self.folder_darknet_btn = tk.Button(
            frame,
            text = "Ruta Darknet",
            command = self.DialogDarknet
        )
        self.folder_darknet_lbl = tk.Label( frame )
        
        # Path for yolomark
        self.folder_yolo_mark_btn = tk.Button(
            frame,
            text = "Ruta yolo_mark",
            command = self.DialogYoloMark
        )
        self.folder_yolo_mark_lbl = tk.Label( frame )

         # Back to main
        self.back_home_btn = tk.Button(
            frame,
            text = "Volver",
            command = lambda : self.Run('Main')
        )

        if self.DARKNET in self.controller.config.paths:
            path_darknet = self.controller.config.paths[self.DARKNET]
            self.SetLabelText(self.folder_darknet_lbl, path_darknet)

        if self.YOLOMARK in self.controller.config.paths:
            path_yolo_mark = self.controller.config.paths[self.YOLOMARK]
            self.SetLabelText(self.folder_yolo_mark_lbl, path_yolo_mark)

        # Show widgets
        frame.grid( row = 0, column = 0, padx = 20, pady = 20)

        self.folder_darknet_lbl.grid( row = 3, column = 0, padx = 10 )
        self.folder_darknet_btn.grid( row = 3, column = 1, sticky = 'nsew', pady = 3 )
        self.folder_yolo_mark_lbl.grid( row = 4, column = 0, padx = 10 )
        self.folder_yolo_mark_btn.grid( row = 4, column = 1, sticky = 'nsew', pady = 3 )
        self.back_home_btn.grid( row = 5, column = 0, sticky = 'nsew', columnspan = 11 )

    def DialogDarknet( self ):
        self.path_darknet = filedialog.askdirectory()
        self.SetLabelText(self.folder_darknet_lbl, self.path_darknet)
        if len(self.path_darknet) > 0:
            self.controller.config.paths[self.DARKNET] = self.path_darknet

    def DialogYoloMark( self ):
        self.path_yolo_mark = filedialog.askdirectory()
        self.SetLabelText(self.folder_yolo_mark_lbl, self.path_yolo_mark)
        if len(self.path_yolo_mark) > 0:
            self.controller.config.paths[self.YOLOMARK] = self.path_yolo_mark

    def SetLabelText( self, label, text ):
        label["text"] = text

    def Run(self, window):
        self.controller.show_frame(window)
