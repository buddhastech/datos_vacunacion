import pandas as pd # se importa la libreria pandas
import matplotlib.pyplot as plt
import seaborn as sns

resumen_vacunacion = pd.read_csv('COVID-19 CCSS  Vacunación-resumen.csv') 
detalle_vacunacion = pd.read_csv('COVID-19 CCSS  Vacunación-detalle.csv') # se abre y almacenan los csv en una variable

data_frame_detalle = pd.DataFrame(detalle_vacunacion)
data_frame_resume = pd.DataFrame(resumen_vacunacion)

# 1- Ejercicio
# agrupación de datos por Provincia junto con la Cantidad, sumando la cantidad 
# y el reset_index permite resetear el los indices para que tome los encabezados que debe 
data_frame_agrupado_provincia = data_frame_detalle.groupby(['Provincia'])[['Cantidad']].sum().reset_index()
data_frame_agrupado_dosis = data_frame_detalle.groupby(['Nº dosis'])[['Cantidad']].sum().reset_index()
data_framte_agrupado_mes = data_frame_detalle.groupby(['Período'])[['Cantidad']].sum().reset_index()


# 2- Ejercicio 
data_frame_grupo_edad = data_frame_resume.groupby(['Grupo edad en vacunación'])[['Total']].sum().reset_index()
data_frame_grupo_sexo = data_frame_detalle.groupby(['Sexo']).sum().reset_index()


# 3- Ejercicio
data_frame_porcentaje_lab = data_frame_detalle.groupby(['Laboratorio']).sum().reset_index()


# 4 - Ejercicio
data_frame_agrupado_region = data_frame_resume.groupby(['Región'])[['Total']].sum().reset_index()
data_frame_agrupado_lab_dosis = data_frame_resume.groupby(['Región'])[['1º dosis', '2º dosis','Total']].sum().reset_index()

# 5 - Ejercicio
data_frame_establecimientos_vacunados = data_frame_resume.groupby(['Establecimiento de salud'])[['Total']].sum().reset_index()
data_frame_establecimientos_dosis = data_frame_resume.groupby(['Establecimiento de salud'])[['1º dosis','2º dosis','Total']].sum().reset_index()

def grafico_provincia_cantidad():

    plt.figure(figsize=(20, 9))
    plt.bar(
        data_frame_agrupado_provincia['Provincia'],
        data_frame_agrupado_provincia['Cantidad']
    )# crea el grafico de barras utilizando en su eje X las provincias y en el eje Y las cantidades
    plt.show() # mantiene mostrando el grafico

def grafico_dosis_cantidad():
    plt.bar(
        data_frame_agrupado_dosis['Nº dosis'],
        data_frame_agrupado_dosis['Cantidad']
    )
    plt.show() # mantiene mostrando el grafico

def grafico_mes_cantidad():
    
    plt.stem(
        data_framte_agrupado_mes['Período'],
        data_framte_agrupado_mes['Cantidad']
    )
    plt.show()

def tabla_grupo_edad():

    print(data_frame_grupo_edad.set_index('Grupo edad en vacunación'))

def tabla_grupo_sexo():
    
    print(data_frame_grupo_sexo.set_index('Sexo'))
 
def distribucion_porcentual():
    
    data_frame_porcentaje_lab['Cantidad'] = "100%"
    print(data_frame_porcentaje_lab.set_index('Laboratorio'))
 
def region_mayor_vacunados():
    
    total_vacunados = data_frame_agrupado_region['Total'].sum()
    media_vacunados = total_vacunados // 7
    indices_eliminar = []
    
    for indice in range(0, len(data_frame_agrupado_region)):
        
        if data_frame_agrupado_region.loc[indice, 'Total'] < media_vacunados:
            indices_eliminar.append(indice)
    
    
   # data_frame_agrupado_region.drop([*indices_eliminar], axis=0
    
    sns.lineplot(
        x=data_frame_agrupado_region.drop([*indices_eliminar], axis=0)['Region'], 
        y=data_frame_agrupado_region.drop([*indices_eliminar], axis=0)['Total'],
        data=data_frame_agrupado_region
    )
    plt.show()
    
def region_mayor_dosis():

    total_dosis = data_frame_agrupado_lab_dosis['Total'].sum()
    media_dosis = total_dosis // 7
    indices_eliminar = []
    
    for indice in range(0, len(data_frame_agrupado_lab_dosis)):
        # por cada registro en el data_frame_agrupado_lab_dosis

        
        if data_frame_agrupado_lab_dosis.loc[indice, 'Total'] < media_dosis:
        # si el total de cada uno es menor a la media de la totalidad
           indices_eliminar.append(indice)
           # agrega el indice a la lista de indices a eliminar
    

    print(data_frame_agrupado_lab_dosis.drop([*indices_eliminar], axis=0))
        
def region_menor_vacunados():
    plt.figure(figsize=(20, 11))
    total_vacunados = data_frame_agrupado_region['Total'].sum()
    media_vacunados = total_vacunados // 7
    indices_eliminar = []
    
    for indice in range(0, len(data_frame_agrupado_region)):
        
        if data_frame_agrupado_region.loc[indice, 'Total'] > media_vacunados:
            indices_eliminar.append(indice)
    
    sns.lineplot(
        x=data_frame_agrupado_region.drop([*indices_eliminar], axis=0)['Region'], 
        y=data_frame_agrupado_region.drop([*indices_eliminar], axis=0)['Total'],
        data=data_frame_agrupado_region
    )
    plt.show()

