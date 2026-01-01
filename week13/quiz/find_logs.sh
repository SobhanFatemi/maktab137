#!/bin/bash
LOG_DIR="/media/mushroomyumi/Mushroom/Python/maktab137/week13/quiz"
OUTPUT_FILE="all_logs.txt"
> "$OUTPUT_FILE"
find "$LOG_DIR" -type f -name "*.log" -exec cat {} + >> "$OUTPUT_FILE"
echo "All log files have been added into $OUTPUT_FILE"
