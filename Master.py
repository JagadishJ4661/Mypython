Total = 10000
Effort = input( "what is your daily effort ?" )
Effort = int(Effort)
Days = Total // Effort
Hours = Total % Effort
Months = Days // 30
Days = Days % 30
Year = Months // 12
Months = Months % 12 
print(Year , "Years" , Months , "Months" , Days , "Days" , Hours , "Hours" )
