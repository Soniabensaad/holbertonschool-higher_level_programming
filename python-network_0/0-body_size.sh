#!/bin/bash

# Read the URL from command-line argument
url="$1"

# Send a request using curl and store the response in a variable
response=$(curl -sI "$url")

# Extract the Content-Length header from the response headers
content_length=$(echo "$response" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r')

# Display the size of the body in bytes
echo "Size of the response body: $content_length bytes"
