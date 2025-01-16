# URL Safety Checker

This is a simple Python tool to check the safety of URLs.

## Features:
- Check if a URL uses HTTPS.
- Verify if the SSL certificate is valid.
- Check if the URL contains suspicious words.
- Detect if the URL is from a blacklisted domain.

## Requirements:
- Python 3.x
- `termcolor` library
- `emoji` library

## Installation:
1. Clone this repository:
    ```bash
   git clone https://github.com/Abdoaljrmy/LinkoCheck.git
    ```

2. Navigate to the project directory:
    ```bash
    cd LinkoCheck
    ```

3. Install the required libraries:
    ```bash
    python3-venv python3-pip
    
    python3 -m venv venv
    
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```

## Usage:
To run the tool, use the following command:
```bash
python3 LinkoCheck.py
