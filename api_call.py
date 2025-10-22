import os
import requests
import dotenv
import json

# 문제
# 2015년 1월부터 2024년 12월까지의
# 개인 유형
# 현년 
# 전기(EUS), 가스(GUS), 수도(WUS), 지역난방(HUS) 에너지 사용량 데이터

# API KEY
dotenv.load_dotenv()
api_key = os.getenv('API_KEY')


# 2015년 1월부터 2024년 12월까지
def get_year_months():
    year_months=[]
    for year in range(2015, 2024+1):
        for month in range(1, 12+1):
            year_months.append((year, f"{month:02d}"))
    return year_months

# Request parameters
params = {
    'KEY': api_key,
    'TYPE': 'json',
    'SERVICE': 'energyUseDataSummaryInfo',
    'START_INDEX': 1,
    'END_INDEX': 100,
    'YEAR': '2015',
    'MONTH': '01',
} 


responses = []

for year_month in get_year_months():
    year, month = year_month
    params['YEAR'] = str(year)
    params['MONTH'] = month
    
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/{params['TYPE']}/{params['SERVICE']}/{params['START_INDEX']}/{params['END_INDEX']}/{params['YEAR']}/{params['MONTH']}"
    response = requests.get(url, params=params)

    
    if response.status_code == 200:
        print(f"{year}-{month}: API 호출 성공!🚀") 
        data = response.json().get('energyUseDataSummaryInfo', {}).get('row', [])
        if data:
            responses.extend(data)
    else:
        print("호출 실패 😞:", response.status_code)



# JSON 파일로 저장
json_file = "energy_data_2015_2024.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(responses, f, ensure_ascii=False, indent=2)

print(f"💾 {json_file} 저장 완료!")