"""Matplotlib-related routines"""

__all__ = ["set_facecolor_white", "format_BLB", "format_legend", "set_figure_size", "remove_line", "thanksgod",
           "show_maximized", "set_window_title", "sca"]

import PyQt5
from matplotlib import rc, pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import dates as mdates
from matplotlib import _pylab_helpers


def set_facecolor_white():
    rc("figure", facecolor="white")

# TODO this was being called here, is this right? set_facecolor_white()

def format_BLB():
    """Sets some formatting options in Matplotlib. Selected for preservation due to aesthetic,
    social or historical importance."""
    rc("figure", facecolor="white")
    rc('font', family = 'serif', size=10) #, serif = 'cmr10')
    rc('xtick', labelsize=10)
    rc('ytick', labelsize=10)
    rc('axes', linewidth=1)
    rc('xtick.major', size=4, width=1)
    rc('xtick.minor', size=2, width=1)
    rc('ytick.major', size=4, width=1)
    rc('ytick.minor', size=2, width=1)
    # plt.minorticks_on()
    #minorLocator = AutoMinorLocator()
    # plt.tick_params(which="both", width=2)
    # plt.tick_params(which="major", width=2)
    #rc('text', usetex=True)


def format_legend(leg):
    """Sets some formatting options in a matplotlib legend object."""
    # rect = leg.get_frame()
    # rect.set_linewidth(2.)


def set_figure_size(width, height):
    """Sets MatPlotLib figure width and height in pixels

    Reference: https://github.com/matplotlib/matplotlib/issues/2305/
    """
    fig = plt.gcf()
    dpi = float(fig.get_dpi())
    fig.set_size_inches(float(width) / dpi, float(height) / dpi)


def remove_line(line2D):
    """
    Removes line from matplotlib plot.
    # http://stackoverflow.com/questions/4981815/how-to-remove-lines-in-a-matplotlib-plot
    """
    l = line2D.pop(0)
    l.remove()
    del l

def thanksgod():
    """Thanks God with capital "G" for this decent date/datetime/time x-labels."""
    axis = plt.gca()
    locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
    formatter = mdates.ConciseDateFormatter(locator)
    axis.xaxis.set_major_locator(locator)
    axis.xaxis.set_major_formatter(formatter)


def show_maximized(flag_tight=True, block=True):
    try:
        mng = plt.get_current_fig_manager()
        mng.frame.Maximize(True)
    except AttributeError:
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
    if flag_tight:
        fig = plt.gcf()
        fig.set_tight_layout(True)
    plt.show(block=block)


def set_window_title(title):
    fig = plt.gcf()
    fig.canvas.manager.set_window_title(title)


def sca(ax):
    """
    Set the current Axes instance to *ax*.

    The current Figure is updated to the parent of *ax*.
    """
    managers = _pylab_helpers.Gcf.get_all_fig_managers()
    for m in managers:
        if ax in m.canvas.figure.axes:
            _pylab_helpers.Gcf.set_active(m)
            m.canvas.figure.sca(ax)
            return
    raise ValueError("Axes instance argument was not found in a figure")


