import justpy as jp


class Doc:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        main_div = jp.Div(a=wp, classes="italic text-lg")
        jp.Div(a=main_div, text="Instant Dictionary API", classes="text-center text-4xl m-4")
        jp.Hr(a=main_div)
        jp.Div(a=main_div, text="This page explains how to use url requests to get "
                                "an instant English words definition",
               classes="text-2xl text-center m-3")
        jp.Hr(a=main_div)
        jp.Br(a=main_div)
        jp.Div(a=main_div, text="Following url request: ", classes="underline")
        jp.Br(a=main_div)
        jp.Strong(a=main_div, text="http//:www.example.com/api?w=moon")
        jp.Hr(a=main_div)
        jp.Br(a=main_div)
        jp.Div(a=main_div, text="Returns following response in Json format: ", classes="underline")
        jp.Br(a=main_div)
        jp.Strong(a=main_div, text='{"word": "moon", "definition": ["A natural satellite of a planet.", '
                                   '"A month, particularly a lunar month (approximately 28 days).", '
                                   '"To fuss over adoringly or with great affection.", '
                                   '"Deliberately show ones bare ass (usually to an audience, or at a place, '
                                   'where this is not expected or deemed appropriate).", '
                                   '"To be lost in phantasies or be carried away by some internal vision, '
                                   'having temporarily lost (part of) contact to reality."]}')
        jp.Hr(a=main_div)

        return wp
