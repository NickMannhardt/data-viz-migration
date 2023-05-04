# Interactive Data Visualiation & Society - Final Project
Zoe DeSimone, Natasha Hirt, Niklas Mannhardt


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

