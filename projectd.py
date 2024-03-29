#-----------------------------------------------------------------------#
# SCRIPT: projectd_template.py						#
# PURPOSE: Template for project D					#
#									                #
#-----------------------------------------------------------------------#

#----------#
# Notes:   #
#----------#


#----------------------#
# Required libraries   #
#----------------------#

import csv
import math
import numpy as np
import matplotlib.pyplot as plt


#------------------#
# Main function    #
#------------------#

def main():

    filename = './NOAA_data.csv'

    # Run the read_data function
    data = read_data(filename=filename)

    # Find the list of unique site codes
    usites = unique_sites(sitecode=data[0])
    print("Unique site codes")
    print(usites)

    # Calculate the data counts
    counts = data_counts(filename)

    # Calculate data statistics
    summarystats = data_stats(filename)
    print(summarystats)


#----------#
# PART A   #
#----------#

# Purpose: read in the data and clean the data

def read_data(filename):

    # Read in the NOAA data file
    
    # Correct site codes

    # Return the compound list, including the corrected site codes
    site_codes = {'wisconsin':'LEF', 'wisc':'LEF', 'waco':'WKT', 'maryland':'TMD', 'sutro':'STR', 'oklahoma':'SGP'}
    data_list = []
    sitecode_list = []
    sitecode_list_final = []
    yr_list = []
    doy_list = []
    obs_list = []
    with open(filename, 'r') as csvfile:
        next(csvfile)
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            sitecode_list.append(row[0])
            yr_list.append(int(row[1]))
            doy_list.append(int(row[2]))
            obs_list.append(float(row[3]))
        for i in sitecode_list:
            if i in site_codes:
                translated_code = site_codes[i]
                sitecode_list_final.append(translated_code)
            else:
                sitecode_list_final.append(i)
        data_list.append(sitecode_list_final)
        data_list.append(yr_list)
        data_list.append(doy_list)
        data_list.append(obs_list)
    return data_list

    pass


#----------#
# PART B   #
#----------#

# Purpose: Create a unique list of sites

def unique_sites(sitecode):

    # Convert the site codes to a set
    
    # Convert to a list and sort
    
    # Return a list of unique sites
    unique_sites_list = []
    for i in sitecode:
        if i not in unique_sites_list:
            unique_sites_list.append(i)
    unique_sites_list = sorted(unique_sites_list)
    return unique_sites_list
    
    pass


#----------#
# PART C   #
#----------#

def data_counts(filename):

    # Read in the data
    
    # Create a unique list of sites
    
    # Find the number of data points associated with each site
    
    # Find the site with the maximum and minimum number of data points
    
    # Return the data counts
    NOAA_list = read_data(filename)
    sites_list = NOAA_list[0]
   
    num_obs_dict = {}
    for i in sites_list:
        if i in num_obs_dict:
            prev_obs_num = num_obs_dict[i]
            num_obs_dict[i] = prev_obs_num + 1
        else:
            num_obs_dict[i] = 1

    num_obs_dictKeys = sorted(list(num_obs_dict.keys()))
    num_obs_dict_alpha = {i:num_obs_dict[i] for i in num_obs_dictKeys}
    
    alpha_site_count = []
    for i in num_obs_dict_alpha:
        alpha_site_count.append(num_obs_dict_alpha[i])
        
    largest_count = max(alpha_site_count)
    smallest_count = min(alpha_site_count)
    

    for i in num_obs_dict_alpha:
        if num_obs_dict_alpha[i] == largest_count:
            largest_site = i
        elif num_obs_dict_alpha[i] == smallest_count:
            smallest_site = i
    
    print(f'Site {largest_site} has the largest number of observations with {largest_count} observations')
    print(f'Site {smallest_site} has the smallest number of observations with {smallest_count} observations')  

    return alpha_site_count

    pass


#----------#
# PART D   #
#----------#

# Calculate statistics on each site and write the data to a file as a visually-pleasing table.


