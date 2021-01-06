# Intro

Hi, due to Corona virus, I like many other people had too much free time. I spent my time catching up on anime. After taking a class on Machine Learning I thought I would combine my two passions together, anime and computer science. 

# About

This app is meant to give other anime lovers recommendations on what to watch based on their favorite anime. So a user would input an anime title that they liked in a search bar and press enter. Afterwards the application would display a gallery of other anime titles that the user might like. This applications uses a React/Flask stack. Im using React to make a stylish frontend while I am using Flask to handle the data science part of the application. 

# Running the Application

## Frontend

`cd` into the `frontend` directory and run the following to install all the packages needed for the project:

```bash
npm i
```

Afterwards all you have to do is run:

```bash
npm start
```

You can now view the app on `http://localhost:3000`

## Backend

`cd` into the `backend` directory and run the following:

```bash
pipenv shell
```

Afterwards run the following command to install the dependacies:

```bash
pipenv install --dev
```

Finally you can run the following to start up the Flask server:

```bash
export FLASK_APP=autoapp.py
flask run
```

# Sources

Before coding out the recommendation part for Flask, I decided to test out some code in `simple.ipynb` with this tutorial, https://www.kaggle.com/astandrik/simple-anime-recommendation-system-content-based/notebook?select=anime.csv.

I used that tutorial to write the recommendation feature of the app.
