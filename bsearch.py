numbers = [1,2,4,8,16,16,16,32]
def bsearch(suspect, start, end):
    if end - start == 0:
        return None # or start if you want it to be ambitious
    mid = (start + end) // 2
    if suspect < numbers[mid]:
        return bsearch(suspect, start, mid)
    if numbers[mid] < suspect:
        return bsearch(suspect, mid + 1, end)
    return mid

def lefty_bsearch(suspect, start, end, where = float('inf')):
    if end - start == 0:
        return where # or start if you want it to be ambitious
    mid = (start + end) // 2
    if suspect < numbers[mid]:
        return lefty_bsearch(suspect, start, mid, where)
    if numbers[mid] < suspect:
        return lefty_bsearch(suspect, mid + 1, end, where)
    return lefty_bsearch(suspect, start, mid, min(where, mid))

def righty_bsearch(suspect, start, end, where = float('-inf')):
    if end - start == 0:
        return where # or start if you want it to be ambitious
    mid = (start + end) // 2
    if suspect < numbers[mid]:
        return righty_bsearch(suspect, start, mid, where)
    if numbers[mid] < suspect:
        return righty_bsearch(suspect, mid + 1, end, where)
    return righty_bsearch(suspect, mid + 1, end, max(where, mid))
