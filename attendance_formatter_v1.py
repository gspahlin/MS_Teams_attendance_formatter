import pandas as pd
import datetime as dt

#note - I had to reencode the csv in order to load it: it was not properly UTF-8 encoded
attd = pd.read_csv('Attendance.csv')

#change the timestamp field so that it functions as a timestamp
attd['Timestamp'] = pd.to_datetime(attd['Timestamp'])

#event list is all the names, including duplicates
#time_list is all the times someone entered or left
#this function calculates the in class time  of a participant based on when the entered and left

def timekeeper(event_list, times_list):
    
    #find lat time in list
    last_out = max(times_list)
    
    #initialize dictionary
    times_dict = {}
    
    #derive name list from event list
    name_list = list(set(event_list))
    
    #in order to create the dictionary I want, I need to zip together name_list and a list of times associate with the name
    
    #create a list of times associated with each name 
    for name in name_list:
        #initialize counter for counting up event list
        ctr = 0
        
        #make a list for event times
        event_times = []
        
        #loop through the events
        for event in event_list:
            
            #check for agreement between name and event
            if name == event:
                
                #add event to list in case of agreement
                event_times.append(times_list[ctr])
            
            #count up
            ctr += 1
            
        #after finding all the relevant times check to see if the list has odd occupancy
        if len(event_times) % 2 != 0:
            
            #append the official final time of the meeting if so
            event_times.append(last_out)
        
        #split the list into two lists one for even terms one for odd terms
        even = []
        odd = []
        
        #iterate through the list and place even terms in even, else put them in odd
        for n in range(len(event_times)):
            
            if n % 2 == 0:
                even.append(event_times[n])
                
            else:
                odd.append(event_times[n])
        
        #start a list for deltas
        deltas = []
        
        #compute the differences and add to deltas list
        for e in range(len(even)):
            
            d = odd[e] - even[e]
            
            deltas.append(d)
        
        #update times dict with name: deltas.sum()
        
        times_dict.update({name: sum(deltas, dt.timedelta())})
        
        
    return times_dict

#event list
e_list = attd['Full Name'].to_list()

#times list 
t_list = attd['Timestamp'].to_list()

att_times = timekeeper(e_list, t_list)

print(att_times)

#consolidate into a dataframe

timedelts = list(att_times.values())

st_names = list(att_times.keys())

times_dict = {'Name': st_names, 'Time_in_class': timedelts}

att_df = pd.DataFrame(times_dict)

#next problem - split out the names and identify first and last name

name_lst = att_df['Name'].to_list()

#make a new list
formatted = []

#split all the names in the name_lst and add them back into the dataframe in the format last, first
for name in name_lst:
    
    f_name = name.split(' ')
    
    formatted.append(f'{f_name[-1]}, {f_name[0]}')
    
att_df['Name'] = formatted

#sort the dataframe
att_df = att_df.sort_values(by = 'Name')

#Write out a .csv

att_df.to_csv('formatted_attendance.csv', index = False)