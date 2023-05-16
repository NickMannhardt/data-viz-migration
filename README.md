# Interactive Data Visualiation & Society - Final Project
Zoe De Simone, Natasha Hirt, Niklas Mannhardt

Check out our live site [here]( https://nickmannhardt.github.io/data-viz-migration/).

## Getting Started
After pulling from main, run
```
cd frontend
npm install
```
and
```
cd server/src
pip install -r requirements.txt
```

Then to start the development server for the backend run
```
cd server/src
python app.py
```

to start the development server for the frontend run
```
cd frontend
npm run dev --open
```

## To update the live website
```
cd frontend
npm run gh-pages
```
then switch to the branch `gh-pages` and add a file named `.nojekyll`. If you skip this then the page won't render the css correctly.


## To update the live API
Only Niklas can do this since it's tied to his google account.

```
cd server
gcloud builds submit --tag gcr.io/data-viz-adventure-team/flask-server 
gcloud run deploy --image gcr.io/data-viz-adventure-team/flask-server
```
