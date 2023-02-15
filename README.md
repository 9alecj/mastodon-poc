# Mastodon PoC app
This app is built to give a basic GUI to some of the Mastodon APIs. Currently the plan is to build out using combined public APIs from various federated systems. I'd like to 
expand into the ActivityPub space eventually but the lift is much larger and so that is not on the immediate road map. I believe there are fun, interesting and useful
applications that can be made without diving into that.

## What is this app about?
I'm building this app because I think Mastodon is neat and I want to learn more about languages, libraries and frameworks I haven't used or don't use often. 

On a related note this project uses Python (which I have never used for anything larger than one file scripts) and Vue.js which I have never used before. So if you have any tips,tricks or recommendations let me know!

Right now the app uses only the public Mastodon API and Micro.blog API.

## What APIs does this use?
The two main APIs in use are:
1. https://docs.joinmastodon.org/methods/timelines/
2. https://docs.joinmastodon.org/methods/trends/

With the addition of some micro.blog content:
1. https://micro.blog/posts/discover

## How can I run this?
You'll need the following setup to run this locally:
1. Docker desktop 
2. Node.js
3. python 3.10+

## What is this "samples" folder?
The samples folder contains a python file "test.py" which I use to get sample responses from the Mastodon APIs I'm using. I find having sample responses helps build out the data models more easily and this way I can sanity check the API request before building out a whole flow.

Additionally I added a sample JSON file for the microblog endpoint I am using. I haven't added retrieving this to the script so you'll need to grab it manually if you want a new sample.

## Tips
Once you get it running with docker-compose the frontend can be reached at http://localhost:8080/ and you can see the OpenAPI docs at http://localhost:5000/docs

Sometimes the Mastodon API is slow to respond or times out, I haven't implemented a retry system yet so you'll have to refresh manually if the request hangs.