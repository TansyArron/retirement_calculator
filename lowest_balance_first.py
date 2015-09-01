from strategy import Strategy


class LowestBalanceFirst(Strategy):
  ''' Pay debts with lowest balance first. Once all debts are paid, start investing
  '''

  def allocate_extra_funds(self, budget, debts, investments):
    debts_after_extra_payments = []
    debts_paid_off = []
    if debts:
      ordered_debts = sorted(
        debts,
        key=lambda d: d.total,
      )
      for debt in ordered_debts:
        if budget > 0:
          payment = min(debt.total, budget)
          budget -= payment
          new_debt = debt._replace(total=debt.total - payment)
          if abs(new_debt.total) > .1:
            debts_after_extra_payments.append(new_debt)
          else:
            debts_paid_off.append(debt.name)
        else:
          debts_after_extra_payments.append(debt)
    if budget > 0:
      investments_after_extra_payments = self.invest_highest_return_first(budget, investments)
    else:
      investments_after_extra_payments = investments
    return (debts_after_extra_payments, debts_paid_off, investments_after_extra_payments)
