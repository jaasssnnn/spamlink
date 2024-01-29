from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check-link', methods=['POST'])
def check_link():
    link = request.form.get('link')
    
    # Perform your link safety check here
    # For demonstration purposes, let's assume all links are safe
    is_safe = True

    if is_safe:
        status = 'safe'
    else:
        status = 'not safe'

    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(debug=True, port=5500)
