# Phonepe Pulse Data Visualization and Exploration

## Project Overview

This project aims to create a user-friendly tool using Streamlit and Plotly to visualize data extracted from the Phonepe Pulse GitHub repository. The tool will provide valuable insights and information about various metrics and statistics related to Phonepe.

## Problem Statement

The Phonepe Pulse GitHub repository contains a large amount of data that needs to be extracted, processed, and visualized in an interactive and visually appealing manner. The goal is to create a live geo visualization dashboard that allows users to explore different facts and figures.

## Approach

1. **Data Extraction**: Clone the GitHub repository using scripting.
2. **Data Transformation**: Use Python and Pandas for data manipulation and cleaning.
3. **Database Insertion**: Use `mysql-connector-python` to insert transformed data into a MySQL database.
4. **Dashboard Creation**: Use Streamlit and Plotly to create an interactive dashboard.
5. **Data Retrieval**: Fetch data from the MySQL database to update the dashboard.
6. **Deployment**: Ensure the solution is secure, efficient, and user-friendly.

## Results

The result will be a live geo visualization dashboard with at least 10 dropdown options for users to select different facts and figures. The dashboard will provide valuable insights and information about the data in the Phonepe Pulse GitHub repository.

vedio drive link "https://drive.google.com/file/d/1sneMX8YJdq-fDwDmiP49612WlYMWZdQS/view?usp=sharing"

## Learning Outcomes

1. Data extraction and processing using Python and Pandas.
2. Database management with MySQL.
3. Visualization and dashboard creation using Streamlit and Plotly.
4. Geo visualization using Plotly's geo map functions.
5. Dynamic updating of dashboards based on the latest data.
6. Project development and deployment best practices.

## Evaluation Metrics

- Code should be modular, maintainable, and portable.
- GitHub repository must be maintained and public.
- Proper README file with project development details.
- Follow Python coding standards (PEP 8).
- Create a demo/presentation video for LinkedIn.

## phonepe dataset download from git

First install GIt  and the git clone

```import git

repository_url='https://github.com/phonepe/pulse.git'

destination_data= r"data"
git.Repo.clone_from(repository_url,destination_data)

```

## Dataset

Dataset Link: [Data Link](link_to_data)

Inspired From: PhonePe Pulse

## Software Requirements

- Python 3.x
- MySQL
- Streamlit
- Plotly

## Libraries

- pandas
- mysql-connector-python
- streamlit
- plotly

## Usage

1. Clone the repository.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`

## Credits

This project is inspired by the PhonePe Pulse dataset and leverages the power of Python, Pandas, MySQL, Streamlit, and Plotly for data visualization and exploration.
