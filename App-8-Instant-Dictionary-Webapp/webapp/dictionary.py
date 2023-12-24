import justpy as jp
import pandas
import os


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, '../data.csv')
        df = pandas.read_csv(file_path)
        return tuple(df.loc[df['word'] == self.term]['definition'])


class Dictionary:
    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        main_div = jp.Div(a=wp, classes='bg-gray-200 h-screen')

        jp.Div(a=main_div, text='Instant Dictionary',
               classes='italic text-3xl text-purple-900 text-center')
        jp.Div(a=main_div, text='Get the definition of any English word instantly as you type.',
               classes='italic text-lg text-center')

        input_div = jp.Div(a=main_div, classes='italic grid grid-cols-2 m-5')
        input_box = jp.Input(a=input_div, placeholder='Start typing here...',
                             classes='text-lg bg-gray-100 focus:bg-white m-5 border-2 border-black')
        output_box = jp.Div(a=main_div, classes='border-2 border-black h-40 m-5')
        jp.Button(a=input_div, text='Get Definition', click=cls.get_definition, inputbox=input_box,
                  outputbox=output_box,
                  classes='bg-red-300 m-5 border-2 border-black')

        print(cls, req)
        return wp

    @staticmethod
    def get_definition(widget, msg):
        word_definition = Definition(widget.inputbox.value).get()
        widget.outputbox.text = word_definition


# jp.Route(Dictionary.path, Dictionary.serve)
#
# jp.justpy()
