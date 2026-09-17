import xml.etree.ElementTree as ET
import os
import inspect

class Tank:
    def __init__(self, name, alive, damage_dealt, hp_lost, ratio, kills, distance_traveled, total_score):
        self.name = name
        self.alive = alive
        self.damage_dealt = damage_dealt
        self.hp_lost = hp_lost
        self.ratio = ratio
        self.kills = kills
        self.distance_traveled = distance_traveled
        self.total_score = total_score
        self.games_played = 0
        self.final_score = 0

class Tank_averages(Tank):
    def __init__(self, name):
        self.name = name
        self.final_score = 0
        self.final_distance = 0
        self.final_damage = 0
        self.final_hp_lost = 0
        self.final_ratio = 0
        self.average_damage = 0
        self.average_hp_lost = 0
        self.average_ratio = 0
        self.average_score = 0
        self.average_distance = 0
        self.games_played = 0
        
        
    def get_average(self):
        score_average =  round(self.final_score / self.games_played, 1)
        self.average_score = score_average
        distance_average = round(self.final_distance / self.games_played, 1)
        self.average_distance = distance_average
        damage_average = round(self.final_damage / self.games_played, 1)
        self.average_damage = damage_average
        hp_lost_average = round(self.final_hp_lost / self.games_played, 1)
        self.average_hp_lost = hp_lost_average
        ratio_average = round(self.final_ratio / self.games_played, 1)
        self.average_ratio = ratio_average


        
class Game: # Contains the game number and the info for the tanks
    def __init__(self, tanks, index):
        self.index = index
        self.tanks = tanks
        self.highest_score = 0
        self.best_ratio = 0
        self.most_distance = 0
        self.tank_best_score = ''
        self.tank_best_ratio = ''
        self.tank_best_distance = ''
        
    
    
    
def get_tank_data(xml): # and add tank
    tanks = []
    
    
    name = ''
    health = 0
    alive = False
    damage_dealt = 0
    hp_lost = 0
    ratio = 0
    kills = 0
    distance_traveled = 0
    total_score = 0
    for child in xml:
        if child.tag == "Tanks":
            for tank in child:
                for tank_att in tank:
                    value = tank_att.text
                    key = tank_att.tag
                    match key:
                        case "Name":
                            name = value
                        case "Health":
                            health = int(value)
                        case "Alive":
                            alive = value
                        case "DamageDealt":
                            damage_dealt = int(value)
                        case "HPLost":
                            hp_lost = int(value)
                        case "Ratio":
                            ratio = float(value)
                        case "Kills":
                            kills = int(value)
                        case "DistanceTraveled":
                            distance_traveled = int(value)
                        case "TotalScore":
                            total_score = int(value)
                player_tank = Tank(name, alive,damage_dealt,hp_lost,ratio, kills, distance_traveled, total_score)
                tanks.append(player_tank)
    return tanks
                
                
                            
    
game_data = []       # all the games that got played       


def set_xml_data(path):
    global xml_data
    xml_data = path
    
def make_file(): 
 global xml_data
 if xml_data:
  for idx, file in enumerate(os.listdir(xml_data)): # XML file directory, #enumerate for index
   
   split_tup = os.path.splitext(file) # Splits into a tuple of two items, the file name and the extension
   if split_tup[1] == ".xml": # [1] is the extension, if its an xml it will continue
     dir = os.path.join(xml_data,file)
     try:
    
      tree = ET.parse(dir)
      root = tree.getroot()
      tanks = get_tank_data(root)
      game = Game(tanks, idx)
      game_data.append(game)
      
      
     except:
    
      print("Invalid XML File!")
 make_scores()
 make_tank_scores()

 GenerateXML("tank_averages.xml")
        
        
