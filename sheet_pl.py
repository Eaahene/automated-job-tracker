# Module Imports
import gspread
from google.oauth2.service_account import Credentials
from fetch_jobs import run_etl

#setting up google sheets

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credential = Credentials.from_service_account_file(
    "service_account.json",
    scopes = scope
)

client = gspread.authorize(credential)
sheet =client.open("Joblisting").sheet1

all_jobs = run_etl()

# the job aggregator
def save_sheets(all_jobs):
    

    sheet.clear()
    rows = []
    headers = [[
        "ID","Company", "Position", "Location",
        "isRemote", "Date Published", "Type",
        "Job Site", "Apply Link"
    ]]

    for job in all_jobs:
        rows.append([
            job["id"],
            job["Company"],
            job["Position"],
            job["location"],
            job["isRemote"],
            job["datePublished"],
            job["employmentType"],
            job["jobSite"],
            job["applyLink"]
        ])
    
    # saving to google sheets
    sheet.update(range_name="A1:I1",values=headers)
    sheet.append_rows(rows)
    print("Google Sheet updated successfully")
    

save_sheets(all_jobs)


# Automatic refresh  
# schedule.every().sunday.at("00:00").do(job_aggregator)

# while True:
#     schedule.run_pending()
#     time.sleep(60)


