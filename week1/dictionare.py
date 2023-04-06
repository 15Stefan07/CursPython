dictionar = {"key1": 1,
             "key2": 2,
             3: 4,
             5.3: [0, 2, 5],
             "key1": 50}
# print(dictionar, type(dictionar))
# print(dictionar.keys())
# print(dictionar.values())
# print(dictionar.items())
# dictionar.get("Key1", 100)
dictionar["key1"] = 500
dictionar.update({"Key1": 100})
print(list(dictionar))
