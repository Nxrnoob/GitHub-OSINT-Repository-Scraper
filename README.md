# GitHub-OSINT-Repository-Scraper

A powerful OSINT (Open-Source Intelligence) tool to scrape GitHub repositories based on specific keywords, sort them by stars, and filter them by programming language. This tool allows easy exploration of top repositories and opens them in a browser directly from the terminal.

Features

    Fetches repositories using GitHub API v3.
    Filters repositories based on programming languages.
    Sorts results by stars for most popular projects.
    Saves cleaned data into CSV format.
    Interactive menu-based navigation to browse repositories.
    Opens repository links directly in a browser.
    Can be used for OSINT research, tech scouting, and data collection.
Installation
1. Clone the Repository

    git clone https://github.com/Nxrnoob/GitHub-OSINT-Repository-Scraper.git
    cd GitHub-OSINT-Repository-Scraper

2. Create a Virtual Environment (Optional but Recommended)

    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies
    pip install -r requirements.txt

4. Configure Your GitHub API Key
  Open gitai.py and replace "YOUR_GITHUB_API_KEY" with your actual API key.
  Get a GitHub API key from: GitHub Developer Settings
Usage
  Run the Script
    python gitai.py

What Happens Next?

    Fetches repositories matching your search query.
    Stores data in github_repos.csv and github_repos_cleaned.csv.
    Displays programming languages with repo counts.
    Lets you browse repositories by selecting a language.
    Opens the selected repository in a browser.

Example Workflow
    Fetching GitHub repositories...
Fetched 1000 repositories.
Saved raw data to github_repos.csv.
Cleaned data saved to github_repos_cleaned.csv.

Select a programming language to browse repositories (0 to exit):
1. Python: 120 repos
2. JavaScript: 85 repos
3. C++: 45 repos
4. Go: 20 repos
Enter your choice (0 to exit): 1  # Select Python

After selecting Python, it will show a list of repositories with numbers.
Enter a number, and the repository opens in the browser.

Example CSV Output
Name	URL	Description	Stars	Forks	Language
TensorFlow	Repo	Open-source ML library	170000	87000	Python
PyTorch	Repo	Deep learning framework	120000	64000	Python
Scikit-Learn	Repo	ML for Python	55000	25000	Python

Contributions

Feel free to fork, improve, and submit a pull request.
For any issues, report them here: GitHub Issues
