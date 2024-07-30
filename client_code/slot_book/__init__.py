from ._anvil_designer import slot_bookTemplate
from anvil import *
import anvil.server
from datetime import datetime, timedelta
import random
import string
from datetime import date
# import global_vars

class slot_book(slot_bookTemplate):
    def __init__(self, oxi_id=None, location_name=None, id_of_serviceprovider=None, service_type=None, oxi_username=None, **properties):
        self.init_components(**properties)
        self.set_button_date()
        self.oxi_id = oxi_id  # Store the oxi_id
        self.oxi_username = oxi_username   # Store received values
        self.location_name = location_name  # Store the location_name
        self.id_of_serviceprovider = id_of_serviceprovider
        self.service_type = service_type
       # Print the values to the console
        print(f" oxi_id in Slot Book: {self.oxi_id}")
        print(f"Location Name in Slot Book: {self.location_name}")
        print(f"ID of Service Provider in Slot Book : {self.id_of_serviceprovider}")
        print(f"User Name in Slot Book: {self.oxi_username}")
        print(f"Service Type in slot book: {self.service_type}")
   
    def set_button_date(self):
        current_date = datetime.now()
        for i in range(1, 5):  # Assuming you have 4 buttons named button_1, button_2, ..., button_4
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            date_for_button = current_date + timedelta(days=i-1)
            # Format the date as "Day" (e.g., "Tue") and day number (e.g., "17")
            formatted_date = date_for_button.strftime("%a %d")
            button.text = formatted_date
        
    def button_1_click(self, **event_args):
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          button_time = datetime.strptime(button.text, "%I:%M %p").time()
          if current_time > button_time:
              button.enabled = False  
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

    def button_2_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          
          button.enabled = True 
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

    def button_3_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          
          button.enabled = True 
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

    def button_4_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          
          button.enabled = True 
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

    def primary_color_1_click(self, oxi_id=None, **event_args):
        # self.oxi_id = oxi_id  # Store the oxi_id
        try:
            # Generate random booking ID
            oxi_book_id = f"BI{random.randint(10000, 99999)}"  # Example: BI70000
    
            # Set the booking time
            oxi_book_time = '19:00 - 21:00'  # Fixed time range
    
            # Get the current date
            current_date = datetime.now()
            oxi_book_date_db = current_date.date()  # Store as date type for the database
    
            # Format current date for display purposes
            oxi_book_date_display = current_date.strftime('%d %b %Y')  # Format to "23 Jul 2024"
    
            # Get current datetime and format oxi_date_time
            current_datetime = datetime.strptime(f'{current_date.strftime("%d-%m-%Y")} {oxi_book_time.split(" - ")[0]}', '%d-%m-%Y %H:%M')
            oxi_date_time = current_datetime.strftime('%a, %d %b %I:%M %p')
            
            # Prepare variables
            oxi_id = self.oxi_id  # From new_dashboard form
            oxi_servicer_id = self.id_of_serviceprovider  # The ID of the selected service provider
            oxi_service_type = self.service_type  # The type of service selected (OxiGym, OxiWheel, OxiClinic)
            oxi_username = self.oxi_username  # Username from the login form
            oxi_payment_id ="0000"
          
            # Call the server function to insert booking data
            anvil.server.call('insert_booking_data', oxi_id, oxi_book_date_db, oxi_servicer_id, oxi_book_id, oxi_date_time, oxi_book_time, oxi_payment_id, oxi_service_type, oxi_username)

            
            print("Booking data inserted successfully.")
            open_form('Activity')
        except Exception as e:
            print(f"Error: {e}")
      
