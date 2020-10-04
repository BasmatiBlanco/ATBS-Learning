Sample_Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
new = {}
for i in range(len(Sample_Data)):
    if Sample_Data.count(Sample_Data[i].values()) == 1:
        new[i] = Sample_Data[i].values()

