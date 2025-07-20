'''
한국사 - 일제강점기 통계 분석 (학생)
'''

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["figure.dpi"] = 100

df = pd.read_csv('./공립국민학교_학생변동.csv')
fig, ax = plt.subplots(2, 2)

plt.suptitle('공립국민학교 학생변동 (1911년~1942년) 분석')

df.plot(kind='area', x='시점', y='합계_입학', ax=ax[0][0], label='합계 입학', color='aqua')
df.plot(kind='area', x='시점', y='남_입학', ax=ax[0][0], label='남자 입학', color='deepskyblue')
df.plot(kind='area', x='시점', y='여_입학', ax=ax[0][0], label='여자 입학', color='dodgerblue')

df.plot(kind='area', x='시점', y='합계_졸업', ax=ax[0][1], label='합계 졸업', color='greenyellow')
df.plot(kind='area', x='시점', y='남_졸업', ax=ax[0][1], label='남자 졸업', color='lawngreen')
df.plot(kind='area', x='시점', y='여_졸업', ax=ax[0][1], label='여자 졸업', color='lime')

df.plot(kind='area', x='시점', y='합계_퇴학', ax=ax[1][0], label='합계 퇴학', color='fuchsia')
df.plot(kind='area', x='시점', y='남_퇴학', ax=ax[1][0], label='남자 퇴학', color='mediumorchid')
df.plot(kind='area', x='시점', y='여_퇴학', ax=ax[1][0], label='여자 퇴학', color='darkorchid')

df.plot(kind='area', x='시점', y='합계_사망', ax=ax[1][1], label='합계 사망', color='orange')
df.plot(kind='area', x='시점', y='남_사망', ax=ax[1][1], label='남자 사망', color='tomato')
df.plot(kind='area', x='시점', y='여_사망', ax=ax[1][1], label='여자 사망', color='red')

ax[0][0].set_title('입학')
ax[0][1].set_title('졸업')
ax[1][0].set_title('퇴학')
ax[1][1].set_title('사망')

ax[0][0].set_ylim([0, 32000])
ax[0][1].set_ylim([0, 32000])
ax[1][0].set_ylim([0, 32000])
ax[1][1].set_ylim([0, 400])

ax[0][0].set_xlabel('연도(1911년~1942년)')
ax[0][0].set_ylabel('학생 수(단위: 명)')
ax[0][1].set_xlabel('연도(1911년~1942년)')
ax[0][1].set_ylabel('학생 수(단위: 명)')
ax[1][0].set_xlabel('연도(1911년~1942년)')
ax[1][0].set_ylabel('학생 수(단위: 명)')
ax[1][1].set_xlabel('연도(1911년~1942년)')
ax[1][1].set_ylabel('학생 수(단위: 명)')

plt.style.use('ggplot')
plt.legend()
plt.show()
