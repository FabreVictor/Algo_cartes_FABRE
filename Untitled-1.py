class Carte:
    def __init__(self,name,cost,description,effet):
        self._name = name
        self._manacost = cost 
        self._description = description
        self._effet = effet
       
class crystal(Carte): 
 
    def __init__(self,name,cost,description,effet,gain):
         self._managain = gain #valeur de regeneration
    def gainMana(self,manamax,manactuel): #mana actuel et mana max sont se du mage qui joue la crystal
        manamax+=1
        manactuel+=self._managain
        return manamax,manactuel#regenere les mana actuel et augmnanter de 1 le manamax
        
         
    super().__init__(self,name,cost,description,effet)

class creature(Carte): 
 
    def __init__(self,name,cost,description,effet,pv,degat,defense):
        self._pv =pv
        self._degat = degat 
        self._defense = defense
        
    def inflictedamage(self,targetpv,degat,targetdefense):
        targetpv -= (degat-targetdefense)
    def getpv(self):
        return self._pv #accesseur
    
    def getdegat(self):
        return self._degat #accesseur
          
    def getdefense(self):
        return self._defense #accesseur  
            
    super().__init__(self,name,cost,description,effet)
    
class blast(Carte): 
 
    def __init__(self,name,cost,description,effet,degat):
         self._degat = degat
         
    def inflictedamage(self,targetpv,degat,targetdefense):
        targetpv -= (degat-targetdefense) #selectione une cible et leu inflige les degat moins sa defens esi elle en a.
        
         
    super().__init__(self,name,cost,description,effet)      
        
class mage ():        
    def __init__(self,name,manamax,manaactuel,mains,defausse,zonejeu):
        self._name = name
        self._manamax = manamax #mana maximum du jouer augmznte avec les crystaux il augmante chaque fin de tour 
        self._manaactuel = manaactuel
        self._mains = mains #transphormé en liste
        self._defausse = defausse
        self._zonejeu = zonejeu
    def playcard (self):
        return self._mains
                #permet de posé et jouer une carte
    def regenmana (self):#regeneration a chaque fine de tour au niveau max de mana
        self._manaactuel = self._manamax 
        self._manamax += 1
        return self._manaactuel
    def usecreature (self):
        return self._zonejeu
                #selection une creature et lui permet d'ataqué
        
