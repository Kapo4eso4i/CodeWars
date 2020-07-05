def namelist(names):
    names = [x['name'] for x in names]
    result = ' & '.join(names)
    return result.replace(" & ", ", ", result.count("&") - 1)

