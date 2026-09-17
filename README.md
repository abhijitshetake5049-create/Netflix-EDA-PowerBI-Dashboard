# Netflix Movies & TV Shows — EDA & Power BI Dashboard

Data analysis project exploring Netflix Movies and TV Shows using Python, Pandas, and NumPy for data cleaning and Exploratory Data Analysis (EDA), followed by an interactive Power BI dashboard for visualization and insight generation.

---

## 📊 Project Overview

This project analyzes the Netflix Movies and TV Shows dataset to understand the characteristics and distribution of Netflix content.

Python was used for **data cleaning, preprocessing, feature engineering, and Exploratory Data Analysis (EDA)** using Pandas and NumPy.

The final processed dataset was then used to create an interactive **Power BI dashboard** covering content type, genres, ratings, countries, directors, movie durations, TV show seasons, and release trends.

---

## 📌 Dashboard Pages

### 1. Netflix Overview

Provides a high-level overview of Netflix content, including:

- Total Titles
- Total Movies
- Total TV Shows
- Total Countries
- Movies vs TV Shows
- Titles Added by Year
- Rating Distribution
- Titles by Release Year

![Netflix Overview](screenshots/overview.png)

---

### 2. Content Analysis

Analyzes the structure and duration of Netflix Movies and TV Shows, including:

- Content Type by Release Year
- Movie Duration Distribution
- Movie Duration Categories
- TV Shows by Number of Seasons
- TV Shows by Release Year
- Average Movie Duration
- Average TV Show Seasons

![Content Analysis](screenshots/content-analysis.png)

---

### 3. Genre & Rating Analysis

Analyzes Netflix content based on genres and ratings, including:

- Genre by Content Type
- Rating by Content Type
- Average Movie Duration by Rating
- Rating Distribution
- Most Common Rating
- Total Genres
- Movie Percentage

![Genre & Rating Analysis](screenshots/genre-rating.png)

---

### 4. Country Analysis

Analyzes the geographical distribution of Netflix content, including:

- Country Distribution
- Country by Content Type
- Movies by Country
- TV Shows by Country
- Total Countries
- Average Countries per Title
- TV Show Percentage

![Country Analysis](screenshots/country-analysis.png)

---

### 5. Release & Growth Analysis

Analyzes Netflix content across release years and content addition years, including:

- Titles by Release Year
- Titles Added by Year
- Titles Added by Year & Type
- Titles by Release Year & Type
- Total Releases
- Oldest Release Year
- Latest Release Year
- Highest Titles in a Year
- Peak Release Year

![Release & Growth Analysis](screenshots/release-growth.png)

---

### 6. Director Analysis

Analyzes Netflix content based on directors and the number of titles associated with them, including:

- Titles by Director
- Director by Content Type
- Movies by Director
- TV Shows by Director
- Total Directors
- Highest Titles by Director
- Average Titles per Director

![Director Analysis](screenshots/director-analysis.png)

---

### 7. Final Insights

Summarizes the major findings from the Netflix analysis using KPIs and visualizations, including:

- Most Common Rating
- Long Movies %
- One Season TV Shows %
- Most Common Release Year
- Content Type Distribution
- Top Genres
- Titles Added by Year and Type
- Top Countries

![Final Insights](screenshots/final-insights.png)

---

## 🧹 Data Cleaning & EDA

Python was used to prepare and analyze the Netflix dataset.

### Data Cleaning

- Handled missing values
- Replaced infinite and negative infinite values
- Removed duplicate records
- Converted `date_added` into datetime format
- Handled missing director, cast, country, rating, and duration values

### Exploratory Data Analysis

EDA was performed using **Pandas and NumPy** to analyze:

- Movies vs TV Shows
- Content ratings
- Genres
- Countries
- Directors
- Movie durations
- TV show seasons
- Release years
- Content added by year

### Feature Engineering

Additional features were created for analysis, including:

- Movie duration
- TV show seasons
- Movie duration categories
- TV show season categories
- Year-based analysis features

The complete Python implementation is available in:

`Netflix_EDA.py`

---

## 🛠️ Tools & Technologies

- **Python** – Data cleaning, preprocessing, feature engineering, and EDA
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical operations and data preprocessing
- **Power BI** – Interactive dashboard development and visualization
- **Jupyter Notebook / VS Code** – Python development
- **GitHub** – Project documentation and version control

---

## 📈 Key Insights

The project helps analyze:

- Distribution of Movies and TV Shows
- Most common content ratings
- Popular genres
- Country-wise content distribution
- Movie duration patterns
- TV show season patterns
- Director-level content distribution
- Netflix content release trends
- Netflix content addition trends

---

## 🎯 Project Objective

The objective of this project is to transform raw Netflix data into meaningful insights using **Python-based data analysis and Power BI visualization**.

The project demonstrates a complete data analytics workflow from **data cleaning and EDA to interactive dashboard development**.

---

## 📂 Project Structure

```text
Netflix-EDA-PowerBI-Dashboard/
│
├── README.md
├── Netflix_EDA.py
├── netflix_final.csv
├── Netflix_Dashboard.pbix
│
├── dataset/
│   └── netflix_titles.csv
│
└── screenshots/
    ├── overview.png
    ├── content-analysis.png
    ├── genre-rating.png
    ├── country-analysis.png
    ├── release-growth.png
    ├── director-analysis.png
    └── final-insights.png
