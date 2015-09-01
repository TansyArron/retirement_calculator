from strategy import Strategy


class EqualPayments(Strategy):
  ''' Divide budget equally between all debts, then invest remainder.
  '''

  def allocate_extra_funds(self, budget, debts, investments):
    debts_after_extra_payments = []
    debts_paid_off = []
    if debts:
      payment = budget/len(debts)
      remaining_budget = 0
      for debt in debts:
        if debt.total < payment:
          remaining_budget += payment-debt.total
          debts_paid_off.append(debt.name)
        else:
          new_debt = debt._replace(total=debt.total - payment)
          debts_after_extra_payments.append(new_debt)
    else:
      remaining_budget = budget      
    investments_after_extra_payments = self.invest_highest_return_first(remaining_budget, investments)

    return (debts_after_extra_payments, debts_paid_off, investments_after_extra_payments)
