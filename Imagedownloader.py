import requests
from bs4 import BeautifulSoup
import os

# for download image file from URL
def download_image(url, folder_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_name = os.path.join(folder_path, url.split('/')[-1])
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"File {file_name} downloaded.")
        else:
            print(f"error downloading from URL: {url}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to get image url from web page
def get_image_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            img_tags = soup.find_all('img')  # get all tag img from page

            image_links = []
            for img_tag in img_tags:
                src = img_tag.get('src')  # get atribut src from tag img
                if src and (src.endswith('.jpg') or src.endswith('.jpeg') or src.endswith('.png')):
                    image_links.append(src)

            return image_links
        else:
            print(f"Cannot get page url: {url}")
            return []
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

def main():
    website_url = print("type link website for download image : ")
    image_links = get_image_links(website_url)

    download_folder = 'downloaded_images'
    os.makedirs(download_folder, exist_ok=True)

    if image_links:
        for link in image_links:
            download_image(link, download_folder)
    else:
        print("Not found url jpg, jpeg, png.")

if __name__ == "__main__":
    main()
