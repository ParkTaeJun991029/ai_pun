import os

folder_path = "/home/developer/ptj/ai_pun/2D_yolo_format/val/labels"  # 실제 폴더 경로로 변경해주세요

for filename in os.listdir(folder_path):
    if filename.endswith("_yolo_numeric.txt"):
        new_filename = filename.replace("_yolo_numeric", "")  # _yolo_numeric 부분을 제거
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)
        os.rename(old_filepath, new_filepath)
