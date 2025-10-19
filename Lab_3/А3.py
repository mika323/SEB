pre_reading = int(input("Enter previous meter reading: "))
cur_reading = int(input("Enter current meter reading: "))
volume_used = cur_reading - pre_reading
if cur_reading < pre_reading:
    volume_used = 10000 - pre_reading + cur_reading
else:
    volume_used = cur_reading - pre_reading
if volume_used <= 300:
    total_cost = 21.00
elif volume_used <= 600:
    total_cost = 21.00 + (volume_used - 300) * 0.06
elif volume_used <= 800:
    total_cost = 21.00 + (300 * 0.06) + (volume_used - 600) * 0.04
else:
    total_cost = 21.00 + (300 * 0.06) + (200 * 0.04) + (volume_used - 800) * 0.025
total_cost = round(total_cost, 2)
average_cost = round(total_cost / volume_used, 2) if volume_used > 0 else 0.00

print("Previous   Current   Used   Cost   Average Cost")
print("  {}       {}    {}   {:.2f}      {:.2f}".format(pre_reading, cur_reading, volume_used, total_cost, average_cost))
