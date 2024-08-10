import cv2
import numpy as np



def process_image(image_path, climate_type):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unable to load.")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if climate_type == 'bright_sunlight':
        # Adjust for bright lighting conditions
        # Apply adaptive histogram equalization
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        equalized = clahe.apply(gray)
        processed_image = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
      BASIC IMAGE PROCESSING FOR DIFFERENT CLIMATE 
    elif climate_type == 'low_light':
        # Adjust for low-light conditions
        # Increase brightness and contrast
        alpha = 1.5  # Contrast control
        beta = 50    # Brightness control
        processed_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        
    elif climate_type == 'snowy':
        # Adjust for snowy conditions
        # Apply median blur to reduce noise and smooth the image
        blurred = cv2.medianBlur(gray, 5)
        # Increase contrast
        alpha = 1.2  # Contrast control
        beta = 30    # Brightness control
        processed_image = cv2.convertScaleAbs(blurred, alpha=alpha, beta=beta)
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_GRAY2BGR)
        
        else:
        raise ValueError("Unsupported climate type. Choose from 'bright_sunlight', 'low_light', or 'snowy'.")

    # Display the processed image
    cv2.imshow('Processed Image', processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'terrain.jpg'
climate_type = 'bright_sunlight'  # Change to 'low_light' or 'snowy' as needed
process_image(image_path, climate_type)
