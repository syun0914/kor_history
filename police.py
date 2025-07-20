'''
한국사 - 일제강점기 통계 분석 (경찰)
'''

import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./경찰관서_및_직원_20240123161118.csv')
fig, ax = plt.subplots(2, 2)

plt.suptitle('경찰관서 및 직원(1914년~1941년) 분석')

df.plot(
    kind='line',
    x='시점',
    y='경찰관주재소',
    ax=ax[0][0],
    label=f'경찰관주재소 (1914년:1941년 = 1:{df['경찰관주재소'].max()/df['경찰관주재소'].min():5.3f})',
    color='red'
)
df.plot(
    kind='line',
    x='시점',
    y='경찰관파출소',
    ax=ax[0][0],
    label=f'''경찰관파출소 (1914년:1941년 = 1:{
        df['경찰관파출소'].max()/df['경찰관파출소'].min():5.3f})''',
    color='orange'
)
df.plot(
    kind='line',
    x='시점',
    y='경찰서',
    ax=ax[0][0],
    label=f'경찰서 (1914년:1941년 = 1:{df['경찰서'].max()/df['경찰서'].min():5.3f})',
    color='lawngreen'
)
df.plot(
    kind='line',
    x='시점',
    y='경찰관출장소',
    ax=ax[0][0],
    label='경찰관출장소',
    color='aqua'
)

df.plot(
    kind='area',
    x='시점',
    y='경찰관리(합계)',
    ax=ax[0][1],
    label='경찰관리(합계, 100%)',
    color='greenyellow'
)
df.plot(
    kind='area',
    x='시점',
    y='조선인경찰관리',
    ax=ax[0][1],
    label=f'조선인경찰관리({df['조선인경찰관리'].sum()/df['경찰관리(합계)'].sum()*100:5.3f}%)',
    color='lawngreen'
)
df.plot(
    kind='area',
    x='시점',
    y='일본인경찰관리',
    ax=ax[0][1],
    label=f'일본인경찰관리({df['일본인경찰관리'].sum()/df['경찰관리(합계)'].sum()*100:5.3f}%)',
    color='lime'
)

df.plot(kind='line', x='시점', y='경부보(조선인)', ax=ax[1][0], label='경부보(조선인)', color='fuchsia')
df.plot(kind='line', x='시점', y='경부보(일본인)', ax=ax[1][0], label='경부보(일본인)', color='mediumorchid')

df.plot(kind='line', x='시점', y='순사(조선인)', ax=ax[1][1], label='순사(조선인)', color='orange')
df.plot(kind='line', x='시점', y='순사(일본인)', ax=ax[1][1], label='순사(일본인)', color='tomato')

ax[0][0].set_title('경찰관서')
ax[0][1].set_title('경찰관리')
ax[1][0].set_title('경부보')
ax[1][1].set_title('순사')

ax[0][0].set_xlabel('연도(1914년~1941년)')
ax[0][0].set_ylabel('경찰관서 수(단위: 개소)')
ax[0][1].set_xlabel('연도(1914년~1941년)')
ax[0][1].set_ylabel('경찰관리 수(단위: 명)')
ax[1][0].set_xlabel('연도(1914년~1941년)')
ax[1][0].set_ylabel('경부보 수(단위: 명)')
ax[1][1].set_xlabel('연도(1914년~1941년)')
ax[1][1].set_ylabel('순사 수(단위: 명)')

plt.style.use('ggplot')
plt.legend()
plt.show()
