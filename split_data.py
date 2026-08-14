import os
import random
import shutil

# ===================== 只需要改这里的路径 =====================
# 图片文件夹（所有图片在这里）
RAW_IMG_DIR = r"E:\111\cell phone\images"
# 标注文件文件夹（所有txt在这里）
RAW_LABEL_DIR = r"E:\111\cell phone\labels"
# 划分后的数据集保存位置
TARGET_DIR = r"E:\111\phone_dataset"
# 训练集和验证集比例（这里8:2）
TRAIN_RATIO = 0.8
# ============================================================

# 创建目标文件夹结构
os.makedirs(os.path.join(TARGET_DIR, "images/train"), exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "images/val"), exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "labels/train"), exist_ok=True)
os.makedirs(os.path.join(TARGET_DIR, "labels/val"), exist_ok=True)

# 获取所有有对应标注的图片
imgs = []
for f in os.listdir(RAW_IMG_DIR):
    if f.endswith(('.jpg', '.png', '.jpeg')):
        # 把图片后缀替换成 .txt 得到标注文件名
        txt_name = os.path.splitext(f)[0] + ".txt"
        # 检查标注文件是否存在
        if os.path.exists(os.path.join(RAW_LABEL_DIR, txt_name)):
            imgs.append(f)

if not imgs:
    print("❌ 没找到带标注的图片！请检查图片和标注路径是否正确")
    exit()

# 随机打乱数据
random.shuffle(imgs)

# 按比例划分训练集和验证集
split_idx = int(len(imgs) * TRAIN_RATIO)
train_imgs = imgs[:split_idx]
val_imgs = imgs[split_idx:]

# 复制训练集文件
for img in train_imgs:
    txt = os.path.splitext(img)[0] + ".txt"
    shutil.copy(os.path.join(RAW_IMG_DIR, img), os.path.join(TARGET_DIR, "images/train", img))
    shutil.copy(os.path.join(RAW_LABEL_DIR, txt), os.path.join(TARGET_DIR, "labels/train", txt))

# 复制验证集文件
for img in val_imgs:
    txt = os.path.splitext(img)[0] + ".txt"
    shutil.copy(os.path.join(RAW_IMG_DIR, img), os.path.join(TARGET_DIR, "images/val", img))
    shutil.copy(os.path.join(RAW_LABEL_DIR, txt), os.path.join(TARGET_DIR, "labels/val", txt))

print(f"✅ 数据集划分完成！")
print(f"总数据量：{len(imgs)}")
print(f"训练集：{len(train_imgs)} 张")
print(f"验证集：{len(val_imgs)} 张")