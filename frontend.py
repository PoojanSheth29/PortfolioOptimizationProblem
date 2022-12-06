import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from app import *
from PIL import Image

st.title("Portfolio Optimization")

#reading data
def get_data():
    path = r'C:/Users/POOJAN/OneDrive/Desktop/Protfolio_Project/finalcode/companies.csv'
    return pd.read_csv(path)

df = get_data()

#drop down menu to select companies
companies = df['Company Name'].dropna()
company_choice = st.multiselect('Select your company:', companies)

#user amount input box
investment = st.number_input('Enter Amount (in Rs) :')

y=[]
#var = st.sidebar.multiselect("Select multiple Companies from the drop down list" ,["TCS","BEL","SBI","WIPRO","HCL Tech","HDFC Bank","TATA Steel","Axis Bank","ICICI Bank Ltd","Bajaj Finserv","JSW Steel","Hindustan Unilever","Larsen & Tourbo Ltd","Maruti Suzuki India","Titan company","Infosys","TATA Motors"])

#generating everything if you click the button
if st.button("Add to My Portfolio"):
    x = companies.tolist()
    length = len(x)
 
    length2 = len(company_choice)
    
    for i in range(length):

        for j in range(length2):
            if(company_choice[j] == x[i]):
                y.append(df['Symbol'][i])

    y_pd = pd.DataFrame(
        {
            "Companies Selected": y 
        }
    )
    

    #displaying selected stocks 
    stock_name = st.table(y_pd)
    stocksymbol = y
    
    inputdata = len(stocksymbol)
    invested_amt = st.write('You have invested Rs.', investment)

    #output variables
    perc_var,perc_vola,perc_returns,allocation,leftover,data = backend(inputdata, stocksymbol, investment)
    
    #Graph display section
    st.header(' ')
    st.header('Graphical analysis') 

    

    st.set_option('deprecation.showPyplotGlobalUse', False)

    #graph1 = plt.scatter(data['a'],data['b'])
    plt.rcParams["figure.figsize"] = [8.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    fig.subplots_adjust(bottom=0.1)
    for i in data.columns.values:
        plt.plot(data[i], label = i)
    plt.title('STOCK COMPARISON CHART')
    plt.xlabel('Time', fontsize = 18)
    plt.ylabel('Price (Rs)',fontsize = 18)
    plt.legend(data.columns.values, loc = 'upper left')
    plt.savefig('foo.png')
    # foo = Image.open('foo.png')
    # st.image(foo, caption='Enter any caption here')
    plt.show()
    st.pyplot(fig)

    #output
    
    # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    #conversion of list to dataframe with specific key names\
    alloc_k = allocation.keys()
    alloc_v = allocation.values()

    allocation_pd = pd.DataFrame(
        {
            "Company Stock Name": alloc_k ,
            "Number of Stocks" : alloc_v
        }
    )

    #output values
    st.text('Optimized number of stocks to buy for each company : ')
    st.table(allocation_pd)
    st.text(' ')
    st.write('Leftover amount is :    ' , round(leftover,2) , '  Rs')

    perc_var = float(perc_var[:-1])
    st.write('Annual variance is :    ' , round(perc_var,2) , '  %')

    perc_vola = float(perc_vola[:-1])
    st.write('Annual volatility (Risk) is :    ' , round(perc_vola,2) , '  %')

    perc_returns = float(perc_returns[:-1])
    st.write('Annual Returns are :    ' , round(perc_returns,2) , '  %')


    st.subheader('Key Points:')

    st.markdown('**1.  _Annual Returns_**')
    st.write('Annual return basically helps in calcualting total retun rate. ')
    st.write('It is the total income generated over the investment made by the individual over a particular period of time. ')
    st.write('It can be calcualted as follows : (Ending value - Beginning value) / Beginning value ^ 1/no of years  - 1')

    st.markdown('**2.  _Annual Variance_**')
    st.write('Variance is a measurement of the degree of risk in an investment')
    st.write('High variance in a stock is associated with higher risk, along with a higher return. Low variance is associated with lower risk and a lower return')

    st.markdown('**3.  _Annual Volatility_**')
    st.write('Annual volatility basically helps in determing the swings in the price ranges of any commodity / assest or any kind of share around its mean price level. ')
    st.write('Hence it is from the measurement of volatitlity an investor can identify the total deviation of share price from its avearge price and helps them in decsion making over the deployement of finances.')
    st.write('It serves as an important decision making tool because a security with higher volatility normamlly carries a high risk level as the prices of it are spreaded out and are tend to have fluctuations over a short period of time and thus resulting in risk')
    
    