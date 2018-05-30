def slices(series, length):
    if length < 1 or length > len(series) or series == '':
        raise ValueError('reee')
    else:
        return slices_help(series, length)

def slices_help(series, length, series_list=None):
    if series_list == None:
        series_list = []

    if len(series) < length:
        return series_list
    else:
        series_list.append(series[:length])
        temp_series = series[1:]
        return slices_help(temp_series, length, series_list)
