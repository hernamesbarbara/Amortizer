def pRate(i, nper):
    """Calculates the Periodic Interest Rate.
    Args:
        i: nominal rate
        nper: number of payment periods in an annuity

    Returns:
        periodic interest rate
    """
    return i / nper

def iPart(pb, rate):
    """Calculates interest component of a payment.
    Args:
        pb: principal balance outstanding
        rate: periodic interest rate (i.e. rate per period)
    Returns:
        i: portion of this payment to be applied to interest (float)
    """
    return pb * rate

def pPart(pmt, ipart):
    """Calculates principal component of a payment.
    Args:
        pmt: total payment amount
        ipart: the interest portion of this payment
    Returns:
        principal portion of this payment (float)
        (i.e. total payment less interest part)
    """
    return pmt - ipart

def Pmt(i, nper, pv):
    """
    Args:
        i: periodic interest rate
        nper: number of payment periods in loan
        pv: present value of funds drawn
    Returns:
        payment amount (float) (i.e. payment)
    """
    m = (1 + i)**nper
    return (pv * i * m / (m - 1))

def Breakdown(p, pmt, r):
    """Calculates the P/I breakdown of a payment.
    Args:
        p: principal balance outstanding
        pmt: a payment
        r: periodic interest rate
    Returns:
        a tuple of length 2 (interest, principal)
    """
    i = iPart(p, r)
    p = pPart(pmt, i)
    return (i, p)

def eApr(i, freq="monthly"):
    """Calculates either the monthly or daily effective APR
    Args:
        i: nominal rate
        nper: number of compounding periods (e.g. 12 times per year)
        freq: frequency of compounding --> options: 'Daily', 'Monthly' (default)
    Returns:
        effective annual rate (float)
    """
    if freq in ['Daily', 'daily']:
        return ((1.+pRate(i,365))**365) -1
    elif freq in ['Monthly', 'monthly']:
        return ((1.+pRate(i,12))**12) -1
    else:
        print """Unknown compounding frequency.\nPlease use 'daily' or 'monthly'"""
        return
