# Gravity Falls Code Checker

## Overview
This is a Python script designed to check potential codes related to the *Gravity Falls* quests. The script submits these codes to a specific URL and logs the results to determine if they are valid. It’s particularly useful for fans or developers exploring interactive aspects of *Gravity Falls* content or similar projects.

## Features
- **Load Codes from a File**: The script reads potential codes from a `possible_codes.txt` file, skipping comments and blank lines.
- **Code Validation**: Each code is submitted to a designated URL to check its validity. The script handles different HTTP response statuses and logs the outcome of each code (e.g., valid, not found, rate limited).
- **Logging**: Results are logged into a `code_results.log` file, including timestamps and the status of each code checked.

## How It Works
1. **Code Loading**: The script reads potential codes from `possible_codes.txt`. It skips lines that are blank or start with a `#`, treating them as comments.
2. **HTTP Request**: For each code, an HTTP POST request is made to the specified URL.
3. **Response Handling**: The script handles different HTTP responses:
   - `200 OK`: The code is valid.
   - `404 Not Found`: The code is not recognized.
   - `429 Too Many Requests`: The server has rate-limited the request; the script will wait and retry.
   - Other statuses are logged as unexpected.
4. **Result Logging**: The outcome of each code check is logged in `code_results.log`.

`https://codes.thisisnotawebsitedotcom.com/`

## Example `possible_codes.txt`
```plaintext
# Main Characters
DIPPER
Mabel
Stan
Soos

# Supporting Characters
Ford
Bill
Pacifica
````

## Side note
I've found when running the code, once it gets to Stan it returns a lot more info then what is displayed on the site, enjoy ;)