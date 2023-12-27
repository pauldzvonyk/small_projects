import justpy as jp


class Doc:
    path = "/about"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        jp.Div(a=wp, text="This page explains how to use url requests to get "
                          "an instant definition of English words",
               classes="text-2xl text-center m-3")
        jp.Hr(a=wp)

        return wp

jp.Route(Doc.path, Doc.serve)
jp.justpy()
