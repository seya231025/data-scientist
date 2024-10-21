#Level1：タイタニック号の乗客データ（titanic.csv）があり、乗客の年齢、性別、客室クラスなどの情報から、生存者を予測するモデルを作成する。

import pandas as pd

#csv読み込み
titanic_data = pd.read_csv('csv/titanic.csv')

#データフレーム化
titanic_df = pd.DataFrame(titanic_data)

#先頭５行を表示
print(titanic_df.head().to_markdown(index=False, numalign="left", stralign="left"))