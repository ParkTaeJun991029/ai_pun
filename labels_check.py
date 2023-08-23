import os
import json

# 입력 폴더 경로 설정
input_folder = "/home/developer/ptj/ai_pun/2D Bounding Box/validation/labels"  # 본인의 폴더 경로로 변경해주세요
output_file = "all_labels_val.txt"

# 중복 없이 라벨 추출 함수
def extract_labels(json_data):
    labels = set()
    for annotation in json_data["Annotation"]:
        labels.add(annotation["Label"])
    return labels

# 폴더 내 JSON 파일 읽기
all_labels = set()
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            labels = extract_labels(data)
            all_labels.update(labels)

# 중복 없는 라벨들을 파일에 저장
with open(output_file, "w") as f:
    for label in all_labels:
        f.write(label + "\n")

print("Labels from all JSON files have been saved to", output_file)
