import math
import numpy as np

def longiLatiToImageUV(radius, longitude, latitude, imgWidth, imgHeight, fovU, camPosition, camDirection, camUp, dropEdgeAngle = 20):
    # Get XYZ positon @ longitude, latitude.
    ## Spherical coordinates -> rectangular coordinates
    ### Longitude   0 at X+. Go counter-clockwise:
    ### Longitude  90 at Y+;
    ### Longitude 180 at X-;
    ### Longitude -90 at Y-;
    x = radius * math.cos(math.radians(latitude)) * math.cos(math.radians(longitude))
    y = radius * math.cos(math.radians(latitude)) * math.sin(math.radians(longitude))
    z = radius * math.sin(math.radians(latitude))
    P = np.array([x, y, z])
    
    # Compute Focal Length
    f = imgWidth / 2 / math.tan(math.radians(fovU / 2))
    
    
    k = np.array(camDirection)
    j = np.array(camUp)
    i = np.cross(camUp, camDirection) # camLeft
    OP = P - np.array(camPosition)
    # Angle between -OP and P
    cos_theta = np.dot(-OP, P) / (np.linalg.norm(OP) * np.linalg.norm(P))
    
    # check if OP pass through the sphere
    if (cos_theta < math.pi/180*dropEdgeAngle): return None, None
    
    
    # OP projected to k
    OP_k = OP / (np.dot(OP, k) / np.linalg.norm(k)) * f
    
    # Calculate UV (origin at img center)
    U = -np.dot(OP_k, i) / np.linalg.norm(i)
    V = -np.dot(OP_k, j) / np.linalg.norm(j)
    
    # Offset UV (origin at img top-left corner)
    U += imgWidth / 2
    V += imgHeight / 2
    
    return round(U), round(V)
    

def projectToGround(orbitalPos):
    x, y, z = orbitalPos
    long = math.degrees(math.atan(-x / y))
    if y < 0:
        long = 180 + long
    elif x > 0 and y > 0:
        long = 360 + long
    xydis = (x**2 + y**2) ** 0.5
    la = math.degrees(math.atan(z / xydis))
    return [long, la]
    
if __name__ == "__main__":
    pass