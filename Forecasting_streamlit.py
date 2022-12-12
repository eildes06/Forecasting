import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image



model = pickle.load(open("Forcasting.pkl", "wb")
#dtf = pd.read_excel('Veri-Seti.xlsx', index_col='Date',parse_dates=True)
                
#image = Image.open('car.jpg')
html_temp = """
<div style="background-color:Blue;padding:10px">
<h2 style="color:white;text-align:center;">Employee Churn Prediction - GROUP-9 </h2>
</div><br>"""
st.set_page_config(page_title='Car Price Prediction', page_icon='👩‍💻')
st.image(image)
st.markdown('***')
st.markdown('# <center><span style="color:#286608">Car Price Prediction</span></center>',unsafe_allow_html=True )
st.markdown("#### <center>Use the sidebar to enter your cost's specifications.</center>",unsafe_allow_html=True)
st.markdown('***')
					    

OTV Orani = st.sidebar.slider(label="OTV Orani", min_value=0.0, max_value=1.0, step=0.01)
Faiz = st.sidebar.slider(label="Faiz", min_value=0.0, max_value=1.0, step=0.01)
EUR/TL = st.sidebar.slider(label="EUR/TL", min_value=0, max_value=10, step=1)
Kredi Stok = st.sidebar.slider(label="Kredi Stok", min_value=0, max_value=350, step=10)


churn = pd.DataFrame({"OTV Orani" : [OTV Orani],
                    "Faiz" : [Faiz],
                    "EUR/TL" : [EUR/TL],
                    "Kredi Stok" : [Kredi Stok]
               
                    })

hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """        
st.markdown(hide_table_row_index, unsafe_allow_html=True)   

showdf = churn.rename(columns={'OTV Orani': 'OTV Orani',
                             'Faiz': 'Faiz',
                             'EUR/TL': 'EUR/TL',
                             'Kredi Stok': 'Kredi Stok'
                          })
st.markdown("#### <center>Cost Information</center>",unsafe_allow_html=True)
st.table(showdf)

prediction = model.predict(churn)


st.subheader('Click PREDICT if configuration is OK')

if st.button('PREDICT'):
	
		st.success(prediction.mean())
		st.success(f'Cost will BE :)')
	


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
