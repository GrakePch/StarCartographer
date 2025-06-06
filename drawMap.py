import matplotlib.pyplot as plt
import numpy as np

def drawMapGrid (img, dots = [], annotates = []):
    OM_GROUND = np.array([[0, 0],
                [0, 90], [0, -90], [90, 0], [-90, 0], [0, 0], [180, 0]])
    OM_GROUND_LO = OM_GROUND[1:, 0]
    OM_GROUND_LA = OM_GROUND[1:, 1]

    fig = plt.figure(figsize=(20,10))
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    ax = fig.gca()

    ax.set_xticks(np.arange(-180, 180, 30))
    ax.set_yticks(np.arange(-90, 90, 10))
    ax.set_xlabel("Longitude (°)")
    ax.set_ylabel("Latitude (°)")
    plt.grid()
    plt.scatter(OM_GROUND_LO, OM_GROUND_LA,c="red", s=10)

    for i, txt in enumerate(range(1, 7)):
        ax.annotate(txt, (OM_GROUND_LO[i], OM_GROUND_LA[i]), xytext=(OM_GROUND_LO[i] + 2, OM_GROUND_LA[i] + 1), c="red")
        
    if dots:
        dots = np.array(dots)
        # Filter out [None, None] elements
        valid_mask = ~((dots[:,0] == None) | (dots[:,1] == None))
        dots = dots[valid_mask]
        if annotates:
            annotates = [a for i, a in enumerate(annotates) if valid_mask[i]]
        plt.scatter(dots[:,0], dots[:,1], c="green", s=10)
        
        for i, txt in enumerate(annotates):
            ax.annotate(txt, (dots[i][0], dots[i][1]), xytext= (dots[i][0] + 2, dots[i][1] + 1), c="green")
    
    if img is not None:
        plt.imshow(img, extent = [-180, 180, -90, 90])
    plt.show()