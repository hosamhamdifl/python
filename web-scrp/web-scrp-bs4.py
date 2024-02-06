from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


unfamiliar_skill=input('Put skill that you are familiar with> ')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
    job_data = []  # Create an empty list to store job information
    html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
    soup=BeautifulSoup(html_text,'lxml')
    # jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    # with open (f'web-scrp/posts/jobs.txt','+w') as f:
    for index,job in enumerate(jobs):
        post_date=job.find('span',class_='sim-posted').span.text
        if 'few' in post_date:
            company_name=job.find('h3',class_="joblist-comp-name").text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(" ",'')
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                     job_data.append({
                    "Job Number": index + 1,
                    "Company Name": company_name,
                    "Required Skills": skills,
                    "More Info": more_info
                })
     # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(job_data)
    # Handle empty DataFrame gracefully
    if df.empty:
        print("No jobs found matching your criteria.")
        return
    # Write the DataFrame to an Excel file with formatting
    df.to_excel("web-scrp/posts/timesjobs_python_jobs.xlsx", index=False)
    print(f"Successfully saved job data to timesjobs_python_jobs.xlsx!")
                        
                        # f.write(f'company name : {company_name.strip()} \n') 
                        # f.write(f'required skills : {skills.strip()} \n') 
                        # f.write(f'more info : {more_info.strip()} \n') 
                        # print(f"file saved successfully : {index}")
                        
        #             print(
        #                 f'''company name : {company_name.strip()}
        # required skills: {skills.strip()}
        # more info : {more_info}''')
    # print(html_text)
if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
        