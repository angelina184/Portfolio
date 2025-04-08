import pandas as pd


df = pd.read_csv('bookings.csv', sep=';')

#print(df.columns, df.dtypes)

#changing column's names according to standards
columns = {'Hotel' : 'hotel', 
            'Is Canceled' : 'is_cancelled', 
            'Lead Time' : 'lead_time', 
            'arrival full date' : 'arrival_full_date',
            'Arrival Date Year' : 'arrival_date_year', 
            'Arrival Date Month' : 'arrival_date_month', 
            'Arrival Date Week Number' : 'arrival_date_week_number',
            'Arrival Date Day of Month' : 'arrival_date_day_of_month', 
            'Stays in Weekend nights' : 'stays_in_weekend_nights',
            'Stays in week nights' : 'stays_in_week_nights', 
            'stays total nights' : 'stays_total_nights',
            'Adults' : 'adults', 
            'Children' : 'children',
            'Babies' : 'babies', 
            'Meal' : 'meal', 
            'Country' : 'country', 
            'Reserved Room Type' : 'reserved_room_type', 
            'Assigned room type' : 'assigned_room_type',
            'customer type' : 'customer_type', 
            'Reservation Status' : 'reservation_status', 
            'Reservation status_date' : 'reservation_status_date'}
df.rename(columns=columns, inplace=True, errors='raise')

"""
print("Top 5 places that tourists visit")
sort = df.query('is_cancelled == 0')
group = sort.groupby('country', as_index=False)
count = group.agg({'is_cancelled': 'count'})
sorted = count.sort_values('is_cancelled', ascending=False)
print(sorted[:5])
"""

"""
print("The standart/avarage number of nights people book:")
sort_total_nght = df.query('stays_total_nights != 0')
group_hot_nght = sort_total_nght.groupby('hotel', as_index=False)
avarege = group_hot_nght.agg({'stays_total_nights':'mean'})
print(round(avarege))"
"""

"""
print("How often people change their mind about the room to stay in:")
sort_changed_rooms = df.query('reserved_room_type != assigned_room_type')
group_hotels = sort_changed_rooms.groupby('hotel', as_index=False)
sorted = group_hotels.agg({'reserved_room_type':'count'})
print(sorted)
"""

""""
print("TOP 3 common monthes were booked between(2016/2017):")
sort_year = df.query('arrival_date_year in [2016,2017]')
group_monthes = sort_year.groupby('arrival_date_month', as_index=False)
count_cuntries = group_monthes.agg({'country':'count'})
sort = count_cuntries.sort_values('country',ascending=False)
print(sort[:3])
"""
"""
print("monthes and years when people usually cancelled the booking:")
sort_conseled = df.query('hotel == "City Hotel" & is_cancelled == 1')
group_month= sort_conseled.groupby(['arrival_date_year','arrival_date_month'], as_index=False)
count_cuntries = group_month.agg({'is_cancelled':'count'})
sort = count_cuntries.sort_values(['arrival_date_year','is_cancelled','arrival_date_year'],ascending=False)
print(sort)
"""
"""
print(df.describe()[1:2])
"""
# create table "total_kids"
# which hotels are popular among adults with kids


total_kids = df['babies'] + df['children']
df['total_kids'] = total_kids
"""
group_hotels = df.groupby('hotel', as_index=False)
kids = group_hotels.agg({'total_kids' : 'mean'})
res = kids.sort_values('total_kids', ascending=False)
print(res)
print(df['total_kids'][:5])
"""

#finding out how many bookings were cancelled by guests who had kids

# przyjmuje wartosc True lub False
df['has_kids'] = df['total_kids'] > 0
print(df['has_kids'])
#count the number of records and canceled the visit
canceled = df.query('has_kids == True and is_cancelled == 1')
records =canceled.agg({'hotel'  : 'count'}) 
#count the total number of bookings made by guests with kids.
not_canceled = df.query('has_kids == True')
records2 = not_canceled.agg({'hotel'  : 'count'})

print(records)
print(records2)