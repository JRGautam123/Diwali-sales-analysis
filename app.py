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
        st.title('Gender Wise Comparision on Purchase of Diwali Goods')
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

# if options=='Age_Group Lense':
#     btn1=st.sidebar.button('Show Age group based analysis')
#     if btn1:
#         ax=sns.countplot(data=df,x="age_group",hue='gender')
#         for bars in ax.containers:
#              ax.bar_label(bars)
#         plt.title("")