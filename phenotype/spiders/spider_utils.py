def extract_field(element, query):
    result = element.css(query).extract_first()
    return result.strip() if result else result


def extract_list(element, query):
    results = element.css(query).extract()
    res = ""
    for result in results:
        res += ", " + result.strip()
    return res
