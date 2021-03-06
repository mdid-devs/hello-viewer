## Hello, Viewer!

A basic MDID3 viewer to use as a launchpad for making new MDID3 viewers. Vaguely inspired by the classic "Hello World" program, except that if we're honest we have to admit that just seeing the words "Hello. World" in a browser window doesn't impress anyone.

### What's a Viewer tho?

MDID3 has a feature called "Viewers" - it shipped with several which you may be familiar with including View Presentation, Package Files, Print View. All (or most?) of the links that show up under "actions" on the edit presentation/light table page are technically "viewers." The Viewer is the feature that is responsible for

* Getting the images in a presentation
* Formatting/processing/packaging/etc. the images and associated data as desired 
* Presenting the results to the end user


### Features

* See a presentation of your choice rendered in glorious-but-not-particularly-refined HTML
* Use the included source code to build your own
    * Once it's working, try editing rooibos/apps/hello_viewer/templates/hello.html to change

### Requirements

* Admin access on an [MDID](https://github.com/vrchost/rooibos/) server running version 3.5 (Django 1.11, python3)
* An idea for a new kind of viewer

## Installation

1. cd to your mdid/rooibos directory (where settings_local.py and manage.py are located) and type the following command:

        git clone git@github.com:mdid-devs/hello_viewer.git apps/hello_viewer

1. Save a copy of rooibos/apps/hello_viewer/settings_local_template.py as settings_local.py

1. Add the following to your rooibos/settings_local.py:

`python
additional_settings = [
    'rooibos.apps.hello_viewer.settings_local',
]
INSTALLED_APPS = (
    'rooibos.apps.hello_viewer',
)
`

1. Restart the web server (just httpd/nginx/iis - not the server)

## Viewing a presentation in hello_viewer

1. Edit a presentation (e.g. click Organization > Edit {Presentation Name}

1. In the Actions side bar, click the link titled "HelloViewer"


## What hello_viewer does

It  outputs the items (aka slides) of a presentation to a page (similar in formatting to PDF View but not as refined) with full-sized image, both thumbnails and metadata.

However, the real purpose of hello_viewer is to see how it's not that hard to make your own custom viewer if you have worked with any web page creation task in the past.  Start by editing
[hello.html](https://github.com/mdid-devs/hello_viewer/templates/hello.html), if you know HTML it shouldn't be too hard to adjust to
[django's template language](https://docs.djangoproject.com/en/1.6/topics/templates/). 

For reference, here are some variables that you can use in your own template:

{{ tag }}        | Function                 | Example
---------------- | ------------------------ | --------------------------------------
{{&nbsp;return_url&nbsp;}} | link for a back button   | `<a href="{{ return_url }}">Back</a>`
{{&nbsp;options_form&nbsp;}}|  include the options form   | `<form method="post">{% csrf_token %}form method="post">{% csrf_token %}{{ options_form }}</form>`
{%&nbsp;static&nbsp;'file'&nbsp;%} | url of the static files  (unchanging files like images, css, etc. | `<img src="{% static 'hello_mdid.png' %}">`
{{&nbsp;notes&nbsp;}} | The notes variable (supplied via the options_form)   | ` {{ notes|default:'Hey, no form passed me anything!' }}`
{{&nbsp;options_form&nbsp;}}|  include the options form   | `<form method="post"> {% csrf_token %} {{ options_form } </form>`
{%&nbsp;url&nbsp;hello_static&nbsp;%} | url of the static files  | `<img src="{% url hello_static 'hello_mdid.png' %}">`
{{&nbsp;notes&nbsp;}} | The notes variable (supplied via the options_form)   | `{{ notes }}`

## Still TODO

Maybe write a better tutorial?

![Image of Hello Viewer](https://github.com/mdid-devs/hello_viewer/raw/master/hello-viewer.png)

