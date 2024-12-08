#!/bin/bash

echo "setting up..."

dir="day$1"
mkdir "$dir"
cp boilerplate.py "$dir"/main.py
chmod a+x "$dir"/main.py
touch "$dir"/input.txt "$dir"/example.txt

echo "setup complete for $dir"
