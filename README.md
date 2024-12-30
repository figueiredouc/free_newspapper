# HTML Fetcher API

This project provides an API built with **Flask** that fetches the HTML content from a given URL, processes it, and returns it in a cleaned and formatted structure. The API allows users to submit URLs and retrieve the corresponding HTML content through a simple interface. It includes Swagger documentation for easy interaction and testing.

## Features

- Fetch HTML content from a given URL.
- Return cleaned HTML with unnecessary CSS and JavaScript removed.
- Interactive API documentation via Swagger UI.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/html-fetcher-api.git
    cd html-fetcher-api
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. To run the Flask application locally, use the following command:

    ```bash
    python main.py
    ```

2. The Flask server will start and will be accessible at `http://127.0.0.1:5000/`.

## Viewing Swagger UI

Once the Flask application is running, you can access the Swagger UI to interact with the API:

1. Open your browser and navigate to:

    ```bash
    http://127.0.0.1:5000/swagger
    ```

2. This will display the interactive Swagger UI, where you can test the API's endpoints.

3. In the Swagger UI, you will see the `/fetch-html` endpoint. You can use the **"Try it out"** button to send a POST request to the API. You will need to provide a valid URL in the JSON body:

    Example:

    ```json
    {
      "url": "https://example.com"
    }
    ```

4. Once the request is sent, you should receive the processed HTML content as a response.

## Testing the API Manually (Optional)

You can also test the API using Postman or curl.

### Example cURL Request:

```bash
curl --location 'http://127.0.0.1:5000/fetch-html' \
--header 'Content-Type: application/json' \
--data '{"url": "https://example.com"}'
