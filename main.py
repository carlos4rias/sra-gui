import config
import tkinter as tk
from tkinter import filedialog


class Main( tk.Frame ):

    def __init__( self, parent, controller ):
        tk.Frame.__init__( self, parent )
        self.controller = controller

        frame = tk.LabelFrame(self, text = "Menu", padx = 10, pady = 10)


        # Training button
        training_btn = tk.Button( frame, text = "Entrenar", command = self.Run, state = tk.DISABLED )
        mark_btn = tk.Button( frame, text = "Marcar Imagenes", command = self.Run )
        run_btn = tk.Button( frame, text = "Ejecutar", command = self.Run )
        settings_btn = tk.Button( frame, text = "Configuracion", command = self.Run )

        if 'darknet' in config.paths:
            training_btn.state = tk.ACTIVE

        # Show widgets
        frame.grid( row = 0, column = 0, padx = 20, pady = 20)
        
        training_btn.grid( row = 0, column = 0, sticky="nsew")
        mark_btn.grid( row = 1, column = 0, sticky="nsew")
        run_btn.grid( row = 2, column = 0, sticky="nsew")
        settings_btn.grid( row = 3, column = 0, sticky="nsew")


    def Run(self):
        print("HOLA")