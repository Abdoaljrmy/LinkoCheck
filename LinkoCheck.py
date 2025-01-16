import ssl
import socket
import os
import time
import webbrowser
from urllib.parse import urlparse
from termcolor import colored
import emoji

# دالة إضافة الألوان في النصوص
def print_colored(text, color='cyan', attrs=['bold']):
    """طباعة النص بالألوان مع التأثيرات."""
    print(colored(text, color, attrs=attrs))

def is_https(url):
    """Check if the URL uses HTTPS"""
    return url.startswith("https://")

def is_valid_ssl_certificate(url):
    """Check if the SSL certificate of the site is valid"""
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    try:
        conn = ssl.create_default_context().wrap_socket(socket.socket(), server_hostname=domain)
        conn.connect((domain, 443))
        cert = conn.getpeercert()
        if cert:
            return True
    except Exception as e:
        print(f"Error checking the certificate: {e}")
    return False

def has_suspicious_words(url):
    """Check for suspicious words in the URL"""
    suspicious_words = ["free", "win", "click", "offer", "prize", "promo", "discount", "giveaway", "secure", "login"]
    for word in suspicious_words:
        if word in url.lower():
            return True
    return False

def is_blacklisted_domain(url):
    """Check if the domain in the URL is in a blacklist"""
    blacklisted_domains = ["example.com", "phishing.com", "malicious.com"]  # You can add more suspicious domains
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()
    
    if domain in blacklisted_domains:
        return True
    return False

def print_logo():
    """Print the logo with decorations and emojis"""
    logo = """
##############################################
#        Dark Men LinkoCheck                 #
#    🚨 URL Safety Checker 🚨                #
#    Verify the safety of your links!         #
##############################################
"""
    print_colored(logo, color='yellow', attrs=['bold'])

def check_url(url):
    """Check the URL to see if it's safe or potentially malicious"""
    parsed_url = urlparse(url)
    
    if not parsed_url.scheme:
        return "❌ Invalid URL (does not contain HTTPS/HTTP protocol)."
    
    if not is_https(url):
        return "❌ Unsafe URL (does not use HTTPS)."
    
    if not is_valid_ssl_certificate(url):
        return "❌ The URL has an invalid or expired SSL certificate."
    
    if has_suspicious_words(url):
        return "⚠️ The URL contains suspicious words."
    
    if is_blacklisted_domain(url):
        return "⚠️ The URL contains a blacklisted domain."
    
    return "✅ The URL seems safe."

def loading_animation():
    """Display loading animation while the URL is being checked"""
    print("🔍 Checking the URL...")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()  # Just to move to the next line after animation

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def open_in_browser(url):
    """Open the URL in the default web browser"""
    webbrowser.open(url, new=2)  # new=2 opens in a new tab

def user_menu():
    """Display the menu options to the user"""
    print_colored("\nPlease choose an option:", color='cyan')
    print("1. Open the URL in your browser.")
    print("2. Check another URL.")
    print("3. Exit.")

def main():
    """Main function to run the program"""
    clear_screen()  # Clear the screen at the beginning
    print_logo()

    while True:
        url_to_check = input("🔍 Enter the URL to check: ")

        loading_animation()  # Show loading animation

        result = check_url(url_to_check)
        print_colored(f"\n🔎 Scan result: {result}\n", color='green', attrs=['bold'])

        # Show the user menu
        user_menu()
        choice = input("Please enter your choice (1/2/3): ")

        if choice == '1':
            open_in_browser(url_to_check)
        elif choice == '2':
            continue  # Start the loop again for checking another URL
        elif choice == '3':
            print("🚪 Exiting the tool. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("❌ Invalid choice. Please select a valid option.")

# Run the main function
if __name__ == "__main__":
    main()
