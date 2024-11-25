import pandas as pd
import os
import logging

# ロギング設定：INFOレベル以上のログを出力
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_titanic_data(titanic_data: str = "titanic.csv"):
    """
    タイタニック号の乗客データを分析し、生存者数や客室クラスごとの統計を計算します。

    Args:
        titanic_data (str): 分析するCSVファイル名またはパス。デフォルトは'titanic.csv'。

    Returns:
        dict: 分析結果を含む辞書形式のデータ。
    """
    logger.info(f"Starting analysis for file: {titanic_data}")
    
    # 現在のスクリプトのディレクトリを基準にCSVファイルのフルパスを解決
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, "..", "csv", titanic_data)

    # ファイルの存在確認
    if not os.path.exists(full_path):
        logger.error(f"File not found at {full_path}")
        return {"error": f"File not found at {full_path}"}

    # CSVデータを読み込む
    try:
        titanic_df = pd.read_csv(full_path)
        logger.info("CSV file successfully loaded.")
    except Exception as e:
        logger.error(f"Failed to load data: {str(e)}")
        return {"error": f"Failed to load data: {str(e)}"}

    # 必要な列が存在するか確認
    required_columns = ["survived", "pclass"]  # 必須列を指定
    missing_columns = [col for col in required_columns if col not in titanic_df.columns]
    if missing_columns:
        logger.error(f"Missing required columns: {missing_columns}")
        return {"error": f"Missing required columns: {missing_columns}"}

    # 生存者数と非生存者数を計算
    survived_count = (titanic_df["survived"] == 1).sum()
    nosurvived_count = (titanic_df["survived"] == 0).sum()
    logger.info(f"Survived: {survived_count}, Not Survived: {nosurvived_count}")

    # 客室クラスごとの総数を計算
    class_survivors = {
        "1st_class": (titanic_df["pclass"] == 1).sum(),
        "2nd_class": (titanic_df["pclass"] == 2).sum(),
        "3rd_class": (titanic_df["pclass"] == 3).sum(),
    }

    # 客室クラスごとの生存者数を計算
    class_survivor_counts = {
        "1st_class_survived": titanic_df[(titanic_df["pclass"] == 1) & (titanic_df["survived"] == 1)].shape[0],
        "2nd_class_survived": titanic_df[(titanic_df["pclass"] == 2) & (titanic_df["survived"] == 1)].shape[0],
        "3rd_class_survived": titanic_df[(titanic_df["pclass"] == 3) & (titanic_df["survived"] == 1)].shape[0],
    }

    # データ整合性チェック：各クラスの生存者数合計が全体の生存者数と一致するか
    total_survived_by_class = sum(class_survivor_counts.values())
    is_data_consistent = total_survived_by_class == survived_count
    if not is_data_consistent:
        logger.warning("Data inconsistency detected: Class survivor counts do not match total survivors.")

    logger.info("Analysis complete.")

    result = {
        'summary': {
            'survived_count': survived_count,
            'nosurvived_count': nosurvived_count,
            'data_consistency': is_data_consistent,
        },
        'class_analysis': {
            'total_counts': class_survivors,
            'survived_counts': class_survivor_counts,
        },
    }

    # 結果のデバッグ出力
    print(result)

    return result
