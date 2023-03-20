def f_array_list_to_gif(array_list, gif_savename):
    """create a gif from an array list

    Args:
        array_list (list): list of numpy arrays; each array is treated as a frame
        gif_savename (str): filename for output gif (don't specify any extension)

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
        
        state = (array_list[i] / max_cell_value) * 255 # changes to intensity levels corresponding to 8-bit image
        state = Image.fromarray(state).convert('P')
        state = cv2.cvtColor(np.asarray(state), cv2.COLOR_RGB2BGR)
        state = cv2.applyColorMap(state, heatmap_used)
        
        im = Image.fromarray(state).convert('P')
        images.append(im)

    images[0].save(gif_savename, save_all=True, append_images=images[1:], optimize=False, duration=100)
    
    
    return None