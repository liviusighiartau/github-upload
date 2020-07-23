def salary_calculator(state, gross_salary):
    """
    Function which calculates the net salary in each US state
    :param state: US state name
    :param gross_salary: Gross salary amount
    :return: Net salary amount
    """
    states = {'Arizona': 0.1, 'Texas': 0.05, 'Washington': 0.06}
    if state in states.keys():
        state_tax = states[state]
        taxes_to_pay = gross_salary * state_tax
        net_salary = gross_salary - taxes_to_pay
        return net_salary

    return None


salary = salary_calculator('Florida', 1000)
print(salary)
