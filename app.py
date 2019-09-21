from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # Extract the query term from url using request.args.get()

    query = request.args.get('query')
    print(query)
    #Equivalent to retrieve name 'query' for a form request
    #q = request.form['query']

    # Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {
        'q': query,
        'key': '4MW2HHGJDLMK',
        'limit': 10
    }
#limit changed to 18 to accomodate Grid Layout
    # Make an API call to Tenor using the 'requests' library.
    # Tenor Reference, see: https://tenor.com/gifapi/documentation
    r = requests.get("https://api.tenor.com/v1/search", params=params).json()

    # Use the '.json()' function to get the JSON of the returned response
    # gifs_json = r.json()
    # if r.status_code == 200:


    # Use dict. notation with results param of JSON which contains the GIFs as a list
    gifs = r['results']
    print(gifs)

    # Render the 'index.html' template, passing the list of gifs as a named parameter called 'gifs'
    return render_template("index.html", gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True)
