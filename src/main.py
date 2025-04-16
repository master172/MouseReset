import customtkinter
import mouseReset as mR

class App(customtkinter.CTk):
    def __init__(self):
        self.initalization_done:bool = False
        super().__init__()
        self.geometry("600x500")
        self.title("Mouse Reset")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # add widgets to app
        self.button = customtkinter.CTkButton(self,text="start save timer",corner_radius = 25, command=self.button_click)
        self.label = customtkinter.CTkLabel(self, text="", fg_color="transparent")
        self.label1 = customtkinter.CTkLabel(self, text="press ctrl+shift+k to save the mouse position", fg_color="transparent")
        self.label2 = customtkinter.CTkLabel(self, text="press ctrl+shift+r to return the mouse to the saved position", fg_color="transparent")
        self.button.grid(row=0, column=0, padx=0, pady=10)
        self.label.grid(row=1,column=0,padx=0, pady=10)
        self.label1.grid(row=2,column=0,padx=0, pady=10)
        self.label2.grid(row=3,column=0,padx=0, pady=10)
        #self.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
        self.grid_columnconfigure(0, weight=1)
        mR.start(self,self.messsage_protocols)
    # add methods to app
    def button_click(self):
        if self.initalization_done == False:   
            mR.start_loop(self)
            self.initalization_done = True
        elif self.initalization_done == True:
            print("reaching here")
            self.label.configure(text="")
            mR.restart_timer()
       
        #self.label.configure(text="Remaing Time: 00:01")
        
    def on_closing(self):
        mR.end_process()
        self.destroy()
        
    def get_timer_time(self,message:str):
       self.label.configure(text=message)
    
    def messsage_protocols(self,type:int = -1):
        if type == 0:
            self.position_saved()
        elif type == 1:
            self.position_returned()
            
    def position_saved(self):
        self.label.configure(text="position saved")
        
    def position_returned(self):
        self.label.configure(text="position returned")
        
app = App()
app.mainloop()