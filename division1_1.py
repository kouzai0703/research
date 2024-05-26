#シード値固定で指定元フォルダ内の画像を指定先フォルダ内へ1:1で画像分割
#8:1:1交差検証用

import os
import random
import shutil

def move_images(source_folder, dest_folder, split_ratio, random_seed=1234):
    # シード値を設定
    random.seed(random_seed)

    # 対象フォルダが存在しない場合は終了
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' not found.")
        return

    # 指定先フォルダが存在しない場合は作成
    os.makedirs(dest_folder, exist_ok=True)

    # 画像ファイルのリストを取得
    image_files = [f for f in os.listdir(source_folder) if f.endswith(".png")]

    # ランダムな順番で画像を選択
    random.shuffle(image_files)

    # 分割するインデックスを計算
    split_index = int(len(image_files) * split_ratio)

    # ランダムに選ばれた画像を指定先フォルダに移動
    for image_file in image_files[:split_index]:
        source_path = os.path.join(source_folder, image_file)
        dest_path = os.path.join(dest_folder, image_file)
        shutil.move(source_path, dest_path)

if __name__ == "__main__":
    source_folder = "/workspace/AllImages/AllImages-8:1:1-51234/val/class2"
    dest_folder = "/workspace/AllImages/AllImages-8:1:1-51234-test/val/class2"
    split_ratio = 0.5  # 画像を半分に分割する

    move_images(source_folder, dest_folder, split_ratio)
