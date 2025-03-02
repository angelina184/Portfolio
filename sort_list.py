def bubble_sort(arr):
#            5
    n = len(arr)
#        0           
#        1
#        2
#        3           4
    for i in range(n - 1):  # Количество проходов по списку     
        swapped = False # Флаг для оптимизации
#           0           5 - 1 - 0 (4)     от 0 до 3 -> 4 проверок
#           1 
#           2 
#           3
#           0          5 - 1 - 1 (3)
#           0          5 - 1 - 2 (2)      только 0,1
#           0          5 - 1 - 3 (1)      только 0
        for j in range(n - 1 - i):  # Проход по неотсортированной части     
#              [0]->5       0+1 [1]->2
#              [1]->5       1+1 [2]->9
#              [2]->9       2+1 [3]->1
#              [3]->9       3+1 [4]->6
#              
#              [0]->2       0+1 [1]->5
#              [1]->5       1+1 [2]->1
#              [2]->5       2+1 [3]->6
#   
#              [0]->2       0+1 [1]->1
#              [1]->2       1+1 [2]->5 
# 
#              [0]->1       0+1 [1]->2      
            if arr[j] > arr[j + 1]:  # Если элементы стоят в неправильном порядке
#              
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Меняем их местами        если фолс то не выполняеться (не меняеться)
                swapped = True  # Фиксируем факт обмена  
#    если обмена не было то swappped = True становится not swapped (и цыфры не переставляються).  swapped становится  False как  и было в начале на 9 линейке. Когда
# опять фиксируется обмен то он и записываеться(цифры обмениваються)                          
        if not swapped:  
            break

# Пример использования:
arr = [5, 2, 9, 1, 6]
bubble_sort(arr)
print("Отсортированный массив:", arr)

# [2, 5, 9, 1, 6]
# [2, 5, 9, 1, 6]
#[2, 5, 1, 9, 6]
#[2, 5, 1, 6, 9]
#[2, 1, 5, 6, 9]
#[1, 2, 5, 6, 9]