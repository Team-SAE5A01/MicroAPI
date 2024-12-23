import requests
import json

def make_api_request(url, params=None, headers=None):
    # Send the GET request to the API
    res = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if res.status_code == 200:
        # Parse the JSON response if the status code is OK
        data = res.json()
        print('JSON Response:', data)
        
        #for test
        with open('Reponse.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)  # Write JSON with indentation

        return data  # Return the parsed data
    else:
        print(f"Error {res.status_code}: {res.text}")
        return None

# Example usage of this function for the IDFM API
def fetch_lines_from_api(count=2, api_key='Wthw9UFyhoc3uoCss4mJ2QpWwi51X8kY'):
    # URL of the API
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/lines'

    # Request parameters
    params = {
        'count': count
    }

    # API headers with the provided API key
    headers = {'Accept': 'application/json', 'apikey': api_key}

    # Use the generic make_api_request function
    return make_api_request(url, params=params, headers=headers)

# Example of calling the function
result = fetch_lines_from_api(2)
