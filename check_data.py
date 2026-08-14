import os
from PIL import Image

# 检查路径
data_root = r"E:/phone"
train_img = os.path.join(data_root, "images/train")
val_img = os.path.join(data_root, "images/val")
train_label = os.path.join(data_root, "labels/train")
val_label = os.path.join(data_root, "labels/val")

print("=" * 50)
print("数据路径检查")
print("=" * 50)

for name, path in [
    ("训练图片", train_img),
    ("验证图片", val_img),
    ("训练标注", train_label),
    ("验证标注", val_label),
]:
    exists = os.path.exists(path)
    print(f"{name}: {path}")
    print(f"  存在: {exists}")
    if exists and "images" in path:
        files = [f for f in os.listdir(path) if f.endswith(('.jpg', '.png', '.jpeg'))]
        print(f"  图片数量: {len(files)}")
    elif exists and "labels" in path:
        files = [f for f in os.listdir(path) if f.endswith('.txt')]
        print(f"  标注数量: {len(files)}")
    print()

# 检查一张图片和对应的标注是否匹配
if os.path.exists(train_img) and os.path.exists(train_label):
    img_files = [f for f in os.listdir(train_img) if f.endswith(('.jpg', '.png', '.jpeg'))]
    if img_files:
        sample_img = img_files[0]
        sample_txt = sample_img.replace('.jpg', '.txt').replace('.png', '.txt')
        txt_path = os.path.join(train_label, sample_txt)

        print(f"检查示例:")
        print(f"  图片: {sample_img}")
        print(f"  标注文件存在: {os.path.exists(txt_path)}")

        if os.path.exists(txt_path):
            with open(txt_path, 'r') as f:
                content = f.read().strip()
                print(f"  标注内容: {content[:100] if content else '空标注'}")

            # 获取图片尺寸
            img_path = os.path.join(train_img, sample_img)
            with Image.open(img_path) as img:
                w, h = img.size
                print(f"  图片尺寸: {w} x {h}")