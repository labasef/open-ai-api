#!/home/bferry/Projects/openai/env-openai/bin/python

import sys
import os
import argparse
import requests
import openai
from dotenv import load_dotenv

load_dotenv("/home/bferry/Projects/openai/.env")

api_key = None


api_key = os.getenv("API_KEY") if not api_key else api_key
if not api_key or api_key=="":
    raise Exception("Seems like no API key was provided or that it is empty")

parser = argparse.ArgumentParser(description="A simple openai api interface to download dalle images generated from prompt")

prompt = None
if not sys.stdin.isatty():
    input_stream = sys.stdin
    #prompt = " ".join([line for line in input_stream])
    prompt = input_stream.read().replace('\n', ' ')
else:
    parser.add_argument("prompt", type=str, help="the prompt for image generation")
parser.add_argument("-n", "--num", type=int, help="the number of images to generate", default=1)
parser.add_argument("-s", "--size", type=str, help="the size of the image to generate (must be in ['256x256', '512x512', '1024x1024'])", default="1024x1024")

args = parser.parse_args()

prompt = prompt if prompt else args.prompt
openai.api_key = api_key

response = openai.Image.create(
  prompt=prompt,
  n=args.num,
  size=args.size
)

img_id = response['created']

for img_id, data in enumerate(response['data']):
    img_url = data['url']

    with open(f'{prompt.replace(" ", "_")}_{img_id}.jpg', 'wb') as handle:
        response = requests.get(img_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


