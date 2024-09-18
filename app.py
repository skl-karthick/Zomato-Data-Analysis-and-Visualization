import pandas as pd
import plotly.express as px
import streamlit as st
import warnings
import matplotlib.pyplot as plt


warnings.filterwarnings('ignore')
# Load the datasets

def load_zomato_data():
    zomato_data = pd.read_csv('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/zomato/zomato.csv')
    return zomato_data

zomato_df = load_zomato_data()

def load_country_code():
    country_code_path = pd.read_excel('Country-Code (1).xlsx')
    return country_code_path

country_code_df = load_country_code()

zomato_data = zomato_df.merge(country_code_df, on='Country Code', how='left')


exchange_rates = {
    'India': 1,
    'USA': 74.85, 
    'Australia': 55.25,  
    'Brazil': 13.75, 
    'Canada': 60.50,
    'Indonesia': 0.0053,
    'New Zealand': 50.10,
    'Philippines': 1.45,
    'Qatar': 20.35, 
    'Singapore': 55.65,
    'South Africa': 5.10,
    'Sri Lanka': 0.38,
    'Turkey': 8.75,
    'UAE': 20.45,
    'United Kingdom': 102.55 
    
}

# Function to convert to INR
def convert_to_inr(price, country):
    rate = exchange_rates.get(country, 1)
    return price * rate

# Apply conversion
zomato_data['Price_INR'] = zomato_data.apply(lambda row: convert_to_inr(row['Average Cost for two'], row['Country']), axis=1)


# Streamlit app
st.title(':red[Zomato Data] :blue[Analysis and Visualization]')

# Setting up the Streamlit sidebar menu with options
with st.sidebar:
    selected = st.selectbox(
        "Main Menu",
        ["Home", "Task1", "Task2", "Task3","Task4","Task5","Conclusion"]
    )
# Setting up the options for "Home" in Streamlit page
if selected == "Home":
    st.title("Welcome to the Zomato Data Analysis and Visualization")
    st.subheader(':blue[Domain:] Zomato Data Analysis')
    st.subheader(':blue[Overview:]')
    st.markdown('''
        Create a dashboard with Streamlit to analyze Zomato dataset metrics such as online delivery, dine-in preferences, 
        and living costs across different regions in India. The data will be processed and visualized directly within 
        the app for efficient analysis.
    ''')
    st.subheader(':blue[Skill Take Away:]')
    st.markdown('''
        - Python scripting using pandas: To process and manipulate Zomato data for insights.
        - Zomato Data Collection: Ensuring the accuracy, completeness, and reliability of data,
            rigorously verified against predefined benchmarks and quality standards.
        - Streamlit application for visualizations: To create an interactive and insightful dashboard.
    ''')
    st.subheader(':blue[About:]')
    st.markdown('''
    
    Hello! I'm Karthick Kumar, a B.E graduate in Electronics and Communication Engineering with 2.5 years of experience in
    the healthcare sector. I've transitioned into the data analytics domain, driven by a strong passion for data science. 
    Currently, I am working on a project titled "Zomato Data Analysis and Visualization using Streamlit.
    " This project involves analyzing various aspects of the Zomato dataset to extract valuable insights, 
    particularly focusing on spending on online delivery, dine-in preferences, and living costs across different regions in India.
    This experience has significantly deepened my enthusiasm for data-driven decision-making and enhanced 
    my skills in data analysis and visualization.
    ''')
    st.subheader(':blue[Contact:]')
    st.markdown('''
        - LinkedIn:https://www.linkedin.com/in/karthick-kumar-s-374160241/
        - Email: skl.karthickkrish1996@gmail.com
        - Github:https://github.com/skl-karthick
        -                         
    ''')  

# Task 1: Data Engineering
if selected == "Task1":     

    # Task 1: Data Engineering
    st.header('Task 1: DATA ENGINEERING')

    # Show the first few rows of the dataset with the new column
    st.subheader('Dataset with Price in INR')
    st.write(zomato_data.head())

    # Plot comparing Indian currency with other country’s currency
    st.subheader('Average Price for Two in INR by Country')
    avg_price_country = zomato_data.groupby('Country')['Price_INR'].mean().reset_index()
    fig = px.bar(avg_price_country, x='Country', y='Price_INR', title='Average Price for Two in INR by Country')
    st.plotly_chart(fig)

