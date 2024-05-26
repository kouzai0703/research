#研究画像をclass1,2ファイルへ分ける
#文字列を入力し、0ならclass1,1ならclass2へコピーし移動
#0はメチル化なし、1はメチル化あり

import os
import shutil

def copy_and_move_folders(binary_sequence, source_folder, class1_folder, class2_folder):
    # List all files in the source folder
    files = sorted(os.listdir(source_folder))

    # Iterate through each character in the binary sequence
    for i, bit in enumerate(binary_sequence):
        # Determine the destination folder based on the bit
        destination_folder = class1_folder if bit == '0' else class2_folder

        # Build paths for source and destination folders
        source_path = os.path.join(source_folder, files[i])
        destination_path = os.path.join(destination_folder, files[i])

        # Copy the folder to the corresponding class
        shutil.copytree(source_path, destination_path)

        print(f"Moved {files[i]} to {destination_folder}")

if __name__ == "__main__":
    # Input binary sequence
    binary_sequence = input("Enter a binary sequence (0 or 1): ")

    # Paths
    source_folder = "/workspace/data/train"
    class1_folder = "/workspace/class1"
    class2_folder = "/workspace/class2"

    # Function call
    copy_and_move_folders(binary_sequence, source_folder, class1_folder, class2_folder)
