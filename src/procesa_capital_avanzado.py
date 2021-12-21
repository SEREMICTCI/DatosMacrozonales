import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math_service as ms

# Lectura de datos

print('******** Leyendo datos ')

#Ruta guardado
path = r"H:/Mi unidad/Datos/Compilados/"
pathIni = r"C:\Users\Asesor 2\Desktop\Workspace\Sources\Seremi\CienciaDatosSeremiMZN"

# 2021
path2021 = pathIni + r"\input\capitalHumano\Base-Personal-Academico-2021_SIES.xlsx"
data2021 = pd.read_excel(path2021,header=2)

# 2020
path2020 = pathIni + r"\input\capitalHumano\Base-Personal-Academico-2020_SIES.xlsx"
data2020 = pd.read_excel(path2020,header=2)

# 2019
path2019 = pathIni + r"\input\capitalHumano\Base-Personal-Academico-2019_SIES_.xlsx"
data2019 = pd.read_excel(path2019,header=2)

# 2018
path2018 = pathIni + r"\input\capitalHumano\BD_PAC_2018_SIES_2018_3-1.xlsx"
data2018 = pd.read_excel(path2018,header=2)

# 2017
path2017 = pathIni + r"\input\capitalHumano\bd_pac_2017_sies2017.xlsx"
data2017 = pd.read_excel(path2017,header=2)

# 2016
path2016 = pathIni + r"\input\capitalHumano\bd_pac_2016_sies2016_v2.xlsx"
data2016 = pd.read_excel(path2016,header=2)

print('******** Cambiando nombre de columna Institución ')

# Cambio de nombre de columnas
data2021 = data2021.rename(columns={'Unnamed: 1':'Institución'})
data2020 = data2020.rename(columns={'Unnamed: 1':'Institución'})
data2019 = data2019.rename(columns={'Unnamed: 1':'Institución'})
data2018 = data2018.rename(columns={'Unnamed: 1':'Institución'})
data2017 = data2017.rename(columns={'Unnamed: 1':'Institución'})
data2016 = data2016.rename(columns={'Unnamed: 1':'Institución'})

data2021 = data2021.rename(columns={'Unnamed: 2':'Mujeres'})
data2020 = data2020.rename(columns={'Unnamed: 2':'Mujeres'})
data2019 = data2019.rename(columns={'Unnamed: 2':'Mujeres'})
data2018 = data2018.rename(columns={'Unnamed: 2':'Mujeres'})
data2017 = data2017.rename(columns={'Unnamed: 2':'Mujeres'})
data2016 = data2016.rename(columns={'Unnamed: 2':'Mujeres'})

data2021 = data2021.rename(columns={'Unnamed: 3':'Hombres'})
data2020 = data2020.rename(columns={'Unnamed: 3':'Hombres'})
data2019 = data2019.rename(columns={'Unnamed: 3':'Hombres'})
data2018 = data2018.rename(columns={'Unnamed: 3':'Hombres'})
data2017 = data2017.rename(columns={'Unnamed: 3':'Hombres'})
data2016 = data2016.rename(columns={'Unnamed: 3':'Hombres'})

print('******** Quitando espacios de extremos ')

data2021['Institución'] = data2021['Institución'].str.strip()
data2020['Institución'] = data2020['Institución'].str.strip()
data2019['Institución'] = data2019['Institución'].str.strip()
data2018['Institución'] = data2018['Institución'].str.strip()
data2017['Institución'] = data2017['Institución'].str.strip()
data2016['Institución'] = data2016['Institución'].str.strip()

print('******** Llevando a mayusculas ')

data2021['Institución'] = data2021['Institución'].str.upper()
data2020['Institución'] = data2020['Institución'].str.upper()
data2019['Institución'] = data2019['Institución'].str.upper()
data2018['Institución'] = data2018['Institución'].str.upper()
data2017['Institución'] = data2017['Institución'].str.upper()
data2016['Institución'] = data2016['Institución'].str.upper()

print('******** Normalizando nombre de columnas ')

