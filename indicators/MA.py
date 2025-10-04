def moving_avg(data, window_size):
    result = []
    moving_sum = sum(data[:window_size])
    result.append(moving_sum / window_size)
    for i in range(len(data)-window_size):
        moving_sum += data[i + window_size] - data[i]
        result.append(moving_sum / window_size)
    return result