import sys
import time
from datetime import datetime

token = str(sys.argv[1]).lower().strip()

if token == 'now':
    ts = int(time.time())
    print('Epoch: ' + str(ts))
else:
    ts = int(token)

dt_format = '%a, %d %b %Y %H:%M:%S '
dt_utc = datetime.utcfromtimestamp(ts)
dt_local = datetime.fromtimestamp(ts)

delta = dt_local - dt_utc
print(dt_local.strftime(dt_format) + time.strftime('%z', time.gmtime()))
print(dt_utc.strftime(dt_format) + 'GMT')
