import requests
import json

def make_api_request(url, params=None, headers=None):
    # Send the GET request to the API

    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()  # Raise an exception for HTTP errors
        data = res.json()        
        #for test
        with open('Reponse.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)  # Write JSON with indentation
        return data 
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")
        return None

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

def get_lines_by_transport_mode(physical_mode, api_key='Wthw9UFyhoc3uoCss4mJ2QpWwi51X8kY'):
    base_url = 'https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia'
    
    # Ensure that the physical mode is a valid one
    valid_modes = ["Bike", "BikeSharingService", "Bus", "Car", "Funicular", "Metro", 
                   "RailShuttle", "RapidTransit", "Train", "LocalTrain", "Tramway"]
    
    if physical_mode not in valid_modes:
        print(f"Invalid physical mode: {physical_mode}")
        return None

    # Construct the URL with the given parameters
    url = f"{base_url}/line_reports/physical_modes/physical_mode%3A{physical_mode}/lines"

    # Set the request headers with the provided API key
    headers = {'Accept': 'application/json', 'apikey': api_key}
    
    # Make the API request using the helper function
    return make_api_request(url, headers=headers)

# Example of calling the function
result = get_lines_by_transport_mode("Metro")

print(result['lines'])
