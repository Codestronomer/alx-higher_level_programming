#!/bin/bash
# bash script prints the size of a url
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
