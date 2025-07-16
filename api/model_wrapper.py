import os
import torch
import requests

from torchvision.models import mobilenet_v3_small
from torchvision import transforms
from PIL import Image


WEIGHT_PATH = os.environ.get("WEIGHT_PATH")


class ModelWrapper:
    def __init__(self):
        self.id_to_class = self.get_class_labels()
        self.model = self.load_model()

    def get_class_labels(self):
        return {
            0: "T-shirt/top",
            1: "Trouser",
            2: "Pullover",
            3: "Dress",
            4: "Coat",
            5: "Sandal",
            6: "Shirt",
            7: "Sneaker",
            8: "Bag",
            9: "Ankle boot",
        }

    def load_model(self):
        model = mobilenet_v3_small(pretrained=False)

        in_features = model.classifier[3].in_features
        model.classifier[3] = torch.nn.Linear(in_features, 10)

        state_dict = torch.load(WEIGHT_PATH, map_location=torch.device("cpu"))
        model.load_state_dict(state_dict)
        model.eval()

        return model

    def predict(self, img_tensor):
        with torch.no_grad():
            output = self.model(img_tensor.unsqueeze(0))
            probs = torch.softmax(output.squeeze(0), dim=0)
            return self.id_to_class[int(torch.argmax(probs).item())]

    def transform_image(self, img):
        transform = transforms.Compose(
            [
                transforms.Resize((224, 224)),
                transforms.Grayscale(num_output_channels=3),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225],
                ),
            ]
        )
        return transform(img)

    def load_image_from_url(self, url: str):
        headers = {"User-Agent": "Mozilla/5.0"}
        img = Image.open(requests.get(url, stream=True, headers=headers).raw)
        return img

    def predict_from_url(self, url: str):
        img = self.load_image_from_url(url)
        tensor = self.transform_image(img)
        return self.predict(tensor)
