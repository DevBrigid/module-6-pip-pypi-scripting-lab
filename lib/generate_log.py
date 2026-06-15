from datetime import datetime
import os
import requests

def generate_log(data):
    """
    Validates input data, generates a timestamped file, 
    writes the list items exactly to disk, and returns the filename.
    """
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list of log entries.")

    # STEP 2: Generate a filename with today's date (e.g., "log_20260615.txt")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    # Using "\n".join(data) ensures exact string content matches 
    # and leaves a completely empty file if data is an empty list [].
    with open(filename, "w") as file:
        file.write("\n".join(data))

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")

    # STEP 5: Return filename to satisfy the pytest fixture tracking requirements
    return filename


def fetch_data():
    """
    Fetches text data from a public REST API endpoint.
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    return {}


if __name__ == "__main__":
    # Fetch real-time data from the external API endpoint
    post = fetch_data()
    post_title = post.get("title", "No title found")
    
    # Construct structured, dynamic logging payload list
    log_entries = [
        "User logged in", 
        "User updated profile", 
        "Report exported",
        f"Fetched Post Title: {post_title}"
    ]
    
    # Run the automated file pipeline execution block
    generate_log(log_entries)