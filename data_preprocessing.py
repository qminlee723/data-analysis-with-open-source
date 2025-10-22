import pandas as pd

data = pd.read_json('energy_data_2015_2024.json', dtype={'YEAR': str, 'MON': str})
pd.set_option('display.float_format', '{:.0f}'.format) 

df = pd.DataFrame(data)

df = df[df['MM_TYPE'] == '개인']

# print("✅ 기본 정보: ")
# print(df.info())
# print("\n✅기본 통계량: ")
# print(df.describe())


def month_to_season(month):
    if month in ['03', '04', '05']:
        return '봄'
    elif month in ['06', '07', '08']:
        return '여름'
    elif month in ['09', '10', '11']:
        return '가을'
    else:
        return '겨울'
    
df['SEASON'] = df['MON'].apply(month_to_season)

selected_col = df[['YEAR', 'SEASON', 'EUS', 'WUS', 'GUS', 'HUS']]

print("✅ 선택 컬럼 첫 5개: ")
print(selected_col.head(5))


# JSON 파일로 저장
selected_col.to_json('preprocessed_energy_data.json', orient='records', force_ascii=False, indent=2)