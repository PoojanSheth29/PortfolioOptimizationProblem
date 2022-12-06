import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Portfolio Optimization")

st.header('Your Portfolio') 

#portfolio display

stock_name,stock_price,buy_no = st.columns(3)
graph1,graph2 =st.columns(2)



#sidebar section


data = pd.read_csv('comapnies.csv')
print(data)


var = st.sidebar.multiselect("Select multiple Companies from the drop down list" ,data['Symbol'])

if st.sidebar.button("Add to My Portfolio"):
    stock_name = st.write(var)
    stock_price.write("100 Rs")
    buy_no.number_input(" ",min_value=1 ,max_value=1000)



#Graph display section
st.header(' ')
st.header('sample Graphical analysis generated') 

data = pd.DataFrame(
    np.random.randn(100,3),
    columns = ['a','b','c']
)

st.set_option('deprecation.showPyplotGlobalUse', False)

graph1 = plt.scatter(data['a'],data['b'])
graph2 = st.pyplot()

st.line_chart(data)