"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

# figure out when checkpoint opens and closes
# how long to wait until open or close is where it is using control_dist_km

# brevet_start_time is an arrow object
# hours and minutes should be integers (round minutes to nearest integer)





# compute hrs and mins based on control_dist_km and shift brevet_start_time


# first checkpoint at 0km always opens at brevet start time(not shifted)
# and always closes after 1 hour(dont have to calculate, just shift by 1 hour)

# brevet_dist_km. Figure out where first checkpoint and last checkpoint(s) is/are
# how? if control_dist_km is >= brevet_dist_km, meaning if you have a 200km brevet, 210, up tp 240 (which is the max distance for a 200km brevet) (up to 20% higher), then its the last checkpoint
# this is for open time
# close time from the table in the link.


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    hours, minutes =  # figure out how to calculate
    return brevet_start_time.shift(hours=hours, minutes=minutes)
 
def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    hours, minutes =  # figure out how to calculate
    return brevet_start_time.shift(hours=hours, minutes=minutes)
