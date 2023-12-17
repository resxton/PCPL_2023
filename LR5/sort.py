data_lambda = [4, -30, 100, -100, 123, 1, 0, -1, -4]
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)
    result = sorted(data, key=abs, reverse=True)
    print(result)
