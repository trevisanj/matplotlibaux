__all__ = ["fig2base64", "file2base64", "base642imgtag", "fig2imgtag", "fileobj2base64",]
"""
Not everything is matplotlib-based, but whatever
"""


import matplotlib.pyplot as plt, io, base64


def fig2base64(fig=None, flag_close=True):
    """Converts matplotlib figure to base64 image to embed in <img> tag.

    Args:
        fig: matplotlib figure
        flag_close: whether to close the figure when done

    Returns:
        base64str: string
    """
    if fig is None:
        fig = plt.gcf()
    h = io.BytesIO()
    fig.savefig(h, format='png')
    if flag_close: plt.close(fig)
    h.seek(0)
    base64str = fileobj2base64(h)
    return base64str


def file2base64(filepath):
    """Returns base64-encoded image as string."""
    with open(filepath, 'rb') as h:
        return fileobj2base64(h)


def base642imgtag(base64str):
    return "".join(['<img src="data:image/png;base64,', base64str, '">'])


def fig2imgtag(fig=None, flag_close=True):
    if fig is None:
        fig = plt.gcf()
    return base642imgtag(fig2base64(fig, flag_close))


def fileobj2base64(fileobject):
    """Returns base64-encoded image as string."""
    data_base64 = base64.b64encode(fileobject.read()).decode()
    return data_base64
