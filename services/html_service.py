import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """
    Fetches the HTML content of the given URL and processes it using BeautifulSoup.

    Args:
        url (str): The URL from which the HTML content will be fetched.

    Returns:
        str: The prettified HTML content of the page.

    Raises:
        ValueError: If an HTTP error occurs (e.g., 4xx or 5xx response code).
        requests.exceptions.RequestException: For general network or request errors.
    """

    # Define custom headers, including a 'User-Agent' to simulate a request from a real browser.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Sending the GET request with the custom headers
        response = requests.get(url, headers=headers)

        # If the response status code indicates an error (4xx or 5xx), raise an HTTPError
        response.raise_for_status()

        # Parse the content of the response using BeautifulSoup to extract and process the HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Return the prettified HTML content, which formats it for easier readability
        return soup.prettify()

    except requests.exceptions.HTTPError as err:
        # Handle HTTP errors (e.g., 404, 500), and raise a ValueError with the error message
        raise ValueError(f"Error fetching URL: {err}")
    
    except requests.exceptions.RequestException as e:
        # Catch all for network issues, timeouts, or other request-related exceptions
        raise ValueError(f"Network error or invalid URL: {e}")

