import Amortizer
from pprint import pprint as pp

class Loan(object):
    def __init__(self, amount, interest_rate, term, nper=12):
        self.periods = nper
        self.amount = self.present_value = self.outstanding = amount
        self.term = term
        self.interest_rate = interest_rate
        self.rate = Amortizer.rate(interest_rate, self.periods)
        self.pmt()

    def pmt(self):
        self.payment = Amortizer.pmt(self.rate, self.periods*self.term, self.present_value)

    def makePayment(self):
        print 'Total Payment: ', self.payment
        print 'Interest Part: %s\nPrincipal Part: %s' % Amortizer.breakdown(self.outstanding,self.payment, self.rate)
        self.outstanding -= self.payment
        print 'Principal Outstanding: ', self.outstanding, '\n'


    def amortize(self):
        nth_pmt = 1
        while int(self.outstanding) > 0:
            print "_"*80+'\n'
            print 'Payment Number: ', nth_pmt, '\n'
            self.makePayment()
            nth_pmt += 1
            if nth_pmt % 2 == 0:
                try:
                    selection = raw_input("Hit 'enter' to continue\nHit 'q' to quit\n")
                    if selection.lower()=='q': break                    
                    continue
                except (KeyboardInterrupt,ValueError):
                    continue

    def Print(self):
        pp(vars(self))
        print '\n'
        
l = Loan(1000, 0.075, 1)
l.amortize()
