# Username_BruteForce_Enumeration


## Description

This script is designed to identify registered usernames on a login page by brute-forcing with a given wordlist. It sends HTTP POST requests to the target login page and checks if the response contains indicators of a valid username (e.g., "Wrong password").

## Features

- Uses multiprocessing for faster execution.
- Reads a wordlist from a file and processes it in parallel.
- Detects valid usernames based on response messages.
- Can be customized with different target URLs and wordlists.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/JoshuaFerando/Username_BruteForce_Enumeration
   cd Username_BruteForce_Enumeration
   ```

## Usage

1. Modify the script to set the target login URL (`http://login.php`) and the correct wordlist path.
2. Run the script:
   ```bash
   python brute_force_login_page_php_for_username.py
   ```

## Disclaimer

This script is intended for educational and ethical penetration testing purposes only. Unauthorized usage against systems you do not own or have explicit permission to test is illegal.

## Contribution

Pull requests are welcome! Feel free to improve the script by optimizing performance or adding new features.

## Author

Your Name Joshua Fernando

Password Brute Force on PHP Login Page
======================================

🛠️ Description
--------------
This script attempts to brute-force login credentials by testing a known username against a list of possible passwords. It is designed to work with PHP-based login pages by sending repeated POST requests and analyzing responses for signs of successful login.

🚀 Features
-----------
- Fast execution using multiprocessing
- Uses a password wordlist to test combinations
- Identifies successful logins by checking specific response patterns
- Easily customizable for different target URLs, parameters, and success indicators

📦 Requirements
---------------
- Python 3.x
- requests library

Install the required dependencies:
    pip install requests

📥 Installation
---------------
    git clone https://github.com/JoshuaFerando/Username_BruteForce_Enumeration
    cd Username_BruteForce_Enumeration

▶️ Usage
--------
1. Edit the script to set:
   - TARGET_URL → The login page (e.g., http://example.com/login.php)
   - USERNAME → The known or discovered username
   - PASSWORD_LIST → Path to the file containing passwords
   - SUCCESS_INDICATOR → Text in the response indicating a successful login

2. Run the script:
    python brute_force_login_page_php_for_password.py

Example output:
    [+] Trying: admin : 123456
    [+] Trying: admin : letmein
    [✔] Password found: admin : password123

⚠️ Disclaimer
-------------
This tool is meant for educational and authorized security testing only.
Do not use this against systems you do not own or have permission to test.
Unauthorized usage is a criminal offense and against ethical hacking principles.

🤝 Contributing
---------------
Feel free to open issues or submit pull requests for:
- New features (e.g., proxy support, rate-limiting)
- Code optimization
- Custom response logic (for sites using tokens, cookies, or redirects)

👤 Author
---------
Joshua Fernando
GitHub: https://github.com/JoshuaFerando