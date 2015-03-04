## Hello, Viewer!

A basic MDID3 viewer to use as a launchpad for making new MDID3 viewers. Vaguely inspired by the classic "Hello World" program, except that if we're honest we have to admit that just seeing the words "Hello. World" in a browser window doesn't impress anyone.


### Features

* See a presentation of your choice rendered in glorious-but-not-particularly-refined HTML
* Use the included source code to build your own

    * Once it's working, try editing rooibos/apps/hello-viewer/templates/hello.html to change

### Requirements

* A working [MDID3](https://github.com/jmu-cit/) server

## Installation

1. cd to your mdid/rooibos directory (where settings_local.py and manage.py are located) and type the following command:

        git clone git@github.com:mdid-devs/hello-viewer.git apps/hello-viewer

1. Save a copy of rooibos/apps/hello-viewer/settings_local_template.py as settings_local.py

1. Add the following to your rooibos/settings_local.py:

```python
additional_settings = [
    'apps.hello-viewer.settings_local',
]
INSTALLED_APPS = (
    'rooibos.apps.hello-viewer',
)
```

1. Restart the web server (just httpd/nginx/iis - not the server)

## Viewing a presentation in hello-viewer

1. Edit a presentation (e.g. click Organization > Edit {Presentation Name}

1. In the Actions side bar, click the link titled "HelloViewer"


## What hello-viewer does

It  outputs the items (aka slides) of a presentation to a page (similar in formatting to PDF View but not as refined) with full-sized image, both thumbnails and metadata.

However, the real purpose of hello-viewer is to see how it's not that hard to make your own custom viewer.  Start by editing
[hello.html](https://github.com/mdid-devs/hello-viewer/templates/hello.html), if you know HTML it shouldn't be too hard to adjust to
[django's template language](https://docs.djangoproject.com/en/1.2/topics/templates/).

For reference, here are some variables that you can use in your own template:

{{ tag }}        | Function                 | Example
---------------- | ------------------------ | --------------------------------------
{{ return_url }} | link for a back button   | ```<a href="{{ return_url }}">Back</a>```
 {{ options_form }}|  include the options form   | ```<form method="post">{% csrf_token %}form method="post">{% csrf_token %}{{ options_form }}</form>```
{% url 'file'  %} | url of the static files  | ```<img src="{% url 'hello_mdid.png' %}">```
{{ notes }} | The notes variable (supplied via the options_form)   | ``` {{ notes|default:'Hey, no form passed me anything!' }}```



![Image of Hello Viewer](https://github.com/mdid-devs/hello-viewer/raw/master/hello-viewer.png)
