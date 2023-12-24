import justpy as jp
from webapp import layout
from webapp import page


class About(page.Page):
    path = '/about'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        main_div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=main_div, text='Hello there!', classes='italic text-2xl')
        jp.Div(a=main_div, text='lorem ipsum sdfbgerd esgsdvsea avsdfva avsdvc asvsvdasv asdvavwfv d  dfdf dfSFAWSF '
                                'ACSD edfgdfg dxfbg dfgedgdvd xfbg!',
               classes='italic text-lg')

        return wp


