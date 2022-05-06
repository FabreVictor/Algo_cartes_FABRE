class Carte:
    def __init__(self,name,cost,description,effet):
        self._name = name
        self._manacost = cost 
        self._description = description
        self._effet = effet
       
class crystal(Carte): 
 
    def __init__(self,name,cost,description,effet,gain):
         self._managain = gain
    def gainMana(self):
        return "mana"
        
         
    super().__init__(self,name,cost,description,effet)

class creature(Carte): 
 
    def __init__(self,name,cost,description,effet,pv,degat,defense):
        self._pv =pv
        self._degat = degat 
        self._defense = defense
        
    def inflictedamage(self,targetpv,degat,targetdefense):
        targetpv -= (degat-targetdefense)
    def getpv(self):
        return self._pv
    
    def getdegat(self):
        return self._degat
          
    def getdefense(self):
        return self._defense   
            
    super().__init__(self,name,cost,description,effet)
    
class blast(Carte): 
 
    def __init__(self,name,cost,description,effet,degat):
         self._degat = degat
         
    def inflictedamage(self,targetpv,degat,targetdefense):
        targetpv -= (degat-targetdefense)
        
         
    super().__init__(self,name,cost,description,effet)      
        
class mage ():        
    def __init__(self,name,manamax,manaactuel,mains,defausse,zonejeu):
        self._name = name
        self._manamax = manamax 
        self._manaactuel = manaactuel
        self._mains = mains
        self._defausse = defausse
        self._zonejeu = zonejeu
    def playcard ():
        
    def regenmana ():
        
    def usecreature ():
        
