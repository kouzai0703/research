#指定元と指定先ファイル内の画像の名前を比較し、何パーセント合致するかを調査
#crossentropy用で分割している画像が各提案手法において本当に同じ画像を用いているかの調査用
#100%なら、各提案手法ごとで学習、val,testに用いられている画像は同じと判断できる
#各提案手法毎にそれぞれの生成した画像になっているか確認しておく

import os

def calculate_overlap_ratio(folder1, folder2):
    # それぞれのフォルダから画像ファイルの名前を取得
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))

    # 両方のフォルダに存在する画像ファイルの数を計算
    common_files_count = len(files1.intersection(files2))

    # それぞれのフォルダの画像ファイルの総数を取得
    total_files1 = len(files1)
    total_files2 = len(files2)

    # 同じ名前のデータが存在する割合を計算
    overlap_ratio = common_files_count / max(total_files1, total_files2) * 100

    return overlap_ratio

if __name__ == "__main__":
    source_folder = "/workspace/AllImages/AllImages-8:1:1-12345-test/val/class1"
    dest_folder = "/workspace/AllImages/AllImages-8:1:1-34512-test/val/class1"

    ratio = calculate_overlap_ratio(source_folder, dest_folder)

    print(f"Overlap Ratio: {ratio:.2f}%")
