# Edge AI Model: Image Classification (Recyclable vs Non-Recyclable)
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Step 1: Preprocess Images
train_gen = ImageDataGenerator(rescale=1./255)
train_data = train_gen.flow_from_directory(
    'train_data/',  # Folder with subfolders: /recyclable/, /non_recyclable/
    target_size=(64, 64),
    class_mode='binary',
    batch_size=32
)

# Step 2: Build Model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification
])

# Step 3: Train Model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_data, epochs=5)

# Step 4: Convert to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Step 5: Save the TFLite model
with open('recycler_model.tflite', 'wb') as f:
    f.write(tflite_model)