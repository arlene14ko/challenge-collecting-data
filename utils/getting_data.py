#importing the pandas package 
import pandas as pd
from Typing import List, Dict


class GettingData:
                
        
    def getting_data(dict_elements: Dict[str,str]) -> List(str):
        """
        Function that will convert the data from a dictionary to a list
        With the proper details
        Initiating the attributes:
        :address = the address in the data
        :type_of_property = type of the property 
        :subtype_of_property = the subtype of the property 
        :price = price of the property 
        :type_of_sale = "For Sale" #Depending on the search 
        :num_of_rooms = number of bedrooms
        :area = the residential area of the property
        If it is yes, it is 1, if it is a no then it is 0
        :fully_equipped_kitchen = is either a yes or a no
        :furnished = either a yes or a no
        :open_fire = either a yes or no
        If it is no, it will be 0, if it is yes it will be the area
        :terrace = terrace in the property
        :garden = garden of the property
        :surface_of_the_land = the residential area
        :surface_area_of_the_plot_of_land = the ground area
        :number_of_facades = 0
        :swimming_pool = 0 #Yes/No
        :state_of_the_building = 0 #New, to be renovated, ...
        :locality = depends on the search file
        """
        address = "None"
        type_of_property = "None" 
        subtype_of_property = "None"
        price = 0
        type_of_sale = "For Sale" #For sale based on the search file 
        num_of_rooms = 0
        area = 0
        fully_equipped_kitchen = 0 
        furnished = 0 
        open_fire = 0
        terrace = 0 
        garden = 0 
        surface_of_the_land = 0
        surface_area_of_the_plot_of_land = 0
        number_of_facades = 0
        swimming_pool = 0 #Yes/No
        state_of_the_building = 0 
        locality = "Antwerp" #depending on your search file
       
        """
        Getting the data and putting it into each correct attribute
        :attrib details will contain all the details of the property
        Then we will return the details as a list
        
        """
        for key, value in dict_elements.items():
            if key ==  'Prijs' and value is not None:
                price = value
            elif key == 'Adres' and value is not None:
                address = value
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

        details = (address, type_of_property, subtype_of_property, price, 
                   type_of_sale, num_of_rooms, area, fully_equipped_kitchen, 
                   furnished, open_fire, terrace, garden, surface_of_the_land,
                   surface_area_of_the_plot_of_land, number_of_facades, 
                   swimming_pool, state_of_the_building, locality)
        
        return details
    
    
    def convert_to_csv(properties: List(str)):
        """
        This function will have the parameter properties and it will convert it to a dataframe
        We have to initialize again for the dataframe for each column
        And then it will be distributed using a loop
        :attrib df will contain the properties in a dataframe
        This function will also return the attrib df
        """
        locality = []
        address = []
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
            address.append(x[0])
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
            locality.append(x[17])
        
        df = pd.DataFrame({'Locality': locality, 'Address': address, 'Type of Property' : type_of_property, 
                         'Subtype of Property' : subtype_of_property, 'Price' : price, 
                         'Type Of Sale' : type_of_sale, 'Number of Rooms' : num_of_rooms, 
                         'Area' : area, 'Fully Equipped Kitchen' : fully_equipped_kitchen, 
                         'Furnished' : furnished, 'Open Fire' : open_fire, 'Terrace' : terrace, 
                         'Garden' : garden, 'Surface of the Land' : surface_of_the_land,
                         'Surface Area of the Plot of the Land' : surface_area_of_the_plot_of_land, 
                         'Number of Facades' : number_of_facades, 'Swimming Pool' : swimming_pool, 
                         'State of the Building' : state_of_the_building })
        
        return(df)

       