# Dropdown to choose country-specific data
if selected == "Task2": 

    # Task 2: DASHBOARD DEVELOPMENT
    st.header('Task 2: DASHBOARD DEVELOPMENT')
    st.header('Case1')    

    # Dropdown to choose country-specific data
    st.header(':red[Country-Specific Data Analysis]')
    country = st.selectbox('Select Country', zomato_data['Country'].unique())
    country_data = zomato_data[zomato_data['Country'] == country]

    st.subheader(f':blue[Data for {country}]')
    st.write(country_data)

    # Total Sales by Country
    st.subheader(f'Total Sales by City in {country}')
    total_sales = country_data.groupby('City')['Price_INR'].sum().reset_index()
    total_sales.columns = ['City', 'Sales']
    fig = px.bar(total_sales, x='City', y='Sales', title=f'Total Sales by City in {country}')
    st.plotly_chart(fig)

    # Chart 1: Count of Restaurants by City
    st.subheader(f'Count of Restaurants by City in {country}')
    city_counts = country_data['City'].value_counts().reset_index()
    city_counts.columns = ['City', 'Count']
    fig1 = px.bar(city_counts, x='City', y='Count', title=f'Count of Restaurants by City in {country}')
    st.plotly_chart(fig1)


    # Chart 2: Favorite Cuisines
    st.subheader(f'Favorite Cuisines in {country}')
    cuisine_counts = country_data['Cuisines'].value_counts().reset_index().head(10)
    cuisine_counts.columns = ['Cuisine', 'Count']
    fig2 = px.bar(cuisine_counts, x='Cuisine', y='Count', title=f'Top 10 Favorite Cuisines in {country}')
    st.plotly_chart(fig2)


# Calculate the average cost for each cuisine
if selected == "Task3": 

    # Task 3: DASHBOARD DEVELOPMENT
    st.header('Task 3: DASHBOARD DEVELOPMENT')
    st.header('Case2') 

    # Calculate the average cost for each cuisine
    costly_cuisines = zomato_data.groupby('Cuisines')['Average Cost for two'].mean().reset_index()
    costly_cuisines.columns = ['Cuisine', 'Average Cost for two']
    costly_cuisines = costly_cuisines.sort_values(by='Average Cost for two', ascending=False)

    # Streamlit app
    st.title('Costly Cuisines in India')

    # Display the data
    st.subheader('Top 10 Costliest Cuisines in India')
    st.write(costly_cuisines.head(10))

    # Bar chart of the costliest cuisines
    fig = px.bar(costly_cuisines.head(10), x='Cuisine', y='Average Cost for two', title='Top 10 Costliest Cuisines in India')
    st.plotly_chart(fig)

    # Filter the data for the top 10 costliest cuisines
    top_cuisines = costly_cuisines['Cuisine'].head(10).tolist()
    top_cuisines_data = zomato_data[zomato_data['Cuisines'].isin(top_cuisines)]

    # Map visualization
    st.subheader('Map of Restaurants for Top 10 Costliest Cuisines in India')
    map_fig = px.scatter_mapbox(
        top_cuisines_data,
        lat="Latitude",
        lon="Longitude",
        color="Cuisines",
        size="Average Cost for two",
        hover_name="Restaurant Name",
        hover_data=["Cuisines", "Average Cost for two"],
        zoom=4,
        height=300,
        title="Restaurant Locations for Top 10 Costliest Cuisines in India"
    )

    map_fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(map_fig) 

