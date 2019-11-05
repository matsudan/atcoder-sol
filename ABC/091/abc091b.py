n = int(input())
s_list = [input() for i in range(n)]
m = int(input())
t_list = [input() for j in range(m)]


def list_diff(list1, list2):
    result = list1.copy()
    for val in list2:
        if val in result:
            result.remove(val)
    return result


def count_max(diff_list):
    cnt_list = [diff_list.count(ele) for ele in set(diff_list)]
    if len(cnt_list) != 0:
        return max(cnt_list)
    else:
        return 0


lst = list_diff(s_list, t_list)
print(count_max(lst))
