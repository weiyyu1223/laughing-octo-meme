from ultralytics import YOLO
import torch

device = 0 if torch.cuda.is_available() else 'cpu'

if torch.cuda.is_available():

    print(f" 使用设备: {torch.cuda.get_device_name(0)}")
    print(f" 显存: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")


model = YOLO(r"C:\Users\27808\666\pythonProject\马\手动标注\yolov8s.pt")

# ==========  训练配置 ==========
if __name__ == '__main__':
    results = model.train(

        # -------- 数据配置 --------
        data=r"C:\...\data.yaml",  # 数据集配置文件路径（指定图片和标注位置）
        imgsz=640,  # 输入图片尺寸（640x640像素）
        batch=8,  # 每批处理8张图片
        epochs=50,  # 训练50轮


        device=device,  # 使用GPU（或CPU）
        workers=2,  # 数据加载线程数（加速读取）
        cache=False,  # 不缓存图片到内存（节省内存）
        rect=True,  # 矩形训练（节省显存）

        # -------- 优化器配置 --------
        optimizer='auto',
        lr=0.01,
        lrf=0.01,
        momentum=0.937,
        weight_decay=0.0005,

        cos_lr=True,  # 余弦退火（学习率平滑下降）
        warmup_epochs=3,  # 预热3轮（学习率从低到高）
        warmup_momentum=0.8,  # 预热时的动量

        # -------- 数据增强（提高泛化能力） --------
        hsv_h=0.015,  # 色调变化（模拟不同颜色）
        hsv_s=0.7,  # 饱和度变化（模拟不同色彩）
        hsv_v=0.4,  # 明度变化（模拟不同光照）
        degrees=0.0,  # 旋转角度（0表示不旋转）
        translate=0.1,  # 平移（左右上下偏移）
        scale=0.5,  # 缩放（放大缩小）
        shear=0.0,  # 剪切（不变形）
        perspective=0.0,  # 透视（不变形）
        flipud=0.0,  # 上下翻转（关闭）
        fliplr=0.5,  # 左右翻转（50%概率）
        mosaic=1.0,  # Mosaic增强（拼图，100%开启）
        mixup=0.0,  # Mixup增强（关闭）

        # -------- 保存与验证 --------
        patience=50,  # 早停耐心值
        save=True,  # 保存模型
        save_period=10,  # 每10轮保存一次
        val=True,  # 每轮验证
        plots=True,  # 生成训练图表
        verbose=True,  # 打印详细信息
        seed=42,  # 随机种子（保证结果可复现）
    )

    # ========== 4. 训练完成 ==========
    print(f"训练完成！最佳模型：{results.save_dir}/weights/best.pt")