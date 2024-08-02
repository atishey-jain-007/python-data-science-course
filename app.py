import streamlit as st
import pandas as pd
import plotly.express as px

# ui configruration
st.set_page_config(
    page_title="pokemon App",
    page_icon="🫎",
    layout="wide",

)

# load data
@st.cache_data
def load_data():
    return pd.read_csv("Pokemon.csv",index_col="#")

#ui intergration
with st.spinner("loading dataset..."):
    df =load_data()
    st.snow()

    st.title("Pokemon Data Analytics")
    st.subheader("A simple data app to analyze Pokemon data")

    st.sidebar.title("Menu")
    choice =st.sidebar.radio("Options",["view Data","Visualize Data"])
    if choice =='view Data':
        st.header("view Dataset")
        st.dataframe(df)
    else:
        st.header("visualization")  
        cat_cols= df.select_dtypes(include='object').columns.tolist()
        num_cols= df.select_dtypes(exclude='object').columns.tolist()
        cat_cols.remove('Name')
        num_cols.remove('Generation')
        num_cols.remove('Legendary')
        cat_cols.append('Generation')
        cat_cols.append('Legendary')


        snum_col= st.sidebar.selectbox("Select a numeric column", num_cols)
        scat_col= st.sidebar.selectbox("Select a categorical column",cat_cols)

        c1,c2 = st.columns(2)
        #Visualize numerical column
        fig1 = px.histogram(df,
        x=snum_col,
        title=f"Distribution of {snum_col}"
        )
        #Visualize categroical column
        fig2= px.pie(df,
                     names=scat_col,
                     title=f"Distribution of {scat_col}",
                     hole=0.3
                     )
        c1.plotly_chart(fig1)
        c2.plotly_chart(fig2)

        fig3=px.box(df,x=scat_col,y=snum_col,title=f"{snum_col} by {scat_col}")
        st.plotly_chart(fig3)
        fig4= px.treemap(
            df,
            path=['Generation','Type 1'],
            title=f"Pokemon Type Disribution"
        )
        st.plotly_chart(fig4)
        

        



#to run this program,open terminal and run the following command
# streamlit app.py