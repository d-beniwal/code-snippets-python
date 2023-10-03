def f_2Darray_list_to_gif(array_list, gif_savename, remap_values=True, apply_cmap=True):
    """create a gif from an array list

    Args:
        array_list (list): list of numpy arrays; each array is treated as a frame
        gif_savename (str): filename for output gif (don't specify any extension)
        remap_values (bool): default=True; rescale array values by factor of (255/maxValue)
        apply_cmap (bool): default=True; applies a colormap to images

    Returns:
        None
    """
    
    # -----------------
    # Library imports
    import numpy as np
    import cv2
    from PIL import Image
    
    # -----------------
    heatmap_used = cv2.COLORMAP_JET
    max_cell_value = np.max(array_list)
    images = []

    for i in range(0, len(array_list)):
        
        if remap_values == True:
            frame = (array_list[i] / max_cell_value) * 255 # changes to intensity levels corresponding to 8-bit image
        else:
            frame = array_list[i]
        
        frame = Image.fromarray(frame).convert('P') # converts frame from array to image format
        
        # get 3 channel color image by replicating same frame to 3 channels
        frame = cv2.cvtColor(np.asarray(frame), cv2.COLOR_RGB2BGR)
        
        if apply_cmap == True:
            frame = cv2.applyColorMap(frame, heatmap_used) # apply colormap to image
        
        frame = Image.fromarray(frame).convert('P') # converts 3 channel frame to color image
        images.append(frame) # add frame to images list
    
    # create gif
    images[0].save(f"{gif_savename}.gif", save_all=True, append_images=images[1:], optimize=True, duration=100)
    
    
    return None
