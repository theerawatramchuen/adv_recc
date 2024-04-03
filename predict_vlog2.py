
from ultralytics import YOLO

def predict_vlog2():
    # Load a model
    model = YOLO('runs/detect/train_yolov8n_vlog2_balanced/weights/best.pt')  # pretrained YOLOv8n model

    # Define path to the image file
    source = 'recc_vlog2_v2/valid/*.jpg'  # return a list of Results objects

    # Run inference on the source
    results = model(source, stream=True, device='cpu')

    # Run inference on 'bus.jpg' with arguments
    model.predict('recc_vlog2_v2/valid/', save=True, imgsz=640, conf=0.5)

if __name__ == '__main__':
    predict_vlog2()