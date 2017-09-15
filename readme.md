# journal-backend

See `api_reference.md` for API details

## Install and setup
_Ensure you have python3 and virtualenvwrapper installed. Tested on MacOS 10.12.5_
```bash
$ mkvirtualenv -p python3 backend                                 # call the env whatever you want

$ git clone https://github.com/brahmcapoor/journal-backend.git
$ cd journal-backend
$ pip install -r requirements.txt
$ python manage.py createsuperuser                                # for auth purposes
$ python manage.py runserver                                      # runs server on port 8000
```

## Browsable API

* Run server and navigate to `localhost:8000/posts` or any of the other URLs that support `GET` requests your browser for a visual browser of the database





<p align='center'>
<em> Built with 💻 in 🇸🇬 by Brahm Capoor </em>
</p>
