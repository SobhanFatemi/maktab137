#!/bin/bash

LOG_DIR="/media/mushroomyumi/Mushroom/Python/maktab137/week11/hw"
BACKUP_DIR="/media/mushroomyumi/Mushroom/Python/maktab137/week11/hw/backup"
REPORT_FILE="/media/mushroomyumi/Mushroom/Python/maktab137/week11/hw/report.txt"
PYTHON_TOOL="/media/mushroomyumi/Mushroom/Python/maktab137/week11/hw/logmaster.py"
LOG_FILE="access.log"

mkdir -p "$BACKUP_DIR"

DATE=$(date +"%Y-%m-%d")
cp "$LOG_DIR/$LOG_FILE" "$BACKUP_DIR/${LOG_FILE}_$DATE"

find "$BACKUP_DIR" -type f -name "${LOG_FILE}_*" -mtime +7 -exec gzip {} \;

python3 "$PYTHON_TOOL" scan --file "$LOG_DIR/$LOG_FILE" --errors --export "$REPORT_FILE"

USAGE=$(df "$LOG_DIR" | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$USAGE" -ge 90 ]; then
    echo "WARNING: Low disk space ($USAGE%)"
fi
