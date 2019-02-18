## To run, heroku app

## Step 1: convert excel file into database.db
python prepare_data.py

## Step 2: run application locally to ensure the website works
python app.py

## Step 3: Deploy to Heroku
git add .
git commit . -m ""
git push heroku master
