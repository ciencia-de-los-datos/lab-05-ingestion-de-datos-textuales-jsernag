import pandas as pd
import glob
import os

# A partir de esta informacion debe generar dos archivos llamados "train_dataset.csv" y 
# "test_dataset.csv". Estos archivos deben tener la siguiente estructura:

# * phrase: Texto de la frase. hay una frase por cada archivo de texto.
# * sentiment: Sentimiento de la frase. 
# Puede ser "positive", "negative" o "neutral". 
# Este corresponde al nombre del directorio donde se encuentra ubicado el archivo.

def train_dataset():
    carpeta_principal = "train"

    # Patrón para buscar todos los subdirectorios en el directorio principal
    patron_subcarpetas = os.path.join(carpeta_principal, "*")

    # Obtener una lista de todos los subdirectorios en el directorio principal
    subdirectorios = glob.glob(patron_subcarpetas)
    columnas =['phrase','sentiment']
    df = pd.DataFrame(columns=columnas)

    # Iterar sobre cada subdirectorio
    for subdirectorio in subdirectorios:
        # Patrón para buscar todos los archivos en el subdirectorio actual
        patron_archivos = os.path.join(subdirectorio, "*")
        # Obtener una lista de todos los archivos en el subdirectorio actual
        archivos = glob.glob(patron_archivos)
        # Iterar sobre los archivos en el subdirectorio actual
        for archivo in archivos:
            with open(archivo, 'r') as text:
                lines = text.read()
            # Hacer algo con el archivo, como imprimir su ruta
            nombre = archivo[6:-9]
            #data = (lines, nombre)
            df.loc[len(df)] = {"phrase":lines,"sentiment": nombre}


    df.to_csv("train_dataset.csv",index=False)
    # carpeta = "test"

    # for subcarpeta in glob.glob(carpeta + "/*.txt"):
    #     print(subcarpeta)


            

    # archivos_train = glob.glob("test"+"/*.txt")
    # columnas = ['phrase', 'sentiment']
    # df = pd.DataFrame(columns=columnas,
    # )
    # for archivo in archivos_train:
    #     data = pd.read_csv(archivo)
    #     df = pd.concat([df,data], ignore_index = True)
    df = df['sentiment'].value_counts()
    return df





def test_dataset():
    carpeta_principal = "test"

    # Patrón para buscar todos los subdirectorios en el directorio principal
    patron_subcarpetas = os.path.join(carpeta_principal, "*")

    # Obtener una lista de todos los subdirectorios en el directorio principal
    subdirectorios = glob.glob(patron_subcarpetas)
    columnas =['phrase','sentiment']
    df = pd.DataFrame(columns=columnas)

    # Iterar sobre cada subdirectorio
    for subdirectorio in subdirectorios:
        # Patrón para buscar todos los archivos en el subdirectorio actual
        patron_archivos = os.path.join(subdirectorio, "*")
        # Obtener una lista de todos los archivos en el subdirectorio actual
        archivos = glob.glob(patron_archivos)
        # Iterar sobre los archivos en el subdirectorio actual
        for archivo in archivos:
            with open(archivo, 'r') as text:
                lines = text.read()
            # Hacer algo con el archivo, como imprimir su ruta
            nombre = archivo[5:-9]
            #data = (lines, nombre)
            df.loc[len(df)] = {"phrase":lines,"sentiment": nombre}


    df.to_csv("test_dataset.csv",index=False)
    # carpeta = "test"

    # for subcarpeta in glob.glob(carpeta + "/*.txt"):
    #     print(subcarpeta)


            

    # archivos_train = glob.glob("test"+"/*.txt")
    # columnas = ['phrase', 'sentiment']
    # df = pd.DataFrame(columns=columnas,
    # )
    # for archivo in archivos_train:
    #     data = pd.read_csv(archivo)
    #     df = pd.concat([df,data], ignore_index = True)
    df = df['sentiment'].value_counts()
    return df



print(train_dataset())
print(test_dataset())
