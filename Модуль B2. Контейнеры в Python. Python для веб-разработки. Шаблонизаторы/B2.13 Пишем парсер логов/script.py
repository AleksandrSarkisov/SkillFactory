import re
import collections

file = open("Модуль B2. Контейнеры в Python. Python для веб-разработки. Шаблонизаторы\B2.13 Пишем парсер логов\dummy-access.log")
ipMask = "\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
ipList = []

f = file.readlines()
for line in f:
    ipList.append(re.search(ipMask, line)[0])

ipCount = collections.Counter(ipList)
print(ipCount["79.136.245.135"])
print(ipCount["127.0.0.1"])
print(ipCount.most_common(1))
print(sum(ipCount.values())/len(ipCount))
