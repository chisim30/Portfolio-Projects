import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import streamlit as st 
import streamlit.components.v1 as components

from scipy import stats
from sklearn import preprocessing
from sklearn.linear_model import Ridge
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


# heading
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('car2.jpg')

# title
original_title = '<p style="font-family:sans; color:black; font-size: 80px; text-align:center">ehicle</p>'
st.markdown(original_title, unsafe_allow_html=True)




#Get the data
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names = headers)

# data cleaning
df.replace('?', np.nan, inplace=True)

mean_normalized = df['normalized-losses'].astype('float').mean(axis=0)
mean_horsepower = df['horsepower'].astype('float').mean(axis=0)
mean_stroke = df['stroke'].astype('float').mean(axis=0)
mean_bore = df['bore'].astype('float').mean(axis=0)
mean_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)

df['normalized-losses'].replace(np.nan, mean_normalized, inplace=True)
df['stroke'].replace(np.nan, mean_stroke, inplace=True)
df['bore'].replace(np.nan, mean_bore, inplace=True)
df['horsepower'].replace(np.nan, mean_horsepower, inplace=True)
df['peak-rpm'].replace(np.nan, mean_peakrpm, inplace=True)

df['num-of-doors'].replace(np.nan, 'four', inplace=True)

df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
df[['horsepower']] = df[['horsepower']].astype("float")

ranges = ['Low-end', 'Mid-end', 'High-end']
bin = np.linspace(min(df['price']), max(df['price']), 4)
df['range'] = pd.cut(df['price'], bin, labels=ranges, include_lowest = True)


X = df
y = df.pop('price')


model_body_style = preprocessing.LabelEncoder()
model_body_style.fit(['convertible', 'hatchback' ,'sedan' ,'wagon', 'hardtop'])
X['body-style'] = model_body_style.transform(X['body-style'])

model_drive_wheels = preprocessing.LabelEncoder()
model_drive_wheels.fit(['rwd', 'fwd', '4wd'])
X['drive-wheels'] = model_drive_wheels.transform(X['drive-wheels'])

model_engine_location = preprocessing.LabelEncoder()
model_engine_location.fit(['front', 'rear'])
X['engine-location'] = model_engine_location.transform(X['engine-location'])

model_fuel_type = preprocessing.LabelEncoder()
model_fuel_type.fit(['gas', 'diesel'])
X['fuel-type'] = model_fuel_type.transform(X['fuel-type'])

model_num_of_cylinders = preprocessing.LabelEncoder()
model_num_of_cylinders.fit(['four' ,'six', 'five' ,
                            'three', 'twelve', 'two' ,'eight'])
X['num-of-cylinders'] = model_num_of_cylinders.transform(X['num-of-cylinders'])

model_aspiration = preprocessing.LabelEncoder()
model_aspiration.fit(['std', 'turbo'])
X['aspiration'] = model_aspiration.transform(X['aspiration'])

model_engine_type = preprocessing.LabelEncoder()
model_engine_type.fit(['dohc','ohcv','ohc','l','rotor','ohcf'])
X['engine-type'] = model_engine_type.transform(X['engine-type'])

model_range = preprocessing.LabelEncoder()
model_range.fit(['Low-end', 'Mid-end', 'High-end'])
X['range'] = model_range.transform(X['range'])

model_fuel_system = preprocessing.LabelEncoder()
model_fuel_system.fit(['mpfi','2bbl', 'mfi', '1bbl', 'spfi', '4bbl',
                       'idi', 'spdi'])
X['fuel-system'] = model_fuel_system.transform(X['fuel-system'])

model_num_of_doors = preprocessing.LabelEncoder()
model_num_of_doors.fit(['two', 'four'])
X['num-of-doors'] = model_num_of_doors.transform(X['num-of-doors'])


X = X[['drive-wheels', 'wheel-base', 'length', 'width', 'curb-weight',
         'engine-size', 'fuel-system', 'bore', 
         'horsepower', 'city-mpg', 'highway-mpg', 'body-style', 'num-of-cylinders', 'fuel-type', 'aspiration', 'symboling']]

# renaming columns
X.rename(columns = {'drive-wheels':'drive_wheels', 'wheel-base':'wheel_base',
                              'curb-weight':'curb_weight', 'engine-size':'engine_size',
                    'fuel-system':'fuel_system', 'city-mpg':'city_mpg', 'highway-mpg':'highway_mpg',
                    'body-style':'body_style', 'num-of-cylinders':'num_of_cylinders', 'fuel-type':'fuel_type'}, inplace = True)



