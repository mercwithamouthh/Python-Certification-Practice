def count_smileys(arr):
    smileyface = None
    for x in arr:
        if x == ":" or ";":
            continue
        elif x == "-" or "~" or "":
            continue
        elif x == ")" or "D":
            return smileyface += 1
    return smileyface
