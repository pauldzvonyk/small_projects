import justpy as jp

class Home:
    path = '/'

    def serve(self):
        """Instantiated Quasar webpage framework, but the styling is in tailwind components,
        consult Quasar Framework Documentation if needed.
        """
        wp = jp.QuasarPage(tailwind=True)
        main_div = jp.Div(a=wp, classes='bg-gray-300 h-screen p-2', )

        div1 = jp.Div(a=main_div, classes='grid grid-cols-3 bg-yellow-300')
        jp.Div(a=div1, text='Div 1', classes='italic text-2xl text-center bg-red-200 '
                                             'border border-black m-5')
        jp.Div(a=div1, text='Div 2', classes='italic text-2xl text-center bg-red-200 '
                                             'border border-black m-5')
        jp.Div(a=div1, text='Div 3', classes='italic text-2xl text-center bg-red-200 '
                                             'border border-black m-5')

        div2 = jp.Div(a=main_div, classes='grid grid-cols-2 bg-green-300')
        jp.Div(a=div2, text='Div 4', classes='italic text-2xl text-center bg-red-200 '
                                             'border border-black m-5')
        jp.Div(a=div2, text='Div 5', classes='italic text-2xl text-center bg-red-200 '
                                             'border border-black m-5')

        div3 = jp.Div(a=main_div, classes='grid grid-cols-1 bg-red-300')
        jp.Div(a=div3, text='Div 6', classes='italic text-2xl text-center bg-red-200 '
                                             'border border-black m-5')

        return wp


jp.Route(Home.path, Home.serve)
jp.justpy()
