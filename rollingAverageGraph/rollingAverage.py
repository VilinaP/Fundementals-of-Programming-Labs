def read_data(filename: str) -> list[float]:
    dataList = []
    data = open(filename, 'r')
    for line in data:
        line = float(line.strip('\n'))
        dataList.append(line)
    return dataList    

def rolling_average(a: list[float]) -> list[float]:
    average = []
    list = [a[i:i+5] for i in range(0, len(a)-5)]
    calc = 0
    for item in list:
        calc = sum(item)/5
        average.append(calc)
    return average

from plotter import RollingPlotter
data = read_data('covid.txt')                 
roll_avg = rolling_average(data)                    
RollingPlotter(data, roll_avg, 300, 500, 800, 400)  