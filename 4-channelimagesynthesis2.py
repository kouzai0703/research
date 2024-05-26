#4ch化その2
#これが正解1,3は無駄

import os
import numpy as np
from PIL import Image

def merge_and_save_images(patient_folder_path, output_folder):
    # FLAIR, T1wCE, T2w, T1wのフォルダパス
    flair_folder = os.path.join(patient_folder_path, "FLAIR")
    t1wce_folder = os.path.join(patient_folder_path, "T1wCE")
    t2w_folder = os.path.join(patient_folder_path, "T2w")
    t1w_folder = os.path.join(patient_folder_path, "T1w")

    # FLAIR, T1wCE, T2w, T1wのフォルダが存在するか確認
    if os.path.exists(flair_folder) and os.path.exists(t1wce_folder) and os.path.exists(t2w_folder) and os.path.exists(t1w_folder):
        # 各画像のパスを取得
        flair_path = os.path.join(flair_folder, os.listdir(flair_folder)[0])
        t1wce_path = os.path.join(t1wce_folder, os.listdir(t1wce_folder)[0])
        t2w_path = os.path.join(t2w_folder, os.listdir(t2w_folder)[0])
        t1w_path = os.path.join(t1w_folder, os.listdir(t1w_folder)[0])

        # 画像を開く
        flair_img = Image.open(flair_path)
        t1wce_img = Image.open(t1wce_path)
        t2w_img = Image.open(t2w_path)
        t1w_img = Image.open(t1w_path)

        # すべての画像を同じサイズにリサイズ
        target_size = (512, 512)
        flair_img = flair_img.resize(target_size)
        t1wce_img = t1wce_img.resize(target_size)
        t2w_img = t2w_img.resize(target_size)
        t1w_img = t1w_img.resize(target_size)

        # 各画像をnumpy arrayに変換
        flair_array = np.array(flair_img)
        t1wce_array = np.array(t1wce_img)
        t2w_array = np.array(t2w_img)
        t1w_array = np.array(t1w_img)

        # 各画像を0から255の範囲に正規化
        flair_array = (flair_array / flair_array.max() * 255).astype('uint8')
        t1wce_array = (t1wce_array / t1wce_array.max() * 255).astype('uint8')
        t2w_array = (t2w_array / t2w_array.max() * 255).astype('uint8')
        t1w_array = (t1w_array / t1w_array.max() * 255).astype('uint8')

        # RGBに変換
        merged_array = np.stack((flair_array, t1wce_array, t2w_array, t1w_array), axis=-1)

        # Aチャネルを透明度として設定
        merged_array[:, :, 3] = 255  # T1wノードは透明ノードではないため、透明度を255に設定

        # 4つの画像を合成したImageに変換
        merged_img = Image.fromarray(merged_array)

        # 保存先パス
        output_path = os.path.join(output_folder, f"{os.path.basename(patient_folder_path)}.png")

        # 保存
        merged_img.save(output_path)
        print(f"Merged and saved: {output_path}")

# 対象ディレクトリ
input_folder = "/workspace/research4/class2"
output_folder = "/workspace/research4/class2-4ch"

# 各患者フォルダに対して処理
for patient_folder_name in os.listdir(input_folder):
    patient_folder_path = os.path.join(input_folder, patient_folder_name)
    merge_and_save_images(patient_folder_path, output_folder)
