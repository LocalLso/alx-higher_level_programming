#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body response.
curl -sH "X-School-User-Id: 98" "$1"
