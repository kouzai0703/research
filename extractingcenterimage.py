#研究手法1 研究画像の中央番号を抜き出し
#research_class1_folder = "/workspace/research1-class1"で適用フォルダ名を指定

from PIL import Image
import os

def process_modality_folder(modality_folder):
    # List all image files in the modality folder
    image_files = sorted([f for f in os.listdir(modality_folder) if f.endswith('.png')])

    if not image_files:
        # No image files found, nothing to do
        return

    # Calculate the index of the middle image
    middle_index = len(image_files) // 2

    # Keep only the middle image
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(modality_folder, image_file)
        if i != middle_index:
            os.remove(image_path)

def process_patient_folder(patient_folder):
    modalities = ['FLAIR', 'T1w', 'T1wCE', 'T2w']

    for modality in modalities:
        modality_folder = os.path.join(patient_folder, modality)

        if os.path.exists(modality_folder):
            process_modality_folder(modality_folder)

if __name__ == "__main__":
    research_class1_folder = "/workspace/research1-class1"

    # List all patient folders in research-class1
    patient_folders = sorted([f for f in os.listdir(research_class1_folder) if os.path.isdir(os.path.join(research_class1_folder, f))])

    for patient_folder in patient_folders:
        patient_folder_path = os.path.join(research_class1_folder, patient_folder)
        process_patient_folder(patient_folder_path)
