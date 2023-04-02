import streamlit as st
import os
import pickle
import numpy as np

# Get the absolute path to the directory containing this script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Load the pipeline from the pickle file
with open(os.path.join(dir_path, 'D:/Study Material/Python/Projects/LAPTOP/pipe.pkl'), 'rb') as f:
    pipe = pickle.load(f)

# Load the dataframe from the pickle file
with open(os.path.join(dir_path, 'D:/Study Material/Python/Projects/LAPTOP/df.pkl'), 'rb') as f:
    df = pickle.load(f)

st.title("Laptop Predictor")

# brand
company = st.selectbox('Brand', df['Company'].unique())

# type of laptop
laptop_type = st.selectbox('Type', df['TypeName'].unique())

# Ram
ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',
                          ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

# cpu
cpu = st.selectbox('CPU', df['Cpu Brand'].unique())

# hdd
hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

# ssd
ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

# gpu
gpu = st.selectbox('GPU', df['Gpu Brand'].unique())

# os
os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    # query
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
    query = np.array([company, laptop_type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

    query = query.reshape(1, 12)
    predicted_price = np.exp(pipe.predict(query)[0])
    st.title("The predicted price of this configuration is $%.2f" % predicted_price)
