#研究手法4 頭部がきれいに映っていない最初、最後の画像前後10枚を削除し平均画像を作成
#頭部が映るのは大体何枚目からかを確認しておく
#指定先のファイル内の画像を平均画像化
#opencvの導入が必要

import os
import cv2
import numpy as np

def create_average_image(patient_dir, modality):
    # 画像を読み込んで平均画像を作成
    images = []
    for root, dirs, files in os.walk(os.path.join(patient_dir, modality)):
        # 画像ファイルをファイル名でソート
        files.sort()

        # 最初から10枚と最後から10枚を削除
        files = files[10:-10]

        for file in files:
            # 画像の読み込み
            image_path = os.path.join(root, file)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            images.append(image)

    if not images:
        return  # 画像がない場合は何もしない

    # 画像の平均を計算
    average_image = np.mean(images, axis=0).astype(np.uint8)

    # 平均画像以外の画像を削除
    for root, dirs, files in os.walk(os.path.join(patient_dir, modality)):
        for file in files:
            image_path = os.path.join(root, file)
            if image_path != os.path.join(root, f"{modality}_average.png"):
                os.remove(image_path)

    # 平均画像を保存
    output_path = os.path.join(patient_dir, modality, f"{modality}_average.png")
    cv2.imwrite(output_path, average_image)

def process_patients(root_dir):
    for patient_dir in os.listdir(root_dir):
        patient_path = os.path.join(root_dir, patient_dir)
        if os.path.isdir(patient_path):
            for modality in ["FLAIR", "T1w", "T1wCE", "T2w"]:
                create_average_image(patient_path, modality)

if __name__ == "__main__":
    root_directory = "/workspace/research4/class2"
    process_patients(root_directory)
