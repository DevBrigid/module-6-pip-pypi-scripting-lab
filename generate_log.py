from datetime import datetime
import os
import requests

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list of log entries.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        file.write("\n".join(data))

    print(f"Log written to {filename}")
    return filename

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    return {}

if __name__ == "__main__":
    post = fetch_data()
    post_title = post.get("title", "No title found")
    
    log_entries = [
        "User logged in", 
        "User updated profile", 
        "Report exported",
        f"Fetched Post Title: {post_title}"
    ]
    
    generate_log(log_entries)