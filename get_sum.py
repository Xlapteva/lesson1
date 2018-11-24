def get_summ(one, two, delimiter='&'):
    upper_l_p = str(one) + str(delimiter) + str(two)
    return upper_l_p.upper()

l_p = get_summ("learn","python")

print(l_p)

