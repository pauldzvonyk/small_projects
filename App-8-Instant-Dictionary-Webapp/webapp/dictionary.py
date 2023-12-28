import justpy as jp
# import os
# import pandas
from webapp import layout
from webapp import page
import requests

"""STEP 2.
Read STEP 1 in main.py first.
Uncomment imports above as well as Definition class below.
Go to the bottom and follow STEP 3
"""

# class Definition:
#     def __init__(self, term):
#         self.term = term
#
#     def get(self):
#         script_dir = os.path.dirname(__file__)
#         file_path = os.path.join(script_dir, '../data.csv')
#         df = pandas.read_csv(file_path)
#         return tuple(df.loc[df['word'] == self.term]['definition'])


class Dictionary(page.Page):
    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        main_div = jp.Div(a=container, classes='bg-gray-200 h-screen')

        jp.Div(a=main_div, text='Instant Dictionary',
               classes='italic text-3xl text-purple-900 text-center')
        jp.Div(a=main_div, text='Get the definition of any English word instantly as you type.',
               classes='italic text-lg text-center')

        input_div = jp.Div(a=main_div, classes='italic grid grid-cols-2 m-5')

        output_box = jp.Div(a=main_div, classes='border-2 border-black h-40 m-5')

        input_box = jp.Input(a=input_div, placeholder='Start typing here...', outputbox=output_box,
                             classes='text-lg bg-gray-100 focus:bg-white m-5 border-2 border-black')
        input_box.on('input', cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        """STEP 3
        Comment out 'req' and 'data' and uncomment 'defined' variables.
        Pass 'defined' variable in .join() method like -> " ".join(defined)
        """
        req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
        data = req.json()
        # defined = Definition(widget.value).get()
        widget.outputbox.text = " ".join(data['definition'])