# 2021
data2021MacrozonaUes = data2021[
    (data2021['Región de Arica y Parinacota'] > 0) |
    (data2021['Región de Tarapacá']           > 0) |
    (data2021['Región de Antofagasta']        > 0) |
    (data2021['Región de Atacama']            > 0)
]

data2021MacrozonaUes = data2021MacrozonaUes.rename(columns={
    'Región de Arica y Parinacota':'Región 15',
    'Región de Tarapacá':'Región 1',
    'Región de Antofagasta':'Región 2',
    'Región de Atacama':'Región 3',
})

data2021MacrozonaUes = data2021MacrozonaUes.assign(año=2021)

# 2020
data2020MacrozonaUes = data2020[
    (data2020['Región 15']  > 0)  |
    (data2020['Región 1']   > 0)  |
    (data2020['Región 2']   > 0)  |
    (data2020['Región 3']   > 0) 
]
data2020MacrozonaUes = data2020MacrozonaUes.assign(año=2020)

# 2019
data2019MacrozonaUes = data2019[
    (data2019['Región 15'] > 0) |
    (data2019['Región 1'] > 0)  |
    (data2019['Región 2'] > 0)  |
    (data2019['Región 3'] > 0) 
]
data2019MacrozonaUes = data2019MacrozonaUes.assign(año=2019)

# 2018
data2018MacrozonaUes = data2018[
    (data2018['Región 15'] > 0) |
    (data2018['Región 1'] > 0)  |
    (data2018['Región 2'] > 0)  |
    (data2018['Región 3'] > 0) 
]
data2018MacrozonaUes = data2018MacrozonaUes.assign(año=2018)

# 2017
data2017MacrozonaUes = data2017[
    (data2017['Región 15'] > 0) |
    (data2017['Región 1'] > 0)  |
    (data2017['Región 2'] > 0)  |
    (data2017['Región 3'] > 0) 
]
data2017MacrozonaUes = data2017MacrozonaUes.assign(año=2017)

# 2016
data2016MacrozonaUes = data2016[
    (data2016['Región 15'] > 0) |
    (data2016['Región 1'] > 0)  |
    (data2016['Región 2'] > 0)  |
    (data2016['Región 3'] > 0)
]
data2016MacrozonaUes = data2016MacrozonaUes.assign(año=2016)

# Se buscan relaciones en nombres

print('******** Buscando relaciones de nombres de institución ')

dataMacrozonaUes = pd.concat([
    data2021MacrozonaUes,
    ms.changer(data2021MacrozonaUes,data2020MacrozonaUes,'Institución') ,
    ms.changer(data2021MacrozonaUes,data2019MacrozonaUes,'Institución') ,
    ms.changer(data2021MacrozonaUes,data2018MacrozonaUes,'Institución') ,
    ms.changer(data2021MacrozonaUes,data2017MacrozonaUes,'Institución') ,
    ms.changer(data2021MacrozonaUes,data2016MacrozonaUes,'Institución') ,
])

#resultMatcher =ms.matcher(dataMacrozonaUes['Institución'],dataMacrozonaUes['Institución'])
#resultMatcher.to_excel(path+'result_matcher.xlsx')

print('******** Seleccionando columnas ')

dataMacrozonaUes = dataMacrozonaUes [[
    'Institución',
    'Mujeres',
    'Hombres',
    'Menos de 35',
    'Entre 35 y 44',
    'Entre 45 y 54',
    'Entre 55 y 64',
    'Entre 65 y más',
    'Menos de 35.1',
    'Entre 35 y 44.1',
    'Entre 45 y 54.1',
    'Entre 55 y 64.1',
    'Entre 65 y más.1',
    'En 1 institución',
    'En 2 instituciones',
    'En 3 o más instituciones',
    'Doctor',
    'Magíster',
    'Especialidad médica u odontológica',
    'Titulo Profesional',
    'Licenciatura',
    'Técnico de Nivel Superior',
    'Técnico de Nivel Medio',
    'Licencia de Enseñanza Media',
    'Región 15',
    'Región 1',
    'Región 2',
    'Región 3',
    'año',
]]

print('******** Escribiendo archivos ')

dataMacrozonaUes.to_excel(path + "capital_avanzado.xlsx")