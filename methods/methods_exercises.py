def salary_calculator(state, gross_salary):
    states = {'Arizona': 0.1, 'Texas': 0.05, 'Washington': 0.06}
    if state in states.keys():
        state_tax = states[state]
        taxes_to_pay = gross_salary * state_tax
        net_salary = gross_salary - taxes_to_pay
        return net_salary


salary = salary_calculator('Florida', 1000)
print(salary)
