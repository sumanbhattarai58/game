import requests
from PIL import Image
from io import BytesIO

UNSPLASH_ACCESS_KEY = 'YOUR_UNSPLASH_ACCESS_KEY'

def fetch_latest_car_image(car_name):
    url = 'https://api.unsplash.com/search/photos'
    params = {
        'query': car_name,
        'client_id': UNSPLASH_ACCESS_KEY,
        'per_page': 1,
        'order_by': 'latest',
        'orientation': 'landscape'
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None, f"Error: {response.status_code}"

    data = response.json()
    if not data['results']:
        return None, "No image found."

    image_url = data['results'][0]['urls']['regular']
    return image_url, None

def show_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()

def main():
    car_name = input("Enter your favourite car: ")
    print(f"\nFetching latest image for '{car_name}'...")
    
    image_url, error = fetch_latest_car_image(car_name)
    if error:
        print(error)
    else:
        print(f"Image URL: {image_url}")
        show_image(image_url)

if __name__ == "__main__":
    main()
