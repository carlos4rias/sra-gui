import tkinter as tk
from tkinter import filedialog


class Main( tk.Frame ):

    def __init__( self, parent, controller ):
        tk.Frame.__init__( self, parent )
        self.controller = controller

        frame = tk.LabelFrame(self, text = "Menu", padx = 10, pady = 10)


        # Training button
        training_btn = tk.Button(
            frame,
            text = "Entrenar",
            command = lambda : self.Run('Train'),
            state = tk.DISABLED
        )

        # Mark button
        mark_btn = tk.Button(
            frame,
            text = "Marcar Imagenes",
            command = lambda : self.Run('YoloMark'),
            state = tk.DISABLED
        )

        # Run button
        run_btn = tk.Button(
            frame,
            text = "Ejecutar",
            command = lambda : self.Run('Run'),
            state = tk.DISABLED
        )

        # Setting button
        settings_btn = tk.Button(
            frame,
            text = "Configuracion",
            command = lambda : self.Run('Configuration'),
        )

        left_config_lbl = tk.Label(frame)

        paths = self.controller.config.paths
        
        show_message = not ('darknet' in paths)
        show_message = show_message or (not paths)

        if 'darknet' in paths:
            training_btn["state"] = tk.NORMAL
            run_btn["state"] = tk.NORMAL
        
        if 'yolomark' in paths:
            mark_btn["state"] = tk.NORMAL

        if show_message:
            left_config_lbl["text"] = "Aun no se han seteado algunas rutas, configuralas en la opcion configuracion"
            left_config_lbl.grid( row = 4, column = 0, sticky="nsew", pady = 15)

    
        # Show widgets
        frame.grid( row = 0, column = 0, padx = 20, pady = 20)
        
        training_btn.grid( row = 0, column = 0, sticky="nsew")
        mark_btn.grid( row = 1, column = 0, sticky="nsew")
        run_btn.grid( row = 2, column = 0, sticky="nsew")
        settings_btn.grid( row = 3, column = 0, sticky="nsew")

    def Run(self, window):
        self.controller.show_frame(window)
