#提案手法7 膠芽腫が最も大きく映っている画像を選出(未完成)
#opencvの導入が必要
#画像をグレースケールで読み込み画像を2値化させ腫瘍の領域を強調させる
#画像内の輪郭を検出して面積が最大のものを探索し、面積が最大のものを膠芽腫の領域として設定
#他画像の領域範囲と比べ、最も大きい画像を選択し、それ以外は削除
import os
import cv2

def find_largest_tumor_image(image_folder):
    # 画像ファイルを取得
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]

    # 画像を読み込み、面積が最大の腫瘍を持つ画像を選択
    largest_tumor_image = None
    max_tumor_area = 0

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, binary_image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 輪郭が存在する場合
        if contours:
            tumor_area = cv2.contourArea(max(contours, key=cv2.contourArea))
            if tumor_area > max_tumor_area:
                max_tumor_area = tumor_area
                largest_tumor_image = image_file

    return largest_tumor_image

def process_patient_folder(patient_folder):
    modalities = ['FLAIR', 'T1w', 'T1wCE', 'T2w']

    for modality in modalities:
        modality_folder = os.path.join(patient_folder, modality)

        # フォルダが存在しない場合はスキップ
        if not os.path.exists(modality_folder):
            continue

        selected_image = find_largest_tumor_image(modality_folder)

        if selected_image:
            # 選択された画像以外を削除
            for image_file in os.listdir(modality_folder):
                if image_file != selected_image:
                    os.remove(os.path.join(modality_folder, image_file))

def main(input_folder):
    patient_folders = [f for f in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, f))]

    for patient_folder in patient_folders:
        patient_path = os.path.join(input_folder, patient_folder)
        process_patient_folder(patient_path)

if __name__ == "__main__":
    input_folder = '/workspace/research5/class2'
    main(input_folder)
