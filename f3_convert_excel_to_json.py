def f_excel_csv_to_json(input_filepath, col_for_row_keys, json_savename):
    """convert data stored in excel or csv file to a json dictionary file

    Args:
        input_filepath (str): path to input data file
        col_for_keys (str): column name in input file that should be used for nested keys. The header is by default used for first layer of keys.
        json_savename (str): name for saving json file generated

    Returns:
        data_dict (dict): input data in dictionary format
    """

    # -----------------
    # Library imports
    import pandas as pd
    import json


    extension = input_filepath.split(".")[-1] # get extension of input data file

    if extension not in ["csv", "xlsx"]:
        print(f"'.{extension}' not supported. Only '.csv' and '.xlsx' file extensions are supported.")
    
    else:
        if extension == "csv":
            df = pd.read_csv(input_filepath)
        if extension == "xlsx":
            df = pd.read_excel(input_filepath)
    
    keys_for_rows_list = df[col_for_row_keys].to_list()
    
    df = df.set_index(col_for_row_keys)
    data_dict = {col_name:{} for col_name in df.columns}
    
    for col in data_dict.keys():
        for row_key in keys_for_rows_list:
            data_dict[col][row_key] = df.loc[row_key, col]
    
    # If the savename does not contain .json extension, add the same to it
    if json_savename.split(".")[-1] != "json":
        json_savename += ".json"
    
    # Save data dictionary as json file
    file = open(json_savename,"w+")
    with open(json_savename, "w") as f:
        json.dump(data_dict, f, ensure_ascii=False)
    
    file.close()
    
    
    return (data_dict)
