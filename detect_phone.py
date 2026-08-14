from ultralytics import YOLO

# 加载训练好的模型
model = YOLO(r"C:\Users\27808\666\pythonProject\马\手动标注\runs\detect\train-6\weights\best.pt")  #best 是训练模型

# ##########################识别图片单张#####################
img_path = r"C:\Users\27808\666\pythonProject\马\手动标注\870879aa3fe86b9d45438e6cb1a62666.jpg"

print(f" 正在识别: {img_path}")

results = model(img_path, conf=0.5)

for r in results:
    boxes = r.boxes                         # 如果检测到了
    if boxes:
        print(f"\n 识别到 {len(boxes)} 个物体:")
        for box in boxes:
            cls = model.names[int(box.cls[0])]
            conf = float(box.conf[0])
            print(f"   {cls}: {conf:.2%}")
    else:                                   # 如果没有检测到
        print("\n 未识别到手机")

# 保存结果
results[0].save("result.jpg")
print("\n 结果已保存到 result.jpg")