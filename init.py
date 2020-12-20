import bge
import os
"""
for i in curScene.objects:              #geht jedes object der Scene durch in dem sich der Spieler gerade befindet
    if "ITEM" in i.name:                #wenn ein object mit dem namen ITEM gefunden wird dann:
        print(i['test'])                #printet die property test von sich selbst
        print(i.children[0]['test'])    #printet die property test des kindes
"""
path = bge.logic.expandPath("//")       #speichert den Pfad, wo das blenfile ausgeführt wird

#initialisiere save-ordner um die spielstände zu speichern, sollte noch kein ordner mit dem namen saves vorhanden sein
if not os.path.isdir(path + "/saves"):
    os.system("mkdir " + path + "/saves")
path = path + "/saves/"                 #ab jetzt gehen wir von saves aus

curScene = bge.logic.getCurrentScene()  #speichert die momentane Scene in curScene

if not os.path.isdir(path + curScene.name):
    os.system("mkdir " + path + curScene.name)
    file = open(path + curScene.name + "/items", "w+")
    for i in curScene.objects:
        if "ITEM" in i.name:
            file.write(i.name + ",1\n")
    file.close()
else:
    file = open(path + curScene.name + "/items", "r")
    data = file.readlines()
    file.close()
    for i in data:
        i = i.replace("\n","").split(",")
        for j in curScene.objects:
            if i[0] == j.name:
                if int(i[1]) < 1:
                    j.endObject() 
