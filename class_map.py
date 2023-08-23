import os

# 클래스 라벨을 숫자로 매핑하는 딕셔너리
class_mapping = {
    "pedestrian": 0,
    "motorcycle": 1,
    "special_vehicle": 2,
    "traffic_light": 3,
    "bicycle": 4,
    "none": 5,
    "bus": 6,
    "car": 7,
    "traffic_sign": 8,
    "truck": 9
}

# 입력 폴더 경로 설정
input_folder = "/home/developer/ptj/ai_pun/2D_yolo_format/val/labels"  # 본인의 입력 폴더 경로로 변경해주세요
output_folder = "/home/developer/ptj/ai_pun/2D_yolo_format/val/val_labels"     # 본인의 출력 폴더 경로로 변경해주세요

# 폴더 내 YOLO 포맷 텍스트 파일 읽기 및 클래스 라벨 변환하여 파일로 저장
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(input_folder, filename), "r") as input_file:
            yolo_lines = input_file.readlines()
            
            output_filename = os.path.splitext(filename)[0] + "_numeric.txt"
            output_path = os.path.join(output_folder, output_filename)
            
            with open(output_path, "w") as output_file:
                for yolo_line in yolo_lines:
                    parts = yolo_line.strip().split()
                    if len(parts) > 0:
                        class_label = parts[0]
                        if class_label in class_mapping:
                            numeric_label = class_mapping[class_label]
                            parts[0] = str(numeric_label)
                            output_file.write(" ".join(parts) + "\n")
            
            print("Numeric labels have been saved to", output_path)
