#!/bin/bash
# Sends a request to a URL, and displays only the status code of the response.
#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -o /dev/null -s -w "%{http_code}\n" "$1"
