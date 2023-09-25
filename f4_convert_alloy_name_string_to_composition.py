def f_get_comp_dict(alloy_name):
    """generates compositions for a binary system with two components.

    Args:
    alloy_name(str): alloy name string e.g. “NiAl2”, “BaTiO3”, “Al1.5Ti0.25CrFeNi”

    Returns:
    dict_alloy_comp (dict): composition dict with two keys:
            “el_list”: list of elements in alloys
            “el_at_frac_list”: list of atomic fraction of each element in alloy
    """
    
    # -----------------
    # Library imports
    import numpy as np
    import re

    exclude = set("() {}[]''/,;:?\|~`@#$%&^*-_")
    alloy_name = ''.join(ch for ch in alloy_name if ch not in exclude)

    # split string wherever capital letter is found
    el_stoich_pairs_list = re.findall("[A-Z][^A-Z]*", alloy_name)
    el_list = []
    el_stoich_list = []

    # from each 'el_stoich_pair' extract element name and stoichiometry
    for el_stoich_pair in el_stoich_pairs_list:
        el = "".join(ch for ch in el_stoich_pair if (not ch.isdigit() and ch != "."))
        stoich = "".join(ch for ch in el_stoich_pair if (ch.isdigit() or ch == "."))
        if stoich == "":
            stoich = float(1)
        el_list.append(el)
        el_stoich_list.append(float(stoich))

    # creating atomic fractions
    stoich_total = np.sum(el_stoich_list)
    el_at_frac_list = list(np.around(np.array(el_stoich_list)/stoich_total, 4))

    # sort with elements arranged in alphabetical order
    tuples = zip(*sorted(zip(el_list, el_at_frac_list)))
    el_list_sort, el_at_frac_list_sort = [list(tuple) for tuple in tuples]

    dict_alloy_comp = {
        "el_list": el_list_sort,
        "el_at_frac_list": el_at_frac_list_sort
    }


    return (dict_alloy_comp)
