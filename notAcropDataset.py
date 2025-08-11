import fiftyone as fo
import fiftyone.zoo as foz
import os
import shutil

# --- CONFIGURATION ---
NUM_IMAGES = 2000
SAVE_DIR = os.path.join("C:", "projects", "fyp", "PlantVillage", "negative_dataset")
CLASSES = [
    "Person",
    "Vehicle",
    "Animal",
    "Tree",
    "Sky",
    "House",
    "Building",
    "Tool",
    "Water",
    "Soil",
    "Rock",
    "Fence",
    "Road",
]

print("Script started. Checking and creating directories...")
os.makedirs(SAVE_DIR, exist_ok=True)
export_dir = os.path.join(SAVE_DIR, "not_a_crop")

try:
    print("\nAttempting to load and download the Open Images V7 dataset.")
    print(f"This may take a while as {NUM_IMAGES} images are being downloaded...")

    dataset = foz.load_zoo_dataset(
        "open-images-v7",
        split="validation",
        label_types=["detections"],
        classes=CLASSES,
        max_samples=NUM_IMAGES,
        shuffle=True,
    )

    print(f"\nDataset successfully loaded with {len(dataset)} samples.")

    print("\nExporting images to the 'not_a_crop' folder...")
    dataset.export(export_dir=export_dir, dataset_type=fo.types.ImageDirectory)

    # Verify that the images were exported
    exported_count = len(os.listdir(export_dir)) if os.path.exists(export_dir) else 0
    print(f"\nSuccessfully exported {exported_count} images to '{export_dir}'.")
    print("The script is complete. You can now use this dataset for retraining.")

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("The script was unable to complete the download or export process.")
    print("Please check your internet connection or try again later.")
