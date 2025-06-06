import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
st.set_page_config( page_title="Startup Analysis")

df = pd.read_csv("startup_cleaned.csv")

st.sidebar.title("Startup Funding Analysis")

df["date"] = pd.to_datetime(df['date'],errors='coerce')
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

# overall Analysis
def load_overall_analysis():
    st.title("Overal Analysis")

    #total invested amount
    total = round(df["amount"].sum())

    # average 
    avg_funding = df.groupby('startup')['amount'].sum().mean()

    # totla funded startup 

    num_startup = df['startup'].nunique()



    col1,col2,col3,col4 = st.columns(4)

    # max amount infused in startup

    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    with col1:
        st.metric('Total',str(total) + " " 'Cr')
    with col2:
        st.metric("Max",str(max_funding) + ' Cr')
    with col3:
        st.metric("Average",str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric("Funded Startups", num_startup)

    st.header("MoM Graph")
    selected_options = st.selectbox('Select Type',["Total","Count"])
    if selected_options =='Total':
        temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year','month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig3,ax3 = plt.subplots()
    ax3.plot(temp_df["x_axis"],temp_df['amount'])

    st.pyplot(fig3)
                                    





# Investro functio:
def load_investor_details(investor):
    st.title(investor)
    # load last 5 df 
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader("Most recent Investment ")
    st.dataframe(last5_df)
    col1,col2 = st.columns(2)
    with col1:
        # Money invested more 
        most_place_invested =  df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader("Biggest Investment ")
        st.dataframe(most_place_invested)


        # Plot
        st.subheader("Biggest Investment Amount per Startup")
        fig, ax = plt.subplots()
        ax.bar(most_place_invested.index, most_place_invested.values)
        ax.set_ylabel('Investment Amount')
        ax.set_xlabel('Startup')
        ax.set_title('Top 5 Investments')
        st.pyplot(fig) 
    
    with col2:
        # Sector invested on 
        
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader("Sector Invested In")
        fig1,ax1 = plt.subplots()
        ax1.pie(vertical_series, labels= vertical_series.index, autopct="%0.01f")
        st.pyplot(fig1)


        # Cities where invested in 
        cities = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader("Cities Invested In")
        fig1,ax1 = plt.subplots()
        ax1.pie(cities, labels= cities.index, autopct="%0.01f")
        st.pyplot(fig1)

        # Yealry invested 
        yearly_invested = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader("Yearly Chart ")
        fig1,ax1 = plt.subplots()
        ax1.plot(yearly_invested.index, yearly_invested.values, marker ='o')
        st.pyplot(fig1)



option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option =='Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    StartupBtn = st.sidebar.button("Find Startup Details")
    st.title("Startup Analysis")
else:
    selected_investor = st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    InvestorBtn = st.sidebar.button("Find Investor  Details")
    if InvestorBtn:
        load_investor_details(selected_investor)

    


# Investor page 




