#指定されたフォルダ内の画像を最低先のフォルダの1,2,3,4,5内に2:2:2:2:2の割合で保存する
#交差検証用の画像分割
#乱数は固定ではなくランダム

import os
import random
import shutil
import numpy as np

#乱数を固定
np.random.seed(1234)
random.seed(1234)

def copy_images(source_folder, dest_folder, ratios):
    # 画像ファイルを読み込む
    image_files = [f for f in os.listdir(source_folder) if f.endswith(".png")]

    # 選択済みの画像を保持するセット
    selected_images_set = set()

    # 各クラスに割り当てる画像数を計算
    total_images = len(image_files)
    total_ratios = sum(ratios)
    images_per_class = [int(total_images * ratio / total_ratios) for ratio in ratios]

    # ランダムに画像を選択しコピー
    for class_id, count in enumerate(images_per_class, start=1):
        # まだ選ばれていない画像から選ぶ
        available_images = list(set(image_files) - selected_images_set)
        selected_images = random.sample(available_images, count)
        #selected_images = random.sample(available_images, count)

        # 選ばれた画像をセットに追加
        selected_images_set.update(selected_images)

        for image in selected_images:
            source_path = os.path.join(source_folder, image)
            dest_path = os.path.join(dest_folder, str(class_id), image)

            # フォルダが存在しない場合は作成
            os.makedirs(os.path.join(dest_folder, str(class_id)), exist_ok=True)

            # 画像をコピー
            shutil.copyfile(source_path, dest_path)

if __name__ == "__main__":
    source_folder = "/workspace/research3/class2-3ch"
    dest_folder = "/workspace/research3/randomtest"

    # クラスごとの割合 (1:1:1:1:1)
    class_ratios = [2, 2, 2, 2, 2]

    copy_images(source_folder, dest_folder, class_ratios)
