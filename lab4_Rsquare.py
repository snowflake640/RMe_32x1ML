
import csv
import numpy as np

#function to calculate coefficients for regression line
def coef_estimation(x, y):
    n = np.size(x)

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    SS_xy = np.sum(x*y) - n*x_mean*y_mean
    SS_xx = np.sum(x*x) - n*x_mean*x_mean

    b_1 = SS_xy/SS_xx
    b_0 = y_mean - b_1*x_mean

    return(b_0, b_1)

#function to calculate R_Square value
def rSquare(x, y, b):
    y_hat = []
    y_mean = np.mean(y)
    print(y_mean)
    for i in x:
        y_hat.append(b[0] + b[1]*i)
    
    SS_yyh = np.sum((y_hat - y_mean)**2)
    SS_yym = np.sum((y - y_mean)**2)

    return SS_yyh/SS_yym

#main function
def main():
    filename = "covid-19 infected in June.csv"

    infected_list = []
    tested_list = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)

        for row in csvreader:
            infected_list.append(row[1])
            tested_list.append(row[2])

    infected_list = list(map(int, infected_list))
    tested_list = list(map(int, tested_list))


    y = np.array(infected_list)
    x = np.array(tested_list)
    b = coef_estimation(x, y)
    rsquare = rSquare(x, y, b)

    print(f"Estimated coefficients: {b[0], b[1]}")
    print(f"R-Squared value for the calculated value: {rsquare}")



if __name__ == "__main__":
    main()