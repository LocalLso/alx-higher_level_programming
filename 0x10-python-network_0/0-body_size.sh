#!/bin/bash
# Bash script that displays the body size.
curl -s "$1" | wc -c
