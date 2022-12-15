### SWC_pages
> Developed by [Davis_Software](https://github.com/Davis-Software) &copy; 2022

> Demo: [Davis_Software Homepage](https://pages.software-city.org)

---

Lightweight package-based webserver <br>
Basically Software City's version of [GitHub Pages](https://pages.github.com/) with some special features but also a lot less functionality.


### Development
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

### config.ini

###### Default:
```
# app config
SECRET_KEY=<flask session secret key>

# webserver config
HOST=0.0.0.0
PORT=80
DEBUG=true

# routing config
DEFAULT_PAGE=test_website
ALLOW_LIST=true
```

###### Explanation:
| Parameter         | Description                                        |
|-------------------|----------------------------------------------------|
| SECRET_KEY        | Flask session secret key                           |
| HOST              | Host to listen on                                  |
| PORT              | Port to listen on                                  |
| DEBUG             | Enable debug mode                                  |
| DEFAULT_PAGE      | ID of Default page to show if no page is specified |
| ALLOW_LIST        | Enable allow list                                  |
| WATCH_FOR_CHANGES | Enable automatic page reload on file change        |


### Routing
| Route                                | Description                                       |
|--------------------------------------|---------------------------------------------------|
| `/` and `/d`                         | Default page                                      |
| `/j/<page id>` and `/join/<page id>` | Join page by id                                   |
| `/list`                              | List of all pages (Must be enabled in config.ini) |

* Once a page is joined by id, it will be remembered in the session cookie and will be shown by default.


### Installing pages
Pages are installed by placing them in the `packages` folder. <br>
The page must be a zip file containing a `manifest.json` file and all other website files:
Folders are allowed and will be accessible through the route `/<folder>`.

When the server is started, the pages will be extracted to the `package_cache` folder.
This overwrites the old files, so if you want to update a page, you have to edit the zip file.

* demo.zip
  * \<additional files>
  * index.html
  * manifest.json

###### manifest.json
```json
{
    "name": "Demo",
    "description": "Demo page",
    "author": "Davis_Software",
    "version": "1.0.0",
    "id": "demo",
    "entry": "index.html"                   // entry point of the page
}
```