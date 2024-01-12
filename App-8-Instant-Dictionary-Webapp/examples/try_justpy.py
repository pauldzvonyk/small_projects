import justpy as jp


@jp.SetRoute('/')
def home():
    wp = jp.QuasarPage(tailwind=True)
    main_div = jp.Div(a=wp, classes='bg-gray-200 h-screen')

    div1 = jp.Div(a=main_div, classes='grid grid-cols-3 gap-4')
    input1 = jp.Input(a=div1, placeholder='Enter first number', classes='m-5 form-input border-indigo-600 italic '
                                                                        'hover:bg-green-200')
    input2 = jp.Input(a=div1, placeholder='Enter second number', classes='m-5 form-input border-indigo-600 italic '
                                                                         'hover:bg-green-200')
    output = jp.Div(a=div1, text='Answer will be here...', classes='m-5 text-red-700 italic')

    div2 = jp.Div(a=main_div, classes='grid grid-cols-2 gap-5 m-5')

    """Binding 'click' to sum_up fn, in1 to input1 variable, in2 to input2 variable and out to output variable
    that represent 3 elements in div1
    """
    jp.QBtn(a=div2, style='color: goldenrod', label='Calculate', icon='map', click=sum_up, in1=input1, in2=input2,
            out=output)
    jp.QDiv(a=div2, text='Another area with some text in it, hover over to change the content.',
            classes='italic text-blue-600 bg-red-200 text-center py-4',
            mouseenter=mouse_enter, mouseleave=mouse_leave)

    return wp


def sum_up(widget, msg):
    """in1, in2 and out are parameters that have been passed inside Button widget
    """
    the_sum = float(widget.in1.value) + float(widget.in2.value)
    widget.out.text = the_sum


def mouse_enter(widget, msg):
    widget.text = 'Mouse entered the house!'


def mouse_leave(widget, msg):
    widget.text = 'Oh no, the mouse has left...!'


jp.justpy()
