# Dashboard Quotes & News

A simple Python script that displays the current date, a random motivational quote, and fetches the latest news headline using the NewsAPI.

## Features

- Prints the current date with a nicely formatted day suffix (e.g., 21st, 3rd).
- Shows a random motivational quote from a predefined list.
- Fetches and displays a random top headline from the US via NewsAPI.
- Logs activity and output in a timestamped log file.
- Prints the current working directory.

## Setup

1. Clone this repository.
2. Install dependencies:

   ```
   pip install requests
   ```

3. Obtain a free API key from [NewsAPI](https://newsapi.org/).
4. Replace the `API_KEY` value in the script with your own key.
5. Run the script:

   ```
   python dashboard.py
   ```

## Notes

- Make sure you have internet connectivity for the news API call.
- The script creates a log file with a timestamp on each run.