import json

def abrirJSON():
    dicFinal=[]
    with open("./Data.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Data.json",'w') as outFile:
        json.dump(dic,outFile)