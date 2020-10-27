import sys


def worker_salary(work_hours, salary_per_hours, cash_bonus):
    """
    Функция расчета зарплаты по формуле x * y + z где:
    :param work_hours: Выроботка в часах
    :param salary_per_hours: Ставка в час
    :param cash_bonus: Премия
    """
    return work_hours * salary_per_hours + cash_bonus


name, hours, salary_hours, bonus = sys.argv

print(worker_salary(float(hours), float(salary_hours), float(bonus)))
