import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
import tankxml
import graph
import os
import inspect
import shutil


class MainGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tank Graph UTIL v.1.0.0")
        self.root.resizable(False, False)
        
        self.menubar = tk.Menu(self.root)
        self.root.geometry("800x500") # Window size
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0) # else a dash line at top
        self.filemenu.add_command(label="Upload Files", command=self.upload_action) # MAKE SURE TO ADD A COMMAND!! no brackets btw
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.root.config(menu=self.menubar)
        
        self.title = tk.Label(self.root, text="Tank Graph UTIL v.1.0.0", font=('Arial', 18)) # First pass the parent aka root, then a name Then optionally a font in a tuple, along with its font size
        self.title.pack(padx=20, pady=20) # Padding
        
        self.make_graph_button = tk.Button(self.root, text="Show Graph", font=('Arial', 18), command=self.show_graph)
        self.make_graph_button.pack()
        
        
        # data shit
        self.script_directory =  os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
        
        self.xml_data_path = os.path.join(self.script_directory,'xml_data')
        
        
        self.root.mainloop()
        
      
    def upload_action(self, event=None):
     
     
     xml_files = fd.askopenfilenames(parent=self.root, title='Choose files')
     if xml_files:
      if os.path.isdir(self.xml_data_path): # if it exists
         if messagebox.askyesno(title="Notice",message="Continuing will delete any existing files in the xml_data folder, do you wish to continue?"):
        #ask the user if they want to delete it
          for file in os.listdir(self.xml_data_path): # delete all the files lol ez bye bye
             os.remove(os.path.join(self.xml_data_path,file))
             
      else:
         os.mkdir(self.xml_data_path)
     for file in xml_files:
         shutil.copy(file, self.xml_data_path) # copys the file to the xml_data dir
         
         
    def check_valid_files(self):
        try:
         for file in os.listdir(self.xml_data_path):
            split_tup = os.path.splitext(file)
            if split_tup[1] == ".xml":
                return True
        except FileNotFoundError:
         return False
    
    def show_graph(self):
        if self.check_valid_files():
            print("yay")
            
            tankxml.set_xml_data(self.xml_data_path)
            tankxml.make_file()
            
            graph.show_graph()
            
            
            
        else:
            messagebox.showerror("ERROR!", message="No files in xml_data, Please upload your files first!")
            
            
        
     
    
        
        
if __name__ == '__main__':
    MainGUI()