import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff

df = pd.read_csv('StudentsPerformance.csv')
mathScore_list = df["math score"].to_list()

mean = sum(mathScore_list)/len(mathScore_list)
standardDeviation = statistics.stdev(mathScore_list)
median = statistics.median(mathScore_list)
mode = statistics.mode(mathScore_list)

print("Mean is:", mean)
print("Median is:", median)
print("Mode is:", mode)
print("Standard Deviation is:", standardDeviation)

first_stddev_start, first_stddev_end = mean-standardDeviation, mean+standardDeviation
list_of_data_within_1_stddev = [result for result in mathScore_list if result > first_stddev_start and result < first_stddev_end]
print("{}% of data lies within first standard deviation".format(len(list_of_data_within_1_stddev)*100/len(mathScore_list)))

sec_stddev_start, sec_stddev_end = mean-(2*standardDeviation), mean+(2*standardDeviation)
list_of_data_within_2_stddev = [result for result in mathScore_list if result > sec_stddev_start and result < sec_stddev_end]
print("{}% of data lies within second standard deviation".format(len(list_of_data_within_2_stddev)*100/len(mathScore_list)))

tri_stddev_start, tri_stddev_end = mean-(3*standardDeviation), mean+(3*standardDeviation)
list_of_data_within_3_stddev = [result for result in mathScore_list if result > tri_stddev_start and result < tri_stddev_end]
print("{}% of data lies within third standard deviation".format(len(list_of_data_within_3_stddev)*100/len(mathScore_list)))

#count.append(i)

#fig = px.bar(x = dice_result, y = count)
fig = ff.create_distplot([mathScore_list], ["Result"], show_hist = False)
fig.show()

