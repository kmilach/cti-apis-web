#!/usr/bin/env python3

from functools import wraps
from flask import Flask, request, abort
from flask_cors import CORS

from modules.queryapis import *
from modules.validate_inputs import *

# mapping the 'api' parameter to each function
API_FUNCTIONS = {
    'pulsedive': queryPulsedive,
    'virustotal': queryVirusTotal
}

# creating the Flask app and setting the CORS policy
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

def validate_api_parameter(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        '''
        Wrapper function to validate and pass the parameters to the API request functions.
        Returns HTTP 400 ("Bad Request") if one of the parameters is not present/validated
        :param api: which API will be used
        :param query: IOC to query for
        :param key: API key to perform the request
        :return: the function with the passed arguments
        '''
        api = request.args.get('api')
        query = request.args.get('query')
        key = request.args.get('key')

        if not api:
            abort(400, 'Missing "api" parameter.')
        if not query:
            abort(400, 'Missing "query" parameter.')
        if not key:
            abort(400, 'Missing "key" parameter.')

        if api not in API_FUNCTIONS:
            abort(400, 'Invalid API option.')
        
        if not (validateDomain(query) or validateIpAddress(query) or validateHash(query)):
            abort(400, 'Invalid "query" parameter.')
        if not validateKey(key):
            abort(400, 'Invalid "key" parameter.')

        return f(*args, **kwargs)
    return wrapper

# deifing api endpoint and its functions/parameters
@app.route('/api', methods=['GET'])
@validate_api_parameter
def handleApiRequest():
    api = request.args.get('api')
    query = request.args.get('query')
    key = request.args.get('key')

    '''
    select which API request function based on the 'api' variable.
    the request functions always return a tuple with two items: 
    - tuple[0]: HTTP status code of the request
    - tuple[1]: Response data in JSON format
    '''
    requestFunction = API_FUNCTIONS[api]

    result = requestFunction(key, query)

    if result[0] != 200:
        abort(result[0], result[1])
    else:
        return result[1]

if __name__ == '__main__':
    app.debug = True
    app.run()