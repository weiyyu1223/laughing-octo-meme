from ultralytics import YOLO    # 导入YOLO库
import winsound                 # 导入声音库
import time                     # 导入时间库 控制响铃间隔
import os

model = YOLO(r"C:\Users\27808\666\pythonProject\马\手动标注\runs\detect\train-6\weights\best.pt")

video_path = r"C:\Users\27808\666\pythonProject\马\手动标注\videos\944f12f6c401df1af1b941a4addf0466.mp4"

if not os.path.exists(video_path):
    print(f" 视频不存在: {video_path}")
    exit()

# 测试声音（运行时会先响一声确认音量）
print(" 测试声音...")
winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
time.sleep(1)

results = model(
    source=video_path,
    conf=0.5,                                # 置信度
    save=True,
    project=r"C:\Users\27808\666\pythonProject\马\手动标注\video_results",
    name="detect_result",
    exist_ok=True,
    stream=True,
)

print(" 视频检测中...")

############### 检测到手机时报警 ###############
last_beep_time = 0

for result in results:
    boxes = result.boxes
    if boxes:
        for box in boxes:
            if model.names[int(box.cls[0])] == "phone":
                now = time.time()
                if now - last_beep_time > 1.0:
                    #  大声警报（蜂鸣 + 系统提示音双重）
                    winsound.Beep(2500, 500)           # 高频蜂鸣
                    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)  # 系统提示音
                    last_beep_time = now
                    print(" 检测到手机！")

print(" 视频检测完成！")