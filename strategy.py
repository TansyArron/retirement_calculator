
class Strategy(object):
  def __init__(self, budget, debts, investments, tax_rate):
    ''' budget: some monthly dollar ammount
        debts: a list of named tuples containing total, min_payment, interest_rate.
        investments: a list of named tuples containing total, average rate of return, pre_tax bool, 
        (max annual contribution, employer match still to come?)
    '''
    self.budget = budget
    self.debts = debts
    self.investments = investments
    self.months_log = []
    self.total_interest_accrued = 0
    self.total_returns_on_investments = 0
    self.months_til_debt_free = 0
    self.total_debt = 0
    self.total_investments = 0
    self.net_worth = 0
    self.tax_rate = tax_rate

  def accrue_interest(self, debts):
    after_interest_accrued = []
    total_interest_accrued = 0
    for debt in debts:
      monthly_interest_rate = debt.interest_rate / 12
      interest_accrued = debt.total * monthly_interest_rate
      total_interest_accrued += interest_accrued
      new_debt = debt._replace(total=debt.total + interest_accrued)
      after_interest_accrued.append(new_debt)
    return (after_interest_accrued, total_interest_accrued)

  def make_minimum_payments(self, budget, debts):
    after_min_payments = []
    total_min_payments = 0
    paid_off_this_month = []
    for debt in debts:
      payment = min(debt.total, debt.min_payment)
      total_min_payments += payment
      new_debt = debt._replace(total=debt.total-payment)
      if abs(new_debt.total) > .1:
        after_min_payments.append(new_debt)
      else:
        paid_off_this_month.append(new_debt.name)
    remaining_funds = budget - total_min_payments
    return (remaining_funds, after_min_payments, total_min_payments)

  def invest_highest_return_first(self, budget, investments):
    investments_after_extra_payments = []
    ordered_investments = sorted(
      investments,
      key=lambda i: i.interest_rate,
      reverse=True)
    for investment in ordered_investments:
      if budget > 0:
        if investment.max_monthly is not None:
          payment = min(investment.max_monthly, budget)
        else:
          payment = budget
        new_investment = investment._replace(total=investment.total + payment)
        budget -= payment
        investments_after_extra_payments.append(new_investment)
      else:
        investments_after_extra_payments.append(investment)

    return investments_after_extra_payments

  def allocate_extra_funds(self, budget, debts, investments):
    ''' Write new for each Strategy'''


  def increment_month(self):
    ''' Accrue interest on debts and earnings on investments, make minimum payments,
        allocate remaining funds to debt/investment.
    '''
    this_month = {}
    paid_off_this_month = []
    debts_after_interest, this_months_interest = self.accrue_interest(self.debts)
    investments_after_earnings, this_months_returns = self.accrue_interest(self.investments)
    remaining_budget, debts_after_min_payments, debts_paid_off = self.make_minimum_payments(self.budget, debts_after_interest)

    paid_off_this_month.append(debts_paid_off)
    debts_after_extra_payments, debts_paid_off, investments_after_extra_payments = self.allocate_extra_funds(
      remaining_budget,
      debts_after_min_payments,
      self.investments
    )
    paid_off_this_month.append(debts_paid_off)
    ''' Create this months log 
    '''
    this_month['debts_paid_off'] = paid_off_this_month
    this_month['debts'] = debts_after_extra_payments
    this_month['investments'] = investments_after_extra_payments
    this_month['interest'] = this_months_interest
    this_month['returns'] = this_months_returns

    self.months_log.append(this_month)

    ''' Update State'''
    if self.debts:
      self.months_til_debt_free += 1
    self.debts = debts_after_extra_payments
    
    self.investments = investments_after_extra_payments
    self.total_interest_accrued += this_months_interest
    self.total_returns_on_investments += this_months_returns
    sum_investments = 0
    for investment in self.investments:
      sum_investments += investment.total
    self.total_investments = sum_investments
    sum_debts = 0
    for debt in self.debts:
      sum_debts += debt.total
    self.total_debt = sum_debts
    self.net_worth = self.total_investments - self.total_debt





