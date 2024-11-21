# 目標設定：タイタニック号の乗客データ（データ収集先：titanic.csv）があり、乗客の年齢、性別、客室クラスなどの情報から、生存者を予測するモデルを作成する。

"""
* passenger_id: 乗客ID
* survived: 生存フラグ (1: 生存, 0: 死亡)
* pclass: 客室クラス
* sex: 性別
* age: 年齢
* sibsp: タイタニック号に同乗している兄弟/配偶者の数
* parch: タイタニック号に同乗している親/子供の数
* fare: 料金
* embarked: 出港地
"""

# import
import pandas as pd
import numpy as np

# データの読み込み
def analyze_titanic_data(titanic_data: str):
    titanic_data = pd.read_csv('csv/titanic.csv')

# DataFrameの作成
    titanic_df = pd.DataFrame(titanic_data)

# 生存者の数
    survived_count = (titanic_df["survived"] == 1).sum()
# 死亡者数
    nosurvived_count = (titanic_df["survived"] == 0).sum()

# 客室クラスごとの人数
    first_class_or_higher_count = (titanic_df["pclass"] == 1).sum()
    second_class_or_higher_count = (titanic_df["pclass"] == 2).sum()
    three_class_or_higher_count = (titanic_df["pclass"] == 3).sum()

    print(f"Survived : {survived_count}, Deaths : {nosurvived_count}")

# 客室クラスごとの生存者数
    data01 = titanic_df[(titanic_df["pclass"] == 1) & (titanic_df["survived"] == 1)].shape[0]
    data02 = titanic_df[(titanic_df["pclass"] == 2) & (titanic_df["survived"] == 1)].shape[0]
    data03 = titanic_df[(titanic_df["pclass"] == 3) & (titanic_df["survived"] == 1)].shape[0]

    survived_count_pcclass = data01 + data02 + data03

    print(f"1st Class Survivors: {data01}")
    print(f"2nd Class Survivors: {data02}")
    print(f"3rd Class Survivors: {data03}")

    if survived_count_pcclass != survived_count:
        print('This count is false')
    else:
        print('This count is True')

