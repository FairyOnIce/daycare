## To run, heroku app

## Step 0:
 - modify data/Daycare.xls if necessary
 - modify My Map in google map accordingly
   - change main.html iframe line with the link from "Embeded on mysite"

## Step 1: convert excel file into database.db
python prepare_data.py

## Step 2: run application locally to ensure the website works
python app.py

## Step 3: Deploy to Heroku
git add .
git commit . -m ""
git push
git push heroku master
