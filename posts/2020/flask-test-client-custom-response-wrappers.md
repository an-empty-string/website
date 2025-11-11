---
title: Flask test client custom response wrappers
summary: Notes on using a custom response class when testing Flask apps.
posted_on: 2020-10-13
show_toc: no
---

In the Flask web framework, requests on test clients return response objects which have various attributes (`data` being the most important). It would be useful to be able to wrap the response objects to add utility methods that allow us to parse data and get application-specific attributes from the response. Fortunately, Werkzeug test clients, and thus Flask test clients, can be constructed with a custom response wrapper class. First define the response wrapper class (it can inherit from `flask.wrappers.Response`).

```python
class CustomResponse(flask.wrappers.Response):
    def has_error(self):
        return b"Oh no something bad happened!" in self.data
```

Then set `response_class` on the app:

```python
app = get_flask_app()
app.response_class = CustomResponse
client = app.test_client()
```

Set `app.response_class` wherever you do other configuration on the Flask object. It probably isn't a good idea to set it for responses in production, depending on what you do with/where you make response objects available.
