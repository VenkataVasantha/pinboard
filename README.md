# Pin Board

## Requirements

* Python - 2.7.10
* Django - 1.8.4

## Installation

Clone the git repo to your home directory ($HOME), say $HOME/pinboard

## Starting Server

* `cd $HOME/pinboard`
* `python manage.py runserver localhost:8000`

Runs the web server on localhost port 8000

## Endpoints

* `http://localhost:8000/pinboard` - Loads the pin board with infinite scroll
* `http://localhost:8000/pinboard/api/page/{pagenum}` - REST API used to fetch page data as JSON
