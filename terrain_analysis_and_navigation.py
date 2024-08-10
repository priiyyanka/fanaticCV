import cv2
import pyrealsense2 as rs
import numpy as np



# Initialize standard camera and depth sensor
cap_rgb = cv2.VideoCapture(0)

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipeline.start(config)

try:
    while True:
        # Capture from RGB camera
        ret, frame_rgb = cap_rgb.read()

        # Capture from depth sensor
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        depth_image = np.asanyarray(depth_frame.get_data())

        # Convert depth image to colormap
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Combine RGB and depth images
        combined_image = np.hstack((frame_rgb, depth_colormap))

        # Display the combined image
        cv2.imshow('RGB + Depth', combined_image)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Release resources
    cap_rgb.release()
    pipeline.stop()

cv2.destroyAllWindows()
