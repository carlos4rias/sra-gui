
import tkinter as tk
from tkinter import filedialog
import os
import time


class Train( tk.Frame ):

    DARKNET = 'darknet'

    def __init__( self, parent, controller ):
        tk.Frame.__init__( self, parent )
        self.controller = controller

        #############################################################################
        #                         Load config archive                               #
        #############################################################################

        frame_yolo_cfg = tk.LabelFrame(self, text = "Ruta archivo de configuracion YOLOV3", padx = 10, pady = 10)

        # variables to path
        self.path_darknet = ""
        self.number_objs = 0
        if self.DARKNET in self.controller.config.paths:
          self.path_darknet = self.controller.config.paths[self.DARKNET]
          os.chdir(self.path_darknet)

        # path config
        self.path_yolo_cfg = ""

        # Path for Darknet
        self.folder_darknet_btn = tk.Button(
            frame_yolo_cfg,
            text = "Ruta Config Yolo",
            command = self.DialogDarknet
        )
        self.folder_yolo_cfg = tk.Label( frame_yolo_cfg )

        self.descrip_yolo_cfg_name = tk.Label( frame_yolo_cfg, text = 'Nombre para el nuevo archivo de configuracion:' )
        self.new_yolo_cfg_name = tk.Entry( frame_yolo_cfg)
        self.new_yolo_cfg_name.insert(0, 'my_new_cfg.cfg')
        
         

        # Show widgets
        frame_yolo_cfg.grid( row = 0, column = 0, padx = 20, pady = 20, sticky = 'nsew')

        self.folder_yolo_cfg.grid( row = 3, column = 0, padx = 10 )
        self.folder_darknet_btn.grid( row = 3, column = 1, sticky = 'nsew', pady = 3 )
        self.descrip_yolo_cfg_name.grid(row = 4, column = 0, sticky = 'nsew')
        self.new_yolo_cfg_name.grid(row = 4, column = 1, sticky = 'nsew')
        

        ##############################################################################
        #                         Load objets name                                  #
        #############################################################################
        
        frame_obj_name = tk.LabelFrame(self, text = "Archivo que contiene nombre de los objetos", padx = 10, pady = 10)

        # path objs
        self.path_obj_name = ""

        # Path for Darknet
        self.folder_objs_btn = tk.Button(
            frame_obj_name,
            text = "Ruta Nombre Objs",
            command = self.DialogObjs
        )
        self.folder_obj_name = tk.Label( frame_obj_name )

        self.number_of_objs = tk.Label( frame_obj_name)
       

        frame_obj_name.grid( row = 6, column = 0, padx = 20, pady = 20, sticky = 'nsew')

        self.folder_obj_name.grid( row = 7, column = 0, padx = 10 )
        self.folder_objs_btn.grid( row = 7, column = 1, sticky = 'nsew', pady = 3 )
        self.number_of_objs.grid(row = 8, column = 0, sticky = 'nsew', columnspan = 2)

        #############################################################################
        #                  Load networkk weights for training                       #
        #############################################################################

        frame_weights = tk.LabelFrame(self, text = "Ruta archivo de pesos para el entrenamiento 'darknet53.conv.74' (si lo tiene)", padx = 10, pady = 10)

        # path config
        self.path_net_weights = ""

        # Path for Conv net weights
        self.folder_weights_btn = tk.Button(
            frame_weights,
            text = "Ruta de darknet53.conv.74",
            command = self.DialogWeights
        )
        self.folder_weights = tk.Label( frame_weights )

        frame_weights.grid( row = 11, column = 0, padx = 20, pady = 20, sticky = 'nsew')

        self.folder_weights.grid( row = 13, column = 0, padx = 10 )
        self.folder_weights_btn.grid( row = 13, column = 1, sticky = 'nsew', pady = 3 )
        

        #############################################################################
        #                           Load Train.txt                                  #
        #############################################################################

        frame_train = tk.LabelFrame(self, text = "Ruta del archivo train.txt", padx = 10, pady = 10)

        # path config
        self.path_train_file = ""

        # Path for Conv net weights
        self.archive_train_btn = tk.Button(
            frame_train,
            text = "Ruta del archivo train.txt",
            command = self.DialogTrain
        )
        self.archive_train = tk.Label( frame_train )
        
        # Back to main
        self.back_home_btn = tk.Button(
            self,
            text = "Volver",
            command = lambda : self.Run('Main')
        )

        # Show widgets
        
        frame_train.grid( row = 15, column = 0, padx = 20, pady = 20, sticky = 'nsew')
        self.archive_train.grid( row = 17, column = 0, padx = 10 )
        self.archive_train_btn.grid( row = 17, column = 1, sticky = 'nsew', pady = 3 )

        # Back to main
        self.back_home_btn = tk.Button(
            self,
            text = "Volver",
            command = lambda : self.Run('Main')
        )

        # Train
        self.train_btn = tk.Button(
            self,
            text = "Entrenar",
            command = self.Training
        )

        self.train_btn.grid( row = 18, column = 0, sticky = 'nsew', columnspan = 10 )
        self.back_home_btn.grid( row = 19, column = 0, sticky = 'nsew', columnspan = 10 )

    
    def Training(self):

        if not len(self.archive_train['text']):
            print("faltan datos por llenar")
            return
        
        if not len(self.folder_yolo_cfg['text']):
            print("faltan datos por llenar")
            return
        
        if not len(self.folder_obj_name['text']):
            print("faltan datos por llenar")
            return

        if not len(self.folder_weights['text']):
            self.DownloadWeights()
        
        
        current_dir = 'output_training' + str(int(time.time()))
        os.mkdir(current_dir)
        print(f"Creado el directorio {current_dir} donde sera guardado todo el material de entrenamiento")
        
        data_file = f"{self.path_darknet}/{current_dir}/obj.data" 

        with open(data_file, 'a') as config_data:
            config_data.write("classes = " + str(self.number_objs) + '\n')
            config_data.write("train = " + self.archive_train['text'] + '\n')
            config_data.write("valid = " + self.archive_train['text'] + '\n')
            config_data.write("names = " + self.folder_obj_name['text'] + '\n')
            config_data.write(f"backup = {current_dir}/backup" + '\n')

    def DialogDarknet( self ):
        self.path_yolo_cfg = filedialog.askopenfilename(initialdir=self.path_darknet)
        self.SetLabelText(self.folder_yolo_cfg, self.path_yolo_cfg)

    def DialogTrain( self ):
        self.path_train_file = filedialog.askopenfilename(initialdir=self.path_darknet)
        self.SetLabelText(self.archive_train, self.path_train_file)

    def DialogWeights( self ):
        self.path_net_weights = filedialog.askopenfilename(initialdir=self.path_darknet)
        self.SetLabelText(self.folder_weights, self.path_net_weights)

    def DownloadWeights( self ):
        os.system('wget https://pjreddie.com/media/files/darknet53.conv.74')
        self.folder_weights = self.path_darknet
        print('downloaded weights... ok!')

    def DialogObjs( self ):
        self.path_obj_name = filedialog.askopenfilename(initialdir=self.path_darknet)
        self.number_objs = 0
        with open(self.path_obj_name, 'r') as objs:
            self.number_objs = len(objs.readlines())
        
        self.SetLabelText(self.number_of_objs, "numero de objetos para entrenar: " + str(self.number_objs))
        self.SetLabelText(self.folder_obj_name, self.path_obj_name)

    def SetLabelText( self, label, text ):
        label["text"] = text

    def Run(self, window):
        self.controller.show_frame(window)
