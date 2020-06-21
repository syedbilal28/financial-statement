class Customer:
    def __init__(self,name,phone,address):
        self.name =  name
        self.phone = phone
        self.address = address


class Asset:
    def __init__(self,value,type="Debit"):
        self.value = value
        self.type = type
class Liability:
    def __init__(self,value,type="Credit"):
        self.value = value
        self.type = type
class Revenue:
    def __init__(self,value,type):
        self.value = value
        self.type = type

