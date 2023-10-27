# -*- coding: utf-8 -*-
"""
"""

import os
import re
import pandas as pd

user_name = os.environ['USERPROFILE'].replace('\\', '/')
user_desktop = user_name + '/Desktop/'

input_file = '目標1 www.example.co.jp ページ 20200101-20211231.xlsx'
searched = re.search(r'(.+)www.+', input_file)
output_file = searched.group(1) + 'pagepath_cvr_uniquepageview.xlsx'

df = pd.read_excel(user_desktop + input_file, sheet_name='データセット1')
df = df[['ページ', 'セグメント', 'ページ別訪問数']].dropna()

df_cv = df[df['セグメント'].str.match('.*目標.*')]
df_all = df[df['セグメント'].str.match('.*すべて.*')]

df_merge = pd.merge(df_cv, df_all, how='left', on='ページ')
df_merge = df_merge[['ページ', 'ページ別訪問数_x', 'ページ別訪問数_y']]
df_merge = df_merge.rename(columns={'ページ別訪問数_x': '目標_ページ別訪問数', 'ページ別訪問数_y': 'すべてのユーザー_ページ別訪問数'})
df_merge['CVR'] = df_merge['目標_ページ別訪問数'] / df_merge['すべてのユーザー_ページ別訪問数'] * 100
df_merge['CVR'] = round(df_merge['CVR'], 2)

# 列の並び替え
df_merge = df_merge[['ページ', 'すべてのユーザー_ページ別訪問数', 'CVR', '目標_ページ別訪問数']]

df_merge.to_excel(user_desktop + output_file, index=False)
