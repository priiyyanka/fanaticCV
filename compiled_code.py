import cv2
import numpy as np



def main():
    # Load the terrain image
    image = cv2.imread('terrain.jpg')

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Display the edges
    cv2.imshow('Edges', edges)

    # Define a simple threshold to identify obstacles
    _, obstacle_mask = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)

    # Find contours of the obstacles
    contours, _ = cv2.findContours(obstacle_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    # Create a binary image for the navigation grid
    nav_grid = np.zeros_like(gray)

    # Assume safe areas are those with low intensity (e.g., valleys or flat terrain)
    safe_zone = cv2.inRange(blurred, 0, 100)

# Use dilation to connect safe zones
    kernel = np.ones((5, 5), np.uint8)
    dilated_safe_zone = cv2.dilate(safe_zone, kernel, iterations=2)

    # Combine with the obstacle mask
    nav_grid = cv2.bitwise_or(dilated_safe_zone, obstacle_mask)

    # Find the path using simple contour finding (A* or Dijkstra would be more sophisticated)
    contours, _ = cv2.findContours(nav_grid, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (255, 0, 0), 2)

    # Display the results
    cv2.imshow('Obstacles and Navigation Grid', image)
    cv2.imshow('Navigation Grid', nav_grid)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if _name_ == "_main_":
    main()
