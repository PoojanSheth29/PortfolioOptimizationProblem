import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import app

# sk = app.stocksymbol
# print(sk)

 

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
