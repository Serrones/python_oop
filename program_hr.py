import hr

salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
hour_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)

payroll_system = hr.PayRollSystem()

payroll_system.calculate_payroll([
    salary_employee,
    hour_employee,
    commission_employee
])
