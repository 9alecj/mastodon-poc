# Mastodon PoC app
This app is built to give a basic GUI to some of the Mastodon APIs. At the moment it only supports the public APIs, though proper login flows and corresponding API usage is planned. 

## What is this app about?
I'm building this app because I think Mastodon is neat and I want to learn more about languages, libraries and frameworks I haven't used or don't use often. 

On a related note this project uses Python (which I have never used for anything larger than one file scripts) and Vue.js which I have never used before. So if you have any tips,tricks or recommendations let me know!

Right now the app uses only the public Mastodon API due to issues with getting a proper Application API key due to traffic increases at Mastodon.

## What APIs does this use?
The two main APIs in use are:
1. https://docs.joinmastodon.org/methods/timelines/
2. https://docs.joinmastodon.org/methods/trends/

## How can I run this?
You'll need the following setup to run this locally:
1. Docker desktop 
2. Node.js
3. python 3.10+

## What is this "samples" folder?
The samples folder contains a python file "test.py" which I use to get sample responses from the Mastodon APIs I'm using. I find having sample responses helps build out the data models more easily and this way I can sanity check the API request before building out a whole flow.

