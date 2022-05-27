class Student:
    school="AkiraChix"
    def __init__(self,name,year_of_birth,initials) :
          self.name=name
          self.year=year_of_birth
          self.abbrev=initials
          
    def greeting(self):
        return f"Hello {self.name} from {self.country} welcome to {self.school}" 

    def full_name(self,):
         return f"{self.name}"

    def year_of_birth(self):
         return f"{self.year}"
    
    
    def initials(self):
     initials = ""

     full_name = self.name.split()
     for name in full_name: 
      initials += name[0]

     return initials

    
           
         