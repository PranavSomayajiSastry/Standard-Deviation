import pandas as pd
import statistics
import csv
import 
df=pd.read_csv("data.csv")

height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean= statistics.mean(height_list)
weight_mean= statistics.mean(weight_list)

height_mode= statistics.mode(height_list)
weight_mode= statistics.mode(weight_list)

height_median= statistics.median(height_list)
weight_median= statistics.median(weight_list)

print("The Mean, Median & Mode of Heigth is: {}, {} and {} respectively.".format(height_mean, height_median, height_mode))
print("The Mean, Median & Mode of Weight is: {}, {} and {} respectively.".format(weight_mean, weight_median, weight_mode))

height_sD= statistics.stdev(height_list)
weight_sD= statistics.stdev(weight_list)

height_sD1_start, height_sD1_end= height_mean - height_sD, height_mean + height_sD
height_sD2_start, height_sD2_end= height_mean - (height_sD*2), height_mean + (height_sD*2)
height_sD3_start, height_sD3_end= height_mean - (height_sD*3), height_mean + (height_sD*3)

weight_sD1_start, weight_sD1_end= weight_mean - weight_sD, weight_mean + weight_sD
weight_sD2_start, weight_sD2_end= weight_mean - (weight_sD*2), weight_mean + (weight_sD*2)
weight_sD3_start, weight_sD3_end= weight_mean - (weight_sD*3), weight_mean + (weight_sD*3)

heigthList_sD1= [result for result in height_list if result > height_sD1_start and result < height_sD1_end]
heigthList_sD2= [result for result in height_list if result > height_sD2_start and result < height_sD2_end]
heigthList_sD3= [result for result in height_list if result > height_sD3_start and result < height_sD3_end]

weigthList_sD1= [result for result in weight_list if result > weight_sD1_start and result < weight_sD1_end]
weigthList_sD2= [result for result in weight_list if result > weight_sD2_start and result < weight_sD2_end]
weigthList_sD3= [result for result in weight_list if result > weight_sD3_start and result < weight_sD3_end]

print("{}% of data for height lies within 1st Standard Deviation: ".format(len(heigthList_sD1)*100.0/len(height_list)))
print("{}% of data for height lies within 2st Standard Deviation: ".format(len(heigthList_sD2)*100.0/len(height_list)))
print("{}% of data for height lies within 3st Standard Deviation: ".format(len(heigthList_sD3)*100.0/len(height_list)))

print("{}% of data for weight lies within 1st Standard Deviation: ".format(len(weigthList_sD1)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2st Standard Deviation: ".format(len(weigthList_sD2)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3st Standard Deviation: ".format(len(weigthList_sD3)*100.0/len(weight_list)))

