import cv2

def crop_image(image, x1, y1, x2, y2):
    """
    Crops the input image using the provided bounding box coordinates.

    Args:
    image (numpy.ndarray): The input image in OpenCV format.
    x1 (int): The x-coordinate of the top-left corner of the bounding box.
    y1 (int): The y-coordinate of the top-left corner of the bounding box.
    x2 (int): The x-coordinate of the bottom-right corner of the bounding box.
    y2 (int): The y-coordinate of the bottom-right corner of the bounding box.

    Returns:
    numpy.ndarray: The cropped image in OpenCV format.
    """
    # Extract the region of interest from the input image
    cropped_image = image[y1:y2, x1:x2]

    # Return the cropped image
    return cropped_image

def convert_video_to_images(video_file, output_folder, save_every_n_frames):
    # Open the video file
    video = cv2.VideoCapture(video_file)

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Loop through the frames of the video
    for frame_num in range(total_frames):
        # Read the next frame of the video
        ret, frame = video.read()
        frame_cropped = crop_image(frame,255,130,255+1024,130+768)

        # Check if the frame was successfully read
        if not ret:
            break

        # Check if we should save this frame as an image
        if frame_num % save_every_n_frames == 0:
            # Convert the frame to JPG format
            jpg_frame = cv2.imwrite(f"{output_folder}/frame_{frame_num}.jpg", frame_cropped)

            # Check if the frame was successfully saved as an image
            if not jpg_frame:
                print(f"Failed to save frame {frame_num} as an image.")

    # Release the video file
    video.release()

# Example usage
convert_video_to_images("recc_vlog.mp4", "recc_vlog", 1)