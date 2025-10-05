import time
from datetime import datetime

for i in range(5):
    print("Текущее время:", datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)  # задержка 1 секунда
