import re

dict1 = {"台北市":6, "台中市":8, "台南市":3}

city = str(input("請輸入查詢的城市名稱:"))

if city in dict1:
    print(f"{city} 今天的 AQI 值為: {dict1[city]}")
else:
    AQI = int(input("AQI 值為:"))
    dict1[city] = AQI
    
print("各城市 AQI 情況:")
print("=======================")
print("城市     AQI")
print("-----------------------")

for key, value in dict1.items():
    print(f"{key}   {value}")
    
print("AQI 值由高至低排序")
print("=======================")
print("城市     AQI")
print("-----------------------")

dict2 = dict(sorted(dict1.items(), key = lambda k:(k[1] , k[0]), reverse= True))
for key, value in dict2.items():
    print(f"{key}   {value}")
    
print("=======================")
inputStr = re.sub(r'[^\w\s]','', input("請輸入詩詞:"))
print("-----------------------")

dict3 = {}
for value in inputStr:
    if value not in dict3: dict3[value] = 0
    dict3[value] = dict3[value] + 1
        
dict3 = dict(sorted(dict3.items(), key = lambda k:(k[1] , k[0]), reverse= True))

ans1 = -1
ans2 = []
ans3 = []

for key, value in dict3.items():
    if ans1 == -1 : ans1 = value 
    if ans1 == value : ans2.append(key)
    if value == 1 : ans3.append(key)
    
print(f"重複最多 {ans1} 次的字:")
print(f"[{ans2}]")
print(f"共有 {len(ans2)} 字")
print("-----------------------")
print("不重複:")
print(f"{ans3}")
print(f"共有 {len(ans3)} 字")