# Split the dataset into 70% Training set and 30% Testing set
X_train, X_test, y_train, y_test = train_test_split(X,y,
                                       test_size= 0.3, random_state = 400)




#Get the feature input from the user
def get_user_input():

    wheel_base = st.number_input('Wheel base:',step=1e-7, format="%.6f")
    length = st.number_input('Length:')
    width = st.number_input('Width:')
    curb_weight = st.number_input('Curb weight:')
    engine_size = st.number_input('Engine size:')
    bore = st.number_input('Bore:')
    horsepower = st.number_input('Horsepower:')
    city_mpg = st.number_input('City mpg:')
    highway_mpg = st.number_input('Highway mpg:')
    symboling = st.number_input('Symboling:')

    aspiration = st.selectbox('Aspiration:', ('std', 'turbo'))
    num_of_cylinders = st.selectbox('Number of cylinders:', 
                    ('two', 'three','four','five','six','eight','twelve'))
    fuel_type = st.selectbox('Fuel type:', ('gas', 'diesel'))
    fuel_system = st.selectbox('Fuel system:', 
            ('mpfi', '2bbl','idi','1bbl','spdi','4bbl','mfi','spfi'))
    body_style = st.selectbox('Body style:', 
                    ('sedan', 'hatchback','wagon','hardtop','convertible'))
    drive_wheels = st.selectbox('Drive wheels:', ('fwd', 'rwd', '4wd'))

    # aspiration
    if aspiration == 'std':
        aspiration = 0
    else:
        aspiration = 1

    # num of cylinders
    if num_of_cylinders == 'four':
        num_of_cylinders = 2
    elif num_of_cylinders == 'six':
        num_of_cylinders = 3
    elif num_of_cylinders == 'five':
        num_of_cylinders = 1
    elif num_of_cylinders == 'two':
        num_of_cylinders = 6
    elif num_of_cylinders == 'eight':
        num_of_cylinders = 0
    elif num_of_cylinders == 'three':
        num_of_cylinders = 4
    else:
        num_of_cylinders = 5

    # fuel type
    if fuel_type == 'gas':
        fuel_type = 1
    else:
        fuel_type = 0

    # fuel system
    if fuel_system == 'mpfi':
        fuel_system = 5
    elif fuel_system == '2bbl':
        fuel_system = 1
    elif fuel_system == 'idi':
        fuel_system = 3
    elif fuel_system == '1bbl':
        fuel_system = 0
    elif fuel_system == 'spdi':
        fuel_system = 6
    elif fuel_system == '4bbl':
        fuel_system = 2
    elif fuel_system == 'mfi':
        fuel_system = 4
    else:
        fuel_system = 7

    # body style
    if body_style == 'sedan':
        body_style = 3
    elif body_style == 'hatchback':
        body_style = 2
    elif body_style == 'wagon':
        body_style = 4
    elif body_style == 'hardtop':
        body_style = 1
    else:
        body_style = 0

    # drive wheels
    if drive_wheels == 'fwd':
        drive_wheels = 1
    elif drive_wheels == 'rwd':
        drive_wheels = 2
    else:
        drive_wheels = 0
    
    user_data = {'drive_wheels': drive_wheels,
                'wheel_base': wheel_base,
                'length': length,
                'width': width,
                'curb_weight': curb_weight,
                'engine_size': engine_size,
                'fuel_system': fuel_system,
                'bore': bore,
                'horsepower': horsepower,
                'city_mpg': city_mpg,
                'highway_mpg': highway_mpg,
                'body_style': body_style,
                'num_of_cylinders': num_of_cylinders,
                'fuel_type': fuel_type,
                'aspiration': aspiration,
                'symboling': symboling,
                 }
                 
    features = pd.DataFrame(user_data, index=[0])
    return features
user_input = get_user_input()

bt = st.button('Get Result')



if bt:
    RidgeModel = Ridge(alpha=1)
    RidgeModel.fit(X_train, y_train)
    Y_hat = RidgeModel.predict(user_input) 

    price = round(float(Y_hat), 2)

    st.write(f'The price of the car is ${str(price)}')




