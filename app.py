import  streamlit as st
import pandas as pd
import numpy as np
import pickle
st.title('Smoke Detector')
st.write('This app predicts the probability of a smoke detector being activated based on the data' )
st.write('The data used for this app is from the smoke detector dataset')
model=pickle.load(open('fire_dedection.pkl','rb'))
col1, col2 = st.columns(2)
temp = col1.number_input('Enter the Temperature[C]',min_value=-40, max_value=100, value=0)
humidity = col2.number_input('Enter the Humidity[%]',min_value=0, max_value=100, value=0)
col3,col4=st.columns(2)
with col3:
       co2=st.number_input('Enter the eCO2[ppm]	',min_value=0, max_value=1000, value=0)
with col4:
    TVOC=st.number_input('Enter the TVOC[ppb]',min_value=0, max_value=10000, value=0)
col5,col6=st.columns(2)
with col5:
    Raw_H2=st.number_input('Enter the Raw H2',min_value=0, max_value=100000, value=0)
with col6:
    Raw_ethanol=st.number_input('Enter the Raw Ethanol',min_value=0, max_value=100000, value=0)
col7,col8=st.columns(2)
with col7:
    Pressure=st.number_input('Enter the Pressure[hPa]',min_value=0, max_value=10000, value=0)
with col8:
    Pm1=st.number_input('Enter the PM1.0',min_value=0, max_value=100000, value=0)
col9,col10,col11,col4=st.columns(4)
with col9:
    Pm25=st.number_input('Enter the PM2.5',min_value=0, max_value=100000, value=0)
with col10:
    NCo_0_5=st.number_input('Enter the NC0.5',min_value=0, max_value=100000, value=0)
with col11:
    NCo_1=st.number_input('Enter the NC1.0',min_value=0, max_value=100000, value=0)
with col4:
    NCo_2_5=st.number_input('Enter the NC2.5',min_value=0, max_value=100000, value=0)
if st.button('Predict'):

    input_df=pd.DataFrame({
              'Temperature[C]':[temp],
                'Humidity[%]':[humidity],
           'TVOC[ppb]':[TVOC],
              'eCO2[ppm]':[co2],
                'Raw H2':[Raw_H2],
                'Raw Ethanol':[Raw_ethanol],
                'Pressure[hPa]':[Pressure],
                'PM1.0':[Pm1],
                'PM2.5':[Pm25],
                'NC0.5':[NCo_0_5],
                'NC1.0':[NCo_1],
                'NC2.5':[NCo_2_5]})
    result=model.predict_proba(input_df)
    smoke=result[0][0]
    no_smoke=result[0][1]
    col12,col13=st.columns(2)
    with col12:
        st.write('The probability of smoke being detected is')
        st.subheader(str(smoke))
    with col13 :
        st.write('The probability of no smoke being detected is')
        st.subheader(str(no_smoke))
    if smoke>no_smoke:

        st.header('The smoke detector is activated')
    else:
        st.header('The smoke detector is not activated')






