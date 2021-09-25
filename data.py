import pandas as pd
import statistics 
import csv

df=pd.read_csv("HeightWeight.csv")
HeightList=df["Height(Inches)"].to_list()
WeightList=df["Weight(Pounds)"].to_list()

heightMean=statistics.mean(HeightList)
heightMode=statistics.mode(HeightList)
heightMedian=statistics.median(HeightList)
weightMean=statistics.mean(WeightList)
weightMode=statistics.mode(WeightList)
weightMedian=statistics.median(WeightList)
std_deiviationHeight=statistics.stdev(HeightList)
std_deiviationWeight=statistics.stdev(WeightList)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(heightMean, heightMedian, heightMode))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(weightMean, weightMedian, weightMode))

heightFirstSTDstart,heightFirstSTDend=heightMean-std_deiviationHeight,heightMean+std_deiviationHeight
heightSecondSTDstart,heightSecondSTDend=heightMean-(2*std_deiviationHeight),heightMean+(2*std_deiviationHeight)
heightThirdSTDstart,heightThirdSTDend=heightMean-(3*std_deiviationHeight),heightMean+(3*std_deiviationHeight)

weightFirstSTDstart,weightFirstSTDend=weightMean-std_deiviationWeight,weightMean+std_deiviationWeight
weightSecondSTDstart,weightSecondSTDend=weightMean-(2*std_deiviationWeight),weightMean+(2*std_deiviationWeight)
weightThirdSTDstart,weightThirdSTDend=weightMean-(3*std_deiviationWeight),weightMean+(3*std_deiviationWeight)

height_list_of_data_within_1_std_deviation = [result for result in HeightList if result > heightFirstSTDstart and result < heightFirstSTDend]
height_list_of_data_within_2_std_deviation = [result for result in HeightList if result > heightSecondSTDstart and result < heightSecondSTDend]
height_list_of_data_within_3_std_deviation = [result for result in HeightList if result > heightThirdSTDstart and result < heightThirdSTDend]

weight_list_of_data_within_1_std_deviation = [result for result in WeightList if result > weightFirstSTDstart and result < weightFirstSTDend]
weight_list_of_data_within_2_std_deviation = [result for result in WeightList if result > weightSecondSTDstart and result < weightSecondSTDend]
weight_list_of_data_within_3_std_deviation = [result for result in WeightList if result > weightThirdSTDstart and result < weightThirdSTDend]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(HeightList)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(HeightList)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(HeightList)))

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(WeightList)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(WeightList)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(WeightList)))














