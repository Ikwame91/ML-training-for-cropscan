import tensorflow as tf
import os

SAVED_MODEL_DIR = "C:/projects/fyp/1"

OUTPUT_TFLITE_PATH = "C:/projects/fyp/converted_model.tflite"
# OUTPUT_LABELS_PATH = "C:/projects/fyp/labels.txt"

print(f"Loading SavedModel from: {SAVED_MODEL_DIR}")
try:

    converter = tf.lite.TFLiteConverter.from_saved_model(SAVED_MODEL_DIR)

    # --- UPDATED CHANGE ---
    # Include SELECT_TF_OPS if TFLITE_BUILTINS alone wasn't enough.
    # This instructs the converter to include TensorFlow ops that aren't
    # standard TFLite built-ins, which might be necessary for some models
    # or specific conversion paths with newer TF versions.
    converter.target_spec.supported_ops = [
        tf.lite.OpsSet.TFLITE_BUILTINS,
        tf.lite.OpsSet.SELECT_TF_OPS,  # <--- ADD THIS LINE
    ]
    tflite_model = converter.convert()

    with open(OUTPUT_TFLITE_PATH, "wb") as f:
        f.write(tflite_model)
    print(f"Model successfully converted and saved to: {OUTPUT_TFLITE_PATH}")

except Exception as e:
    print(f"Error converting model: {e}")
    print(
        "Please ensure the 'SAVED_MODEL_DIR' path is correct and it contains 'saved_model.pb' and 'variables' folder."
    )

print("-" * 50)


# model_class_names = [
#     "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
#     "Corn_(maize)___Common_rust_",
#     "Corn_(maize)___Northern_Leaf_Blight",
#     "Corn_(maize)___healthy",
#     "Pepper__bell___Bacterial_spot",
#     "Pepper__bell___healthy",
#     "Tomato_Bacterial_spot",
#     "Tomato_Early_blight",
#     "Tomato_Late_blight",
#     "Tomato_Leaf_Mold",
#     "Tomato_Septoria_leaf_spot",
#     "Tomato_Spider_mites_Two_spotted_spider_mite",
#     "Tomato__Target_Spot",
#     "Tomato__Tomato_YellowLeaf__Curl_Virus",
#     "Tomato__Tomato_mosaic_virus",
#     "Tomato_healthy",
# ]

# print(f"generating labels file at: {OUTPUT_LABELS_PATH}")
# try:
#     with open(OUTPUT_LABELS_PATH, "w") as f:
#         for label in model_class_names:
#             f.write(label + "\n")
#     print(f"Labels successfully created at: {OUTPUT_LABELS_PATH}")
# except Exception as e:
#     print(f"Error creating labels file: {e}")
#     print("Please ensure you have write permissions to the directory.")
