# Module Imports
import pandas as pd
import schedule, time
from fetch_jobs import run_etl


all_jobs = run_etl()
def save_csv(all_jobs):

    # saving all postings in a CSV file
    df = pd.DataFrame(all_jobs)
    df.to_csv("Jobs.csv",index=False)
    print("csv file saved successfully")

save_csv(all_jobs)

# Automatic refresh  
# schedule.every().sunday.at("00:00").do(save_csv)

# while True:
#     schedule.run_pending()
#     time.sleep(60)


