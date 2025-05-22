import json

def abrirJSON():
    dicFinal=[]
    with open("./Datos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Datos.json",'w') as outFile:
        json.dump(dic,outFile)
        print