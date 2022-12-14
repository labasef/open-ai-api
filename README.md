# OPENAI Python wrapper for command line

This is a simple python wrapper for generating images through the open-ai api

## Instructions for use

An API key is needed to get your API key signup to [openai](https://openai.com/api/)
- Create a .env file in the same folder as the script, in which you provide your API key:
```
API_KEY="<your-api-key>"
```
- You ca also provide your API key directly in the code even though it is not recommended
- The script depends on the following python packages: dotenv, openai, requests
- You may want to replace the shebang (#!) in the header to point to the correct python interpreter or environment


# Dall-e

## Usage

Note: The script supports piping the prompt, see example below

### arguments and parameters
- positional arguments:
  
prompt:                the prompt for image generation

- options:

  -h, --help            show this help message and exit

  -n NUM, --num NUM     the number of images to generate

  -s SIZE, --size SIZE  the size of the image to generate (must be in ['256x256', '512x512', '1024x1024'])

### examples
```commandline
python3 dall-e.py "duck in a buck" -n2 -s"512x512"
```
running the above command will generate the images: duck_in_a_buck_0.jpg and duck_in_a_buck_1.jpg at the location the script was run

```commandline
echo "satan is a dead god" | python3 dall-e.py
```
this piping example will generate the image satan_is_a_dead_god__0.jpg




Note: Dall-e generated images are free of copyrights until further notice.

# GPT

## Usage

Note: The script supports piping the prompt, see example below

### arguments and parameters
- positional arguments:

prompt:                the prompt for image generation

- options:

  -h, --help            show this help message and exit

### examples

```commandline
python3 gpt.py "comment est votre blanquette ?"
```
running the above command will print the following to standard output: `Excellente !`
