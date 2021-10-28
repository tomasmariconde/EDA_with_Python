#Analisis exploratorio (EDA) de protestas de campesinos sudamericanos con Python

#PASO 1 - Carga de libreri­as
#Importamos las librerias que utilizaremos para generar nuestro analisis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#PASO 2 - Carga de datos
#Cargamos nuestra base de datos a un DataFrame de pandas al que renombramos "df" mediante la creacion de una nueva variable
pd.read_csv("/Users/elCONDEMARI/Desktop/Python/mmALL_073119_csv.csv")
df=pd.read_csv("/Users/elCONDEMARI/Desktop/Python/mmALL_073119_csv.csv")
print(df)

#Vemos la cantidad de filas y columnas
df.shape

#Vemos los tipos de variable y otra info
df.info()

#PASO 3 - Limpieza general de datos
#Filtramos las columnas del DataFrame para quedarnos con las siguientes solamente:
    #country (name)
    #year (year of protest)
    #region (country region)
    #protest (was there a protest in the relevant period?)
    #protestnumber (protest number in year)
    #startday
    #startmonth
    #startyear
    #endday
    #endmonth
    #endyear
    #protesterviolence (did protesters engage in violence against the state?)
    #location 
    #participants (number of participants)
    #staterespone1
    #staterespone2
    #staterespone3
    #staterespone4
    #staterespone5
    #staterespone6
    #staterespone7
df=df.loc[:,["country", "year", "region", "protest", "protestnumber", "startday", "startmonth", "startyear", "endday", "endmonth", "endyear", "protesterviolence", "location", "participants", "stateresponse1", "stateresponse2", "stateresponse3", "stateresponse4", "stateresponse5", "stateresponse6", "stateresponse7"]]    
print(df)

#Filtramos las columnas "region" y "year" para quedarnos con la region sudamericana y datos a partir del año 2009 (hasta el 2014)
df=df[df["region"]=="South America"]
df=df[df["year"]>=2009]
print(df)

#Eliminamos las columnas "stateresponse2", "stateresponse3", "stateresponse4", "stateresponse5", "stateresponse6" y "stateresponse7" debido a que solo nos interesa conocer las primeras reacciones de los estados ante los conflictos
df.drop("stateresponse2", axis=1, inplace=True)
df.drop("stateresponse3", axis=1, inplace=True)
df.drop("stateresponse4", axis=1, inplace=True)
df.drop("stateresponse5", axis=1, inplace=True)
df.drop("stateresponse6", axis=1, inplace=True)
df.drop("stateresponse7", axis=1, inplace=True)
print(df)

#Reestructuramos el DataFrame de modo que los valores contenidos en las columnas "startday", "startmonth" y "startyear" se agrupen bajo un nueva y unica columna llamada "startdate"
#En primer lugar, eliminamos los valores nulos de la columna "startyear"
df=df.dropna(subset=["startyear"])
print(df)
#En segundo lugar, convertimos el total de las columnas en int para quitar los decimales previo a agruparlas
df["startday"]=df.startday.apply(int)
df["startmonth"]=df.startmonth.apply(int)
df["startyear"]=df.startyear.apply(int)
print(df)
#Por ultimo, agrupamos las tres columnas bajo una nueva llamada "startdate" utilizando la funcion to_datetime
df["startdate"]=pd.to_datetime(df["startday"].apply(str) + "/" + df["startmonth"].apply(str) + "/" + df["startyear"].apply(str), format="%d/%m/%Y", infer_datetime_format=True, errors="coerce")
print(df)

#Reestructuramos el DataFrame de modo que los valores contenidos en las columnas "endday", "endmonth" y "endyear" se agrupen bajo un nueva y unica columna llamada "enddate"
#En primer lugar, convertimos el total de las columnas en int para quitar los decimales previo a agruparlas. No es necesario eliminar los valores nulos como hicimos anteriormenete ya que por esa accion quedaron eliminados en este caso también 
df["endday"]=df.endday.apply(int)
df["endmonth"]=df.endmonth.apply(int)
df["endyear"]=df.endyear.apply(int)
print(df)
#Luego agrupamos las tres columnas bajo una nueva llamada "enddate" utilizando la funcion to_datetime
df["enddate"]=pd.to_datetime(df["endday"].apply(str) + "/" + df["endmonth"].apply(str) + "/" + df["endyear"].apply(str), format="%d/%m/%Y", infer_datetime_format=True, errors="coerce")
print(df)

#Reiniciamos el indice a fin de poder trabajar en el siguiente paso con mayor comodidad
df.reset_index(level=0, inplace=True)
print(df)

#Eliminamos el indice anterior que se convirtio en columna y por tanto no nos sirve
df.drop("index", axis=1, inplace=True)
print(df)

