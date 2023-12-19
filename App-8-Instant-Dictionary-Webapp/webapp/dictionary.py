import justpy as jp


class Dictionary:
    path = '/dictionary'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        main_div = jp.Div(a=wp, classes='bg-gray-200 h-screen')

        jp.Div(a=main_div, text='Instant Dictionary',
               classes='italic text-3xl text-purple-900 text-center')
        jp.Div(a=main_div, text='Get the definition of any English word instantly as you type.',
               classes='italic text-lg text-center')

        input_div = jp.Div(a=main_div, classes='grid grid-cols-2 m-5')
        jp.Input(a=input_div, placeholder='Start typing here...',
                 classes='text-lg bg-gray-100 focus:bg-white m-5 border-2 border-black')
        jp.Button(a=input_div, text='Get Definition', classes='bg-red-300 m-5 border-2 border-black')

        jp.Div(a=main_div, classes='border-2 border-black h-40 m-5')


        return wp