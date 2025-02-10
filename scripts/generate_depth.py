import torch
import cv2
import numpy as np
from PIL import Image  # Importing PIL
from torchvision.transforms import Compose, Resize, ToTensor, Normalize
import os
# Load AI depth estimation model
model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
model.eval()

# Depth estimation function
def generate_depth_map(image_path, output_path):
    # Ensure paths are absolute
    image_path = os.path.abspath(image_path)
    output_path = os.path.abspath(output_path)

    # Debugging: Print the final paths
    print(f"🔹 Looking for image at: \"{image_path}\"")
    print(f"🔹 Saving depth map at: \"{output_path}\"")

    # Check if file exists
    if not os.path.isfile(image_path):
        print(f"❌ ERROR: Image file not found at \"{image_path}\"")
        return

    # Load image
    img = cv2.imread(image_path)

    # Check if OpenCV successfully loaded the image
    if img is None:
        print(f"❌ ERROR: OpenCV could not read the image at \"{image_path}\"")
        return

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert the NumPy array (img) to a PIL Image
    pil_img = Image.fromarray(img)

    # Preprocess image for MiDaS
    transform = Compose([
        Resize((384, 384)), 
        ToTensor(), 
        Normalize(mean=[0.5], std=[0.5])
    ])

    img_tensor = transform(pil_img).unsqueeze(0)

    # Predict depth
    with torch.no_grad():
        depth_map = model(img_tensor)

    depth_map = depth_map.squeeze().cpu().numpy()
    depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min())  # Normalize
    depth_map = (depth_map * 255).astype(np.uint8)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save depth map
    cv2.imwrite(output_path, depth_map)
    print(f"✅ Depth map saved: \"{output_path}\"")

# Run for one image (updated file name for safety)
generate_depth_map(
    "C:/Users/RASHA SINHA/OneDrive/Desktop/2D3DBLENDER/images/apple.jpg",
    "C:/Users/RASHA SINHA/OneDrive/Desktop/2D3DBLENDER/depth_maps/apple_depth.jpg"
)
