#研究手法2 頭部が最も大きい画像一枚を残す
#黒色(頭部以外)が最も要素の少ない画像の抜き出し
#base_folder = "/workspace/research2/class1"で適用フォルダ名を指定

import os
from PIL import Image
import numpy as np

def find_least_black(images_folder):
    # 画像ファイルの一覧を取得
    image_files = [f for f in os.listdir(images_folder) if f.endswith('.png')]

    least_black_images = []
    least_black_percentage = float('inf')

    for image_file in image_files:
        # 画像の読み込み
        image_path = os.path.join(images_folder, image_file)
        img = Image.open(image_path)

        # 画像の黒い領域の割合を計算
        black_pixels = np.sum(np.array(img) == 0)
        total_pixels = img.size[0] * img.size[1]
        black_percentage = black_pixels / total_pixels

        # 黒い部分が最も少ない画像を記録
        if black_percentage < least_black_percentage:
            least_black_percentage = black_percentage
            least_black_images = [image_path]
        elif black_percentage == least_black_percentage:
            # 同じ割合の場合はリストに追加
            least_black_images.append(image_path)

    # 中央に近い画像を選択
    middle_index = len(least_black_images) // 2
    return least_black_images[middle_index]

def process_patient_folder(patient_folder):
    modalities = ['FLAIR', 'T1w', 'T1wCE', 'T2w']
    for modality in modalities:
        modality_folder = os.path.join(patient_folder, modality)

        # 欠損している場合はスキップ
        if not os.path.exists(modality_folder):
            continue

        least_black_image = find_least_black(modality_folder)

        # 選択された画像以外を削除
        for image_file in os.listdir(modality_folder):
            if image_file != os.path.basename(least_black_image):
                os.remove(os.path.join(modality_folder, image_file))

def process_all_patients(base_folder):
    patient_folders = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
    for patient_folder in patient_folders:
        patient_folder_path = os.path.join(base_folder, patient_folder)
        process_patient_folder(patient_folder_path)

if __name__ == "__main__":
    base_folder = "/workspace/research2/class2"
    process_all_patients(base_folder)
