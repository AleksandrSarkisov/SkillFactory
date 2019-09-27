import json

firstFile = open("Модуль B2. Контейнеры в Python. Python для веб-разработки. Шаблонизаторы/B2.14 Парсер журналов событий/data_500.json")
secondFile = open("Модуль B2. Контейнеры в Python. Python для веб-разработки. Шаблонизаторы/B2.14 Парсер журналов событий/data_3000.json")
userAgentNameSet = set()
sumPays = 0
itemFavEventDic = {}

for line in secondFile.readlines():
    jsonObject = json.loads(line)
    if jsonObject["eventType"] == "itemFavEvent" and not jsonObject["detectedDuplicate"] and not jsonObject["detectedCorruption"]:
        if itemFavEventDic.get(jsonObject["item_id"]) is None:
            itemFavEventDic[jsonObject["item_id"]] = 1
        else:
            itemFavEventDic[jsonObject["item_id"]] += 1
    #userAgentNameSet.add(jsonObject["userAgentName"])
    #if jsonObject["eventType"] == "itemBuyEvent" and not (jsonObject["detectedDuplicate"] or jsonObject["detectedCorruption"]):
    #    sumPays += jsonObject["item_price"]

for id in itemFavEventDic:
    if itemFavEventDic[id] == max(itemFavEventDic.values()):
        print(id)
