import cv2
import pandas as pd
import os

# Ensure output directory exists
os.makedirs("generated", exist_ok=True)

df = pd.read_csv('PR CERTI.csv')
list_names = df.values.tolist()
# Sample data
#list_names = [['Santayo Kundu', '3rd', 'IT']]

# Adjusted positions for A4 size (2480×3508 px)
name_area = (400, 1300, 1080, 300)  # Name Position
area2 = (800, 1600, 680, 500)  # Year + Department Position
optional_text_area = (800, 2200, 1680, 2300)  # Optional Third Text Position

for index, name in enumerate(list_names):
    template = cv2.imread('RISHI(DEMO).png')
    font = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 2.5  # Increased for A4 size
    thickness = 5

    # Name text
    text_size = cv2.getTextSize(name[0], font, font_scale, thickness)[0]
    x = name_area[0] + (name_area[2] - name_area[0] - text_size[0]) // 2
    y = name_area[1] + (name_area[3] - name_area[1] - text_size[1]) // 2 + 40  # Adjusted y coordinate
    cv2.putText(template, name[0], (x, y), font, font_scale, (0, 0, 0), thickness)

    # Year and Department text
    text2 = f"{name[2]} {name[1]} year"
    text_size = cv2.getTextSize(text2, font, font_scale, thickness)[0]
    x = area2[0] + (area2[2] - area2[0] - text_size[0]) // 2
    y = area2[1] + (area2[3] - area2[1] - text_size[1]) // 2 + 20  # Adjusted y coordinate
    cv2.putText(template, text2, (x, y), font, font_scale, (0,0,0), thickness)

    # Optional third text (if needed)
    # text3 = "Some additional text"
    # text_size = cv2.getTextSize(text3, font, font_scale, thickness)[0]
    # x = optional_text_area[0] + (optional_text_area[2] - optional_text_area[0] - text_size[0]) // 2
    # y = optional_text_area[1] + (optional_text_area[3] - optional_text_area[1] - text_size[1]) // 2 + 40
    # cv2.putText(template, text3, (x, y), font, font_scale, (0, 0, 0), thickness)

    cv2.imwrite(f"generated/{name[0]}.jpg", template)
    print(f'Processing certificate {index+1}/{len(list_names)}')
