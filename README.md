# Netflix Movies & TV Shows — EDA & Power BI Dashboard

Data analysis project exploring Netflix Movies and TV Shows using Python, Pandas, and NumPy for data cleaning and Exploratory Data Analysis (EDA), followed by an interactive Power BI dashboard for visualization and insight generation.

---

## 📊 Project Overview

This project analyzes the Netflix Movies and TV Shows dataset to understand the characteristics and distribution of Netflix content.

Python was used for **data cleaning, preprocessing, feature engineering, and Exploratory Data Analysis (EDA)** using Pandas and NumPy.

The final processed dataset was then used to create an interactive **Power BI dashboard** covering content type, genres, ratings, countries, directors, movie durations, TV show seasons, and release trends.

---
    🧹 Data Cleaning & Preprocessing

The Netflix dataset was cleaned and prepared using Python, Pandas, and NumPy.

The major operations included:

Handling missing values
Replacing infinite and negative infinite values
Removing duplicate records
Converting date_added into datetime format
Handling missing director information
Handling missing cast information
Handling missing country information
Handling missing ratings
Handling missing duration values
⚙️ Feature Engineering

Additional features were created to support deeper analysis.

🎬 Movie Duration

Movie duration was extracted from the original duration column.

Movies were categorized into:

Short
Medium
Long
📺 TV Show Seasons

The number of seasons was extracted from the duration column for TV Shows.

TV Shows were categorized based on the number of seasons.

📅 Year-Based Analysis

Year-based features were used to analyze:

Content release trends
Netflix content additions over time
Movies vs TV Shows across different years
🔍 Exploratory Data Analysis

EDA was performed using Pandas and NumPy.

The analysis includes:

🎬 Content Analysis
Movies vs TV Shows
Content type distribution
Movie duration distribution
TV show season distribution
Content type by release year
⭐ Rating Analysis
Rating distribution
Rating by content type
Most common rating
Average movie duration by rating
🎭 Genre Analysis
Genre distribution
Most common genres
Genre distribution by content type
🌍 Country Analysis
Country-wise content distribution
Movies by country
TV Shows by country
Country distribution by content type
🎥 Director Analysis
Titles by director
Movies by director
TV Shows by director
Director distribution by content type
📅 Release & Growth Analysis
Titles by release year
Titles added by year
Titles added by year and content type
Release year by content type
📈 Power BI Dashboard

The processed Netflix dataset was used to create an interactive Power BI
dashboard consisting of 7 analytical pages.

1. 🎬 Netflix Overview

Provides a high-level overview of Netflix content using KPI cards and
visualizations.

Includes:
Total Titles
Total Movies
Total TV Shows
Total Countries
Movies vs TV Shows
Titles Added by Year
Rating Distribution
Titles by Release Year
Dashboard Preview

2. 📺 Content Analysis

Analyzes the structure and duration of Netflix Movies and TV Shows.

Includes:
Content Type by Release Year
Movie Duration Distribution
Movies by Duration Category
TV Shows by Number of Seasons
TV Shows by Release Year
Average Movie Duration
Average TV Show Seasons
Dashboard Preview

3. 🎭 Genre & Rating Analysis

Analyzes Netflix content based on genres, ratings, and content type.

Includes:
Genre by Content Type
Rating by Content Type
Average Movie Duration by Rating
Rating Distribution
Most Common Rating
Total Genres
Movie Percentage
Dashboard Preview

4. 🌍 Country Analysis

Analyzes the geographical distribution of Netflix content.

Includes:
Country Distribution
Country by Content Type
Movies by Country
TV Shows by Country
Total Countries
Average Countries per Title
TV Show Percentage
Dashboard Preview

5. 📅 Release & Growth Analysis

Analyzes Netflix content based on release years and content addition trends.

Includes:
Titles by Release Year
Titles Added by Year
Titles Added by Year & Type
Titles by Release Year & Type
Total Releases
Oldest Release Year
Latest Release Year
Highest Titles in a Year
Peak Release Year
Dashboard Preview

6. 🎥 Director Analysis

Analyzes Netflix content based on directors and their associated titles.

Includes:
Titles by Director
Director by Content Type
Movies by Director
TV Shows by Director
Total Directors
Highest Titles by Director
Average Titles per Director
Dashboard Preview

7. 💡 Final Insights

Summarizes the major findings from the complete Netflix analysis.

Includes:
Most Common Rating
Long Movies %
One Season TV Shows %
Most Common Release Year
Content Type Distribution
Genres by Titles
Titles Added by Year & Type
Countries by Titles
Dashboard Preview

📌 Key Insights

The dashboard provides an interactive way to explore:

Distribution of Movies and TV Shows
Most common content ratings
Popular Netflix genres
Country-wise content distribution
Movie duration patterns
TV show season patterns
Director-level content distribution
Netflix release trends
Netflix content addition trends
📂 Project Structure
Netflix-EDA-PowerBI-Dashboard/
│
├── README.md
├── Netflix_EDA.py
├── Netflix_final.csv
├── Netflix_titles.csv
│
├── overview.png
├── content-analysis.png
├── genre-rating.png
├── country-analysis.png
├── release-growth.png
├── director-analysis.png
└── final-insights.png
📁 Files Description

File	Description
Netflix_EDA.py	Python code for data cleaning, preprocessing, feature engineering, EDA, and insights
Netflix_titles.csv	Original Netflix dataset
Netflix_final.csv	Final cleaned and processed dataset
overview.png	Netflix Overview dashboard screenshot
content-analysis.png	Content Analysis dashboard screenshot
genre-rating.png	Genre & Rating Analysis dashboard screenshot
country-analysis.png	Country Analysis dashboard screenshot
release-growth.png	Release & Growth Analysis dashboard screenshot
director-analysis.png	Director Analysis dashboard screenshot
final-insights.png	Final Insights dashboard screenshot
