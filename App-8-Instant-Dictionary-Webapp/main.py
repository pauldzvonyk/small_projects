import justpy as jp
from webapp.home import Home
from webapp.about import About

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)

jp.justpy()
