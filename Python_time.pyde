from datetime import datetime
now = datetime.now()

welcome = "welcome to the Python calendar"
instructions = "Here is today's date:"
instructions_2 = "Here is the time on a 24 hour clock:"
now
other = "You can click the run button again any other day when you want to know the date."

print welcome
print instructions
print '%02d-%02d-%02d' % (now.year,now.month,now.day)
print instructions_2
print '%02d:%02d' % (now.hour,now.minute)
print other
print "Feel free to add anything else you want to make it better or more interactive since i don't know how to make it interactive."
