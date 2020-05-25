# Quote Notifier

## Overview
A process which sends quotes via email, and repeats every given number of minutes.

This uses concepts such as:
* Context Managers
* Reading & Writing JSON Files
* Sending Emails
* Docker

## Setup

### Docker

List Images: 

`docker images`

Build Image: 

`docker build -t quote-notifier:latest . `

List Deployments:

`docker ps`

Deploy Container:

`docker run -d --restart always quote-notifier`

Stop Container:

`docker stop <container>`
