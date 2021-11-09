
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
        datos = pd.read_csv(archivo_cargado).dropna()

    except Exception as e:
        print(e)
        datos = pd.read_excel(archivo_cargado,keep_default_na=False).dropna()


global cols_num
try:
    st.write(datos)# tipos de datos del df, seleccion de columns
    cols_num = list(datos.select_dtypes(['float','int']).columns)
    cols_numNoNumericas = list(datos.select_dtypes(['object']).columns)

except Exception as e:
    print(e)
    st.write("Porfavor suba su archivo a la aplicaión")


# seleccion de graficoooo

sel_graf = st.sidebar.selectbox(label="Selecciona el tipo de gráfico",
                                options=["barras","histograma"])

try:
    if sel_graf == 'barras':
        st.sidebar.subheader("Ajustes")
        x_val = st.sidebar.selectbox(label="X",options=cols_num)
        x_val = st.sidebar.selectbox(label="X", options=cols_num)

        especificar_subdato = st.sidebar.checkbox(
            label="Especificar tipo de dato")

        if especificar_subdato:
            color_v = st.sidebar.selectbox(label="Color",
                                               options=cols_numNoNumericas)
            plot = px.bar(data_frame=datos, x=x_val,
                              y=y_val, color=color_v)

        else:
            plot = px.bar(data_frame=datos, x=x_val,
                              y=y_val)


except Exception as e:
    print(e)