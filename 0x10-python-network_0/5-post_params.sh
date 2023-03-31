#!/bin/bash
# Takes in URL, sends POST request to the URL, and display the body response.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
