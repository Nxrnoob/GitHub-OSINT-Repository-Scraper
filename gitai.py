import requests
import csv
import time
import webbrowser
from collections import defaultdict

GITHUB_API_KEY = "YOUR_GITHUB_API_KEY"
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_API_KEY}"
}

QUERY = "artificial intelligence OR machine learning OR AI projects"
PER_PAGE = 100
MAX_PAGES = 10  # Adjust as needed

def fetch_github_repos():
    all_repos = []
    for page in range(1, MAX_PAGES + 1):
        url = f"https://api.github.com/search/repositories?q={QUERY}&sort=stars&order=desc&per_page={PER_PAGE}&page={page}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            all_repos.extend(data.get("items", []))
        else:
            print(f"Failed to fetch page {page}: {response.status_code}")
        time.sleep(2)  # To avoid rate limits
    return all_repos

def save_to_csv(repos, filename="github_repos.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "URL", "Description", "Stars", "Forks", "Language"])
        for repo in repos:
            writer.writerow([
                repo["name"],
                repo["html_url"],
                repo.get("description", "N/A"),
                repo["stargazers_count"],
                repo["forks_count"],
                repo.get("language", "Miscellaneous")
            ])

def clean_csv(input_file="github_repos.csv", output_file="github_repos_cleaned.csv"):
    cleaned_data = []
    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[2] != "N/A":  # Filter out repos with no description
                cleaned_data.append(row)

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(cleaned_data)

def browse_repos_by_language(csv_file="github_repos_cleaned.csv"):
    lang_dict = defaultdict(list)
    
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            lang = row[5] if row[5] else "Miscellaneous"
            lang_dict[lang].append((row[0], row[1]))
    
    lang_list = list(lang_dict.items())
    
    while True:
        print("\nSelect a programming language to browse repositories (0 to exit):")
        for idx, (lang, repos) in enumerate(lang_list, 1):
            print(f"{idx}. {lang}: {len(repos)} repos")
        
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 0:
                print("Thanks for using this OSINT tool! Goodbye!")
                break
            elif 1 <= choice <= len(lang_list):
                selected_lang, repos = lang_list[choice - 1]
                print(f"\nRepositories for {selected_lang}:")
                for idx, (name, url) in enumerate(repos, 1):
                    print(f"{idx}. {name} - {url}")
                open_repo = input("\nEnter repo number to open in browser (0 to return): ")
                if open_repo.isdigit():
                    open_repo = int(open_repo)
                    if 1 <= open_repo <= len(repos):
                        webbrowser.open(repos[open_repo - 1][1])
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Fetching GitHub repositories...")
    repos = fetch_github_repos()
    print(f"Fetched {len(repos)} repositories.")
    save_to_csv(repos)
    print("Saved raw data to github_repos.csv.")
    clean_csv()
    print("Cleaned data saved to github_repos_cleaned.csv.")
    browse_repos_by_language()

if __name__ == "__main__":
    main()

