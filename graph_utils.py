import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import PIL
import torch
import scipy.signal
from IPython.display import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


def imageFromTensor(tensor, mean, std):
    img = tensor.numpy()
    shape = tensor.shape
    img = img * std + mean
    img = img.reshape(shape[1]*shape[2])
    img = [int(x*255) for x in img]
    return PIL.Image.frombytes('L', shape[1:3], bytes(img))

def fig2data ( fig ):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw ( )
 
    # Get the RGBA buffer from the figure
    w,h = fig.canvas.get_width_height()
    buf = np.frombuffer ( fig.canvas.tostring_argb(), dtype=np.uint8 )
    buf.shape = ( w, h,4 )
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll ( buf, 3, axis = 2 )
    return buf

def fig2img ( fig ):
    """
    @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
    @param fig a matplotlib figure
    @return a Python Imaging Library ( PIL ) image
    """
    # put the figure pixmap into a numpy array
    buf = fig2data ( fig )
    w, h, d = buf.shape
    return PIL.Image.frombytes( "RGBA", ( w ,h ), buf.tostring( ) )

def pltimg(x, y, z=None, filter_len=10):
    figure = Figure()
    canvas = FigureCanvas(figure)
    ax = figure.add_subplot(1, 1, 1)
    ax.set_xlabel('time')
    ax.set_ylabel('loss')
    ax.plot(x, y, 'b')
    if len(y) > filter_len:
        y = scipy.signal.savgol_filter(y, filter_len-1, 1)
        ax.plot(x, y, 'r')
    if z != None:
        ax.plot(x, z, 'g')
        
    return fig2img(figure)


plot_display_id = "ploy_display_id"

def show_plot(iteration, loss):
    display(pltimg(iteration, loss), display_id=plot_display_id)
    
def update_plot(iteration, loss, lr):
    update_display(pltimg(iteration, loss, lr), display_id=plot_display_id)
