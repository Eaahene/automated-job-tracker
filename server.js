import express from 'express';
import cors from 'cors';
import fetch from 'node-fetch';


const app = express();

app.use(cors());
app.use(express.json());

app.get('/',(req,res)=>{
    res.send("hello world")
});


app.post('/jobs', async (req,res)=>{
    const { boards } = req.body;
    let job_info = {}

    // fetch jobs
    
    const fetchPromise = boards.map(async (board) => {
        console.log(`Fetching jobs from ${board}...`);
        const url = `https://api.ashbyhq.com/posting-api/job-board/${board}?includeCompensation=true`;
         
        let response =  await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
            });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
            // pushing the specific jobs into the job_info 
        if (data.jobs && data.jobs.length > 0) {
            job_info[board] = data.jobs.map(job => ({
                title: job.title,
                description: job.description,
                compensation: job.compensation,
                location: job.location,
                job_url: job.jobUrl,
                company: board,
                application_url: job.applyUrl,
                isRemote: job.isRemote,
                datePosted: job.publishedAt,
                employmentType: job.employmentType,
                workplaceType: job.workplaceType,
                }));
            }
        
    })
    // wait for all api requests to finish completely first
    await Promise.all(fetchPromise)

    console.info(job_info)

    
     res.json({message:"Jobs fetched successfully", job_info: job_info});
        });


app.listen(3000, ()=>{
    console.log('server run success on http://localhost:3000')
});


