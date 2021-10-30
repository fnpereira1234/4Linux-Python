import datetime

agora = datetime.datetime.now()
print(agora)
data_nasc = datetime.datetime(1980, 3, 20)

delta = agora - data_nasc

print(delta)
print(delta.total_seconds())
