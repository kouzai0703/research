#指定フォルダ内の画像を指定フォルダ内へコピーし保存
#crossentropy.pyで作った1,2,3,4,5ファイルを4つをtrain,1つをvalファイルへ移動する
#交差検証用

import os
import shutil

def copy_images(source_folder, dest_train_folder, dest_val_folder):
    # 1, 2, 3, 4 ファイルから train フォルダへコピー
    for folder_name in ["5", "1", "2", "3"]:
        source_path = os.path.join(source_folder, folder_name)
        dest_path = dest_train_folder

        # 画像ファイルのみをコピー
        for image_file in os.listdir(source_path):
            if image_file.endswith(".png"):
                image_source_path = os.path.join(source_path, image_file)
                image_dest_path = os.path.join(dest_path, image_file)
                shutil.copyfile(image_source_path, image_dest_path)

    # 5 ファイルから val フォルダへコピー
    source_path = os.path.join(source_folder, "4")
    dest_path = dest_val_folder

    # 画像ファイルのみをコピー
    for image_file in os.listdir(source_path):
        if image_file.endswith(".png"):
            image_source_path = os.path.join(source_path, image_file)
            image_dest_path = os.path.join(dest_path, image_file)
            shutil.copyfile(image_source_path, image_dest_path)

if __name__ == "__main__":
    source_folder = "/workspace/AllImages/crossentropy-AllImagesClass2"
    dest_train_folder = "/workspace/AllImages/AllImages-8:1:1-51234/train/class2"
    dest_val_folder = "/workspace/AllImages/AllImages-8:1:1-51234/val/class2"

    # フォルダが存在しない場合は作成
    os.makedirs(dest_train_folder, exist_ok=True)
    os.makedirs(dest_val_folder, exist_ok=True)

    copy_images(source_folder, dest_train_folder, dest_val_folder)
