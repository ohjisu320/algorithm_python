def solution(data, ext, val_ext, sort_by):
    answer = []
    q_list = ["code", "date", "maximum", "remain"]
    ext_question = q_list.index(ext)
    sort_question = q_list.index(sort_by)

    
    for index, d in enumerate(data) :
        if d[ext_question] < val_ext :
            answer.append(d)



    return sorted(answer, key=lambda x: x[sort_question])
    pass

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))