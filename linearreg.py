"""
Augment scatter plot with linear regression fit 
David Andrzejewski
"""
import numpy as NP
import numpy.random as NPR

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as P
import matplotlib.lines as L
from sklearn import linear_model
import pandas as pd


def linearscatter(xpts, ypts, ax=None, **kwargs):
    """ 
    Augment scatter plot with linear regression 
    
    Unused kwargs will be passed along to .scatter()
    """
    if(ax == None):
        fig, ax = P.subplots()#figure().gca()        
    # Scatter plot
    P.scatter(xpts, ypts, axes=ax, **kwargs)
    # Get ordinary least squares fit
    model = linear_model.LinearRegression()
    model.fit(NP.reshape(xpts, (len(xpts),1)), ypts)
    # Plot line over scatter
    miny = xpts.min() * model.coef_[0] + model.intercept_
    maxy = xpts.max() * model.coef_[0] + model.intercept_
    ax.add_line(L.Line2D([xpts.min(), xpts.max()],
                         [miny, maxy],
                         color='r', linewidth=5))    
    return (ax, model, fig)

if __name__ == '__main__':
    # Generate a synthetic test dataset
    npts = 200
    xpts = NPR.uniform(1.0, 10.0, (npts,))
    coeff = 1.0
    noise = NPR.standard_normal((len(xpts),))
    ypts = (xpts * coeff) + noise
    # Display it
    (ax, model, fig) = linearscatter(xpts, ypts, ax=None)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    r2 = model.score(NP.reshape(xpts, (len(xpts), 1)), ypts)
    ax.set_title('Linear regression (R2 = %.2f)' % r2)

    fig.savefig('regr.svg')