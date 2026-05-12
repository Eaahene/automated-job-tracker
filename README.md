# Automated-job-tracker

This project is an automated ETL (Extract, Transform, Load) pipeline built in Python that collects job postings from multiple company job boards using the Ashby API and processes them into structured datasets.

The system supports both local and cloud-based data persistence by saving results to CSV files and synchronizing them with Google Sheets.

## 🚀 Features
-Extracts job listings from multiple APIs (Notion, OpenAI, Ashby, etc.)
-Transforms raw API data into structured format
-Assigns unique IDs and standardizes job fields
-Supports dual data storage:
-CSV file export (local storage)
-Google Sheets integration (cloud storage)
-Scheduled automation using Python scheduling
-Error handling for API failures and timeouts
-Modular ETL architecture (separation of extract, transform, load)

## 📊 Output
The pipeline generates structured job data including:
-Job title
-Company
-Location
-Remote status
-Employment type
-Application links
-Publication date

## 🛠️ Technologies
- Python
- Requests
- Pandas
- Google Sheets API
- gspread

## Setup

1. Clone repo
2. Install requirements
3. Add service-account.json
4. Run script

## Future Improvements
-Email notifications for new jobs
...