#!/bin/bash

function create() {
    cd  ~/developments/Python/Github_Automation/
    python3 create.py $1 $2
    cd ~/developments/$2/$1
    git init
    git remote add origin https://github.com/koki1610168/$1.git
    touch README.md
    git add .
    git commit -m "Initial Commit"
    git push -u origin master
    code .
}