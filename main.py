import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import time
import altair as alt
from sql_backend import *
import plotly.graph_objs as go


# tab icone

# Set page config
# st.beta_set_page_config(page_title="Phonepe Pluse Analysis Dashboard", page_icon="tab_icone.png")
st.set_page_config(
    page_title="Phonepe Dashboard",
    page_icon="tab_icone.png",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

st.image('download.jpeg'  ,use_column_width="auto")
st.header('', divider='rainbow')


with st.sidebar:
    st.title("welcome back siranjeevi")
    st.header("", divider='rainbow')   
    st.write("This code will be printed to the sidebar.")

   

#data declare globaly 

transaction_data = retrieve_transaction_data()  

st.header("phonepe Pulse data Table")


Type = st.selectbox('Select a color map',
                                    ['State', 'Year', 'Transaction_Type', 'Quarter'], 
                                    index=0)

col1, col2,col3 = st.columns([3.7,3,4.5])

with col1:
    table =  transaction_data.groupby(Type)[['Transaction_Count', 'Transaction_Amount']].sum()  #.reset_index()
    st.write(table)

    max_val = transaction_data
    
    # map
    
    Year = st.selectbox('Select a year',
                                        ['2018','2019','2020','2021','2022','2023'], 
                                        index=0)
    type_num = st.selectbox('Select a year',
                                        ['Transaction_Count','Transaction_Amount'], 
                                        index=0)
    map_data = map_year()

    result2 = map_data.query(f"Year=={Year}").groupby('State')[type_num].sum().reset_index()
    fig = px.choropleth(
        result2,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color=type_num,
        color_continuous_scale='thermal',
        width=850,
        height=600

    )

    fig.update_geos(fitbounds="locations", visible=False)

    st.write(fig)
    
    result = transaction_data.groupby(Type)['Transaction_Count'].sum().reset_index(name='Total_Transaction_Count')
   
    st.write(px.bar(result, y='Total_Transaction_Count', x=Type, orientation='v',color_continuous_scale='haline',width=750))



with col2:
    min_values_idx_count = transaction_data['Transaction_Count'].idxmin()
    min_values_count = transaction_data.loc[min_values_idx_count]
    st.write("Minimum Transaction Count:")
    st.write(min_values_count,column=['test'])
    st.image('images.jpeg',use_column_width="auto")
    st.header(":orange[phonepe] usage in :green[India Analysis]",divider='rainbow')


 
    
with col3:
    result_count = transaction_data.sort_values(by='Transaction_Count', ascending=False).head(1)

    # Execute the second query
    result_amount = transaction_data.sort_values(by='Transaction_Amount', ascending=False).head(1)

    # Display the results in Streamlit
    st.write("Maximum Transaction Count:")
    st.dataframe(result_count,hide_index=True)

    st.write("Maximum Transaction Amount:")
    st.dataframe(result_amount,hide_index=True)
    
    min_values_idx_amount = transaction_data['Transaction_Amount'].idxmin()
    min_values_amount = transaction_data.loc[min_values_idx_amount]

   
    st.write("Minimum Transaction Amount:")
    st.write(min_values_amount)
    
    
        # You can set bins with nbinsx and nbinsy
    fig = px.density_heatmap(transaction_data, x=Type, y='Transaction_Amount', z='Transaction_Count', 
                            color_continuous_scale="thermal")

    st.write(fig)
    
        
    map_data = st.selectbox('Select State wise Total Transaction count & Amount ',
                                        ['Transaction_Amount', 'Transaction_Count'], 
                                       index=0)

    st.image('download.jpeg',use_column_width="auto")
    df = map()
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color=map_data,
        color_continuous_scale='thermal',
        width=700

    )

    fig.update_geos(fitbounds="locations", visible=False)

    st.write(fig)




col1,col2 = st.columns([4,4],gap="medium")
result = transaction_data.groupby(Type)['Transaction_Count'].sum().reset_index(name='Total_Transaction_Count')

with col1:
    scater_result = transaction_data.groupby(Type)[['Transaction_Count', 'Transaction_Amount']].sum().reset_index()
    fig = px.scatter_matrix(scater_result,color_continuous_scale="haline")

    st.write(fig)
        
    VType = st.selectbox('Select data distribution',
                                    ['State', 'Year', 'Transaction_Type', 'Quarter'], 
                                    index=0)
    st.header('Distribution of transaction Amount & count',divider='rainbow')
    fig = px.scatter_3d(transaction_data, x=VType, y='Transaction_Amount', z='Transaction_Count',color=VType
                         ,opacity=0.8, width=700, height=900)
    st.write(fig)
    
    
    Type = st.selectbox('Select a type',
                                    ['State', 'Year', 'Transaction_Type', 'Quarter'], 
                                    index=0)
    type_num1 = st.selectbox('Select a type',
                                        ['Transaction_Count','Transaction_Amount'], 
                                        index=0)
    pieTc = transaction_data.groupby(Type)[type_num1].sum().reset_index(name='Total_Transaction_Count')
    pie =px.pie(pieTc, values='Total_Transaction_Count', names=Type, 
       title='Total_Transaction_Count by ' + str(Type),
       color_discrete_sequence=px.colors.sequential.haline)
    st.write(pie)
    


    
with col2:

    st.write(px.violin(transaction_data,x ='Transaction_Amount',y='Transaction_Count',color= VType, box=True, points='all'))
    
    boxType = st.selectbox('Select a type',
                                    ['State','Transaction_Type', 'Quarter'], 
                                    index=0)
    box_result = transaction_data.groupby(boxType)[['Transaction_Count', 'Transaction_Amount']].sum().reset_index()
    box_plot_data = px.box(box_result, x=boxType, y=['Transaction_Count', 'Transaction_Amount'], 
                            labels={'Type': 'Transaction Type', 'value': 'Transaction Amount/Count'}, 
                            title='Box Plot of Transaction Count and Amount by Type',  color=boxType)
    st.write(box_plot_data)
    
    
    fig = px.scatter(transaction_data, x=Type, y="Transaction_Amount", color=Type,width=650)
    st.write(fig)  
    
    st.image('download.jpeg',use_column_width="auto")
    
    user_data = retrieve_agg_user()
    df = user_data.groupby('State')['Users_count'].sum().reset_index()
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color="Users_count",
        title="phonepe user in distribution in india",
        color_continuous_scale='thermal',
        width=700

    )

    fig.update_geos(fitbounds="locations", visible=False)

    st.write(fig)



user_data_box = st.selectbox('Select a type',
                                    ['Brand_type', 'State', 'Year'], 
                                    index=0)

col1,col2 = st.columns([4,4],gap="medium")
user_data = retrieve_agg_user()


with col1:
    fig = px.scatter(user_data, x='Brand_type', y="Users_count", 
                    title="phonepe user using device Name wise",
                    color=user_data_box,width=650)
    st.write(fig)  
    

with col2:  
    
    pieTc = user_data.groupby(user_data_box)["Users_count"].sum().reset_index(name='Total_Transaction_Count')
    pie =px.pie(pieTc, values='Total_Transaction_Count', names=user_data_box, 
        title='Total_Users Count by ' + str(user_data_box), 
        color_discrete_sequence=px.colors.sequential.thermal)
    st.write(pie)
        
        


