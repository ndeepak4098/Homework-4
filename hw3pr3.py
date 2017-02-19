#
# hw3pr3.py 
#
# Visualizing your own data with matplotlib...
#
# Here, you should include functions that produce two visualizations of data
#   of your own choice. Also, include a short description of the data and
#   the visualizations you created. Save them as screenshots or as saved-images,
#   named datavis1.png and datavis2.png in your hw3.zip folder.
# 
# Gallery of matplotlib examples:   http://matplotlib.org/gallery.html
#
# List of many large-data sources:    https://docs.google.com/document/d/1dr2_Byi4I6KI7CQUTiMjX0FXRo-M9k6kB2OESd7a2ck/edit    
#     and, the birthday data in birth.csv is a reasonable fall-back option, if you'd like to use that...
#          you could create a heatmap or traditional graph of birthday frequency variations over the year...
#

"""
Short description of the two data visualizations...

The first plot is a normal line plot, that looks at the population from the years 2000 to 2008. Some special features
that I used was putting a legend, adding a title, changing font and changing the background colors.

The second plot that I used is a bar plot, that looks at the starbucks sales in the past 4 years. Some of the exra features that
I tried was making the tick marks not in scientific notation, changing the bar plot colors, adding labels to both sides and adding a title.

    +++  Please don't use these two! These are simply placeholders (from xkcd...)  +++

    They do show how to save out a plot to a file with fig.savefig , which is useful.


"""



#
# datavis1()
#
"""
From:  http://matplotlib.org/examples/showcase/xkcd.html
"""

import matplotlib.pyplot as plt
import numpy as np

def example_datavis1():
    """ run this function for the first data visualization """
    with plt.xkcd():
        # Based on "Stove Ownership" from XKCD by Randall Monroe
        # http://xkcd.com/418/

        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        plt.xticks([])
        plt.yticks([])
        ax.set_ylim([-30, 10])

        data = np.ones(100)
        data[70:] -= np.arange(30)

        plt.annotate(
            'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
            xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

        plt.plot(data)

        plt.xlabel('time')
        plt.ylabel('my overall health')
        fig.text(
            0.5, 0.05,
            '"Stove Ownership" from xkcd by Randall Monroe',
            ha='center')

        # Based on "The Data So Far" from XKCD by Randall Monroe
        # http://xkcd.com/373/

        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        ax.bar([0, 1], [0, 100], 0.25)
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.set_xticks([0, 1])
        ax.set_xlim([-0.5, 1.5])
        ax.set_ylim([0, 110])
        ax.set_xticklabels(['CONFIRMED BY\nEXPERIMENT', 'REFUTED BY\nEXPERIMENT'])
        plt.yticks([])

        plt.title("CLAIMS OF SUPERNATURAL POWERS")

        fig.text(
            0.5, 0.05,
            '"The Data So Far" from xkcd by Randall Monroe',
            ha='center')

    # save to file
    #fig.savefig('datavisexample1.png', bbox_inches='tight')
    # and show it on the screen
    plt.show()

# run it!
example_datavis1()


#
# datavis2()
#
"""
From:  http://matplotlib.org/xkcd/examples/pylab_examples/manual_axis.html
"""

import numpy as np
from pylab import figure, show
import matplotlib.lines as lines
import matplotlib.pyplot as plt

def make_xaxis(ax, yloc, offset=0.05, **props):
    """ custom-axis (x) example 
    """
    xmin, xmax = ax.get_xlim()
    locs = [loc for loc in ax.xaxis.get_majorticklocs()
            if loc>=xmin and loc<=xmax]
    tickline, = ax.plot(locs, [yloc]*len(locs),linestyle='',
            marker=lines.TICKDOWN, **props)
    axline, = ax.plot([xmin, xmax], [yloc, yloc], **props)
    tickline.set_clip_on(False)
    axline.set_clip_on(False)
    for loc in locs:
        ax.text(loc, yloc-offset, '%1.1f'%loc,
                horizontalalignment='center',
                verticalalignment='top')

def make_yaxis(ax, xloc=0, offset=0.05, **props):
    """ custom-axis (y) example 
    """
    ymin, ymax = ax.get_ylim()
    locs = [loc for loc in ax.yaxis.get_majorticklocs()
            if loc>=ymin and loc<=ymax]
    tickline, = ax.plot([xloc]*len(locs), locs, linestyle='',
            marker=lines.TICKLEFT, **props)
    axline, = ax.plot([xloc, xloc], [ymin, ymax], **props)
    tickline.set_clip_on(False)
    axline.set_clip_on(False)

    for loc in locs:
        ax.text(xloc-offset, loc, '%1.1f'%loc,
                verticalalignment='center',
                horizontalalignment='right')

def example_datavis2():
    """ run this function for the second data visualization """
    with plt.xkcd():
        props = dict(color='black', linewidth=2, markeredgewidth=2)
        x = np.arange(200.)
        y = np.sin(2*np.pi*x/200.) + np.random.rand(200)-0.5
        fig = figure(facecolor='white')
        ax = fig.add_subplot(111, frame_on=False)
        ax.axison = False
        ax.plot(x, y, 'd', markersize=8, markerfacecolor='blue')
        ax.set_xlim(0, 200)
        ax.set_ylim(-1.5, 1.5)
        make_xaxis(ax, 0, offset=0.1, **props)
        make_yaxis(ax, 0, offset=5, **props)
        # save to file
        #fig.savefig('datavisexample2.png', bbox_inches='tight')
        # and show it on the screen
        show()

# run it!
example_datavis2()




def datavis1():
    """
    This data looks at the world population for the past 8 years
    http://www.worldometers.info/world-population/world-population-by-year/
    """
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    fig.patch.set_facecolor("pink")
    
    csfont = {'fontname':'Comic Sans MS'}
    plt.title('World Population', **csfont)
    
    #copy pasted from above website
    plt.plot([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], [6126622121, 6204310739,  6282301767, 6360764684, 6439842408, 6519635850, 6600220247, 6681607320, 6763732879, 684647952, 6929725043], 'ro', label = "population per year, in billions")
    plt.axis([1999, 2009, 5999999999, 8000000000])
    plt.legend(loc='upper right', frameon=False)
    plt.show()

datavis1()

def datavis2():
    """
    This is a plot comparing the number of Starbucks sales
    https://www.statista.com/statistics/266466/net-revenue-of-the-starbucks-corporation-worldwide/
    """
    import matplotlib.pyplot as plt
    
    csfont = {'fontname':'Comic Sans MS'}
    plt.title('Number of Starbucks Sales!!!', **csfont)
    
    #copy pasted from above website
    y = [21320000000,19160000000, 16450000000, 14900000000, 13300000000]
    x = [2016, 2015, 2014, 2013, 2012]
    width = 1/1.5
    plt.bar(x, y, width, color="purple")
    plt.ticklabel_format(useOffset=False)

    plt.ylabel('Sales in Billions')
    plt.xlabel('Year')
    
    plt.show()

datavis2()