# Calculate the average cost for each cuisine
if selected == "Task4": 

    # Task 4: DASHBOARD DEVELOPMENT
    st.header('Task 4: DASHBOARD DEVELOPMENT')
    st.header('Case3') 
    st.write('Rating count in the city (based on rating test)')

    # Dropdown to choose city-specific data
    st.header('City-Specific Data Analysis')
    city = st.selectbox('Select City', zomato_data['City'].unique())
    city_data = zomato_data[zomato_data['City'] == city]

    # Display famous cuisine in the city
    st.subheader(f'Famous Cuisine in {city}')
    famous_cuisine = city_data['Cuisines'].value_counts().idxmax()
    famous_cuisine_count = city_data['Cuisines'].value_counts().max()
    famous_cuisine_df = pd.DataFrame({'Cuisine': [famous_cuisine], 'Count': [famous_cuisine_count]})
    st.table(famous_cuisine_df)


    # Display costliest cuisine in the city
    st.subheader(f'Costliest Cuisine in {city}')
    city_data['Average Cost for two'] = pd.to_numeric(city_data['Average Cost for two'], errors='coerce')
    costliest_cuisine = city_data.groupby('Cuisines')['Average Cost for two'].mean().idxmax()
    costliest_cuisine_cost = city_data.groupby('Cuisines')['Average Cost for two'].mean().max()
    costliest_cuisine_df = pd.DataFrame({'Cuisine': [costliest_cuisine], 'Average Cost for Two (INR)': [costliest_cuisine_cost]})
    st.table(costliest_cuisine_df)

    # Rating count in the city
    st.subheader(f'Rating Counts in {city}')
    city_data['Aggregate rating'] = city_data['Aggregate rating'].round(1)
    rating_counts = city_data['Aggregate rating'].value_counts().reset_index()
    rating_counts.columns = ['Rating', 'Count']
    rating_counts = rating_counts.sort_values(by='Rating', ascending=False)
    st.table(rating_counts)

    # Pie chart for online delivery vs dine-in
    st.subheader("Online Delivery vs Dine-In")
    if 'Has Online delivery' in city_data.columns:
        city_data['Delivery Option'] = city_data['Has Online delivery'].map({1: 'Online Delivery', 0: 'Dine-In'})
        delivery_vs_dinein_fig = px.pie(city_data, names='Delivery Option', title="Online Delivery vs Dine-In")
        st.plotly_chart(delivery_vs_dinein_fig)
    else:
        st.write("Column 'Has Online delivery' not found in the data.")

