import matplotlib.pyplot as plt
import os
import xml.etree.ElementTree as ET
import numpy as np
import tankxml
from tkinter import messagebox

script_directory = os.getcwd()
tank_averages_filepath = os.path.join(script_directory, "tank_averages.xml")

def show_graph():
    make_graph()
    plt.legend()
    plt.show()
    
def make_graph():
    global tanks
    try:
   
     with open (tank_averages_filepath, "rb"):
        tree = ET.parse(tank_averages_filepath)
        root = tree.getroot()
        
        tanks = tankxml.get_tank_data(root)
        
        
        
    except FileNotFoundError:
     print("ERROR: File doesnt exist!")
     messagebox.showerror("ERROR", message="XML File not found!")
     return
     
    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.set_title("Scores") # Set title

    ax.set_xlabel("Scores")
    ax.set_ylabel("Tanks")
    if tanks:
        
     for idx, tank in enumerate(tanks):
            print(idx)
            print(tank.name)
            y = np.linspace(idx, 8)
            x = np.linspace(0, 8)
            ax.plot(x, y, label=tank.name)



    


            





#x = np.linspace(0, 10) 0 is start, 10 is end
#y1 = np.linspace(1, 5)
#y2 = np.linspace(0, 2)

#ax.plot(x, y1, label="test1")

#ax.plot(x, y2, label="test2")


















