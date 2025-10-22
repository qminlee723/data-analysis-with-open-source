import matplotlib.pyplot as plt
import pandas as pd

# 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'

data = pd.read_json('preprocessed_energy_data.json')
df = pd.DataFrame(data)

df['TotalUsage'] = df[['EUS', 'WUS', 'GUS', 'HUS']].sum(axis=1)

# 각 연도별 에너지 사용 총 사용량 계산
yearly_usage = df.groupby('YEAR')['TotalUsage'].sum()

# 선 그래프
plt.plot(yearly_usage, marker='o')
plt.title("연도별 에너지 사용 총액 변화 - 5979")
plt.xlabel("연도")
plt.ylabel("에너지 사용 총 사용량")
plt.xticks(yearly_usage.index)
plt.grid(linestyle='--', alpha=0.5)


plt.savefig("energy_usage_trend_5979.png")
plt.show()

