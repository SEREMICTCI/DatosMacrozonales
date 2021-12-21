import numpy as np
import pandas as pd
import math_service as ms

# Path de inicio
print("Path de inicio")
pathIni = r"C:\Users\Asesor 2\Desktop\Workspace\Sources\Seremi\CienciaDatosSeremiMZN"
pathProyectos = pathIni + r"\input\proyectos\ProyectosCTCI.xlsx"
pathOutput = r"H:/Mi unidad/Datos/Compilados/"

# Lectura de proyectos nacionales
print('Lectura de proyectos nacionales')
data = pd.read_excel(pathProyectos)

# Filtro de datos por macrozona norte
print('Filtro de datos por macrozona norte')
dataMacrozona = data[
    (data.RegionEjecucion == 'Región de Arica y Parinacota')    |
    (data.RegionEjecucion == 'Región de Tarapacá')              |
    (data.RegionEjecucion == 'Región de Antofagasta')           |
    (data.RegionEjecucion == 'Región de Atacama')          
    ]

# Filtro de datos por proyectos desde el 2018
print('Filtro de datos por proyectos desde el 2018')
dataMacrozona = dataMacrozona[
    dataMacrozona.Año >= 2019         
    ]

# Llevando a mayusculas
print('******** Llevando a mayusculas ')
dataMacrozona['Institucion'] = dataMacrozona['Institucion'].str.upper()

# Quitando palabras
print('******** Quitando palabras ')
dataMacrozona['Institucion'] = dataMacrozona['Institucion'].str.replace('UNIVERSIDAD', '')
dataMacrozona['Institucion'] = dataMacrozona['Institucion'].str.replace('UNIV.', '')

# Quitando espacios de extremos
print('******** Quitando espacios de extremos ')
dataMacrozona['Institucion'] = dataMacrozona['Institucion'].str.strip()

# Se quita nulo
print('******** Se quitan nulos ')
dataMacrozona['Institucion'] = dataMacrozona['Institucion'].fillna('')

# Busqueda comparativa de nombres iguales
print('Busqueda comparativa de nombres iguales')
dataMacrozona = ms.changer(dataMacrozona,dataMacrozona,'Institucion',0.90)

# Ordenamiento
print('Ordenamiento')
dataMacrozona = dataMacrozona.sort_values(by=['Institucion','Agencia'])

# Escritura de excel
print('Escritura de excel')
dataMacrozona.to_excel(pathOutput + 'proyectosMacrozonaNorte.xlsx')

excelResult = pd.read_excel(pathOutput + 'proyectosMacrozonaNorte.xlsx')
print(excelResult.info())
print(excelResult.describe())