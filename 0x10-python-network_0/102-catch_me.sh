#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me and causes the server to respond with a message containing "You got me!", in the body of the response.

curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"