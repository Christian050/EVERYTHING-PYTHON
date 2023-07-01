import phonenumbers
from phonenumbers import timezone, geocoder, carrier


class Contact():    
    def getContact(self, number):     
        self.number = number
        self.phone = phonenumbers.parse(self.number)
        self.time = timezone.time_zones_for_number(self.phone)
        self.carrier = carrier.name_for_number(self.phone, 'en')
        self.registration = geocoder.description_for_number(self.phone, 'en')
        
        print(f'{self.number}\n{self.phone}\n{self.carrier}\n{self.registration}')
    

if __name__ == '__main__':
    Contact().getContact(input('Enter phone number (include zip): '))
    
    
