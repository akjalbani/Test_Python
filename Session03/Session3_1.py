'''1.	 The run time of a match is 105 minutes. Write a python program to calculate in hours and print the result. (understanding and using the floor division operator //). '''
run_time = 105 # minute
hr = 60 # 1 hr = 60 minutes
tot_hrs = run_time//hr
tot_minutes = run_time% hr

print("Match was played for {} hr and {} minutes".format(tot_hrs,tot_minutes))
