#!/bin/bash
cd "/Users/manpreetsingh/Desktop/PRIVATE GIT/daily-scrappers-update"
source .venv/bin/activate
python main.py >> logs/scraper.log 2>&1
