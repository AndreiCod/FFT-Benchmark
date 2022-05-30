import multiprocessing
from Fourier.Benchmark import fft_benchmark
import PySimpleGUI as sg
import multiprocessing as mp
import numpy as np

if __name__ == '__main__':
    multiprocessing.freeze_support()

    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.

    left_column = [[sg.Text('After choosing parameters run benchmark:')],
                   [sg.Button(button_text='Run'), sg.Button(button_text='Cancel')],
                   [sg.HSeparator()],
                   [sg.Text('Cores Count')],
                   [sg.Slider(orientation='horizontal', range=(1, mp.cpu_count()), key='slider_cores_count')],
                   [sg.HSeparator()],
                   [sg.Text('Passes Count')],
                   [sg.Slider(orientation='horizontal', range=(1, 20), key='slider_passes_count')],
                   [sg.HSeparator()],
                   [sg.Text('Number of fft calls')],
                   [sg.Slider(orientation='horizontal', range=(1, 20), key='slider_fft_calls')],
                   [sg.HSeparator()],
                   [sg.Text('Size of an input array as power of 2')],
                   [sg.Slider(orientation='horizontal', range=(1, 20), key='slider_array_size')],
                   ]

    right_column = [[sg.Text('Average time per pass: '), sg.Text(text='', size=(10, 1), key='text_pass_avg_time')],
                    [sg.Text('Total execution time: '), sg.Text(text='', size=(10, 1), key='text_total_time')]]

    layout = [[
        sg.Column(left_column),
        sg.VSeparator(),
        sg.Column(right_column)
    ]]

    # Create the Window
    window = sg.Window('FFT Benchmark', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == 'Run':
            times = fft_benchmark(passes_count=int(values['slider_passes_count']),
                                  array_count=int(values['slider_fft_calls']),
                                  array_size=int(values['slider_array_size']),
                                  cpu_count=int(values['slider_cores_count']))
            total_time = np.sum(times)
            avg_time = np.average(times)
            window['text_pass_avg_time'].update(avg_time)
            window['text_total_time'].update(total_time)

    window.close()
