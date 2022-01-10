# calculate and visualize lifespan statistics
# find lifespan estimate at this website
# https://www.blueprintincome.com/tools/life-expectancy-calculator-how-long-will-i-live/

from datetime import date

birth_date = date(1997, 11, 22)
today = date.today()
death_date = date((1997 + 96), 11, 22)
retire_date = date((1997 + 65), 11, 22)


def calc_lifespan(birth, day, death, retire):
    days_lived = (day - birth).days
    weeks_lived = days_lived / 7
    years_lived = days_lived / 365

    days_left = (death - day).days
    weeks_left = days_left / 7
    years_left = days_left / 365

    retired_days = (death - retire).days
    retired_weeks = retired_days / 7

    total_days = (death - birth).days
    total_weeks = total_days / 7
    percent_lived = (days_lived / total_days) * 100
    percent_lived = round(percent_lived, 2)
    percent_retired = (retired_days / total_days) * 100

    print('birth : ', birth_date)
    print('today : ', today)
    print('estimated death : ', death_date)
    print('')
    print(days_lived, ' days lived, ', percent_lived, '% lived')
    print(weeks_lived, ' weeks lived')
    print(years_lived, ' years lived')
    print('')
    print(days_left, ' days left,', percent_retired, ' % of all days will be spent retired')
    print(weeks_left, ' weeks left')
    print(years_left, ' years left')

    week_counter = 0
    for i in range(0, int(total_weeks)):
        if i <= weeks_lived:
            print('o', end='')
        elif weeks_lived < i < (total_weeks - retired_weeks):
            print('.', end='')
        elif i > (total_weeks - retired_weeks):
            print('R', end='')
        if week_counter % 156 == 2:
            print('\n', end='')
        week_counter += 1


calc_lifespan(birth=birth_date, day=today, death=death_date, retire=retire_date)