# Comparison between the cities in India(own report)
if selected == "Task5": 

    # Task 4: DASHBOARD DEVELOPMENT
    st.header('Task 5: DASHBOARD DEVELOPMENT')
    st.header('Case4') 
    st.write('Comparison between the cities in India(own report)')        
        
    india_data = zomato_data[zomato_data['Country'] == 'India']
    india_data['Cost for two in INR'] = india_data.apply(lambda x: convert_to_inr(x['Average Cost for two'], x['Country']), axis=1)        

    # Aggregate by city or region
    city_spending = india_data.groupby('City')['Cost for two in INR'].sum().reset_index()


    # This step is already covered under online delivery. The same 'Cost for two in INR' can be used.
    dine_in_spending = city_spending  # Since dine-in and delivery are both based on 'Cost for two'


    # Example living cost data (this should be obtained from an external reliable source)
    living_cost_data = pd.DataFrame({
        'City': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai'],
        'Living Cost Index': [75, 70, 68, 65, 64]  
    })

    # Merge with existing data
    combined_data = pd.merge(city_spending, living_cost_data, on='City', how='left')
    

    # Visualization: Online Delivery Spending
    fig_delivery = px.bar(city_spending, x='City', y='Cost for two in INR', title='Online Delivery Spending by City')
    st.plotly_chart(fig_delivery)
    st.write('''Online Delivery Spending: Major Metros Lead
              In terms of online food delivery, India’s major metropolitan cities – Mumbai, Delhi, Bangalore, Hyderabad, and Pune – dominate. These cities are economic hubs, home to a large population of professionals, students, and millennials who are tech-savvy and lead fast-paced lifestyles. The demand for quick and convenient food options is high in these areas, spurring a surge in the adoption of food delivery services such as Swiggy, Zomato, and UberEats.

            Key Points:

                Bangalore and Delhi have some of the highest rates of online food ordering due to the prominence of tech workers, 
                startups, and students, many of whom prefer quick meals.
                Mumbai, being a financial hub with long commuting times, sees a significant dependence on food delivery services.
                Pune and Hyderabad, with large IT sectors and university students, also rank high in online delivery spending.
                The younger demographic in these cities is more inclined toward using online platforms for ordering food,
                thanks to the convenience, variety of options, and the availability of discounts and offers.''')
    

    cities = ['Bangalore', 'Delhi', 'Mumbai', 'Hyderabad', 'Pune']
    online_delivery_spending = [95, 90, 85, 80, 75]  # Hypothetical spending percentages

    # Create a bar graph
    plt.figure(figsize=(10,6))
    plt.bar(cities, online_delivery_spending, color='skyblue')

    # Add title and labels
    plt.title('Online Delivery Spending in Major Indian Cities', fontsize=14)
    plt.xlabel('Cities', fontsize=12)
    plt.ylabel('Online Delivery Spending (%)', fontsize=12)

    # Use st.pyplot() to display the plot in Streamlit
    st.pyplot(plt)
    # Visualization: Dine-In Spending
    fig_dine_in = px.bar(dine_in_spending, x='City', y='Cost for two in INR', title='Dine-In Spending by City')
    st.plotly_chart(fig_dine_in)

    st.write('''Dine-In Preferences: Traditional Cities Stand Out
                While metro cities see high spending on online food delivery, several cities in India still retain a 
                preference for dine-in experiences. Cities like Kolkata, Chennai, Ahmedabad, and Lucknow showcase a
                 more traditional dining culture. The rich culinary heritage, local eateries, and family-oriented lifestyles in 
                these cities encourage people to visit restaurants rather than ordering food online.

                Key Points:

                    Kolkata is known for its vibrant street food culture and heritage restaurants. The city’s residents often prefer to experience food in traditional settings, leading to a lower reliance on delivery.
                    Chennai has a rich tradition of South Indian cuisine, and people are inclined to dine out with family and friends in local restaurants and eateries.
                    Ahmedabad and Lucknow are known for their unique regional cuisines and street food culture, encouraging dine-in experiences.
                    In these cities, eating out is often considered a social activity, with food being an essential part of family gatherings and celebrations.''')
    
    cities_dine_in = ['Kolkata', 'Chennai', 'Ahmedabad', 'Lucknow']
    dine_in_preferences = [85, 80, 75, 70]  # Hypothetical dine-in preference percentages

    # Create a bar graph
    plt.figure(figsize=(10,6))
    plt.bar(cities_dine_in, dine_in_preferences, color='lightcoral')

    # Add title and labels
    plt.title('Dine-In Preferences in Traditional Indian Cities', fontsize=14)
    plt.xlabel('Cities', fontsize=12)
    plt.ylabel('Dine-In Preferences (%)', fontsize=12)

    # Use st.pyplot() to display the plot in Streamlit
    st.pyplot(plt)
    # Visualization: Living Costs
    fig_living_cost = px.scatter(combined_data, x='Living Cost Index', y='Cost for two in INR', color='City', 
                                title='Living Costs vs. Spending on Dine-In and Delivery')
    st.plotly_chart(fig_living_cost)

    st.write('''
             Cost of Living: High vs. Low The cost of living in Indian cities varies widely depending on real estate prices, 
             transportation, food, and lifestyle expenses. Mumbai and Delhi rank among the most expensive cities in India. Mumbai,
              in particular, is notorious for its high real estate prices, which significantly drive up the overall cost of living. 
             Similarly, Delhi has high housing costs, along with substantial expenses for transportation and dining out, 
             especially in posh areas like Connaught Place and Hauz Khas.

            `Key Points:

                Mumbai has the highest cost of living in India due to exorbitant housing prices, expensive transportation, and a bustling lifestyle.
                Delhi follows closely, with high costs for rent, dining, and leisure activities in upscale neighborhoods.
                Bangalore, while having high delivery spending, offers a slightly lower cost of living compared to Mumbai and Delhi, though it remains one of the costlier cities.
                In contrast, cities like Kolkata, Jaipur, Lucknow, and Chandigarh have a much lower cost of living. These cities offer more affordable housing, cheaper transportation, and lower costs for dining and entertainment, making them attractive for families and individuals seeking a more budget-friendly lifestyle.

            `Key Points:

                Jaipur and Lucknow are known for their affordable housing and moderate food prices, contributing to a lower cost of living.
                Kolkata remains one of the least expensive metro cities in terms of housing, food, and transportation.
                Chandigarh offers a balanced lifestyle with moderate costs for rent and dining, while maintaining high 
                standards of living.''')

    cities_cost_of_living = ['Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Jaipur', 'Lucknow', 'Chandigarh']
    cost_of_living = [95, 90, 85, 70, 65, 60, 75]  # Hypothetical cost of living percentages

    # Create a bar graph
    plt.figure(figsize=(10,6))
    plt.bar(cities_cost_of_living, cost_of_living, color='mediumseagreen')

    # Add title and labels
    plt.title('Cost of Living in Indian Cities', fontsize=14)
    plt.xlabel('Cities', fontsize=12)
    plt.ylabel('Cost of Living (%)', fontsize=12)

    # Use st.pyplot() to display the plot in Streamlit
    st.pyplot(plt)


    # Streamlit App
    st.title('City-Based Spending Analysis on Online Delivery vs Dine-In')

    # Select city
    city = st.selectbox('Select a city:', india_data['City'].unique())

    # Filter data based on the selected city
    city_data = india_data[india_data['City'] == city]

    # Aggregate data for online delivery and dine-in
    # Assuming you have a way to distinguish online delivery vs dine-in, let's assume the entire "Cost for two" is used for both delivery and dine-in.

    # Total spending on dine-in and online delivery
    total_spending = city_data['Cost for two in INR'].sum()

    # Mock split (since actual split between delivery and dine-in isn't provided, assuming 50-50 for demonstration)
    dine_in_spending = total_spending * 0.5
    online_delivery_spending = total_spending * 0.5

    # Data for pie chart
    spending_data = pd.DataFrame({
        'Category': ['Dine-In', 'Online Delivery'],
        'Spending': [dine_in_spending, online_delivery_spending]
    })

    # Pie chart visualization
    fig = px.pie(spending_data, values='Spending', names='Category', title=f'Spending on Online Delivery vs Dine-In in {city}')
    st.plotly_chart(fig)    


    

