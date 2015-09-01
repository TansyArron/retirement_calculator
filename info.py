from collections import namedtuple 

Debt = namedtuple('Debt', ['name', 'total', 'interest_rate', 'min_payment'])
Investment = namedtuple('Investment', ['name', 'total', 'interest_rate', 'pre_tax', 'max_monthly'])
''' Debts:
    name: nick name for this account. must be inside quote marks.
    total: dollar value of investment
    interest_rate: Annual interest rate
    min_payment: Minimum monthly payment.
''' 
debts = [
	Debt(name='CC1', total=1000, interest_rate=.22, min_payment=25),
  Debt(name='CC2', total=10000, interest_rate=.26, min_payment=220),
  Debt(name='Student Loan', total=30000, interest_rate=.06, min_payment=700),
]

''' Investments: 
    name: nick name for this account. Must be inside quote marks.
    total: dollar value of investment
    interest_rate: interest or average rate of return
    pre_tax: TODO: show tax savings on pre_tax vehicles.
    max_monthly: annual limit/12. For tIRA etc with annual limit. if no limit, enter None.
    TODO: max monthly fails to max the annual contribution if investments
      start part way through the year
'''
investments = [
  Investment(name='Savings Account', total=0, interest_rate=.01, pre_tax=False, max_monthly=None),
  Investment(name='Pension', total=0, interest_rate=.05, pre_tax=True, max_monthly=None),
  Investment(name='tIRA', total=0, interest_rate=.07, pre_tax=True, max_monthly=542),
  Investment(name='brokerage account', total=0, interest_rate=.07, pre_tax=False, max_monthly=None),
]

budget = 1500 # Number of dollars available each month for debt/investment purposes

tax_rate = .2 # Effective Tax rate.

