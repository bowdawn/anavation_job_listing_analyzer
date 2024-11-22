import json
import os 
with open('./generated/job_listings_with_content.json', 'r') as file:
    json_data = json.load(file)
def analyze_job_data(data):
    analysis = {}
    analysis['total_jobs'] = len(data)
    teams = {}
    for job in data:
        team = job['team']
        if team not in teams:
            teams[team] = 0
        teams[team] += 1
    analysis['jobs_by_team'] = teams
    locations = {}
    for job in data:
        location = job['location']
        if location not in locations:
            locations[location] = 0
        locations[location] += 1
    analysis['jobs_by_location'] = locations
    work_types = {}
    for job in data:
        work_type = job['work_type']
        if work_type not in work_types:
            work_types[work_type] = 0
        work_types[work_type] += 1
    analysis['jobs_by_work_type'] = work_types
    return analysis
job_analysis = analyze_job_data(json_data)

directory_path = "./generated"
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

output_file = 'job_listings_analyze.json'
file_path = os.path.join(directory_path, output_file)
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(job_analysis, file, indent=4)
print(json.dumps(job_analysis, indent=4))