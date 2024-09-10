# Zomato Data Analysis Project

## Overview

This project focuses on analyzing restaurant data from **Zomato**, specifically targeting trends in food consumption patterns across different cities in India and globally. The analysis aims to explore insights related to **online food delivery trends**, **dine-in preferences**, and **cost of living** in major cities. Using interactive visualizations, users can gain a deeper understanding of the restaurant industry and consumer behavior in various regions.

## Key Objectives

- **Online Delivery Trends**: Identify which cities prefer online food delivery over dine-in experiences.
- **Dine-In Preferences**: Explore regions where dine-in experiences are more popular, based on cultural and social factors.
- **Cost of Living**: Compare the cost of living in various cities and its impact on dining choices, including food pricing in restaurants.
- **Global Insights**: Provide a global overview of restaurant data by incorporating currency conversion and country-level analysis.

## Features

- **Data Loading**: The project loads and cleans a Zomato dataset and enriches it with additional country code information for enhanced analysis.
- **Data Merging**: Zomato data is merged with country code and currency exchange rate information to normalize costs and allow global comparisons.
- **Analysis**:
  - **Online Delivery vs. Dine-In Trends**: A comparison of spending preferences in major metropolitan cities.
  - **Cost of Living Analysis**: A breakdown of living expenses in cities like Mumbai, Delhi, Kolkata, and others.
- **Interactive Visualizations**: The project leverages **Streamlit** and **Plotly** to create interactive, web-based visualizations of the insights, including bar charts and graphs for easy analysis.
  
## Datasets

1. **Zomato Dataset**: A dataset containing restaurant details such as name, ratings, location, cost for two, cuisines, and more.
   - [Zomato Data]('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/zomato/zomato.csv)
   
2. **Country Codes Dataset**: This dataset is used to map country codes to their respective country names, enabling analysis across different regions.
   - Path in code: `"C:/Users/sklka/Downloads/Country-Code (1).xlsx"`

3. **Exchange Rates**: A dictionary of currency exchange rates used to normalize costs across different countries for a fair comparison.

## Technologies Used

- **Pandas**: For loading, cleaning, and analyzing data.
- **Plotly**: To create interactive and responsive visualizations, making it easier to explore trends.
- **Streamlit**: A web framework to build and display interactive visualizations and provide a user-friendly interface.
- **Matplotlib**: For generating additional static plots where necessary.
- **Warnings**: Used to manage warning messages that may arise during execution.

- Ensure you have **Python 3.x** installed on your machine. You will also need to install the following libraries:

```bash
-pip install pandas plotly streamlit matplotlib

-Steps to Run the Project
-Clone the Repository:git clone <repository-url>
-Navigate to the Project Directory:cd zomato-analysis
-Install Dependencies: Install the required dependencies using the command mentioned in the "Prerequisites" section.
-Run the Streamlit App: Start the Streamlit server to view the analysis and visualizations.

-Interactive Interface: After running the app, open the browser to explore:

-**Online Delivery Trends**
-**Dine-In Preferences**
-**Cost of Living Analysis**
-**The app provides various filters and interactive plots to help users navigate and explore the data.**

-Project Insights
-1. Online Delivery Trends
-Metropolitan cities like Mumbai, Delhi, and Bangalore show a higher inclination toward online food delivery, driven by a fast-paced lifestyle and tech-savvy populations.
-Tier 2 cities like Pune and Hyderabad are rapidly catching up due to their growing IT sectors and young populations.
-2. Dine-In Preferences
-Traditional cities such as Kolkata, Chennai, and Lucknow show a stronger preference for dine-in experiences. The rich culinary heritage and strong family-oriented dining culture make dine-in a popular choice.
-3. Cost of Living Analysis
-Mumbai has the highest cost of living in India, largely driven by expensive housing and transportation.
-Kolkata and Lucknow have lower living costs, which influences lower food pricing and encourages more dine-in experiences.

-Future Scope
-Global Expansion: Extend the analysis to cover restaurant data from other countries using the country code and exchange rate datasets.
-Advanced Metrics: Incorporate other metrics like restaurant ratings, customer feedback, and time-based trends to provide more in-depth insights.
-Predictive Analysis: Use machine learning models to predict future trends in food delivery and dine-in preferences.

License
This project is licensed under the MIT License.


