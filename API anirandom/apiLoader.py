import requests
import time


def get_random_anime(user_preferences):
    url = "https://api.jikan.moe/v4/random/anime"
    success_count = 0
    required = 3

    while success_count < required:
        response = requests.get(url)

        if response.status_code == 200:
            anime_data = response.json().get("data", {})  # Extracting the 'data' part from the response

            # Extract relevant fields from the anime data
            ani_name = anime_data.get('title', 'Unknown')
            genres_data = anime_data.get('genres', [])
            genres = [genre['name'] for genre in genres_data]
            source = anime_data.get('source', 'Unknown')
            status = anime_data.get('status', 'Unknown')
            img_url = anime_data.get('images', {}).get('jpg', {}).get('image_url', 'Unknown')

            print(ani_name)
            print(genres)
            print(source)
            print(status)
            print(img_url)

            # Check if the anime meets user preferences
            if set(genres) == set(user_preferences["genres"]) and \
                    (not user_preferences["source"] or source in user_preferences["source"]) and \
                    (not user_preferences["status"] or status in user_preferences["status"]):
                success_count += 1
                yield {
                    "ani_name": ani_name,
                    "genres": genres,
                    "source": source,
                    "status": status,
                    "img_url": img_url,
                }
            else:
                print("Does not meet user preferences. Retrieving next...")

        else:
            print("Error:", response.status_code)  # Handle API errors

        time.sleep(2)  # Add a delay between requests to avoid hitting rate limits
