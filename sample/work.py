
import csv

  
with open("data.csv","w+") as csvfile:
    writer = csv.writer(csvfile)
    writer .writerow(["Name","Address","Phone","Area","Image","Image url"])
    writer.writerow(["AC MARRIOTT","1712 Commerce","214-290-0111","Main Street District","AC-Marriot.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/AC-Marriot.jpg"])


with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


with open("data.csv","a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ADOLPHUS HOTEL","1321 Commerce St","214-742-8200","Main Street District","Adolpus.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Adolphus.jpg"])


with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)   
    writer.writerow(["ALOFT","1033 Young Street", "214-761-0000","Civic Center","Aloft.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Aloft.jpg"])     


with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["BELMONT HOTEL","901 Fort Worth Av" ,"214-393-2300","Trinity Groves","Belmont.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Belmont.jpg"])        


with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["CAMBRIA HOTEL","1907 Elm St" ,"214-220-2900","Main Street District","cambria.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Cambria.jpg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["CANOPY BY HILTON","2950 Cityplace West", "214-522-2929","Uptown","canopy.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Canopy.jpg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["COURTYARD BY MARRIOTT","310 S Houston St.", "214-238-6589","Main Street District","courtyard.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Courtyard-by-marriot.jpg"]) 

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["CROWNE PLAZA DALLAS","1015 Elm Street" ,"877-270-1393","Main Street District","crowe.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/crowne-plaza-dallas-e1546627876794.jpeg"])     

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["DALLAS MARRIOTT DOWNTOWN","650 North Pearl St","214-979-9000","Main Street District","Lobby.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Lobby_JPG.jpg"])    


with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["ELEMENT BY WESTIN","4005 Gaston ","469-399-1049","Old East Dallas","element.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Element.jpg"])


with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["DALLAS MARRIOTT DOWNTOWN","650 North Pearl St.","214-979-9000","Main Street District","dallas.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Lobby_JPG.jpg"])  

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["FAIRMONT HOTEL","1717 North Akard Str", "214-720-2020","Dallas Arts District","Fairmount.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Fairmont.jpg"])      

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["HALL ARTS HOTEL","2323 Ross Ave", "214-269-9535","Dallas Arts District","Hall.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Hall-arts.png"])  

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["HAMPTON INN & SUITES DALLAS DOWNTOWN","1700 Commerce Street", "214-290-9090","Main Street District","hampton.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/hampton-inn-suites-dallas.jpg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow (["HILTON GARDEN INN DOWNTOWN DALLAS","1600 Pacific Ave","214-299-8982","Main Street District","Hilton.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/HIlton-garden-inn.jpg"])
    
    
with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow (["HOME 2 SUITES BY HILTON","3301 Gaston", "214-765-2690","Old East Dallas","home2.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/home2-suites-by-hilton.jpg"]) 

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["HOMEWOOD SUITES","1025 Elm Street", "214-748-4000","Main Street District","Homwood.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Homewood.jpg"]) 

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["HOTEL INDIGO","1933 Main Street", "214-741-7700","Main Street District","Hotel.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Hotel-indigo.jpeg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow (["HOTEL SAINT GERMAIN","2516 Maple Avenue" ,"214-871-2516","Uptown","hotelg.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/hotel-st-germain.jpg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow (["HOTEL ZAZA","2332 Leonard Street ","214-468-8399","Uptown","zaza.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Hotel-zaza.jpg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["PITTMAN HOTEL","2551 Elm St.", "469.498.2500","Deep Ellum","pit.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Klyde_Warren_Park_SF8mfHpHwMcKDysv55XUPzt18q0ABlZBh_rgb_l-e1546906453840.jpg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["ROSEWOOD CRESCENT HOTEL","400 Crescent Court ","214-871-3200","Uptown","Rose.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Rosewood.jpg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["THE GUILD HOTEL VICTORY PARK","3111 North Houston St.", "(512) 623-7480","Victory Park","guild.jpg","https://downtowndallas.com/wp-content/uploads/2018/11/110608-View-to-downtown-resized-Aerial-Photos-June-8-2011-61.jpg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["THE JOULE","1530 Main St. ","214-748-1300","Main Street District","Joule.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/The-Joule.jpg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["W DALLAS – VICTORY","2440 Victory Park La ","214-397-4100","victory Park","wDallas.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/w-Dallas.jpg"])

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv","a") as csvfile:
    
    writer = csv.writer(csvfile)  
    writer.writerow(["WESTIN DALLAS DOWNTOWN","1201 Main Street ","972-584-6650","Main Street District","Wertin.jpg","https://downtowndallas.com/wp-content/uploads/2018/09/Westin.jpg"])                              
          