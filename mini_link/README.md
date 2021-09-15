Mini Link
=========

URL Shortner That Works!



## Development

Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/). Start your virtual machines with the following shell command:

Change .env DOMAIN to pxr.app or any other url depending on your environment and url

`docker-compose up --build`

Submitted in order to satisfy interview for pxr.

If all works well, you should be able to create an admin account with:

`docker-compose run backend python manage.py createsuperuser`

Stats features were not implemented but they are few clicks away. Time was a bit short for me.
I am open for disscussion regarding this.


#what could be improved

    - Providing auto docs
    - Completing Stats
    - providing api for other apps to be used
    - implementing user login and registration