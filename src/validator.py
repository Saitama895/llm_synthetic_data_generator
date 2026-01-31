def seo_validate(data, max_words=60):
    clean = []
    for item in data:
        if all(k in item for k in ["instruction", "input", "output"]):
            words = item["output"].split()
            if len(words) <= max_words and item["input"].lower() in item["output"].lower():
                clean.append(item)
    return clean
