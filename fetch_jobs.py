import requests
import schedule, time, datetime

# Companies to take the Job posting from
companies = ["notion", "openai", "Ashby"]

def extract_data_from_source():
    job_data = []
    for job_board in companies:

        # Ashby job posting API
        print(f"Fetching Jobs from {job_board}")
        url = f"https://api.ashbyhq.com/posting-api/job-board/{job_board}?includeCompensation=true"
        
        response = requests.get(url) 
        
        #Catching errors which might happen
        if response.status_code != 200:
            print(f"Failed to fetch job posting from {job_board}")
            continue
        
        data = response.json()

        job_data.append(
            {
                "company": job_board,
                "jobs": data["jobs"]
            })

    return job_data


def data_transform(data):
    all_jobs = []
    job_id = 0
    
    for company_data in data:
        company = company_data["company"]
        jobs = company_data["jobs"]

        for job in jobs:
            
            all_jobs.append(
                {
                    "id" : job_id,
                    "Company": company,
                    "Position": job["title"],
                    "location": job["location"],
                    "isRemote": job["isRemote"],
                    "datePublished": job["publishedAt"],
                    "employmentType": job["employmentType"],
                    "jobSite": job["jobUrl"],
                    "applyLink": job["applyUrl"]
                }
            )  
            job_id +=1
    
    return all_jobs

def run_etl():
    data = extract_data_from_source()

    transform_data = data_transform(data)

    return transform_data

