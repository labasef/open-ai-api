#!/home/bferry/Projects/openai/env-openai/bin/python

import sys
import os
import argparse
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv("/home/bferry/Projects/openai/.env")

api_key = ""


api_key = os.getenv("OPENAI_API_KEY") if not api_key else api_key
if not api_key or api_key=="":
    raise Exception("Seems like no API key was provided or that it is empty; pass it with the OPENAI_API_KEY environment variable")

parser = argparse.ArgumentParser(description="A simple openai api interface to download dalle images generated from prompt")

parser.add_argument("-m", "--model", type=str, help="the openai model to use", default="gpt-3.5-turbo", choices=['gpt-3.5-turbo', 'gpt-4o', 'gpt-4-turbo'])

prompt = None
if not sys.stdin.isatty():
    input_stream = sys.stdin
    prompt = input_stream.read().replace('\n', ' ')
else:
    parser.add_argument("prompt", type=str, help="the prompt for image generation")

args = parser.parse_args()

prompt = prompt if prompt else args.prompt
model = args.model

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
