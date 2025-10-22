import matplotlib.pyplot as plt
import pandas as pd


# 계절별 가스 사용량 평균
# 막대 그래프로 시각화 
# 각 막대에 구체적인 수치를 표시

# 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'

data = pd.read_json('preprocessed_energy_data.json')

seasonal_gas_usage = data.groupby('SEASON')['GUS'].mean()
seasonal_gas_usage = seasonal_gas_usage.reindex(['봄', '여름', '가을', '겨울'])

seasons = seasonal_gas_usage.index
avg_gas_usage = seasonal_gas_usage.values

plt.bar(seasons, avg_gas_usage, width=0.5)
plt.title("계절별 가스 사용량 평균 - 5979", pad=15)
plt.xlabel("계절")
plt.ylabel("평균 가스 사용량")
plt.grid(axis='y', linestyle='--', alpha=0.3)

for i, v in enumerate(avg_gas_usage):
    plt.text(i, v*1.01, f"{v:,.0f}", ha='center', fontsize=8 )
    
plt.savefig("seasonal_gas_usage_5979.png")
plt.show()