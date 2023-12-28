import inspect
import justpy as jp
from webapp import page

# These imports are necessary for route registration, even though they are marked as unused.
from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dictionary

"""STEP 1. 
This App uses Instant Dictionary Rest API in App-9 project, 
which must be running first in order for this Webapp to work.
To use this Webapp directly, without Rest API,
go to dictionary.py in cwd and follow STEP 2...
"""
imports = list(globals().values())
for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

jp.justpy(port=8001)
