#!/bin/bash

ORIGINAL_BRANCH=$(git branch | grep '\* ' | sed 's/\* //');

# git config user.email niklas.manhardt@gmail.com

# switch to gh-pages branch
git checkout gh-pages;

# create and push .nojekyll
# touch .nojeykyll
# git add .nojekyll
# git commit -m "auto-commit add .nojekyll"
# git push origin gh-pages

# # switch to original branch
# git checkout $ORIGINAL_BRANCH