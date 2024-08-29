#!/usr/bin/env python3

import os 
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')

url = 'https://notify-api.line.me/api/notify'

def send_text(token: str, text: str) -> None:
    """
    Send a LINE Notify message with the given token and text.
    
    Args:
        token (str): The LINE Notify token.
        text (str): The message to send.
    """
    # Set the headers for the request
    LINE_HEADERS = {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + token
    }
    
    # Set the data for the request
    data = {'message': text}
    
    # Post the request
    session_post = requests.post(url, headers=LINE_HEADERS, data=data)
    
    # Print the response
    print(session_post.text)

def send_image(token: str, text: str, image_path: str) -> None:
    """
    Send a LINE Notify message with the given token, text, and image.
    
    Args:
        token (str): The LINE Notify token.
        text (str): The message to send.
        image_path (str): The path to the image to send.
    """
    # Open the image file in binary mode
    with open(image_path, 'rb') as img_file:
        # Create a dictionary to hold the image file
        file_img = {'imageFile': img_file}
        # Set the headers for the request
        LINE_HEADERS = {
            'Authorization': 'Bearer ' + token
        }
        # Post the request
        session_post = requests.post(url, headers=LINE_HEADERS, files=file_img, data={'message': text})
        # Print the response
        print(session_post.text)


if __name__ == '__main__':
    text = "oh! Hello Chat"
    image_path = "images.jpg"
    send_image(token, text, image_path)
    