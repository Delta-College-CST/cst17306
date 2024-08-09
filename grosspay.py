# This program receives hours worked and pay rate for an hourly
# worker.  It calcualates gross pay based on standard overtime rules.

BASE_HOURS = 40.0
  
hours  = float(input("Enter hours worked: "))
rate   = float(input("Enter pay rate: "))

if hours <= BASE_HOURS:
    pay = hours * rate
else:
    pay = hours * BASE_HOURS + (hours - BASE_HOURS) * 1.5 * rate

print("For", hours, "hours, Pay = $%7.2f" % (pay))
