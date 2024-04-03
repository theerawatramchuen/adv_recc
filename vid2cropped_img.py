"""
Prompt: 
write me python code with opencv library to convert mp4 file to jpg files with predefine number of skipped frame 
and crop image at x1,y1 and x2,y2 bounding box top left, bottm right respectively prior save to specific folder


Output: mixtral-8x7b-instruct-v0.1 
Sure! Here's some sample code that uses OpenCV to convert an MP4 file to JPG frames, skipping a specified number 
of frames between each saved image, and cropping the image to a defined bounding box before saving it to a specific folder:
"""

import cv2
import os

# Define the video file path, output folder path, number of frames to skip, and bounding box
video_file_path = 'recc_vlog.mp4'
output_folder_path = 'recc_vlog'
frames_to_skip = 1
x1 = 252
y1 = 125
bounding_box = (x1, y1, x1+1024, y1+768) # x1, y1, x2 = x1+1024, y2 = y1+768

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Open the video file and get its width and height
video = cv2.VideoCapture(video_file_path)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

# Process each frame of the video
frame_count = 0
while True:
    # Read the next frame
    ret, frame = video.read()
    if not ret:
        break

    # Increment the frame count and check if it's time to save a frame
    frame_count += 1
    if frame_count % frames_to_skip != 0:
        continue

    # Crop the frame to the defined bounding box
    cropped_frame = frame[bounding_box[1]:bounding_box[3], bounding_box[0]:bounding_box[2]]

    # Save the cropped frame as a JPG image in the output folder
    output_file_path = os.path.join(output_folder_path, f'frame_{frame_count}.jpg')
    cv2.imwrite(output_file_path, cropped_frame)

    # Write the original frame to the output video file
    out.write(frame)

# Release the video capture and writer objects
video.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()