# Import required libraries
from ultralytics import YOLO
import yaml

def train():
    # Load the YAML configuration
    with open('data.yaml') as f:
        data = yaml.safe_load(f)

    # Define the model configuration
    model = YOLO('yolov8n.pt')  # Load a pretrained model (recommended for training)

    # Set up the training
    results = model.train(data='data.yaml', 
                            epochs=1000, 
                            imgsz=640, 
                            patience = 1000, 
                            batch=32, 
                            device=0,
                            name='train_yolov8n_vlog2_balanced') #device='cpu'

if __name__ == '__main__':
    from torch.utils.tensorboard import SummaryWriter
    writer = SummaryWriter()
    train()


#yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=recc_vlog2/valid show=True imgsz=1280 name=yolov8n hide_labels=False device='cpu'

