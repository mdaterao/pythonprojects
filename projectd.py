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
import numpy
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
    
    # Create a time series plot of the data
    '''your code'''

    # Display the plot
    plt.show()

     # Plot a histogram of the data
    '''your code'''

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

    # Loop over each month
    
    # Plot the average flux by month
    '''your code'''

    # Return the result
    
    pass


#---------------------------#
# PART G	                  #
#---------------------------#

def HFregression(filename):
	
    # Purpose: 
        #    Create a regression model for CO2 fluxes
        #    Visualize the outputs of the model

    # Read in the data from the Harvard Forest
    '''your code'''

    # Create the X matrix for the regression
    '''your code'''
    
    # Estimate the regression coefficients
    '''your code'''
    
    # Create the model estimate
    '''your code'''
    
    # Calculate the correlation coefficient
    '''your code'''
    
    # Plot the model estimate
    '''your code'''
    
    # Add the correlation coefficient to the plot
    
    # Create a plot of the model components
    '''your code'''
    
    # Load 2023 data and create X matrix for regression
    
    # Create the model estimate for 2023 data
    
    # Plot the model estimate for 2023 data
    
    # Display the plot
    plt.show()

    # Return the regression coefficients 
    
    pass


#----------------#
# Run the code   #
#----------------#

if __name__ == "__main__": main()


#-----------------------------------------------------------------------#
# END OF SCRIPT  							#
#-----------------------------------------------------------------------#


