import justpy as jp


class Home:

    @classmethod
    def serve(cls, req):
        """Instantiated Quasar webpage framework, but the styling is in tailwind components,
        consult Quasar Framework Documentation if needed.
        """
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode='left', bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=qlist, text='Home', href='/', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='About', href='/about', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu", click=cls.move_drawer,
                drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        container = jp.QPageContainer(a=layout)

        main_div = jp.Div(a=container, classes='bg-gray-300 h-screen p-2', )
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

    path = '/'

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
