import justpy as jp


class About:
    path = '/about'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        main_div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=main_div, text='Hello there!', classes='italic text-2xl')
        jp.Div(a=main_div, text='lorem ipsum sdfbgerd esgsdvsea avsdfva avsdvc asvsvdasv asdvavwfv d  dfdf dfSFAWSF '
                                'ACSD edfgdfg dxfbg dfgedgdvd xfbg!',
               classes='italic text-lg')

        return wp


jp.Route(About.path, About.serve)
jp.justpy()
