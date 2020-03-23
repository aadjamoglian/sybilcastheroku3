def get_coords(street_num, street_name, city, state):
    import requests
    import json
    from keyz import gkey
    
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    #'{street_num}+{street_name}+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY'
    url2 = f'{street_num}+{street_name},+{city},+{state}&key={gkey}'
    url = base_url + url2
    response = requests.get(url)
    json_response = response.json()
    person_lat = json_response['results'][0]['geometry']['location']['lat']
    person_lon = json_response['results'][0]['geometry']['location']['lng']
    return person_lat, person_lon
