import logging

import numpy as np
from scipy import stats


def msn(a):
    '''
    Returns mean, std, n of array
    '''
    return np.mean(a), np.std(a), len(a)

def statistics(mu=None, sigma=None, mean=None, std=None, n=None):
    '''
    Compute the value of statistics and its p-value
    '''
    if n is None:
        raise ValueError('n cannot be None')
    if mu is None:
        if sigma is None and std is None:
            raise ValueError('cannot calculate: mu, sigma, std is all None')
        logging.info('(%i-1) * %f^2 / %f^2 ~ chi2(%i)' % (n, std, sigma, n-1))
        v = (n-1) * std * std / sigma / sigma
        return v, stats.chi2.sf(v, n-1)
    # mu is not None
    if mean is None:
        raise ValueError('mean cannot be None when mu is not None')
    if sigma is None and std is None:
        raise ValueError('sigma, std cannot all be None when mu, mean is not None')

    if sigma is not None:
        logging.info('(%f-%d) * sqrt(%i) / %f ~ N(0, 1)' % (mean, mu, n, sigma))
        v = (mean-mu) * np.sqrt(n) / sigma
        p = 2 * stats.norm.cdf(v)
        if v > 0:
            p = 2 - p
        return v, p
    if std is not None:
        logging.info('(%f-%d) * sqrt(%i) / %f ~ t(%i)' % (mean, mu, n, std, n-1))
        v = (mean-mu) * np.sqrt(n) / std
        p = 2 * stats.t.cdf(v, n-1)
        if v > 0:
            p = 2 - p
        return v, p
