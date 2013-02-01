from flask import render_template, jsonify, request
from app import app, config
from bi.scrape import Scraper


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def api():
    return jsonify({'Version': '0.0.1'})


@app.route('/api/grab')
def grab():
    username = request.args.get('username')

    if not username:
        return jsonify({'error': 'true', 'message': 'You need a valid ID'})

    scraper = Scraper(username)
    songs = scraper.fetch()

    return jsonify({'success': 'true', 'results': [s.to_dict() for s in songs]})


if __name__ == "__main__":
    app.run(port=config['PORT'], host=config['HOST'])
