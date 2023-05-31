#!/bin/bash
# Read the URL from command-line argument
curl -s -v "$1" --stderr - | grep Content-Length: | cut -d' '  -f 3
