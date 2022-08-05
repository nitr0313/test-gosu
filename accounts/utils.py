

def secure_passport(passport_num):
    tmp = list(passport_num)
    tmp = tmp[:1] + ["* *****"] + tmp[-2:]
    return "".join(tmp)


def secure_fio(full_name):
    res = []
    for st in full_name.split():
        res.append(st[0]+"***")
    return " ".join(res)
