from ultralytics import YOLO   # 导入YOLO库，用于加载模型和识别
import os                      # 导入os库，用于文件/文件夹操作

# ========== 配置 ==========
# 加载训练好的模型
model = YOLO(r"C:\Users\27808\666\pythonProject\马\手动标注\runs\detect\train-6\weights\best.pt")   #best是训练模型

# 输入文件夹（放你要识别的图片）
input_folder = r"C:\Users\27808\666\pythonProject\马\手动标注\test_images"

# 输出文件夹（识别结果保存位置）
output_folder = r"C:\Users\27808\666\pythonProject\马\手动标注\detect_results"

# 置信度阈值（0.5以上才显示）
confidence = 0.5

os.makedirs(output_folder, exist_ok=True)   #创建输出文件夹

# ========== 开始识别 ==========
print(f" 输入文件夹: {input_folder}")
print(f" 输出文件夹: {output_folder}")
print(f" 置信度阈值: {confidence}")
print("=" * 50)

# 获取所有图片文件
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tif')   #支持的图片格式
image_files = []

for f in os.listdir(input_folder):
    if f.lower().endswith(image_extensions):
        image_files.append(f)

print(f" 找到 {len(image_files)} 张图片")

if len(image_files) == 0:
    print(" 没有找到图片！请检查输入文件夹路径")
    exit()

# ========== 批量识别 ==========
results = model(
    source=input_folder,      # 输入文件夹
    conf=confidence,          # 置信度阈值
    iou=0.45,                 # 重叠框阈值
    save=True,                # 保存结果图片
    project=output_folder,    # 保存到输出文件夹
    name="batch",             # 子文件夹名称
    exist_ok=True,            # 允许覆盖文件夹
)

print("=" * 50)
print(" 批量识别完成！")
print(f" 结果保存在: {output_folder}/batch")