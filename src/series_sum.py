def series_sum(n):
    series = [1]
    y = 1
    for num in range(n):
        series.append(1 / (y + 3))
        y = y + 3
    ans = sum(series[:n])
    return str('%.2f' % ans)
