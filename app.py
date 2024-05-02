import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

#reading dataset
df=pd.read_csv('diwali_cleaned.csv')


st.set_page_config(layout='wide',page_title='Diwali Analysis')
st.title('Sales Analysis on Diwali ')
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
        
if options=='Marital Status Lense':
    btn3=st.sidebar.button('Show Marital Based Analysis')
    if btn3:
        st.title('Matarial Based Analysis on Purchase of  Goods During Diwali')
        st.markdown('<hr color="#ff0000" size="1">', unsafe_allow_html=True)

        ax=sns.countplot(data=df,x='marital_status',width=0.4,hue='gender')
        plt.xticks(ticks=[0,1],labels=['married','unmarried'])
        for i in ax.containers:
            ax.bar_label(i)
            
        plt.ylabel('Orders Count',fontsize=30)
        plt.xlabel('Marital Staus',fontsize=30)
        plt.title("Marital Status Analysis",fontsize=50)

        st.pyplot()

# Product Category Lense','Occupation Lense
if options=='Product Category Lense':
    btn4=st.sidebar.button('Show Most Ordered Product')
    if btn4:
        st.title('Most Higlighted Product During  Diwali')
        st.markdown('<hr color="#ff0000" size="1">', unsafe_allow_html=True)
        
        product_cat=df.groupby('product_category',as_index=False)['orders'].sum().sort_values(by='orders',ascending=False,ignore_index=True)
        plt.figure(figsize=(16,8))
        ax=sns.barplot(data=product_cat,x='product_category',y='orders')
        plt.xticks(rotation=90)

        for bar in ax.containers:
            ax.bar_label(bar)

        plt.ylabel('Orders Count',fontsize=30)
        plt.xlabel('Product Category',fontsize=30)
        plt.title("Product wise Analysis",fontsize=50)
        st.pyplot()
        
if options=="Occupation Lense":
    btn5=st.sidebar.button("Show Occupation Based Analysis")
    if btn5:
        st.title('purchase analysis according to the occupation of Customer')
        st.markdown('<hr color="#ff0000" size="1">', unsafe_allow_html=True)

        product=df.groupby('occupation',as_index=False)['orders'].sum().sort_values(by='orders',ascending=False,ignore_index=True)
        ax=sns.barplot(product,x='occupation',y='orders')
        plt.xticks(rotation=90)

        for bar in ax.containers:
            ax.bar_label(bar)

        plt.ylabel('Orders Count',fontsize=20)
        plt.xlabel('Occupation',fontsize=20)
        plt.title("Occupation Wise Analysis",fontsize=30)

        st.pyplot()
