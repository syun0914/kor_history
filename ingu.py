'''
한국사 - 일제강점기 통계 분석 (인구)
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit


def func(x, a, b):
    return a * np.exp(b * x)


def func1(x, a, b):
    return a * x + b


plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["figure.dpi"] = 150

df = pd.read_csv('./시군도별_호구_및_인구_20240118214243.csv')
year = np.arange(11, 44)
year2 = np.arange(11, 125)
cases = df['인구수 (명)'].to_numpy() / 10000

popt, pcov = curve_fit(func, year, cases)

plt.plot(year, cases, 'co', label='전국 인구(1911년~1943년)')
plt.plot(
    year2,
    func(year2, *popt),
    'r-',
    label='지수함수(a*e^b)의 계수: a = %5.3f, b = %5.3f' % tuple(popt)
)

point = (124, func(124, *popt))

plt.plot(*point, label=f'2024년: {int(point[1]*10000):,d}명')
plt.style.use('ggplot')
plt.xlabel('연도(1911년~2024년)')
plt.ylabel('인구(단위: 만 명)')
plt.title('시군도별 호구 및 인구(1911년~1943년) 분석')
plt.legend()
plt.show()
