#!/bin/bash

# Read the URL from command-line argument
url="$1"

# Set the header variable
header="X-HolbertonSchool-User-Id: 98"

# Send a GET request using curl, include the custom header, and store the response in a variable
response=$(curl -s -H "$header" "$url")

# Display the body of the response
echo "$response"
