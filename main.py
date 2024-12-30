from flask import Flask, request, jsonify
from flask_cors import CORS  # Importing the CORS extension to handle cross-origin requests
from services.html_service import fetch_html  # Importing the function to fetch and process HTML
from flask_swagger_ui import get_swaggerui_blueprint
import swagger  # Import the Swagger configuration


# Initialize Flask application
app = Flask(__name__)


# Swagger UI configuration
SWAGGER_URL = '/swagger'  # URL for accessing the Swagger UI
API_URL = '/static/swagger.json'  # Path to the Swagger JSON file
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "HTML Fetcher API"})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Enable Cross-Origin Resource Sharing (CORS) for all routes
CORS(app)

@app.route('/fetch-html', methods=['POST'])
def fetch_html_endpoint():
    """
    Endpoint to fetch and process HTML content from a provided URL.

    Expects a POST request with a JSON payload containing a 'url' field.
    Returns a JSON response with the processed HTML content or an error message.

    Returns:
        Response (JSON): Processed HTML content if successful, error message otherwise.
    """
    
    # Check if the incoming request has a JSON content type
    if not request.is_json:
        # Return error message if Content-Type is not application/json
        return jsonify({'error': 'Content-Type must be application/json'}), 415

    # Parse the incoming JSON data
    data = request.get_json()
    
    # Extract the 'url' field from the JSON payload
    url = data.get('url')

    # Validate that the 'url' field exists in the request payload
    if not url:
        return jsonify({'error': '"url" field is required'}), 400

    try:
        # Call the function to fetch and process HTML content from the provided URL
        html_content = fetch_html(url)
        
        # Return the processed HTML content in the response
        return jsonify({'html': html_content}), 200
    except ValueError as e:
        # Handle errors raised during the HTML fetching process (e.g., HTTP or scraping errors)
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Start the Flask development server with debugging enabled
    app.run(debug=True)
