# Overview

This software analyzes a free dataset of international soccer match results using Python and Pandas.

The dataset includes international men's soccer match results, including the teams, scores, dates, tournaments, and locations. I got the dataset from the International Football Results repository and it is also available on Kaggle.

International Football Results Dataset:
https://github.com/martj42/international_results

Kaggle Dataset:
https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017

The purpose of this software is to practice working with real-world data and using Python to find useful information from it. The program uses Pandas to organize, filter, sort, and analyze the data.

The program also creates a bar graph showing the teams with the most total goals as a stretch challenge.

[Software Demo Video](https://youtu.be/48BvPc5Mtxw)

# Data Analysis Results

### Question 1: Which teams have scored the most goals in the dataset?

The teams with the most total goals were:

1. England - 2,401 goals
2. Germany - 2,331 goals
3. Brazil - 2,315 goals
4. Sweden - 2,178 goals
5. Argentina - 2,047 goals
6. Hungary - 2,011 goals
7. Netherlands - 1,852 goals
8. South Korea - 1,794 goals
9. Mexico - 1,777 goals
10. France - 1,735 goals

The program answered this question by combining the home and away results for each team, grouping the data by team, adding up the goals scored, and sorting the results from highest to lowest.

### Question 2: Which teams have the highest average goals per match among teams with at least 100 matches?

The teams with the highest average goals per match were:

1. Jersey - 2.74 goals per match
2. Tahiti - 2.71 goals per match
3. New Caledonia - 2.63 goals per match
4. Guernsey - 2.57 goals per match
5. Fiji - 2.27 goals per match
6. Germany - 2.25 goals per match
7. England - 2.19 goals per match
8. Brazil - 2.18 goals per match
9. Papua New Guinea - 2.17 goals per match
10. Solomon Islands - 2.16 goals per match

For this question, the program first filtered out teams with fewer than 100 matches. It then calculated the average goals per match and sorted the results from highest to lowest.

# Development Environment

I used the following tools to make this software:

- Visual Studio Code
- Python
- Pandas
- Matplotlib
- Git and GitHub

The programming language used for this project is Python. Pandas was used to load, clean, filter, sort, and analyze the dataset. Matplotlib was used to create the graph.

# Useful Websites

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas 10 Minute Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [International Football Results Dataset](https://github.com/martj42/international_results)
- [Kaggle International Football Results Dataset](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017)

# Future Work

- Add more questions about the soccer data.
- Add more graphs to compare teams and statistics.
- Add more options for analyzing the data.