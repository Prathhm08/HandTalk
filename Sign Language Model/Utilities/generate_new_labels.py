import os
import shutil

input_folder = "D:\\HandTalk\\Sign Language Model\\Data 1\\valid\\labels"


for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)
        output_filename = filename.split(".")[0] + "__r.txt"
        output_path = os.path.join(input_folder, output_filename)

        shutil.copy(input_path, output_path)

        # print(f"Copied: {filename} to {output_filename}")

print("Done.")
