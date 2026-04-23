import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image
import json

# Load model and labels
interpreter = tflite.Interpreter(model_path='models/animal_classifier_fp16.tflite')
interpreter.allocate_tensors()

with open('models/labels.json', 'r') as f:
    labels = json.load(f)

# Prepare image
image = Image.open('path/to/image.jpg').resize((160, 160))
input_data = np.expand_dims(np.array(image, dtype=np.float32), 0)

# Run inference
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
output = interpreter.get_tensor(output_details[0]['index'])

# Get prediction
pred_idx = np.argmax(output[0])
confidence = output[0][pred_idx] * 100

print(f"Detected: {labels[str(pred_idx)]}")
print(f"Confidence: {confidence:.2f}%")