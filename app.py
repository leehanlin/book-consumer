from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# URL of the API service
api_url = os.environ.get('BOOK_API_URL')

# Home page to input filter criteria
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get filter criteria from the user input
        filter_criteria = {
            'id': request.form.get('id'),
            'title': request.form.get('title'),
            'author': request.form.get('author'),
            'publication_year': request.form.get('publication_year'),
            'genre': request.form.get('genre')
        }

        # Make a request to the API with the filter criteria
        response = requests.get(api_url, params=filter_criteria)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract filtered data from the response (considering it's JSON)
            filtered_books = response.json()

            return render_template('results.html', books=filtered_books, filter_criteria=filter_criteria)
        else:
            return render_template('error.html', error_message="Failed to retrieve filtered books from the API")
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
