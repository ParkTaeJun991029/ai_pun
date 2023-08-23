import os
import json

# YOLO 포맷으로 변환하는 함수
def convert_to_yolo_format(json_annotation, img_width, img_height):
    yolo_format = []
    for annotation in json_annotation:
        label = annotation["Label"]
        x_min = annotation["Coordinate"][0]
        y_min = annotation["Coordinate"][1]
        width = annotation["Coordinate"][2]
        height = annotation["Coordinate"][3]
        
        # YOLO 포맷에서 x_center, y_center, normalized_width, normalized_height 계산
        x_center = (x_min + width / 2) / img_width
        y_center = (y_min + height / 2) / img_height
        normalized_width = width / img_width
        normalized_height = height / img_height
        
        yolo_format.append(f"{label} {x_center:.6f} {y_center:.6f} {normalized_width:.6f} {normalized_height:.6f}")
    return yolo_format

# 입력 폴더 경로 설정
input_folder = "/home/developer/ptj/ai_pun/2D Bounding Box/validation/labels"  # 본인의 입력 폴더 경로로 변경해주세요
output_folder = "/home/developer/ptj/ai_pun/2D_yolo_format/val/labels"     # 본인의 출력 폴더 경로로 변경해주세요

# 폴더 내 JSON 파일 읽기 및 YOLO 포맷 변환하여 파일로 저장
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        with open(os.path.join(input_folder, filename), "r") as json_file:
            json_data = json.load(json_file)
            
            img_width = json_data["Source_Image_Info"]["Resolution"][0]
            img_height = json_data["Source_Image_Info"]["Resolution"][1]
            
            yolo_annotations = convert_to_yolo_format(json_data["Annotation"], img_width, img_height)
            
            output_filename = os.path.splitext(filename)[0] + "_yolo.txt"
            output_path = os.path.join(output_folder, output_filename)
            
            with open(output_path, "w") as output_file:
                for yolo_annotation in yolo_annotations:
                    output_file.write(yolo_annotation + "\n")
            
            print("YOLO annotations have been saved to", output_path)