def region_menor_dosis():
    
    total_dosis = data_frame_agrupado_lab_dosis['Total'].sum()
    media_dosis = total_dosis // 7
    indices_eliminar = []
    
    for indice in range(0, len(data_frame_agrupado_lab_dosis)):
        # por cada registro en el data_frame_agrupado_lab_dosis

        
        if data_frame_agrupado_lab_dosis.loc[indice, 'Total'] > media_dosis:
        # si el total de cada uno es menor a la media de la totalidad
           indices_eliminar.append(indice)
           # agrega el indice a la lista de indices a eliminar
    

    print(data_frame_agrupado_lab_dosis.drop([*indices_eliminar], axis=0))
    
def diez_establecimientos_mayor_vacunacion():
    
    total_establecimientos = len(data_frame_establecimientos_vacunados['Establecimiento de salud'].index)
    total_vacunados = data_frame_establecimientos_vacunados['Total'].sum()
    media_vacunados = total_vacunados // total_establecimientos
    indices_eliminar = []
    
    for indice in range(0, len(data_frame_establecimientos_vacunados)):
        
        if data_frame_establecimientos_vacunados.loc[indice, 'Total'] < media_vacunados:
            indices_eliminar.append(indice)
    
    data_frame_mas_altos = data_frame_establecimientos_vacunados.drop([*indices_eliminar], axis=0) 
    # el drop muestra el dataframe sin los registros indicados por indices
    data_frame_diez_mas_altos = data_frame_mas_altos.sort_values('Total', ascending=False).head(10)

    # sort_values recibe como parametro la columna por la que queremos ordenar
    # le indicamos que sea de forma ascendente con el False
    # y mostramos con el head, los primeros 10
    
    sns.set_theme(style="whitegrid")
    
    ax = sns.barplot(
        x=data_frame_diez_mas_altos['Total'], 
        y=data_frame_diez_mas_altos['Establecimiento de salud'], 
        data=data_frame_diez_mas_altos
    )    
    plt.show()

def diez_establecimientos_mayor_dosis():

    total_vacunados = data_frame_establecimientos_dosis['Total'].sum()
    media_vacunados = total_vacunados // 2
    indices_eliminar = []

    for indice in range(0, len(data_frame_establecimientos_dosis)):
        
        if data_frame_establecimientos_dosis.loc[indice, 'Total'] > media_vacunados:
            indices_eliminar.append(indice)
    
    data_frame_mas_altos_dosis = data_frame_establecimientos_dosis.drop([*indices_eliminar], axis=0) 
  
    data_frame_diez_mas_altos_dosis = data_frame_mas_altos_dosis.sort_values('Total', ascending=False).head(10)
    
    print(data_frame_diez_mas_altos_dosis.set_index('Establecimiento de salud'))
    
def diez_establecimientos_menor_vacunacion():
    
    total_establecimientos = len(data_frame_establecimientos_vacunados['Establecimiento de salud'].index)
    total_vacunados = data_frame_establecimientos_vacunados['Total'].sum()
    media_vacunados = total_vacunados // total_establecimientos
    indices_eliminar = []
    
    for indice in range(0, len(data_frame_establecimientos_vacunados)):
        
        if data_frame_establecimientos_vacunados.loc[indice, 'Total'] > media_vacunados:
            indices_eliminar.append(indice)
    
    data_frame_mas_altos = data_frame_establecimientos_vacunados.drop([*indices_eliminar], axis=0) 
    # el drop muestra el dataframe sin los registros indicados por indices
    data_frame_diez_mas_altos = data_frame_mas_altos.sort_values('Total', ascending=True).head(10)

    # sort_values recibe como parametro la columna por la que queremos ordenar
    # le indicamos que sea de forma ascendente con el False
    # y mostramos con el head, los primeros 10
    
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(20, 9))
    ax = sns.barplot(
        x=data_frame_diez_mas_altos['Total'], 
        y=data_frame_diez_mas_altos['Establecimiento de salud'], 
        data=data_frame_diez_mas_altos
    )    
    plt.show()

def diez_establecimientos_menor_dosis():
    
    total_vacunados = data_frame_establecimientos_dosis['Total'].sum()
    media_vacunados = total_vacunados // 2
    indices_eliminar = []
    
    for indice in range(0, len(data_frame_establecimientos_dosis)):
        
        if data_frame_establecimientos_dosis.loc[indice, 'Total'] > media_vacunados:
            indices_eliminar.append(indice)
            
    data_frame_mas_bajos_dosis = data_frame_establecimientos_dosis.drop([*indices_eliminar], axis=0) 
    
    data_frame_diez_mas_bajos_dosis = data_frame_mas_bajos_dosis.sort_values('Total', ascending=True).head(10)
    
    print(data_frame_diez_mas_bajos_dosis.set_index('Establecimiento de salud'))
    