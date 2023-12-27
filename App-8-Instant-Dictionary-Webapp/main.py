import inspect
import justpy as jp
from webapp import page
<<<<<<< HEAD
# These imports are necessary for route registration, even though they are marked as unused
from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dictionary
=======
# from webapp.home import Home
# from webapp.about import About
# from webapp.dictionary import Dictionary
>>>>>>> 81074191200efa6791b9623749110440855e40af

imports = list(globals().values())
for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

jp.justpy()
