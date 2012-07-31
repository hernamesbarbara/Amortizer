import Amortizer
from pprint import pprint as pp

class Loan(object):
    """
    Loan class for creating and amortizing loans.
    """
    def __init__(self, amount, interest_rate, term, nper=12):
        """
        Create a new Loan.
        Args:
            amount: loan amount
            interest_rate: nominal interest rate as 'stated' without full effect of compounding (e.g. 10% would be 0.1)
            term: term in years
            nper: compounding frequency will default to 12 (i.e. compounding once per month)
        """
        self.periods = nper
        self.amount = self.present_value = self.outstanding = amount
        self.term = term
        self.interest_rate = interest_rate
        self.rate = Amortizer.rate(interest_rate, self.periods)
        self.pmt()

    def pmt(self):
        """
        Calculate the loan payment for the loan. Called from the __init__().
        Args:
            self.rate: periodic interest rate (i.e. interest rate / period)
            self.periods*(self.term+1): total number of compounding periods
            self.present_value: the loan amount
        Returns:
            self.payment: amount of each payment (float)
        """
        self.payment = Amortizer.pmt(self.rate, self.periods*(self.term+1), self.present_value)

    def makePayment(self):
        """
        Make a payment: reduces the outstanding balance of a loan by 1 payment
        Args:
            self
        Returns:
            self.outstanding -= self.payment
        """
        print 'Total Payment: ', self.payment
        print 'Interest Part: %s\nPrincipal Part: %s' %\
              Amortizer.breakdown(self.outstanding,self.payment, self.rate)
        self.outstanding -= self.payment
        print 'Principal Outstanding: ', self.outstanding, '\n'


    def amortize(self):
        """
        Amortizes the loan from start to finish. It will stop every 10 payments
        and wait for you to hit 'enter'. After each payment is made, the nth_pmt
        counter will be incremented and balance details will be printed.
        """
        nth_pmt = 1
        while int(self.outstanding) > 0:
            print "_"*80+'\n'
            print 'Payment Number: ', nth_pmt, '\n'
            self.makePayment()
            nth_pmt += 1
            if nth_pmt % 10 == 0:
                try:
                    selection = raw_input("Hit 'enter' to continue\nHit 'q' to quit\n")
                    if selection.lower()=='q': break                    
                    continue
                except (KeyboardInterrupt,ValueError):
                    continue

    def Print(self):
        """
        Uses pprint to print the loan's attributes.
        """
        pp(vars(self))
        print '\n'
        
l = Loan(150000, 0.06, 5) #create a loan for $150k over 5 years at a 6% interest rate
l.amortize()              #amortize the loan
