

class categoryClass:

  def __init__(self, name):
    self.name = name
    self.estimatedSale = 0;
    self.actualSale = 0
    self.estimatedProfit = 0
    self.actualProfit = 0
    self.cost = 0

  def getEstimatedSale():
    # loops through all products in category 
      # Estimated Sale = # product * product price
    return self.estimatedSale

  def getActualSale():
    # loops through all products in category 
      # Actual Sale = # product sale * product price
    return self.actualSale

  def getEstimatedProfit():
    # loops through all products in category
      # Estimated Profit = self.estimatedSale - self.cost
    return self.estimatedProfit

  def getActualProfit():
    # loops through all products in category
      # Actual Profit = self.actualSale - self.cost
    return self.actualProfit
  


class productClass:
    
  def __init__(self, name, category, price, source):
    self.name = name
    self.category = category
    self.price = price
    self.source = source

  def getName():
    return self.name
  
  def getCategory():
    return self.category

  def getPrice():
    return self.price
  
  def getSource():
    return source


class inventoryClass:

  def __init__(self, name):
    self.name = name
    self.numberOfProducts = 0
    self.inventoryCost = 0
    self.location = " "
    self.category = {}
  
  def addProduct(category, productName, price, quantity):
    #check if category exist
    if category in self.category:
    
    else
      newCategory = categoryClass(category)
      # category = {'cagetoryName1':{item1, item2, item3}, 'categoryName2':{item1, item2, item3}}
      self.category[newCategory]


