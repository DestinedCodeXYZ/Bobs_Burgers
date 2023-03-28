import datetime
import time
x=datetime.datetime.now()
while x.strftime("%H")> '10' and x.strftime("%H")< '18':
    x=datetime.datetime.now()
        
        
