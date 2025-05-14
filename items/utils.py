# Деактивируем фильтр - удаляем его из url, если он уже был активирован
def delete_double(arr):
    if arr[-1] in arr[:-1]:
        double = arr[-1]
        arr.pop(arr.index(double))
        arr.pop(-1)
    return arr