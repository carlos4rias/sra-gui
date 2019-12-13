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

        # variables to path
        self.folder_images = ''
        self.path_video = ''
        self.path_train = ''
        self.path_names = ''

        # For Image and Video
        self.button_folder_images = tk.Button( self, text = "Folder Img", command = self.DialogFolder )
        self.entry_images_address = tk.Entry( self )

        # Widgets to video
        self.button_video_address = tk.Button( self, text = "Video Address", command = self.DialogVideo )
        self.entry_video_address = tk.Entry( self )
        self.label_fps = tk.Label( self, text = "FPS: " )
        self.entry_fps = tk.Entry( self, width=5)

        # Widgets to Images
        self.button_train_text = tk.Button( self, text = "train.txt Address", command = self.DialogTrain )
        self.entry_train_address = tk.Entry( self )
        self.button_obj_name = tk.Button( self, text = "obj.name Address", command = self.DialogNames )
        self.entry_obj_address = tk.Entry( self )
        
        # Two Option
        self.r = tk.StringVar()
        self.r.set("1")
        tk.Radiobutton( self, text = "Image", variable=self.r, value="1", command=self.Siwtch ).grid( row = 1, column = 0)
        tk.Radiobutton( self, text = "Video", variable=self.r, value="2", command=self.Siwtch ).grid( row = 2, column = 0)
        
        # Show 
        self.entry_images_address.grid( row = 3, column = 0, padx = 10 )
        self.button_folder_images.grid( row = 3, column = 1, sticky = 'nsew', pady = 3 )
        self.ShowImage()
        tk.Button( self, text = "Next", command = self.Run ).grid( row = 6, pady = 3 )


    def ShowVideo( self ):
        self.entry_video_address.grid( row = 4, column = 0, padx = 10 )
        self.button_video_address.grid( row = 4, column = 1, sticky = 'nsew', pady = 3 )
        self.label_fps.grid( row = 5, column = 0, padx = 10 )
        self.entry_fps.grid( row = 5, column = 1, sticky = 'nsew' )


    def ShowImage( self ):
        self.entry_train_address.grid( row = 4, column = 0, padx = 10 )
        self.button_train_text.grid( row = 4, column = 1, sticky = 'nsew', pady = 3 )
        self.entry_obj_address.grid( row = 5, column = 0, padx = 10 )
        self.button_obj_name.grid( row = 5, column = 1, sticky = 'nsew', pady = 3 )


    def NoShowVideo( self ):
        self.entry_video_address.grid_forget()
        self.button_video_address.grid_forget()
        self.label_fps.grid_forget()
        self.entry_fps.grid_forget()


    def NoShowImage( self ):
        self.entry_train_address.grid_forget()
        self.button_train_text.grid_forget()
        self.entry_obj_address.grid_forget()
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
        self.entry_images_address.delete( 0, tk.END )
        self.entry_images_address.insert( 0, self.folder_images )


    def DialogVideo( self ):
        self.path_video = filedialog.askopenfilename( initialdir = "/", title = "Select file",
                                        filetypes = (("mp4 files","*.mp4"), ) )
        self.entry_video_address.delete( 0, tk.END )
        self.entry_video_address.insert( 0, self.path_video )


    def DialogTrain( self ):
        self.path_train = filedialog.askopenfilename( initialdir = "/", title = "Select file",
                                        filetypes = (("txt files","*.txt"), ) )
        self.entry_train_address.delete( 0, tk.END )
        self.entry_train_address.insert( 0, self.path_train )


    def DialogNames( self ):
        self.path_names = filedialog.askopenfilename( initialdir = "/", title = "Select file",
                                        filetypes = (("name files","*.name"), ) )
        self.entry_obj_address.delete( 0, tk.END )
        self.entry_obj_address.insert( 0, self.path_names )


    def Run( self ):
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