#PASO 4 - Preparacion de datos para su graficación
#Duración de las protestas (¿Fueron mas largas que la Argentina?)
#Calculamos la duración exacta de las protestas y creamos una nueva columna llamada "daysofconflict"
df["daysofconflict"]=df["enddate"]-df["startdate"]
print(df)

#Convertimos los días de la columna "daysofconflict" en int
df["daysofconflict"]=df["daysofconflict"].astype(str)
df["daysofconflict"]=df["daysofconflict"].str.strip("days").astype(int)

#Extension territorial de las protestas (¿Se extendieron mayoritariamente a nivel nacional?)
#Reenombramos todos aquellos valores similares a "National level" para que queden todos bajo ese mismo nombre
df["location"]=df["location"].replace({"national":"National level", "National":"National level", "national level":"National level", "nation wide":"National level", "Nation wide":"National level", "nationwide":"National level"})
print(df)

#Reemplazamos todas las localidades que no sean "National level" por "Local level" ya que solo nos interesa saber si fueron a nivel nacional o a nivel local, mas no las especificidades de estas ultimas
location_changes=df["location"]!="National level"
df.loc[location_changes, "location"]="Local level"
print(df)

#Virulencia de las protestas (¿Participaron los manifestantes de actos de violencia contra el Estado?)
#Reemplazamos los valores 0 y 1 por las respuesta "No" y "Si" respectivamente (asumiendo que esos valores corresponden a esas respuestas en base al manual de usuario compartido, en particular la variable "protest" de similar construccion)
df["protesterviolence"]=df["protesterviolence"].replace({1:"Si"})
protesterviolence_changes=df["protesterviolence"]!= "Si"
df.loc[protesterviolence_changes, "protesterviolence"]= "No"
print(protesterviolence_changes)

#PASO 5 - Analisis de datos
#Duración de las protestas (¿Fueron las protestas mas largas que la argentina del 2008?)
#Obtenemos información general como ser el promedio
print(df.daysofconflict.describe())
print("El promedio de duracion de las protestas es de:", df.daysofconflict.mean())
print("La mediana de duracion de las protestas es:", df.daysofconflict.median())
print("El valor minimo de duracion de las protestas es", df.daysofconflict.min())
print("El valor maximo de duracion de las protestas es", df.daysofconflict.max())

#Graficamos la distribucion de los valores
fig, ay = plt.subplots()
ay.boxplot(df.daysofconflict) 
plt.show()

#Duplicamos la columna "daysofconflict" en una nueva que creamos llamada "daysofconflict_duplicated". En ella intercambiamos los elementos originales por nuevas categorias que los agrupan, que nos permiten graficar un "pie" mas legible. 
dayofconflict_conditions=[
    (df["daysofconflict"]<1),
    (df["daysofconflict"]>=1) & (df["daysofconflict"]<=5),
    (df["daysofconflict"]>5) & (df["daysofconflict"]<=10),
    (df["daysofconflict"]>=11)
    ]
daysofconflict_values=["Menos de 24 hs", "Entre 1 y 5 dias", "Entre 6 y 10 dias", "Mas de 10 dias"]
df["daysofconflict_duplicated"]=np.select(dayofconflict_conditions, daysofconflict_values)
colors=["#EE6055","#60D394","#AAF683","#FFD97D"]
desfase= (0.1, 0, 0, 0)
daysofconlict_duplicated_plot=df["daysofconflict_duplicated"].value_counts().plot(kind="pie",colors=colors, explode=desfase, autopct="%1.1f%%", fontsize=12, figsize=(6,6), title="Duracion de las protestas")
plt.show()

#Extension territorial de las protestas (¿Se extendieron las protestas mayoritariamente a nivel nacional?)
location_plot=df["location"].value_counts().plot(kind="barh", color="cadetblue", fontsize=12, figsize=(6,6), title="Distribucion territorial de las protestas")
plt.show()

#Virulencia de las protestas (¿Participaron los manifestantes de actos de violencia contra el Estado?)
colors2=["#6B8ba4","#9dbcd4"]
desfase2 = (0.1, 0)
protesterviolence_plot=df["protesterviolence"].value_counts().plot(kind="pie",colors=colors2, explode=desfase2, fontsize=12, autopct="%1.1f%%", figsize=(6,6), title="¿Participaron los manifestantes de actos de violencia contra el Estado?")
plt.show()

#Respuesta frente a las protestas (¿Cuál fue la primera respuesta más extendida por parte de los Estados frente al conflicto?)
stateresponse1_plot=df["stateresponse1"].value_counts().plot(kind="bar", color="palegreen", fontsize=12, figsize=(6,6), title="¿Cuál fue la primera respuesta más extendida por parte de los Estados frente al conflicto?")
plt.xticks(rotation=75)
plt.show()

