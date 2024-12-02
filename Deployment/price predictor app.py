import streamlit as st
import numpy as np
import pandas as pd
import pickle as pk


# Set page configuration
st.set_page_config(
    page_title='Property Price Predictor',
    page_icon='🏠',
    layout='centered',
)

# loading the dataframe
with open('database/modified_df.pkl','rb') as file:
    df=pk.load(file)
# loading the pipeline
with open('database/xgboost_pipeline.pkl','rb') as file:
    pipeline=pk.load(file)
#st.dataframe(df)
# create form for  taking inputs
st.subheader('Property Price Predictor')
with st.form('Enter your (Valid) property details'):
    #st.subheader('Property Price Predictor')
    st.subheader('Enter your (Valid) property details')
    # type
    type=st.selectbox('Enter your property type',df['type'].unique().tolist())
    #'''bedRoom bathroom
    #     luxury balcony '''
    sector=st.selectbox('Your prefeble sector',
        df['sector'].unique().tolist())
    built_up_area=st.number_input('Your estimated area',help='Enter your area in sq-ft')
    built_up_area=float(built_up_area)
    agePossession=st.selectbox('How old property are you looking',
        df['agePossession'].unique().tolist()
    )
    #2-->unfurnished,1-->furnished,0-->semifurnished
    furnishing_type=st.selectbox('Which type of furnishing you want',
        df['furnishing_type'].unique().tolist()
    )
    luxury=st.selectbox('Which type of luxury you want',df['luxury'].unique().tolist())
    # floor_type
    floor_type=st.selectbox('Your prefeble floor',
        df['floor_type'].unique().tolist()
    )
    balcony=st.selectbox('How many balcony you prefer',df['balcony'].unique().tolist())
    bedRoom=float(st.selectbox('BHK',sorted(df['bedRoom'].unique().tolist())))
    bathroom=float(st.selectbox('Bathroom',sorted(df['bathroom'].unique().tolist())))
    pooja_room=st.selectbox('Do you want pooja room',df['pooja room'].unique().tolist())

    # 1-->yes,0-->no
    servant_room=st.selectbox('Do you want servant room',df['servant room'].unique().tolist())

    if st.form_submit_button('Predict'):
        data=[[bedRoom, bathroom, balcony, floor_type, agePossession,
        sector, type, built_up_area, servant_room, pooja_room,
        furnishing_type, luxury]]
        column=['bedRoom', 'bathroom', 'balcony', 'floor_type', 'agePossession',
       'sector', 'type', 'built_up_area', 'servant room', 'pooja room',
       'furnishing_type', 'luxury']
        one_df=pd.DataFrame(data,columns=column)
        price=np.expm1(pipeline.predict(one_df))
        base_price=round(price[0],3)
        low_price=base_price
        # Display the prediction interval
        st.markdown(
            f'<div style="font-size: 18px; font-weight: bold; color: White;">The estimated price for your property is around {base_price:.2f} cr.</div>',
            unsafe_allow_html=True)
css="""
<style>
    [data-testid="stForm"] {
        background: Grey;
    }
</style>
"""
st.write(css, unsafe_allow_html=True)
