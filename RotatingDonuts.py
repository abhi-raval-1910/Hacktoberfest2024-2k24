import math
import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def rotating_donuts(num_donuts):
    A, B = 0, 0
    width, height = 40, 20  # Set screen width and height
    radius_inner, radius_outer = 2, 4  # Radii for donuts
    
    while True:
        clear_screen()
        z = [0] * (width * height)      # Z buffer
        output = [' '] * (width * height)  # ASCII buffer

        # Loop through each "donut" (ring) and calculate the points
        for d in range(num_donuts):
            A += 0.02  # Adjust rotation speed
            B += 0.01  # Adjust rotation speed for 3D effect

            # Loop through each angle theta and phi to create the donut shape
            for theta in range(0, 628, 5):    # theta: 0 to 2pi
                for phi in range(0, 628, 5):  # phi: 0 to 2pi
                    # Math to rotate and project the 3D point onto a 2D plane
                    sinA, cosA = math.sin(A), math.cos(A)
                    sinB, cosB = math.sin(B), math.cos(B)
                    cosTheta, sinTheta = math.cos(theta / 100), math.sin(theta / 100)
                    cosPhi, sinPhi = math.cos(phi / 100), math.sin(phi / 100)

                    # Calculate the coordinates for each point on the surface of the torus
                    circle_x = radius_outer + radius_inner * cosTheta
                    circle_y = radius_inner * sinTheta

                    x = int(width / 2 + (circle_x * (cosB * cosPhi + sinA * sinB * sinPhi) - circle_y * cosA * sinB))
                    y = int(height / 2 + (circle_x * (sinB * cosPhi - sinA * cosB * sinPhi) + circle_y * cosA * cosB))
                    ooz = int(8 * (cosA * cosPhi * sinTheta + cosB * sinTheta - circle_y * sinA))

                    # Compute luminance index
                    luminance_index = int(8 * (cosTheta * cosPhi * sinB - sinTheta * cosA * cosB + circle_y * sinA))
                    luminance_index = max(0, min(11, luminance_index))
                    
                    # Plot the point if within screen bounds
                    if 0 <= x < width and 0 <= y < height and ooz > z[y * width + x]:
                        z[y * width + x] = ooz
                        output[y * width + x] = ".,-~:;=!*#$@"[luminance_index]

        # Print the frame
        print('\n'.join(''.join(output[i:i + width]) for i in range(0, len(output), width)))
        time.sleep(0.03)

# Run the rotating donut function
try:
    num_donuts = int(input("Enter the number of rotating donuts: "))
    rotating_donuts(num_donuts)
except KeyboardInterrupt:
    print("Animation stopped.")
