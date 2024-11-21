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

import pandas as pd
import os

def analyze_titanic_data(titanic_data: str):
    # 現在のスクリプト（titanic.py）のディレクトリを基準にパスを解決
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, "..", "csv", titanic_data)  # app/csv/titanic.csvを指す

    # ファイルの存在確認
    if not os.path.exists(full_path):
        return {"error": f"File not found at {full_path}"}

    # データの読み込み
    try:
        titanic_df = pd.read_csv(full_path)
    except Exception as e:
        return {"error": f"Failed to load data: {e}"}

    # 統計情報の計算
    survived_count = (titanic_df["survived"] == 1).sum()
    nosurvived_count = (titanic_df["survived"] == 0).sum()

    # 客室クラスごとの生存者数
    class_survivors = {
        "1st_class": (titanic_df["pclass"] == 1).sum(),
        "2nd_class": (titanic_df["pclass"] == 2).sum(),
        "3rd_class": (titanic_df["pclass"] == 3).sum(),
    }
    class_survivor_counts = {
        "1st_class_survived": titanic_df[(titanic_df["pclass"] == 1) & (titanic_df["survived"] == 1)].shape[0],
        "2nd_class_survived": titanic_df[(titanic_df["pclass"] == 2) & (titanic_df["survived"] == 1)].shape[0],
        "3rd_class_survived": titanic_df[(titanic_df["pclass"] == 3) & (titanic_df["survived"] == 1)].shape[0],
    }

    # 整合性チェック
    total_survived_by_class = sum(class_survivor_counts.values())
    is_data_consistent = total_survived_by_class == survived_count

    # 結果を辞書形式で返す
    return {
        "survived_count": survived_count,
        "nosurvived_count": nosurvived_count,
        "class_counts": class_survivors,
        "class_survivor_counts": class_survivor_counts,
        "data_consistency": is_data_consistent,
    }
