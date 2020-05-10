def display_lcd(in_lines):
    lines = in_lines[:4]
    n = 4
    for line in lines:
        n+=-1
        print(line[:20])
    for i in range(n):
        print('#')
    print('--------------------')


class menu():
    def __init__(self,options):
        self.options = list(options)
        self.index = 0
        self.onscreen = self.options[:4]
    
    def select(self,option):
        option_type = type(option)
        if option_type == str:
            try:
                option_index = self.options.index(option)
            except:
                return False
        elif option_type == int:
            option_index = option
        else:
            return False
        try:
            self.options[option_index]
            self.index = option_index
            if option_index > 3:
                self.onscreen = self.options[option_index-3:option_index+1]
            else:
                self.onscreen = self.options[:4]
            self.display()
            return True
        except:
            return False
    
    def forward(self,amount=1):
        change = (self.index+amount)%len(self.options)
        self.index = change
        if change > 3:
            self.onscreen = self.options[change-3:change+1]
        elif change < 4:
            self.onscreen = self.options[:4]
        self.display()
        return change
        
    def display(self):
        tokend_list = []
        for item in self.onscreen:
            if self.options.index(item)==self.index:
                indicator = '>'
            else:
                indicator = '-'
            tokend_list.append(indicator + item)
        display_lcd(tokend_list)
        #TODO
    
    
    
getränke = menu(['Wasser','Sprudel','Fanta','Cola','Apfelsaft','Bier','Schnaps','Pepsi'])

zeug = menu(["Scanen","Wissen"])

zeug.display()

import time
while 1==1:
    zeug.forward()
    time.sleep(1)

#wenn wir knöpfe einsparen wollen, können wir auch nur nach unten gehen:
#   Cola -> Fanta -> Wasser -> Sprite -> Cola -> Fanta -> ...

