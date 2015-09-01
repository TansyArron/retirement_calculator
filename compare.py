from high_interest_debts_first import HighestInterestDebtsFirst
from highest_interest_first import HighestInterestFirst
from lowest_balance_first import LowestBalanceFirst
from equal_payments import EqualPayments
from info import budget, debts, investments, tax_rate


strategies = [
  HighestInterestDebtsFirst,
  HighestInterestFirst,
  LowestBalanceFirst,
  EqualPayments,
  ]

class Compare(object):
  def __init__(self, budget, debts, investments, tax_rate, strategies, time_period=None):
    self.budget = budget
    self.debts = debts
    self.investments = investments
    self.strategies = strategies
    self.time_period = time_period
    self.strategy_instances = []

  def create_instances(self):
    for strategy in strategies:
      self.strategy_instances.append(strategy(self.budget, self.debts, self.investments, tax_rate))

  def compare_strategies(self):
    if self.time_period is None:
      for strategy in self.strategy_instances:
        while strategy.debts:
          strategy.increment_month()
        print(strategy.__class__.__name__)
        print('Number of Months til debt free: {}'.format(strategy.months_til_debt_free))
        print('Total interest paid: {}'.format(strategy.total_interest_accrued))
        print('Net worth at end of period: {}'.format(strategy.net_worth))
        print()
    else:
      for strategy in self.strategy_instances:
        for i in range(self.time_period):
          strategy.increment_month()
        print(strategy.__class__.__name__)
        print('Net worth after {} months is {}'.format(self.time_period, strategy.net_worth))
        print()

  def run_comparison(self):
    self.create_instances()
    # self.run_strategies()
    self.compare_strategies()


comparison = Compare(budget, debts, investments, tax_rate, strategies)
comparison.run_comparison()
