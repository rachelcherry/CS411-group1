import requests
import cgi
from config import GOOGLE_CLIENT_KEY

def get_directions(api_key, origin, destination):
    base_url = "https://maps.googleapis.com/maps/api/directions/json"

    params = {
        "origin": origin,
        "destination": destination,
        "key": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["status"] == "OK":
            # Extracting and printing the steps
            steps = data["routes"][0]["legs"][0]["steps"]
            for i, step in enumerate(steps, 1):
                print(f"Step {i}: {step['html_instructions']}")
                print(f"    Distance: {step['distance']['text']}")
                print(f"    Duration: {step['duration']['text']}")
                print()

        else:
            print(f"Error: {data['status']} - {data.get('error_message', '')}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
api_key = GOOGLE_CLIENT_KEY
form = cgi.FieldStorage()
start_address = form.getvalue('start')
end_address = form.getvalue('end')

get_directions(api_key, start_address, end_address)