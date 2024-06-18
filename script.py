from influxdb import InfluxDBClient
import requests
import hashlib
import time
import json

# Reemplaza estas variables con tus claves públicas y privadas
public_key = 'public_key'
private_key = 'private_key'

# URL base de la API de Marvel
base_url = 'http://gateway.marvel.com/v1/public/'

def get_marvel_data(endpoint, params=None):
    timestamp = str(int(time.time()))  # Añade esta línea
    print(f"Timestamp: {timestamp}")  # Verifica que timestamp está definido
    hash_md5 = hashlib.md5((timestamp + private_key + public_key).encode()).hexdigest()
    if params is None:
        params = {}
    params.update({
        'ts': timestamp,
        'apikey': public_key,
        'hash': hash_md5
    })
    response = requests.get(base_url + endpoint, params=params)
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.json().get('status')}")
        return None
    data = response.json()
    if 'data' not in data:
        print(f"Error: 'data' not in response")
        return None
    return data

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Personajes más populares
def get_popular_characters():
    response = get_marvel_data('characters')
    if response is None:
        return
    characters = [
        {
            'name': character['name'],
            'comics_available': character['comics']['available']
        } for character in response['data']['results']
    ]
    save_to_influxdb(characters)
    
# Creadores más prolíficos
def get_prolific_creators():
    response = get_marvel_data('creators')
    if response is None:
        return
    creators = [
        {
            'full_name': creator['fullName'],
            'comics_available': creator['comics']['available']
        } for creator in response['data']['results']
    ]
    save_to_influxdb_creators(creators)

# Eventos más grandes
def get_biggest_events():
    response = get_marvel_data('events')
    if response is None:
        return
    events = [
        {
            'title': event['title'],
            'characters_available': event['characters']['available']
        } for event in response['data']['results']
    ]
    save_to_influxdb_events(events)
    
# Personajes más involucrados en eventos
def get_characters_involved_in_events():
    response = get_marvel_data('characters')
    if response is None:
        return
    characters = [
        {
            'name': character['name'],
            'events_available': character['events']['available']
        } for character in response['data']['results']
    ]
    save_to_influxdb_characters(characters)
    
# Series más largas
def get_longest_series():
    response = get_marvel_data('series')
    if response is None:
        return
    series = [
        {
            'title': serie['title'],
            'comics_available': serie['comics']['available']
        } for serie in response['data']['results']
    ]
    save_to_influxdb_series(series)
    
# Distribución de géneros de cómics
def get_comic_genres():
    response = get_marvel_data('comics')
    if response is None:
        return
    genres = {}
    for comic in response['data']['results']:
        genre = comic.get('format', 'Unknown')
        if genre not in genres:
            genres[genre] = 0
        genres[genre] += 1
    save_to_influxdb_genres(genres)
    
# Cómics más populares
def get_popular_comics():
    response = get_marvel_data('comics')
    if response is None:
        return
    comics = [
        {
            'title': comic['title'],
            'issue_number': comic['issueNumber']
        } for comic in response['data']['results']
    ]
    save_to_influxdb_comics(comics)
    
# Evolución de personajes nuevos por año
def get_new_characters_by_year():
    response = get_marvel_data('characters')
    if response is None:
        return
    characters_by_year = {}
    for character in response['data']['results']:
        year = character['modified'][:4]
        if year not in characters_by_year:
            characters_by_year[year] = 0
        characters_by_year[year] += 1
    save_to_influxdb_characters_by_year(characters_by_year)

def save_to_influxdb(character_data):
    print("Connecting to InfluxDB...")
    client = InfluxDBClient(host='influxdb', port=8086)
    print("Switching to database 'mydb'...")
    client.switch_database('mydb')
    json_body = [
        {
            "measurement": "popular_characters",
            "tags": {
                "name": character['name']
            },
            "fields": {
                "comics_available": character['comics_available']
            }
        } for character in character_data
    ]
    print("Writing data to InfluxDB...")
    client.write_points(json_body)
    print("Data successfully written to InfluxDB.")
    