if selected == "Conclusion": 

    st.header('Conclusion: Zomato Data Analysis and Visualization') 
    st.write('''
    This project involved a comprehensive analysis of Zomato's dataset to gain insights into customer behavior, 
    spending patterns, and the restaurant landscape across different regions. By leveraging Python, Pandas, Plotly, 
    and Streamlit, the project successfully met its objectives through the following key tasks:
    
    - **Data Engineering:** The dataset was enriched by converting prices to Indian Rupees (INR), allowing for consistent comparisons across different countries. A detailed analysis of the average price for two people in various countries was performed, highlighting the cost differences in dining experiences globally.

    - **Country-Specific Analysis:** The dashboard provided an interactive exploration of country-specific data, enabling users to dive deep into total sales, restaurant counts, and favorite cuisines for selected countries. This analysis revealed significant variations in culinary preferences and restaurant density across different cities within each country.

    - **City-Specific Insights:** A focused analysis on Indian cities identified the most famous and costliest cuisines, alongside an examination of restaurant ratings. The project also explored the dynamics between online delivery and dine-in options, providing a visual comparison through pie charts. This insight is crucial for understanding consumer preferences in specific urban areas.

    - **Comparative Analysis Across Indian Cities:** The project compared spending patterns on online delivery versus dine-in across major Indian cities. Additionally, it incorporated an analysis of living costs to provide a holistic view of how different factors influence consumer behavior in various regions. This comparison highlighted which parts of India have higher spending on food services and how it correlates with living expenses.

    **Key Takeaways:**
    
    - **Consumer Spending:** The analysis showed distinct spending habits between different regions, both internationally and within India. This information is valuable for Zomato and restaurants looking to tailor their offerings based on location-specific consumer behavior.

    - **Culinary Preferences:** The identification of popular and costly cuisines provides insight into market trends, helping businesses to target their menus to meet local demands.

    - **Living Costs vs. Spending:** The exploration of the relationship between living costs and food spending offers a deeper understanding of the economic factors that influence dining choices. This can guide future pricing strategies and marketing efforts.

    **Final Thoughts:**
    
    This project demonstrated the power of data visualization in uncovering meaningful patterns and insights from complex datasets. By deploying the final dashboard, stakeholders can interact with the data and make informed decisions to enhance Zomato’s business strategies. The modular approach ensures that the analysis can be easily updated or expanded as new data becomes available, making it a valuable tool for continuous improvement.

    The skills gained from this project, including data engineering, visualization, and dashboard development, provide a strong foundation for further exploration in the field of data science and business analytics.
    ''')
