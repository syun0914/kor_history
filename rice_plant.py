'''
한국사 - 일제강점기 통계 분석 (벼 시세)
'''

import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["figure.dpi"] = 150

df = pd.read_csv('./벼_시세_20240121103523.csv')

ax = plt.gca()

df.plot(
    x='시점',
    y='상',
    ax=ax,
    label=f'상 (최댓값:최솟값 = {df['상'].max()/df['상'].min():.5f}:1)',
    color='aqua'
)
df.plot(
    x='시점',
    y='중',
    ax=ax,
    label=f'중 (최댓값:최솟값 = {df['중'].max()/df['중'].min():.5f}:1)',
    color='deepskyblue'
)
df.plot(
    x='시점',
    y='하',
    ax=ax,
    label=f'하 (최댓값:최솟값 = {df['하'].max()/df['하'].min():.5f}:1)',
    color='dodgerblue'
)

ax.set_title('벼 시세(1914년 1월~1935년 12월) 분석')
ax.set_xlabel('시간(1914년 1월~1935년 12월)')
ax.set_ylabel('시세[단위: 원/1석(石)]')

plt.style.use('ggplot')
plt.legend()
plt.show()
