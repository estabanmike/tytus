import tablaDGA as TS

from variables import tabla as ts
from reportAST import *
from reportAST import *
import grammar2 as g
import pickle
from reportTable import *




pila = ''
Listaselects = []
correlativos = []
contador = -1
jsonObject = None

def execute(script: str):
    
    
    raiz = g.parse(script)
    
    for a in raiz:
        ts = a.ejecutar()[1]

    print(type(ts), ts)
    graphTable(ts)
    return ts
    


def execute1(script: str):
    global contador
    global pila
    contador = contador+1
    if script == '3D':
        cargar()
        raiz = g.parse(pila)
        Listaselects = cargar()
        for s in Listaselects:
            if isinstance(raiz, list):
                try:
                    raiz.insert(correlativos.pop(), s)
                except:
                    '''No hay selects'''
        executeGraphTree(raiz)
        for a in raiz:
            print(a)
            a.ejecutar()
    elif 'SELECT * FROM temp' in script:
        correlativos.append(contador)
    else:
        pila+= '\n' + script


def serialaizer():
    with open('data.pickle', 'wb') as f:
        pickle.dump(Listaselects, f, pickle.DEFAULT_PROTOCOL)

def insertarS(s):
    Listaselects.append(s)

def cargar():
    with open('data.pickle', 'rb') as f:
        return pickle.load(f)
    

def carga():
    with open('table.pickle', 'rb') as f:
        return pickle.load(f)

def guarda():
    with open('table.pickle', 'wb') as f:
        pickle.dump(ts, f, pickle.DEFAULT_PROTOCOL)