def data_stats(filename):

    # Read in the data
    
    # Create a unique list of sites
    
    # Loop over each site and find the mean, min, and max value at each site
    
    # Write the values to file as a formatted table
    # Each column will be 8 spaces wide. Center each value within the column.
    
    # return data statistics
    NOAA_list = read_data(filename)
    NOAA_sites = NOAA_list[0]
    uniquesites = unique_sites(NOAA_sites)
    NOAA_obs = NOAA_list[3]
    lef_co2measures = []
    sgp_co2measures = []
    str_co2measures = []
    tmd_co2measures = []
    wkt_co2measures = []    
    
    for i in range(len(NOAA_sites)):
        if NOAA_sites[i] == 'LEF':
            lef_co2measures.append(NOAA_obs[i])
        elif NOAA_sites[i] == 'SGP':
            sgp_co2measures.append(NOAA_obs[i])
        elif NOAA_sites[i] == 'STR':
            str_co2measures.append(NOAA_obs[i])
        elif NOAA_sites[i] == 'TMD':
            tmd_co2measures.append(NOAA_obs[i])
        elif NOAA_sites[i] == 'WKT':
            wkt_co2measures.append(NOAA_obs[i])
    
    data_summary_list = [[],[],[]]   
    site_measures_list = [lef_co2measures, sgp_co2measures, str_co2measures, tmd_co2measures, wkt_co2measures]
    
    
    for i in site_measures_list:
        if len(i) != 0:
            data_summary_list[0].append(min(i))
            data_summary_list[1].append(max(i))
            data_summary_list[2].append(round((sum(i) / len(i)),2))
   
    min_list = data_summary_list[0]
    max_list = data_summary_list[1]
    mean_list = data_summary_list[2]
    table_data_list = (mean_list, min_list, max_list)
    
    with open('data_summary.txt', 'w') as file:
        file.write('|  site  |  mean  |  min   |  max   |\n')
        
        for i in range(len(table_data_list[0])):
            file.write(f'| {uniquesites[i]}    | {table_data_list[0][i]} | {table_data_list[1][i]} | {table_data_list[2][i]} |\n')
    
 
    return data_summary_list

    pass


#----------#
# PART E   #
#----------#

def summarizedata(filename):
    # Purpose:
    #	Create a plot of the CO2 data as a time series
    #	Plot a histogram of the data
    
    # Read in data from the Harvard Forest
    '''your code'''
    data = np.genfromtxt(filename, delimiter=',', skip_header=1)
    year = data[:,0]
    co2_flux = data[:,3]
    
        
    # Create a time series plot of the data
    '''your code'''
    plt.scatter(year, co2_flux, s=5)
    plt.xlabel('Date')
    plt.ylabel('CO2 flux')
    plt.title('Time series of model fit')

    # Display the plot
    plt.show()
    
     # Plot a histogram of the data
    '''your code'''
    plt.hist(co2_flux, bins=20, density=True)
    plt.xlabel('CO2 flux')
    plt.title('Histogram of CO2 flux')
    
    
    # Display the plot
    plt.show()
 

#---------------------------#
# PART F                   #
#---------------------------#

def seasonalcycle(filename):

    # Purpose: 
    # 	Find the average flux by month (averaged over all years)
    #	Plot the average monthly flux to visualize the seasonal cycle

    # Read in the data from the Harvard Forest
    '''your code'''
    # Load data from CSV file
    data = np.genfromtxt(filename, delimiter=',', skip_header=1)

    # Extract month columns
    month = data[:, 1]

    # Extract CO2 flux column
    flux = data[:, 3]

    # Calculate average flux by month of year
    
    monthly_means = np.zeros(12)
    for m in range(1, 13):
        mask = (month == m)
        monthly_means[m-1] = np.mean(flux[mask])

    # Plot the seasonal cycle
    months = np.arange(1, 13)
    plt.plot(months, monthly_means)
    plt.xlabel('Month')
    plt.ylabel('Average CO2 Flux (umol/m2/s)')
    plt.title('Seasonal Cycle of CO2 Flux')
    plt.show()

    # Return the monthly means
    return monthly_means
    pass


#---------------------------#
# PART G	                  #
#---------------------------#

