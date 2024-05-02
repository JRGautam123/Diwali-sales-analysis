import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

#reading dataset
df=pd.read_csv('diwali_cleaned.csv')

st.set_page_config(layout='wide',page_title='Diwali Analysis')
# adding sidebar 
options=st.sidebar.selectbox("MENU",['Gender Lense','Age_Group Lense','State Lense',"Marital Status Lense",'Product Category Lense','Occupation Lense'],placeholder='Choose an options',index=None)


if options=='Gender Lense':
    btn0=st.sidebar.button('Show Gender Based analysis')
    if btn0:
        st.title('Gender Wise Comparision on Purchase of Goods During Diwali')
        temp_ser=df['gender'].value_counts()

        plt.figure(figsize=(5,4))
        plt.bar(temp_ser.index,temp_ser.values,color='maroon',width=0.5)
        plt.title("Genders involvement in pruchase")
        plt.xticks(ticks=["M","F"],labels=['male','female'])
        plt.xlabel('Gender')
        plt.ylabel('Count')
        st.pyplot()
        st.write('This shows number of Males and Females in the total customers')

        st.markdown('<hr color="#ff0000" size="1">', unsafe_allow_html=True)
        
        # money spend on the basis of gender
        sales_gen=df.groupby('gender',as_index=False)['amount'].sum()
        sns.barplot(x='gender',y='amount',data=sales_gen,width=0.5)
        plt.title("Total money spend by males and females")
        st.pyplot()
        st.write('This shows that Femles expends more money than Males')
        st.markdown('<hr color="#ff0000" size="4">', unsafe_allow_html=True)
        st.write("From above grpah we can see that most of the buyer are females and even the money spend by them on buying is greater than that of male")

if options=='Age_Group Lense':
    btn1=st.sidebar.button('Show Age group based analysis')
    if btn1:
        st.title('Age Group Wise Comparision on Purchase of  Goods During Diwali')
        ax=sns.countplot(data=df,x="age_group",hue='gender')
        for bars in ax.containers:
             ax.bar_label(bars)
        plt.title("Age Group vs Number of Orders")
        plt.ylabel("Number of Orders")
        st.pyplot()

        st.markdown('<hr color="#ff0000" size="4">', unsafe_allow_html=True)

        sales_age=df.groupby('age_group',as_index=False)['amount'].sum()
        ax=sns.barplot(x='age_group',y='amount',data=sales_age,color='maroon')
        for bars in ax.containers:
            ax.bar_label(bars)
        plt.title("Total Sales Amount vs Age Group")
        st.pyplot()

        st.markdown('<hr color="#ff0000" size="4">', unsafe_allow_html=True)
        st.write(" From above graph we can see the most of the buyers are of the age group between 26-35 yrs female")

if options=='State Lense':
    btn2=st.sidebar.button('Show State Wise Analysis')
    if btn2:
        st.title('State Wise Comparision on Purchase of  Goods During Diwali')
        st.markdown('<hr color="#ff0000" size="1">', unsafe_allow_html=True)
    
        top_10=df.groupby('state',as_index=False)['orders'].sum().sort_values(by='orders',ascending=False,ignore_index=True).head(10)
        plt.bar(x=top_10['state'],height=top_10['orders'])
        plt.xticks(rotation=90)

        for i in range(top_10.shape[0]):
            plt.text(top_10['state'].values[i],top_10['orders'].values[i],top_10['orders'].values[i])

        plt.title("Top 10 Highest Ordering States")
        plt.xlabel('States')
        plt.ylabel('Number of Orderd items')
        st.pyplot()

        st.markdown('<hr color="#ff0000" size="1">', unsafe_allow_html=True)

        top_amount=df.groupby('state',as_index=False)['amount'].sum().sort_values(by='amount',ascending=False,ignore_index=True).head(10)
        
        plt.bar(x=top_amount['state'],height=top_amount['amount'])
        plt.xticks(rotation=90)

        for i in range(top_amount.shape[0]):
            plt.text(top_amount['state'].values[i],top_amount['amount'].values[i],top_amount['amount'].values[i],fontsize=6)

        plt.title("Top 10 Highest Money Spending States")
        plt.xlabel('States')
        plt.ylabel('Amount(RS.)')
        st.pyplot()
        

