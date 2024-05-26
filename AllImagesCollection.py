#指定したファイル+フォルダーの中にある画像を指定先のフォルダへそのまま移動
#class1,2のファイル内の画像をAllImagesClass1,2へコピーし移動を行う
#研究ですべての画像を使用するAllImages用

import os
import shutil

def copy_images(source_folder, destination_folder):
    # フォルダ内のすべての患者ファイルを取得
    patient_folders = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

    for patient_folder in patient_folders:
        patient_path = os.path.join(source_folder, patient_folder)
        modalities = ['FLAIR', 'T1w', 'T1wCE', 'T2w']
        folders_to_copy = []

        # 存在するフォルダをリストに追加
        for modality in modalities:
            modality_folder = os.path.join(patient_path, modality)
            if os.path.exists(modality_folder):
                folders_to_copy.append(modality_folder)

        # フォルダが存在する場合に画像をコピー
        if folders_to_copy:
            for modality_folder in folders_to_copy:
                images = [f for f in os.listdir(modality_folder) if f.endswith('.png')]

                for image in images:
                    # ファイル名が被らないように連番を付け加える
                    dest_image_name = f"{patient_folder}_{os.path.basename(modality_folder)}_{image}"
                    dest_image_path = os.path.join(destination_folder, dest_image_name)
                    shutil.copyfile(os.path.join(modality_folder, image), dest_image_path)

if __name__ == "__main__":
    source_folder = '/workspace/AllImages/class2'
    destination_folder = '/workspace/AllImages/AllImagesClass2'
    copy_images(source_folder, destination_folder)
