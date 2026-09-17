# Python-Tank-App
Processes XML's  back into a terminal and forms a funny graph

# Technologies
* ```Python``` As programming language
* ```matplotLib``` For the graph
* ```shutil``` for file tools
* ```Tkinter``` for the UI

# Features
* a commandline showing all the stats of the tanks ```CLI```
* a small UI that has a button you can click to show the graph
* a script that processes each ```tank``` from an XML file, then it returns its ```name``` ```average score``` and ```average distance```

# How it works
Opening ```app.py``` will start the application and upon clicking "Show Graph" it will make the graph and the data in command line,
first the tankdata will be processed with ```tankxml.py``` using the XML file(s) in the ```xml_data``` folder (you can add your own)
After it will be saved in the root folder named ```tank_averages.xml```.
Then a graph will be made and be shown on screen using matplotLib which makes a cool image using the players tank number 


# Running (EXE)
1. Clone repository
2. Open ```dist```
3. Execute ```app.exe```

# Running (manual install)
1. Download Python 3.13
2. Download modules: ```Tkinter, matplotLib, shutil, Tkinter```
3. run app.py


