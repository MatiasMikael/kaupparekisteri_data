## Project Overview

This project involves fetching, processing, and visualizing data about companies registered in Helsinki. The data comes from the Kaupparekisteri API, and the primary focus is on limited liability companies (OY) registered since 2020.

Key objectives include:

* Understanding registration trends over time.
* Identifying the impact of the COVID-19 pandemic on business registrations.
* Exploring the most common registration addresses for businesses.

## Features

Fetching data from the Kaupparekisteri API using Python. Processing and cleaning the fetched data. Filtering data to include only Helsinki-based companies registered as limited liability companies (OY) since 2020. Visualizing data in Tableau to reveal key insights.

## Installation Instructions

Clone this repository to your local machine: ``bash git clone https://github.com/MatiasMikael/kaupparekisteri_data.git``

Ensure you have the following installed:

* Python (3.8 or higher)
* Required Python libraries (requests, pandas)
* Tableau Desktop for creating and exploring visualizations.
* Run the script to fetch and process data: ``bash python fetch_data.py``

Data Output: A CSV file named helsinki_osakeyhtiot_2020.csv 
containing the following fields:
* CompanyName
* BusinessID
* City
* CompanyForm
* Address
* RegistrationDate


Open Tableau Desktop and connect the generated CSV file for visualization.


## Visualizations

Multiple Tableau visualizations were created using the processed data. Key visualizations include:

* Monthly Registrations:
A line chart showing the number of company registrations per month in 2020.
Purpose: Highlights the dramatic decline in registrations after March 2020 due to the COVID-19 pandemic.

* Most Active Registration Days:
A bar chart showing the days with the highest number of registrations in 2020.
Purpose: Identifies trends in registration activity at the daily level.

* Top Registration Addresses:
A horizontal bar chart showing the top 10 most common registration addresses in Helsinki.
Purpose: Highlights areas of business concentration.

## License

This work is licensed under the MIT License. However, the data fetched from the Kaupparekisteri API is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). More details on the API and licensing can be found on https://www.avoindata.fi/data/fi/apiset/kaupparekisterin-rekisteroidyt-ilmoitukset-api





