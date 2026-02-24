# 🛠️ Vibe Coding Prompts: Utility Scripts

> Copy-paste these prompts into your AI-Native IDE to automate boring tasks
> and build powerful CLI tools — all with natural language!

---

## 📁 File Management

### Batch Rename Files

```
Write a Python script that batch renames files in a given directory:

1. Accept command-line arguments: directory path, rename pattern
2. Support patterns like:
   - Add prefix: "photo_" + original name
   - Add date: "2025-01-01_" + original name
   - Sequential numbering: "001_", "002_", etc.
   - Replace text in filenames
3. Show a preview of changes BEFORE applying (dry-run mode)
4. Ask for confirmation before renaming
5. Add a --undo flag that can revert the last rename operation
6. Handle edge cases: duplicate names, special characters

Use only standard library modules. Add colorful terminal output.
```

### Duplicate File Finder

```
Create a Python script that finds and manages duplicate files:

1. Scan a given directory recursively
2. Use file hash (MD5) to identify exact duplicates
3. Show results grouped by duplicate sets
4. Display: file name, size, path, last modified date
5. Interactive mode: ask which copy to keep for each duplicate set
6. Add a --dry-run flag to just report without deleting
7. Show total space that would be freed
8. Export report to CSV

Use only standard library modules. Show a progress bar during scanning.
```

---

## 📊 Data Processing

### CSV Data Cleaner

```
Build a Python CLI tool that cleans messy CSV files:

1. Accept input CSV and output path as arguments
2. Auto-detect encoding (UTF-8, GBK, Latin-1, etc.)
3. Cleaning operations:
   - Remove completely empty rows/columns
   - Trim whitespace from all cells
   - Standardize date formats (detect and convert to YYYY-MM-DD)
   - Remove duplicate rows
   - Fix common encoding issues (mojibake)
4. Show a summary report: rows before/after, columns cleaned, issues found
5. Support --preview flag to show first 10 rows of cleaned data

Use pandas if available, fall back to csv module if not.
```

### Excel Report Generator

```
Write a Python script that generates a formatted Excel report:

1. Read data from a CSV file
2. Create an Excel file with:
   - A summary sheet with key statistics
   - A data sheet with the raw data, auto-filtered
   - A chart sheet with a bar chart of the top 10 items
3. Apply formatting:
   - Bold headers with colored background
   - Alternating row colors
   - Number formatting (thousands separator, 2 decimal places)
   - Auto-adjusted column widths
4. Add a company logo placeholder in the header
5. Accept CSV path as command-line argument

Use openpyxl. Install it automatically if not present.
```

---

## 🌐 Web Scraping

### News Headline Aggregator

```
Build a Python script that aggregates top news headlines:

1. Scrape headlines from 3 major tech news RSS feeds:
   - Hacker News (top stories API)
   - TechCrunch RSS
   - The Verge RSS
2. For each article, extract: title, source, URL, published date
3. Output options:
   - Pretty-print in terminal with colors
   - Export to Markdown file
   - Export to JSON
4. Add --category flag to filter by keyword
5. Cache results to avoid repeated requests (expire after 1 hour)
6. Handle network errors gracefully

Use requests + feedparser. Show a loading spinner while fetching.
```

---

## ⏰ Automation

### Daily Standup Report Generator

```
Create a Python script that auto-generates a daily standup report:

1. Scan git log for today's commits (in the current repository)
2. Group commits by type (feat, fix, refactor, docs, etc.)
3. Generate a formatted report with:
   - What I did yesterday (previous workday's commits)
   - What I'm doing today (based on open branches and recent files)
   - Blockers (any failed CI runs or unresolved TODOs)
4. Output as Markdown, ready to paste into Slack/Teams
5. Optionally copy to clipboard automatically
6. Support --days flag to look back N days

Use gitpython or subprocess for git operations.
```

---

## 💡 Tips for Utility Script Prompts

| Tip                        | Example                                               |
| -------------------------- | ----------------------------------------------------- |
| **Specify the interface**  | "Accept command-line arguments" or "Interactive menu" |
| **Ask for error handling** | "Handle network errors gracefully"                    |
| **Request a dry-run mode** | Prevents accidental data loss                         |
| **Ask for colored output** | Makes terminal tools feel professional                |
| **Mention dependencies**   | "Use only standard library" or "Use pandas"           |

---

<p align="center">
  📚 Learn the full Vibe Coding methodology at <a href="https://www.hoppypy.com/en/learn/python-vibe/01-choose-your-weapon">HoppyPy</a>
</p>
