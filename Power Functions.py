


def power(base, exponent):
    if exponent > 0:
        for i in exponent:
            answer = base * base
        print(answer)
    elif exponent < 0:
        for i in exponent:
            denominator = base * base
        print(float(1 / denominator))
    else:
        print(int(1))
              
