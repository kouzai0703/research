#指定先ファイル内の画像が何チャネルなのかを表示、確認

import os
import cv2

def print_channel_info(image_path):
    # 画像読み込み
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if image is not None:
        # 画像の形状を取得 (height, width, channels)
        shape = image.shape

        # チャンネル数を取得
        channels = shape[2] if len(shape) == 3 else 1

        print(f"Image: {os.path.basename(image_path)}, Channels: {channels}")
    else:
        print(f"Failed to read image: {image_path}")

def process_images(directory_path):
    # 指定ディレクトリ内の画像ファイルを処理
    for filename in os.listdir(directory_path):
        if filename.endswith(".png"):
            image_path = os.path.join(directory_path, filename)
            print_channel_info(image_path)

if __name__ == "__main__":
    target_directory = "/workspace/research4/class2-3ch"

    # 画像処理
    process_images(target_directory)
