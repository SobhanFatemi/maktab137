#!/bin/bash

cd "$(dirname "$0")/.."

export PYTHONPATH=$(pwd)

LOG_FILE="test/test_results_$(date +%Y-%m-%d).log"

echo "---------- Run started at $(date +"%Y-%m-%d %H:%M:%S") ----------" >> $LOG_FILE

./venv/bin/coverage run --source=logmaster -m unittest test.test_logmaster >> $LOG_FILE 2>&1

echo "---------------- End of Run ----------------" >> $LOG_FILE
echo "" >> $LOG_FILE
