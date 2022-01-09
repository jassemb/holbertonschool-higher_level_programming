#!/bin/bash
# takes in a URL sends a request to it, and displays the size of the body
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
