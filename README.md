# GitHub OSINT Repository Scraper

![GitHub Repo](https://img.shields.io/github/stars/Nxrnoob/GitHub-OSINT-Repository-Scraper?style=social)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

A powerful OSINT (Open-Source Intelligence) tool that scrapes GitHub repositories based on specific AI/ML-related keywords. It sorts repositories by popularity (stars), filters them by programming language, and allows you to interactively browse and open repositories in your web browser—all from your terminal.

---

## Features

- **GitHub API Integration:** Fetches repositories using GitHub's API.
- **CSV Data Export:** Saves raw data in `github_repos.csv` and cleans it in `github_repos_cleaned.csv`.
- **Language Categorization:** Groups repositories by programming language. Repositories with no language specified are automatically classified under "Miscellaneous."
- **Interactive Menu:** Browse repositories by selecting a programming language, view the list of repositories, and open any repository directly in your browser.
- **OSINT Research:** Perfect for researchers and tech scouts looking to analyze trends in AI/ML projects on GitHub.

---

## Installation

### 1. Clone the Repository

Open your terminal and run:
```bash
git clone https://github.com/Nxrnoob/GitHub-OSINT-Repository-Scraper.git
cd GitHub-OSINT-Repository-Scraper

### 2. Create a Virtual Environment (Recommended)