# Shows the best stats of each game
def make_scores():
 for game in game_data:
    scores = [] # calculate highest scores of game
    ratios = []
    distances = []
    for tank in game.tanks:
        tank_score = tank.total_score
        scores.append(tank_score)
        tank_ratio = tank.ratio
        ratios.append(tank_ratio)
        tank_distance_traveled = tank.distance_traveled
        distances.append(tank_distance_traveled)
        
        
    highest_score = max(scores)
    for tank in game.tanks:
        if tank.total_score == highest_score:
            game.tank_best_score = tank.name
    game.highest_score = highest_score

    best_ratio = max(ratios)
    for tank in game.tanks:
        if tank.ratio == best_ratio:
            game.tank_best_ratio = tank.name
    game.best_ratio = best_ratio
    most_distance = max(distances)
    for tank in game.tanks:
        if tank.distance_traveled == most_distance:
            game.tank_best_distance = tank.name
    game.most_distance = most_distance
    
    print(f"Game: {game.index}: Highest Score: {game.highest_score} Player: {game.tank_best_score}, Best Ratio: {game.best_ratio} Player: {game.tank_best_ratio}, Most Distance: {most_distance} Player: {game.tank_best_distance}")
    
    
final_tanks = []
tank_names = []
all_tank_data = []

def check_if_same_tank(tank):
     for final_tank in final_tanks:
            if final_tank.name == tank.name:
                final_tank.final_score += tank.total_score
                final_tank.final_distance += tank.distance_traveled
                final_tank.games_played += 1
                final_tank.final_damage += tank.damage_dealt
                final_tank.final_hp_lost += tank.hp_lost
                final_tank.final_ratio += tank.ratio
                
    
# gets all the names
def make_tank_scores():
 for game in game_data:
    tanks = game.tanks
    for tank in tanks:
     if tank.name in tank_names:
        continue
     else:
         
         tank_names.append(tank.name)
     all_tank_data.append(tank)
     
# makes new tanks
 for tank_name in tank_names:
    final_tank = Tank_averages(tank_name)
    final_tanks.append(final_tank)
    
 for game in game_data:
    tanks = game.tanks
    for tank in tanks:
        if tank.name in tank_names:
            check_if_same_tank(tank)
            
    
 for tank in final_tanks:
    tank.get_average()
    print(f"Name: {tank.name}, Average_Score: {tank.average_score}, Average_Distance: {tank.average_distance}")
    


def GenerateXML(fileName) :
    
    root = ET.Element("TankBattleAverages")
    script_directory = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
    filepath =  os.path.join(script_directory,fileName)
    tanks = ET.SubElement(root, "Tanks")
    games = ET.SubElement(root, "Games")
    if os.path.isfile(filepath): # if it exists
        # will return if the file already exists so the xml file wont add
        
        return

    for tank in final_tanks:

       
        tank_element = ET.SubElement(tanks, "Tank")
        name = tank.name
        name = name.replace(' ', '_') # no spaces no nonononono NO YOU CANT REDEEM IT!! NOO NOO!!! 

        name_element = ET.SubElement(tank_element, "Name")
        name_element.text = name

        average_score_element = ET.SubElement(tank_element, "Average_Score")
        average_score_element.text = str(tank.average_score)

        average_distance_element = ET.SubElement(tank_element, "Average_Distance")
        average_distance_element.text = str(tank.average_distance)

        average_damage_element = ET.SubElement(tank_element, "Average_Damage")
        average_damage_element.text = str(tank.average_damage)

        average_hp_lost_element = ET.SubElement(tank_element, "Average_HP_Lost")
        average_hp_lost_element.text = str(tank.average_hp_lost)

        average_ratio_element = ET.SubElement(tank_element, "Average_Ratio")
        average_ratio_element.text = str(tank.average_ratio)

    for idx, game in enumerate(game_data):
        game_element = ET.SubElement(games, "Game_" + str(idx))

        best_score_element =  ET.SubElement(game_element, "Best_Score" , score= str(game.highest_score), player= game.tank_best_score)

        best_ratio_element =  ET.SubElement(game_element, "Best_Ratio" , score= str(game.best_ratio), player= game.tank_best_ratio)

        most_distance_element =  ET.SubElement(game_element, "Most_Distance" , score= str(game.most_distance), player= game.tank_best_distance)
        


    

    
    
    tree = ET.ElementTree(root)
    
    print(filepath)
    

    with open (filepath, "wb") as files :
        tree.write(files)







    
    
    


   
    
    

   

    
    

            
            

        
        
        
        

    
        

    

    

    

    
    
        
        
   



    
    
        
    
      
      
      
      
  