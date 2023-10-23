import json
import csv
import sys
import os

if len(sys.argv) < 2:
    print("Please provide a file path as an argument.")
    sys.exit(1)

input_file_path = sys.argv[1]  # Get the input file path from the command line argument

# Extract the directory path from the input file path
output_dir = os.path.dirname(os.path.abspath(__file__))

with open(input_file_path) as f:
    data = json.load(f)

keyframes = data['keyframes']

camera_positions = []

# Define the column names for the CSV file
columns = ['x', 'y', 'z', 'rx', 'ry', 'rz']

for kf in keyframes:
    pos = kf['position']
    x = pos[0]
    y = pos[1]
    z = pos[2]

    quat = kf['quaternion']
    rx = quat[0]
    ry = quat[1]
    rz = quat[2]

    print("quat", rx, ry, rz)
		
    row = [x, y, z, rx, ry, rz]
    camera_positions.append(row)

# Construct the output CSV file path in the same directory as the input file
output_file_path = os.path.join(f"{output_dir}/", 'camera_positions_luma_jason.csv')

# Write the camera_positions list to the CSV file
with open(output_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)
    writer.writerows(camera_positions)
