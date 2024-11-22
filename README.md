# AnaVation Job Content Extraction and Analysis with Resume Matching

This project is designed to scrape job listings, extract relevant job content, and analyze the data to find the best job matches based on the similarity to a resume. It uses Python, Selenium, BeautifulSoup, Term Frequency-Inverse Document Frequency, and Cosine Similarity to analyze the job descriptions.

## Project Workflow

1. **Extract HTML Content**  
   The first step is to extract the job listings from the company's career page (`anavationllc.com`) using Selenium. The page content is saved as an HTML file.

2. **Extract Job Data**  
   After saving the HTML, we use BeautifulSoup to parse the page and extract job listings. For each job, we fetch additional content from the job's dedicated page using Selenium.

3. **Analyze Job Listings**  
   Once we have all job details, we analyze the data, such as the total number of jobs, job counts by team, location, and work type. The analysis is saved into a JSON file.

4. **Resume Similarity Analysis**  
   We calculate the similarity between the job listings and a provided resume using `TfidfVectorizer` and `cosine_similarity`. The top 5 jobs most similar to the resume are identified and outputted.

## Requirements

- Python 3.x
- `selenium` for web scraping
- `beautifulsoup4` for HTML parsing
- `sklearn` for text vectorization and similarity computation
- `tqdm` for progress bar
- Chrome WebDriver for Selenium (Make sure you have the correct version of ChromeDriver installed)

## Installation
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
    
## How to Use

1. Run the script to start the process:

    ```bash
    python main.py
    ```

2.  The script will:

   - Extract HTML content from the career page.
   - Parse job listings and extract detailed information.
   - Perform a similarity comparison between job listings and the provided resume.
   - Output the top 5 job matches based on similarity.

3. View the results:
  - The extracted job listings are saved in `./generated/job_listings_with_content.json`.
  - Job analysis data (team, location, work type) is saved in `./generated/job_listings_analyze.json`.
  - The top 5 job matches based on the resume similarity are saved in `./generated/similarity_to_resume.txt`.




