#from uuid import uuid4
import pandas as pd


class GettingData:
                
        
    def getting_data(list_elements):
        #initiating the attributes
        #keyId = ""
        """from uuid import uuid4
        keyId = str(uuid4())
        """
        locality = "None"
        type_of_property = "None" #House/apartment #depending on the search term? or it is already in the URL
        subtype_of_property = "None" #Bungalow, Chalet, Mansion, ...
        price = 0
        type_of_sale = "For Sale" #For sale based on the search results #Exclusion of life sales depending on the search term? For Sale or For Rent
        num_of_rooms = 0
        area = 0
        fully_equipped_kitchen = 0 #Yes/No
        furnished = 0 #Yes/No
        open_fire = 0 # Yes/No
        terrace = 0 #Yes/No If yes: Area
        garden = 0 #Yes/No If yes: Area
        surface_of_the_land = 0
        surface_area_of_the_plot_of_land = 0
        number_of_facades = 0
        swimming_pool = 0 #Yes/No
        state_of_the_building = 0 #New, to be renovated, ...
        
        #creating a unique id for each property using uuid4
        #keyId = str(uuid4())
        
        #getting the data and putting it to a dictionary per property
        for key, value in list_elements.items():
            if key ==  'Prijs' and value is not None:
                price = value
            elif key == 'Adres' and value is not None:
                locality = value
            elif key == 'Type' and value is not None:
                type_of_property = value
            elif key == 'Woonopp.' and value is not None:
                area = value
                surface_of_the_land = value
            elif key == 'Grondopp.' and value is not None:
                surface_area_of_the_plot_of_land = value
            elif key == 'Slaapkamers' and value is not None:
                num_of_rooms = value
            elif key == 'Tuin' and value is not None:
                garden = value
            elif key == 'Bebouwing' and value is not None:
                state_of_the_building = value

        #saving each property detail in a dictionary, if the value is not on the list, it will be zero or None on the property details

        details = (locality, type_of_property, subtype_of_property, price, 
                   type_of_sale, num_of_rooms, area, fully_equipped_kitchen, 
                   furnished, open_fire, terrace, garden, surface_of_the_land,
                   surface_area_of_the_plot_of_land, number_of_facades, 
                   swimming_pool, state_of_the_building)
        
        #property_details = { keyId, details}
                
        return details
    
    
    def convert_to_csv(properties):
        #We have to initialize it again for the new file
        locality = []
        type_of_property = [] 
        subtype_of_property = [] 
        price = []
        type_of_sale = [] 
        num_of_rooms = []
        area = []
        fully_equipped_kitchen = [] 
        furnished = [] 
        open_fire = [] 
        terrace = [] 
        garden = [] 
        surface_of_the_land = []
        surface_area_of_the_plot_of_land = []
        number_of_facades = []
        swimming_pool = [] 
        state_of_the_building = []
        
        for x in properties:
            locality.append(x[0])
            type_of_property.append(x[1]) 
            subtype_of_property.append(x[2]) 
            price.append(x[3])
            type_of_sale.append(x[4])
            num_of_rooms.append(x[5])
            area.append(x[6])
            fully_equipped_kitchen.append(x[7]) 
            furnished.append(x[8])
            open_fire.append(x[9])
            terrace.append(x[10])
            garden.append(x[11])
            surface_of_the_land.append(x[12])
            surface_area_of_the_plot_of_land.append(x[13])
            number_of_facades.append(x[14])
            swimming_pool.append(x[15])
            state_of_the_building.append(x[16])
        
        #using pandas to extract the data to a dataframe
        df = pd.DataFrame({'Locality': locality, 'Type of Property' : type_of_property, 
                         'Subtype of Property' : subtype_of_property, 'Price' : price, 
                         'Type Of Sale' : type_of_sale, 'Number of Rooms' : num_of_rooms, 
                         'Area' : area, 'Fully Equipped Kitchen' : fully_equipped_kitchen, 
                         'Furnished' : furnished, 'Open Fire' : open_fire, 'Terrace' : terrace, 
                         'Garden' : garden, 'Surface of the Land' : surface_of_the_land,
                         'Surface Area of the Plot of the Land' : surface_area_of_the_plot_of_land, 
                         'Number of Facades' : number_of_facades, 'Swimming Pool' : swimming_pool, 
                         'State of the Building' : state_of_the_building })
        
        #saving the file to a CSV (: 
        #df.to_csv('output.csv', index=False)
        
        #success = print("Output to csv successful!")
        return(df)

       