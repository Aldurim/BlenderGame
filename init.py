import bge
import os
"""
for i in curScene.objects:              #geht jedes object der Scene durch in dem sich der Spieler gerade befindet
    if "ITEM" in i.name:                #wenn ein object mit dem namen ITEM gefunden wird dann:
        print(i['test'])                #printet die property test von sich selbst
        print(i.children[0]['test'])    #printet die property test des kindes
"""
path = bge.logic.expandPath("//")       #speichert den Pfad, wo das blenfile ausgeführt wird
curScene = bge.logic.getCurrentScene()  #speichert die momentane Scene in curScene

#initialisiere save-ordner um die spielstände zu speichern, sollte noch kein ordner mit dem namen saves vorhanden sein
if not os.path.isdir(path + "/saves"):
    os.system("mkdir " + path + "/saves")
path = path + "saves/"                 #ab jetzt gehen wir von saves aus



#initialisiert die save-dateien für die Items, Türen, NPC, etc.
#sollte noch kein file für diese Szene vorhanden sein, dann werden alle Objekte in die
#dazugehörigen files gespeichert
if not os.path.isdir(path + curScene.name):
    os.system("mkdir " + path + curScene.name)
    
#initialsiert die Items in der temp_item Datei
if not os.path.isfile(path + curScene.name + "/temp_items"):
    temp_item_file = open(path + curScene.name + "/temp_items", "w+")  #legt das file für die Items in der Szene an
    for i in curScene.objects:
        if "ITEM" in i.name:
            temp_item_file.write(i.name + ",1\n")
    temp_item_file.close()
    
#initialiesiere die türen
if not os.path.isfile(path + curScene.name + "/temp_doors"):
    temp_door_file = open(path + curScene.name + "/temp_doors", "w+")  #legt das file für die Items in der Szene an
    for i in curScene.objects:
        if "DOOR" in i.name:
            temp_door_file.write(i.name + ","+str(i["OPEN"])+","+str(i["LOCKED"])+"\n") #Name, Open, Locked
    temp_door_file.close()
            
#Hier wird alles aus den saves geladen wenn der Spieler den Spielstand lädt
if os.path.isfile(path + "LOAD"):
    file = open(path + "LOAD","r")
    load = file.readline()
    file.close()
    if "True" in load:
        file = open(path + "LOAD","w+")
        file.write("False")
        file.close()
        player = curScene.objects["Spieler"]
        file = open(path + "player","r")
        data = file.readlines()
        file.close()
        
        for i in range(len(data)):
            data[i] = data[i].replace("\n","")
        
        #Lade die Rotation und Position des Spielers
        playerRot = data[2].split(",")
        for i in range(len(playerRot)):
            playerRot[i] = float(playerRot[i])
        orientation = player.worldOrientation.to_euler()
        orientation.x = playerRot[0]
        orientation.y = playerRot[1]
        orientation.z = playerRot[2]
        player.worldOrientation = orientation
        
        playerPos = data[1].split(",")
        for i in range(len(playerPos)):
            playerPos[i] = float(playerPos[i])
        player.position = playerPos
        
        
        dirList = os.listdir(path + curScene.name + "/")
        for i in dirList:
            print(i)
            if not "temp" in i:
                savefile = open(path + curScene.name + "/" + i, "r")
                tempfile = open(path + curScene.name + "/temp_" + i, "w+")
                data = savefile.readlines()
                savefile.close()
                for j in data:
                    tempfile.write(j)
                tempfile.close()
        """
        #Lade Items, NPCS, Türen etc in die Temp Datei für die Szene
        #Lade Items in  die Szene indem das temp_items file initalisiert wird
        temp_item_file = open(path + curScene.name + "/temp_items", "w+")  #legt das file für die Items in der Szene an
        item_file = open(path + curScene.name + "/items", "r")
        data = item_file.readlines()
        item_file.close()
        for i in data:
            temp_item_file.write(i)
        temp_item_file.close()
        """

#Object Handler für Items        
if os.path.isfile(path + curScene.name + "/temp_items"):
    #Lädt den Spielstand und vergleicht Inhalt des saves mit den Objekten im Spiel
    #Sollte im save eine 0 für das Item stehen, wird das Item in der Szene dafür gelöscht
    file = open(path + curScene.name + "/temp_items", "r")
    data = file.readlines()
    file.close()
    for i in data:
        i = i.replace("\n","").split(",")
        for j in curScene.objects:
            if i[0] == j.name:
                if int(i[1]) < 1:
                    j.endObject()

#Object Handler für Türen        
if os.path.isfile(path + curScene.name + "/temp_doors"):
    #Lädt den Spielstand und vergleicht Inhalt des saves mit den Objekten im Spiel
    #Sollte im save eine 0 für das Item stehen, wird das Item in der Szene dafür gelöscht
    file = open(path + curScene.name + "/temp_doors", "r")
    data = file.readlines()
    file.close()
    for i in data:
        i = i.replace("\n","").split(",")
        for j in curScene.objects:
            if i[0] == j.name:
                if int(i[1]) == 1:
                    j["OPEN"] = 1
        


    

        
