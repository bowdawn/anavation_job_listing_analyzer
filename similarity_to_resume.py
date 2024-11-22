from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

with open('./generated/job_listings_with_content.json', 'r') as file:
    job_listings = json.load(file)
resume_content = """Bogdan Oleinikov 
Manassas, VA | +1-571-664-8532 
 boleinikov@gmail.com |  linkedin.com/in/boleinikov |  github.com/bowdawn 
Software Engineer 
A proficient Software Engineer with a strong track record in full stack development and system automation, 
leveraging in-depth knowledge and hands-on experience to drive technological advancements and enhance 
operational efficiency. With a passion for implementing innovative solutions, successfully led multiple projects 
that align with business objectives and improve user experiences. Educational background includes a Master's 
Degree in Computer Science from Georgia Tech and a Bachelor's Degree in Computer Science from Stony 
Brook University. Known for the ability to collaborate across teams and communicate complex technical 
concepts clearly, ensuring that technical strategies are accessible and actionable for stakeholders at all levels. 
Education 
Georgia Institute of Technology                                                                                                  Atlanta, Georgia 
M.S. Computer Science                                                                                                  2020 - 2022 
● GPA: 3.80/4.0 
Stony Brook University                                                                                                   Stony Brook, New York 
B.S. Computer Science                                                                                                  2015 - 2019 
● GPA: 3.49/4.0 
Experience                                                                                                    
Lead Software Engineer at Korean Silver Exchange, Namyangju, South Korea Feb 2023 - Dec 2023 
Implemented an automated hourly product pricing system, ensuring accuracy and efficiency in pricing updates. 
Managed and analyzed financial data to support strategic decision-making processes. Additionally, improved 
user experience satisfaction by enhancing interface designs, contributing to better customer engagement and 
operational efficiency. 
Full Stack Software Engineer at Riupack, Seoul, South Korea Aug 2022 - Feb 2023 
Worked on the POJANGPOSS project, developing a React-based shopping mall and admin pages, and creating 
mobile apps with React Native. Utilized Python, Apollo, Django, GraphQL, and the Saleor API for backend 
development, integrating secure and efficient APIs to support front-end functionalities. Collaborated with 
cross-functional teams to align technical implementations with business goals, contributing to the successful 
launch of POJANGPOSS, which facilitated the procurement of customized packaging for small and medium-
sized enterprise., helping them compete with larger companies. 
Full Stack Software Engineer at Jinjoosoft,  Seoul, South Korea  Oct 2019 - Oct 2020 
Contributed to the development of the RUMY project, a hotel collaboration tool that significantly enhanced 
operational efficiency for hotels. Worked extensively with Angular, React, and Vue for web development, 
developed mobile applications using React Native, and utilized Netcore, Docker, and Express for backend 
development. Supported the successful launch and adoption of RUMY, which improved communication and 
task management across 270 hotels. 
Certifications 
Oracle Professional Certification | Java SE 8 Programmer   July 2018 
Verified understanding of Concurrency, Fork - Join Framework, Functional Interfaces, JDBC, Java Design 
Patterns, Java NIO.2 API, Localization, Regular Expressions, Parallel Streams and Stream API. 
Oracle Associate Certification | Java SE 8 Programmer  June 2018 
Verified understanding of Java, JDK 8, Java SE 8, Lambda Expressions, Java Application Development, and 
Java 8 Date & Time API. 
Technical Skills 
Languages: JavaScript, TypeScript, C/C++, Java, Python 
Web Development: Node.js, React, Angular, Vue 
Database: PostgreSQL, MongoDB 
Machine Learning and Data Science: TensorFlow, PyTorch, Pandas, NumPy 
Frameworks and Libraries: Express, Spring, SpringBoot, Django, GraphQL, Netcore, Docker 
Languages 
English (Native / US Citizen) Russian (Fluent / Heritage Speaker) Korean (Fluent / 8 years +) 
"""


documents = [resume_content] + [job['content'] for job in job_listings]
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)
cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
similarity_scores = cosine_sim.flatten()
sorted_indexes = similarity_scores.argsort()[::-1]
top_5_jobs = [(job_listings[i], similarity_scores[i]) for i in sorted_indexes[:5]]
results = []
output_content = "Top 5 Job Matches:\n"
for rank, (job, score) in enumerate(top_5_jobs, start=1):
    job_details = {
        'rank': rank,
        'title': job['title'],
        'similarity_score': score
    }
    for key, value in job.items():
        if key != 'content':  
            job_details[key] = value
    
    results.append(job_details)
    output_content += f"{rank}. Job Title: {job['title']} - Similarity Score: {score:.4f}\n"
    for key, value in job_details.items():
        if key not in ['title', 'similarity_score']:  
            output_content += f"   {key.capitalize()}: {value}\n"
    output_content += "-" * 80 + "\n"  
print(output_content)
directory_path = "./generated"
if not os.path.exists(directory_path):
    os.makedirs(directory_path)
output_file = 'similarity_to_resume.txt'
file_path = os.path.join(directory_path, output_file)
with open(file_path, "w", encoding="utf-8") as file:
    file.write(output_content)
print(f"Data has been successfully extracted and saved to {output_file}")