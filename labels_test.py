import os

print("--- Script started! ---")  # <--- ADD THIS LINE

# This path should be the same as in your convert_model.py script
OUTPUT_LABELS_PATH = "C:/projects/fyp/labels.txt"

# Your full list of class names, exactly as you intend them
model_class_names = [
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy",
]

print(f"Attempting to generate labels file at: {OUTPUT_LABELS_PATH}")
try:
    with open(OUTPUT_LABELS_PATH, "w") as f:
        for label in model_class_names:
            f.write(label + "\n")
    print(f"Labels file successfully created at: {OUTPUT_LABELS_PATH}")
except Exception as e:
    print(f"ERROR: Could not create labels file. Reason: {e}")
    print("Please ensure you have write permissions to the directory.")