def HFregression(filename, filename2):
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))
    # Purpose: 
        #    Create a regression model for CO2 fluxes
        #    Visualize the outputs of the model

    # Read in the data from the Harvard Forest
    '''your code'''
    data = np.genfromtxt(filename, delimiter=',', skip_header=1)

    # Create the X matrix for the regression
    '''your code'''
    pre_X = data[:, 4:]
    num_rows = pre_X.shape[0]
    ones_array = np.ones((num_rows, 1))
    X = np.concatenate((ones_array, pre_X), axis=1)
    z = data[:, 3]
    
    # Estimate the regression coefficients
    '''your code'''
    X_T = np.transpose(X)
    X_T_X = np.dot(X_T, X)
    X_T_X_inv = np.linalg.inv(X_T_X)
    first_dot_prod = np.dot(X_T_X_inv, X_T)
    beta = np.dot(first_dot_prod, z)
    
    # Create the model estimate
    '''your code'''
    X_B = np.dot(X, beta)
    
    date = data[:,0] + data[:,1] / 12
    co2_flux = data[:,3]
    axs[0].plot(date, co2_flux, color='blue', label='Data')
    axs[0].set_xticks([1992.5,1995.0, 1997.5, 2000.0, 2002.5, 2005.0, 2007.5, 2010.0])
    axs[0].set_yticks([-10.0, -7.5, -5.0, -2.5, 0.0, 2.5, 5.0])
    axs[0].set_xlabel('Date')
    axs[0].set_ylabel('CO2 flux')
    axs[0].set_title('Time series of model fit')
    
    
    # Plot the model estimate
    axs[0].plot(date, X_B,  color='orange', label='Model')
    
    
    # Calculate the correlation coefficient
    r = np.corrcoef(co2_flux, X_B,)
    r = r[1,0]
    
    # Add the correlation coefficient to the plot
    axs[0].text(1995.0, 5.0, 'r= {:.2f}'.format(r))
    axs[0].legend()
 

    # Create a plot of the model components
    '''your code'''
    
    contributions = X * beta
    
    intercept = contributions[:,0]
    net_radiation = contributions[:,1]
    air_temp = contributions[:,2]
    water_vapor = contributions[:,3]
    wind_speed = contributions[:,4]
    
    
    
    axs[1].plot(date, intercept, label='intercept')
    axs[1].plot(date, net_radiation, label='net radiation')
    axs[1].plot(date, air_temp, label='air temperature')
    axs[1].plot(date, water_vapor, label='water vapor')
    axs[1].plot(date, wind_speed, label='wind speed')
    
    axs[1].set_xticks([1992.5,1995.0, 1997.5, 2000.0, 2002.5, 2005.0, 2007.5, 2010.0])
    axs[1].set_yticks([-6, -4, -2, 0])
    
    axs[1].set_xlabel('Date')
    axs[1].set_ylabel('CO2 flux')
    axs[1].set_title('Contribution of different model components')
    
    axs[1].legend()
    
  
    
    
    # Load 2023 data and create X matrix for regression
    recent_data = np.genfromtxt(filename2, delimiter=',', skip_header=1)
    recent_pre_X = recent_data[:, 4:]
    recent_num_rows = recent_pre_X.shape[0]
    ones_array = np.ones((recent_num_rows, 1))
    recent_X = np.concatenate((ones_array, recent_pre_X), axis=1)
    
    # Create the model estimate for 2023 data
    recent_days= recent_data[:,2] / 365
    recent_co2_flux = recent_data[:,3]
    
    recent_X_B = np.dot(recent_X, beta)
    
    # Plot the model estimate for 2023 data
    axs[2].plot(recent_days, recent_co2_flux, label='de-calibrated model')
    axs[2].plot(recent_days, recent_X_B, label='Model')
    axs[2].set_yticks([-0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5])
    axs[2].set_xlabel('Date')
    axs[2].set_ylabel('CO2 flux')
    axs[2].set_title('Time series of model fit for 2023 data')
    axs[2].legend()
    
    eddy_flux_sum = 0
    for i in range(len(recent_data[:,3])):
        eddy_flux_sum += recent_X_B[i] - recent_co2_flux[i]
    decalibrated_error = (-eddy_flux_sum / len(recent_data[:,3]))
    print(f'Eddy flux instrument was de-calibrated by {decalibrated_error:.2f} units.')
    # Display the plot
    plt.show()

    # Return the regression coefficients 
    return beta
    
    pass


#----------------#
# Run the code   #
#----------------#

if __name__ == "__main__": main()


#-----------------------------------------------------------------------#
# END OF SCRIPT  							#
#-----------------------------------------------------------------------#


