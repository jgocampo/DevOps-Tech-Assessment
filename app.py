from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# API Key required for accessing the endpoint
API_KEY = '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'


@app.route('/DevOps', methods=['POST'])
def devops():
    # Check if API key is provided in the headers
    if 'X-Parse-REST-API-Key' not in request.headers or request.headers['X-Parse-REST-API-Key'] != API_KEY:
        return 'Unauthorized', 401
    
    # Check if JWT is provided in the headers
    if 'X-JWT-KWY' not in request.headers:
        return 'Unauthorized', 401
    
    # Check if the request contains JSON data
    if not request.is_json:
        return 'ERROR', 400
    
    # Extract the data from the JSON payload
    data = request.get_json()
    message = data.get('message')
    to = data.get('to')
    time_to_live = data.get('timeToLifeSec')
    
    # Check if all required fields are present in the payload
    if not message or not to or not time_to_live:
        return 'ERROR', 400
    
    # Generate a unique transaction ID using UUID
    transaction_id = str(uuid.uuid4())
    
    # Return the response payload
    response_data = {'message': f'Hello {to} your message will be send'}
    response = jsonify(response_data)
    response.headers['X-Transaction-ID'] = transaction_id
    return response, 200


@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
