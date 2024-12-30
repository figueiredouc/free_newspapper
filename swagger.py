# swagger.py

from flask_apispec import doc, use_kwargs, marshal_with
from services.html_service import fetch_html

# Documentation for the fetch-html endpoint
@doc(tags=['HTML Fetcher'])
@use_kwargs({
    'url': {
        'type': 'string',
        'required': True,
        'location': 'json',
        'description': 'The URL of the page to fetch and process'
    }
}, location='json')
@marshal_with({
    'html': {'type': 'string', 'description': 'The processed HTML content'}
})
def fetch_html_endpoint(url):
    """
    Fetch and process the HTML content of the given URL.

    ---
    post:
      summary: Fetch HTML
      description: Given a URL, fetch and process its HTML content and return it.
      parameters:
        - in: body
          name: url
          required: true
          description: The URL to fetch.
          schema:
            type: object
            properties:
              url:
                type: string
                description: The target URL.
      responses:
        200:
          description: The processed HTML content
          schema:
            type: object
            properties:
              html:
                type: string
                description: The prettified HTML content
        400:
          description: Bad request (e.g., missing URL or invalid format)
        415:
          description: Unsupported Media Type (Content-Type must be application/json)
    """
    try:
        # Process the HTML using the fetch_html function
        html_content = fetch_html(url)
        return {'html': html_content}, 200
    except ValueError as e:
        # Handle errors related to fetching or processing the URL
        return {'error': str(e)}, 400
