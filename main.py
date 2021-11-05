
import streamlit as st
import plotly_express as px
import pandas as pd

#configuacion
st.set_option('deprecation.showfileUploaderEncoding',False)
#titulo de la app
st.title("PRUEBA")

# subencabezado
st.sidebar.subheader("AJUSTES")

# CARGA DE ARCHIVOS
archivo_cargado = st.sidebar.file_uploader(label="Sube aqui tus archivos CSV o Excel.",
                         type=['csv','xlsx'])

global datos
# si el archivo cargado no es ninguno
if archivo_cargado is not None:
    print(archivo_cargado)
    try:
        datos = pd.read_csv(archivo_cargado)
    except Exception as e:
        print(e)
        datos = pd.read_excel(archivo_cargado)

global cols_num
try:
    st.write(datos)# tipos de datos del df, seleccion de columns
    cols_num = list(datos.select_dtypes(['float','int']).columns)
    cols_numNoNumericas = list(datos.select_dtypes(['object']).columns)

except Exception as e:
    print(e)
    st.write("Porfavor suba su archivo a la aplicaión")



