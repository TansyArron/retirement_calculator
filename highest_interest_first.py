from strategy import Strategy
from info import debts, budget, investments 

class HighestInterestFirst(Strategy):
  ''' Maximize total net worth: Allocate all extra funds to highest interest vehicle.

  '''

  def allocate_extra_funds(self, budget, debts, investments):
    ''' Well this turned into a complete mess. Needs a refactor.
    '''  
    debts_after_extra_payments = []
    investments_after_extra_payments = []
    debts_paid_off = []
 
    ordered_debts = sorted(
      debts,
      key=lambda d: d.interest_rate,
      reverse=True,
    )

    ordered_investments = sorted(
      investments,
      key=lambda i: i.interest_rate,
      reverse=True)

    i = 0
    d = 0
    remaining_budget = budget
    while remaining_budget > 1:
      if debts:
        debt = ordered_debts[d]
        investment = ordered_investments[i]
        if debt.interest_rate >= investment.interest_rate:
          if debt.total > remaining_budget:
            new_debt = debt._replace(total=debt.total - remaining_budget)
            debts_after_extra_payments.append(new_debt)
            d += 1
            remaining_budget = 0          
          else:
            debts_paid_off.append(debt)
            remaining_budget -= debt.total
            d += 1
        else:
          if investment.max_monthly > remaining_budget:
            new_investment = investment._replace(total=investment.total + remaining_budget)
            remaining_budget = 0
          else:
            remaining_budget -= investment.max_monthly
            new_investment = investment._replace(total=investment.total + investment.max_monthly)
          investments_after_extra_payments.append(new_investment)
          i += 1
      else:
        investment = ordered_investments[i]
        if investment.max_monthly > remaining_budget:
          new_investment = investment._replace(total=investment.total + remaining_budget)
          remaining_budget = 0
        else:
          remaining_budget -= investment.max_monthly
          new_investment = investment._replace(total=investment.total + investment.max_monthly)
        investments_after_extra_payments.append(new_investment)
        i += 1
    debts_after_extra_payments.extend(debts[d:])
    investments_after_extra_payments.extend(investments[i:]) 

    return (debts_after_extra_payments, debts_paid_off, investments_after_extra_payments)
