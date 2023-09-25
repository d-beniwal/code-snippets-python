"""WARNING: Never unpickle data that could have come from an untrusted source, or that could have been tampered with
"""

def f_pickle_save(data, savename, extension):
    """use pickle to save a variable/class/object

    Args:
        data (variable): variable to be saved
        savename (str): filename/filepath for file to be saved
        extension (str): extension to use for saving the file

    Returns:
        None
    """
    
    import pickle
    
    # assign extension if filepath does not have extension
    if savename.split(".")[-1] != extension:
        savename = f"{savename}.{extension}"

    with open(savename, 'wb') as f:
        pickle.dump(data, f)        
    
    return None



def f_pickle_load(filepath):
    """load (unpickle) a pickled file to access data stored in it

    Args:
        filepath (str): path of file to be loaded (unpickled)

    Returns:
        data (extracted object): _description_
    """
    
    check_source = input("Do you TRUST the file being loaded? (y-Yes, n-No): ")
    
    if check_source.lower() in ["y", "yes"]:
        import os
        import pickle
        
        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                data = pickle.load(f)
            
            return (data)
        
        else:
            print(f"ERROR: '{filepath}' does not exist.")
            return None
