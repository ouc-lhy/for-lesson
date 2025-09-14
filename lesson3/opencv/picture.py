import cv2
import numpy as np

# 读取图像
img = cv2.imread("pic.png")
if img is None:
    print("无法读取图像，请检查路径")
    exit()

while True:
    print("\n图像处理演示")
    print("1. 调整亮度")
    print("2. 调整对比度")
    print("3. 缩放图像")
    print("4. 显示图像")
    print("0. 退出")
    
    choice = input("请选择操作: ")
    
    if choice == '0':
        break
        
    elif choice == '1':
        value = int(input("亮度值(-100到100): "))
        img = cv2.convertScaleAbs(img, beta=value)
        cv2.imwrite("pic.png", img)
        print("亮度已调整并保存")
        
    elif choice == '2':
        value = float(input("对比度值(0.5-3.0): "))
        img = cv2.convertScaleAbs(img, alpha=value)
        cv2.imwrite("pic.png", img)
        print("对比度已调整并保存")
        
    elif choice == '3':
        scale = float(input("缩放比例(0.1-3.0): "))
        h, w = img.shape[:2]
        new_size = (int(w*scale), int(h*scale))
        img = cv2.resize(img, new_size)
        cv2.imwrite("pic.png", img)
        print(f"图像已缩放至{new_size[0]}x{new_size[1]}并保存")
        
        
    elif choice == '4':
        cv2.imshow("current picture", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("无效选择")