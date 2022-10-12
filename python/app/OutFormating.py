def decorate(dictionary):
    output = {"results" : []}
    for key, value in dictionary.items():
        output["results"].append({"label" : key, "score" : value})
    return output