def save_to_influxdb_creators(creator_data):
    print("Connecting to InfluxDB...")
    client = InfluxDBClient(host='influxdb', port=8086)
    print("Switching to database 'mydb'...")
    client.switch_database('mydb')
    json_body = [
        {
            "measurement": "prolific_creators",
            "tags": {
                "full_name": creator['full_name']
            },
            "fields": {
                "comics_available": creator['comics_available']
            }
        } for creator in creator_data
    ]
    print("Writing data to InfluxDB...")
    client.write_points(json_body)
    print("Data successfully written to InfluxDB.")
    
def save_to_influxdb_events(event_data):
    print("Connecting to InfluxDB...")
    client = InfluxDBClient(host='influxdb', port=8086)
    print("Switching to database 'mydb'...")
    client.switch_database('mydb')
    json_body = [
        {
            "measurement": "biggest_events",
            "tags": {
                "title": event['title']
            },
            "fields": {
                "characters_available": event['characters_available']
            }
        } for event in event_data
    ]
    print("Writing data to InfluxDB...")
    client.write_points(json_body)
    print("Data successfully written to InfluxDB.")
    
def save_to_influxdb_characters(character_data):
    print("Connecting to InfluxDB...")
    client = InfluxDBClient(host='influxdb', port=8086)
    print("Switching to database 'mydb'...")
    client.switch_database('mydb')
    json_body = [
        {
            "measurement": "characters_in_events",
            "tags": {
                "name": character['name']
            },
            "fields": {
                "events_available": character['events_available']
            }
        } for character in character_data
    ]
    print("Writing data to InfluxDB...")
    client.write_points(json_body)
    print("Data successfully written to InfluxDB.")

def save_to_influxdb_series(series_data):
    print("Connecting to InfluxDB...")
    client = InfluxDBClient(host='influxdb', port=8086)
    print("Switching to database 'mydb'...")
    client.switch_database('mydb')
    json_body = [
        {
            "measurement": "longest_series",
            "tags": {
                "title": serie['title']
            },
            "fields": {
                "comics_available": serie['comics_available']
            }
        } for serie in series_data
    ]
    print("Writing data to InfluxDB...")
    client.write_points(json_body)
    print("Data successfully written to InfluxDB.")
    
def save_to_influxdb_genres(genres_data):
    print("Connecting to InfluxDB...")
    client = InfluxDBClient(host='influxdb', port=8086)
    print("Switching to database 'mydb'...")
    client.switch_database('mydb')
    json_body = [
        {
            "measurement": "comic_genres",
            "tags": {
                "genre": genre
            },
            "fields": {
                "count": count
            }
        } for genre, count in genres_data.items()
    ]
    print("Writing data to InfluxDB...")
    client.write_points(json_body)
    print("Data successfully written to InfluxDB.")    

def save_to_influxdb_comics(comics_data):
    print("Connecting to InfluxDB...")
    client = InfluxDBClient(host='influxdb', port=8086)
    print("Switching to database 'mydb'...")
    client.switch_database('mydb')
    json_body = [
        {
            "measurement": "popular_comics",
            "tags": {
                "title": comic['title']
            },
            "fields": {
                "issue_number": comic['issue_number']
            }
        } for comic in comics_data
    ]
    print("Writing data to InfluxDB...")
    client.write_points(json_body)
    print("Data successfully written to InfluxDB.")


def save_to_influxdb_characters_by_year(characters_by_year_data):
    print("Connecting to InfluxDB...")
    client = InfluxDBClient(host='influxdb', port=8086)
    print("Switching to database 'mydb'...")
    client.switch_database('mydb')
    json_body = [
        {
            "measurement": "new_characters_by_year",
            "tags": {
                "year": year
            },
            "fields": {
                "count": count
            }
        } for year, count in characters_by_year_data.items()
    ]
    print("Writing data to InfluxDB...")
    client.write_points(json_body)
    print("Data successfully written to InfluxDB.")
    
    

if __name__ == "__main__":
    print("Fetching popular characters data...")
    get_popular_characters()
    print("Fetching prolific creators data...")
    get_prolific_creators()
    print("Fetching biggest events data...")
    get_biggest_events()
    print("Fetching characters involved in events data...")
    get_characters_involved_in_events()
    print("Fetching longest series data...")
    get_longest_series()
    print("Fetching comic genres data...")
    get_comic_genres()
    print("Fetching popular comics data...")
    get_popular_comics()
    print("Fetching new characters by year data...")
    get_new_characters_by_year()

