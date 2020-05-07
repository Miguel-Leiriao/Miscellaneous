import datetime
from datetime import timedelta

Time = datetime.datetime.utcnow()+ timedelta(hours=1)
Time = Time.isoformat()
print Time