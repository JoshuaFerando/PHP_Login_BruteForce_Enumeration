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

