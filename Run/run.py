import tkinter as tk
from tkinter import filedialog
import os
from config import *


class Run( tk.Frame ):


    def __init__( self, parent, controller ):
        tk.Frame.__init__( self, parent )
        self.controller = controller

        # Title
        self.frame = tk.LabelFrame(self, text = "Menu", padx = 10, pady = 10)

        # Four Option
        self.r = tk.StringVar()
        self.r.set("1")
        tk.Radiobutton( self.frame, text = "Imagen", variable=self.r, value="1", command = self.Switch ).grid( row = 0, column = 0, sticky="w", columnspan = 2 )
        tk.Radiobutton( self.frame, text = "Video", variable=self.r, value="2", command = self.Switch ).grid( row = 1, column = 0, sticky="w", columnspan = 2 )
        tk.Radiobutton( self.frame, text = "Web Cam", variable=self.r, value="3", command = self.Switch ).grid( row = 2, column = 0, sticky="w", columnspan = 2 )
        tk.Radiobutton( self.frame, text = "RTSP", variable=self.r, value="4", command = self.Switch ).grid( row = 3, column = 0, sticky="w", columnspan = 2 )

        # button
        self.next = tk.Button( self.frame, text = "Siguiente", command = self.Run )
        self.cancel = tk.Button( self.frame, text = "Cancelar", command = lambda: self.controller.show_frame( 'Main' ) )

        # Entries
        self.entries = {}
        self.data_btn = tk.Button( self.frame, text = "*.Data", command = lambda: self.DialogFile( 'data_entry', 'data' ) )
        self.entries["data_entry"] = tk.Entry( self.frame, width = 10 )
        self.cfg_btn = tk.Button( self.frame, text = "*.cfg", command = lambda: self.DialogFile( 'cfg_entry', 'cfg' ) )
        self.entries["cfg_entry"] = tk.Entry( self.frame, width = 10 )
        self.weights_btn = tk.Button( self.frame, text = "*.weights", command = lambda: self.DialogFile( 'weights_entry', 'weights' ) )
        self.entries["weights_entry"] = tk.Entry( self.frame, width = 10 )
        self.image_btn = tk.Button( self.frame, text = "*.jpg", command = lambda: self.DialogFile( 'image_entry', 'jpg' ) )
        self.entries["image_entry"] = tk.Entry( self.frame, width = 10 )
        self.video_btn = tk.Button( self.frame, text = "*.mp4", command = lambda: self.DialogFile( 'video_entry', 'mp4' ) )
        self.entries["video_entry"] = tk.Entry( self.frame, width = 10 )
        self.camera_btn = tk.Label( self.frame, text = "# camara" )
        self.entries["camera_entry"] = tk.Entry( self.frame, width = 10 )
        self.GPU_label = tk.Label( self.frame, text = "# GPU" )
        self.entries["GPU_entry"] = tk.Entry( self.frame, width = 10 )
        self.user_label = tk.Label( self.frame, text = "User" )   #
        self.entries["user_entry"] = tk.Entry( self.frame, width = 10 )
        self.password_label = tk.Label( self.frame, text = "Password" )
        self.entries["password_entry"] = tk.Entry( self.frame, width = 10 )
        self.ip_label = tk.Label( self.frame, text = "IP" )
        self.entries["ip_entry"] = tk.Entry( self.frame, width = 10 )

        # Show widgets
        self.frame.grid( row = 0, column = 0 )
        self.entries["data_entry"].grid( row = 4, column = 0, sticky="nsew" )
        self.data_btn.grid( row = 4, column = 1, sticky="nsew" )
        self.entries["cfg_entry"].grid( row = 5, column = 0, sticky="nsew" )
        self.cfg_btn.grid( row = 5, column = 1, sticky="nsew" )
        self.entries["weights_entry"].grid( row = 6, column = 0, sticky="nsew" )
        self.weights_btn.grid( row = 6, column = 1, sticky="nsew" )
        self.entries["GPU_entry"].grid( row = 7, column = 0, sticky="nsew")
        self.GPU_label.grid( row = 7, column = 1, sticky="nsew")
        self.cancel.grid( row = 11, column = 0, sticky="nsew" )
        self.next.grid( row = 11, column = 1, sticky="nsew" )

        self.Switch()

    def DialogFile( self, name, ext ):
        temp = filedialog.askopenfilename( title = "Select file",
                                        filetypes = ( ( ext + " files","*." + ext ), ) )
        self.entries[name].delete( 0, tk.END )
        self.entries[name].insert( 0, temp )

    def ShowImage( self ):
        self.entries['image_entry'].grid( row = 8, column = 0, sticky="nsew" )
        self.image_btn.grid( row = 8, column = 1, sticky="nsew" )

    def ShowVideo( self ):
        self.entries['video_entry'].grid( row = 8, column = 0, sticky="nsew" )
        self.video_btn.grid( row = 8, column = 1, sticky="nsew" )

    def ShowCamera( self ):
        self.entries['camera_entry'].grid( row = 8, column = 0, sticky="nsew" )
        self.camera_btn.grid( row = 8, column = 1, sticky="nsew" )

    def ShowRTSP( self ):
        self.entries["user_entry"].grid( row = 8, column = 0, sticky="nsew" )
        self.user_label.grid( row = 8, column = 1, sticky="nsew" )
        self.entries["password_entry"].grid( row = 9, column = 0, sticky="nsew" )
        self.password_label.grid( row = 9, column = 1, sticky="nsew" )
        self.entries["ip_entry"].grid( row = 10, column = 0, sticky="nsew" )
        self.ip_label.grid( row = 10, column = 1, sticky="nsew" )

    def NotShowImage( self ):
        self.entries['image_entry'].grid_forget()
        self.image_btn.grid_forget()

    def NotShowVideo( self ):
        self.entries['video_entry'].grid_forget()
        self.video_btn.grid_forget()

    def NotShowCamera( self ):
        self.entries['camera_entry'].grid_forget()
        self.camera_btn.grid_forget()

    def NotShowRTSP( self ):
        self.entries["user_entry"].grid_forget()
        self.user_label.grid_forget()
        self.entries["password_entry"].grid_forget()
        self.password_label.grid_forget()
        self.entries["ip_entry"].grid_forget()
        self.ip_label.grid_forget()

    def Switch( self ):
        if( self.r.get() == "1" ):
            self.NotShowRTSP()
            self.NotShowVideo()
            self.NotShowCamera()
            self.ShowImage()

        if( self.r.get() == "2" ):
            self.NotShowRTSP()
            self.NotShowCamera()
            self.NotShowImage()
            self.ShowVideo()

        if( self.r.get() == "3" ):
            self.NotShowRTSP()
            self.NotShowImage()
            self.NotShowVideo()
            self.ShowCamera()

        if( self.r.get() == "4" ):
            self.ShowRTSP()
            self.NotShowImage()
            self.NotShowVideo()
            self.NotShowCamera()

    def Run( self ):
        if( 'darknet' in self.controller.config.paths ):
            os.chdir( self.controller.config.paths['darknet'] )
            command = self.controller.config.paths['darknet'] + '/darknet'
            if( (self.entries["data_entry"].get() == '') or (self.entries["cfg_entry"].get() == '') or (self.entries["weights_entry"].get() == '') ):
                print( "Faltan Datos" )
            else:
                if( self.r.get() == "1" ):
                    if( self.entries['image_entry'].get() != '' ):
                        command = command + ' detector test \"' + self.entries["data_entry"].get() 
                        command = command + '\" \"' + self.entries["cfg_entry"].get() + '\" \"' + self.entries["weights_entry"].get() 
                        command = command + '\" -ext_output \"' + self.entries['image_entry'].get() + '\"'
                        if( self.entries['GPU_entry'].get() != '' ):
                            command = command + ' -i ' + self.entries['GPU_entry'].get()
                        os.system( command )
                        print( "run command ")
                    else:
                        print( "Falta la ruta de la imagen" )
                if( self.r.get() == "2" ):
                    if( self.entries['video_entry'].get() != '' ):
                        command = command + ' detector demo \"' + self.entries["data_entry"].get() 
                        command = command + '\" \"' + self.entries["cfg_entry"].get() + '\" \"' + self.entries["weights_entry"].get() 
                        command = command + '\" -ext_output \"' + self.entries['video_entry'].get() + '\"'
                        if( self.entries['GPU_entry'].get() != '' ):
                            command = command + ' -i ' + self.entries['GPU_entry'].get()
                        os.system( command )
                        print( "run command ")
                    else:
                        print( "Falta la ruta de la imagen" )
                if( self.r.get() == "3" ):
                    if( self.entries['camera_entry'].get() != '' ):
                        command = command + ' detector demo \"' + self.entries["data_entry"].get() 
                        command = command + '\" \"' + self.entries["cfg_entry"].get() + '\" \"' + self.entries["weights_entry"].get() 
                        command = command + '\" -c \"' + self.entries['camera_entry'].get() + '\"'
                        if( self.entries['GPU_entry'].get() != '' ):
                            command = command + ' -i ' + self.entries['GPU_entry'].get()
                        os.system( command )
                        print( "run command ")
                    else:
                        print( "Falta la ruta de la imagen" )
                if( self.r.get() == "4" ):
                    if( self.entries["user_entry"].get() != '' and self.entries["password_entry"].get() != '' and self.entries["ip_entry"].get() != '' ):
                        command = command + ' detector demo \"' + self.entries["data_entry"].get() 
                        command = command + '\" \"' + self.entries["cfg_entry"].get() + '\" \"' + self.entries["weights_entry"].get() 
                        command = command + '\" rtsp://' + self.entries['user_entry'].get() + ':' + self.entries['password_entry'].get() 
                        command = command + '@' + self.entries['ip_entry'].get() + ':554'
                        if( self.entries['GPU_entry'].get() != '' ):
                            command = command + ' -i ' + self.entries['GPU_entry'].get()
                        os.system( command )
                        print( "run command ")
                    else:
                        print( "Falta la ruta de la imagen" )
                        