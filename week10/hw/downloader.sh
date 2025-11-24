#!/usr/bin/env bash

read -p "Enter your URL: " USER_INPUT

OUTPUT_FILE="log.txt"

echo "$USER_INPUT" >> "$OUTPUT_FILE"

echo "Your input has been saved to $OUTPUT_FILE"





