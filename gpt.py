#!/home/bferry/Projects/openai/env-openai/bin/python

import sys
import os
import argparse
import requests
import openai
from dotenv import load_dotenv

load_dotenv("/home/bferry/Projects/openai/.env")

api_key = ""


api_key = os.getenv("API_KEY") if not api_key else api_key
if not api_key:
    raise Exception("Seems like no API key was provided or that it is empty")

parser = argparse.ArgumentParser(description="A simple openai api interface to download dalle images generated from prompt")

prompt = None
if not sys.stdin.isatty():
    input_stream = sys.stdin
    prompt = input_stream.read().replace('\n', ' ')
else:
    parser.add_argument("prompt", type=str, help="the prompt for image generation")

args = parser.parse_args()

prompt = prompt if prompt else args.prompt
openai.api_key = api_key

response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt=prompt,
    temperature=0.5,
    max_tokens=2048,
    top_p=1,    
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].text)
