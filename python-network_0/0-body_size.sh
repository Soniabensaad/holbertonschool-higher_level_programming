#!/bin/bash
# Read the URL from command-line argument
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
