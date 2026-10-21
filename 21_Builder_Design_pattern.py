class Computer:
    def __init__(self):
         self.cpu = None
         self.ram = None
         self.storage = None
         self.graphics_card = None
         self.os = None        
    
    def display(self):
        print(f" CPU:{self.cpu} RAM:{self.ram} Storage :{self.storage} Graphic:{self.graphics_card} OS:{self.os}")

class ComputerBuilder:
    def __init__(self):
        self.comp=Computer()

    def set_cpu(self,cpu):
        self.comp.cpu=cpu
        return self

    def set_ram(self, ram):
        self.comp.ram = ram
        return self
    def set_storage(self, storage):
        self.comp.storage = storage
        return self

    def set_graphics_card(self, graphics_card):
        self.comp.graphics_card = graphics_card
        return self

    def set_os(self, os):
        self.comp.os = os
        return self
    def build(self):
        return self.comp

builder=ComputerBuilder()
cmps=(
    builder
      .set_cpu("Intel i5")
      .set_ram("16 GB")
      .set_storage("512GB SSD")
      .set_os("Windows")
      .build()
      )
cmps.display()
      
