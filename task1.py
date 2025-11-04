def summarize_sensor_data (readings):
    unique_items = []
    for reading in readings:
        if reading[0]not in unique_items:
             unique_items.append(reading[0])
    items_with_temp = []
    for item in unique_items:
        max_temp = 0
        for reading in readings:
            if item == reading[0] and max_temp < reading[1]:
                max_temp = reading[1]
        items_with_temp.append((item,max_temp))
        items_with_temp.sort()
    return items_with_temp
        

readings = [
	('SensorB', 25.4),
	('SensorA', 22.1),
	('SensorB', 26.1), # New max for SensorB
	('SensorC', 30.5),
	('SensorA', 21.9), # Lower than previous SensorA reading
	('SensorB', 25.9)
]
result=summarize_sensor_data(readings)
print(result)
