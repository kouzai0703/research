#指定先フォルダの画像をtrainとvalに8:2,9:1…で分割する

import os
import random
import shutil

def copy_and_delete_images(source_dir, dest_dir, fraction):
    # 1. コピー元のディレクトリから画像のリストを取得(.png,.JPEG)
    image_list = [f for f in os.listdir(source_dir) if f.endswith('.png')]

    # 2. コピー対象の画像数を計算
    num_images_to_copy = int(len(image_list) * fraction)

    # 3. 画像をランダムに選択
    images_to_copy = random.sample(image_list, num_images_to_copy)

    # 4. 画像をコピーして削除
    for image in images_to_copy:
        source_path = os.path.join(source_dir, image)
        dest_path = os.path.join(dest_dir, image)

        # 画像をコピー
        shutil.copy(source_path, dest_path)

        # コピーが成功したら元の画像を削除
        os.remove(source_path)
        print(f"Image {image} copied to {dest_dir} and deleted from {source_dir}")

# コピー元となるディレクトリ
#source_directory = "/workspace/test_images-1/train/class1"
source_directory = "/workspace/research3/research3-3ch-8:1:1-23451/val/class2"

# コピー先となるディレクトリ
#destination_directory = "/workspace/test_images-1/val/class1"
destination_directory = "/workspace/research3/research3-3ch-8:1:1-23451-test/val/class2"

# 画像のコピー割合（例: 0.2 は元画像の20%をコピー）
copy_fraction = 0.5

# コピーと削除の実行
copy_and_delete_images(source_directory, destination_directory, copy_fraction)
