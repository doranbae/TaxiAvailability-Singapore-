#Taxi-Availability in Singapore

####Background
Last August, I was in Singapore with my husband on a four-day trip. On the second day, we visited Orchard Road, the holy grail of shopping all the luxury brands and amazying restaurants. After lunch, as we were supposed to meet someone, we decided to take a cab to the meeting point.

As it turned out, hailing for a cab was the hardest thing in Singapore. My husband stepped off the sidewalk and stuck his arm out and waved at empty cabs, but no one stoped for us. After 15 minutes, a kind driver told us that cabs cannot pull over the sidewalk, and instructed us to go to a proper taxi station. 

Little confused, but we followed his instruction. We walked 5 minutes to a taxi station and found 50 people in line waiting for a cab. 
Well, when in Rome, do as the Romans do. So we waited in line for an hour. AN HOUR for a cab. Don't you think this was a little outrageous? So I decided to create a map with data of empty cabs' location in real time.

####Data Source
https://www.mytransport.sg

###taxiavail.py
This connects to API to Singapore government's datamall. It downloads real-time location data of all the available cabs in Singapore. 
It saves the result in JSON format.
###savetotable.py
This saves the result into dataframe and then save it to a txt file. 
