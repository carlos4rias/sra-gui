import tkinter as tk
from tkinter import filedialog
import os
from config import *

class YoloMark( tk.Frame ):

    def __init__( self, parent, controller ):
        tk.Frame.__init__( self, parent )
        self.controller = controller

        # Title
        tk.Label( self, text="Yolo Mark", justify="center", font=controller.title_font ).grid( row = 0, column = 0)

        # For Image and Video
        self.button_folder_images = tk.Button( self, text = "Folder Img", command = self.DialogFolder )

        # Widgets to video
        self.button_video_address = tk.Button( self, text = "Video Address", command = self.DialogVideo )
        self.label_fps = tk.Label( self, text = "FPS: " )
        self.entry_fps = tk.Entry( self, width=5)

        # Widgets to Images
        self.button_train_text = tk.Button( self, text = "train.txt Address", command = self.DialogTrain )
        self.button_obj_name = tk.Button( self, text = "obj.name Address", command = self.DialogNames )
        
        # Two Option
        self.r = tk.StringVar()
        self.r.set("1")
        tk.Radiobutton( self, text = "Image", variable=self.r, value="1", command=self.Siwtch ).grid( row = 1, column = 0)
        tk.Radiobutton( self, text = "Video", variable=self.r, value="2", command=self.Siwtch ).grid( row = 2, column = 0)
        
        # Show 
        self.button_folder_images.grid( row = 3, column = 0)
        self.ShowImage()
        #tk.Button( self, text = "Cancel", command = self.test ).grid( row = 6, column = 0)
        tk.Button( self, text = "Next", command = self.Run ).grid( row = 6, column = 0)

    def ShowVideo( self ):
        self.button_video_address.grid( row = 4, column = 0 )
        self.label_fps.grid( row = 5, column = 0 )
        self.entry_fps.grid( row = 5, column = 1 )

    def ShowImage( self ):
        self.button_train_text.grid( row = 4, column = 0)
        self.button_obj_name.grid( row = 5, column = 0)

    def NoShowVideo( self ):
        self.button_video_address.grid_forget()
        self.label_fps.grid_forget()
        self.entry_fps.grid_forget()

    def NoShowImage( self ):
        self.button_train_text.grid_forget()
        self.button_obj_name.grid_forget()
    
    def Siwtch( self ):
        if( self.r.get() == "1" ):
            self.NoShowVideo()
            self.ShowImage()
        else :
            self.NoShowImage()
            self.ShowVideo()

    def DialogFolder( self ):
        self.folder_images = filedialog.askdirectory( )
        print( self.folder_images )

    def DialogVideo( self ):
        self.path_video = filedialog.askopenfilename( initialdir = "/", title = "Select file",
                                        filetypes = (("mp4 files","*.mp4"), ) )
        print( self.path_video )

    def DialogTrain( self ):
        self.path_train = filedialog.askopenfilename( initialdir = "/", title = "Select file",
                                        filetypes = (("txt files","*.txt"), ) )
        print( self.path_train )

    def DialogNames( self ):
        self.path_names = filedialog.askopenfilename( initialdir = "/", title = "Select file",
                                        filetypes = (("name files","*.name"), ) )
        print( self.path_names )

    def Run( self ):
        ##print( self.r.get() + ' ' + self.folder_images + ' ' + self.path_video + ' ' + self.entry_fps.get())
        if( self.r.get() == "1" ) :
            if( (not self.folder_images) or (not self.path_train) or (not self.path_names) ):
                print( "Faltan datos" )
            else:
                command = paths['yolo_path'] + ' ' + self.folder_images + ' ' + self.path_train + ' ' + self.path_names 
                os.system( command )
                print( "run command ")
        else:
            if( (not self.folder_images) or (not self.path_video) or (not self.entry_fps.get()) ):
                print( "Faltan datos" )
            else:
                command = paths['yolo_path'] + ' ' + self.folder_images + ' cap_video ' + self.path_video + ' ' + self.entry_fps.get()
                os.system( command )
                print( "run command ")

    def test( self ):
        pass
