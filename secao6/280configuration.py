import locale
import calendar

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print(locale.getlocale())

print(calendar.calendar(2024))
