#!/usr/bin/bash
# Bash script that displays the body size.
curl -sI "$1" | wc -c
