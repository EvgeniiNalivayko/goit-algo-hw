from datetime import datetime

def get_days_from_today(date):

    input_date:datetime = datetime.strptime(date , '%Y-%m-%d')
    current_date = datetime.today()
    delta = current_date - input_date
    return delta.days

print(get_days_from_today("1999-06-10"))

