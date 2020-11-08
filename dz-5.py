class Title():
    def __init__(self, name):
        if Title.check_name(name):
            self.__name = name
        else:
            raise ValueError

    @staticmethod
    def check_name(text):
        if text:
            return True
        else:
            return False
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if Title.check_name(name):
            self.__name = name
        else:
            raise ValueError


class Product(Title):
    def __init__(self, name, calorific, cost):
        super().__init__(name)
        if Product.check(calorific):
            self.calorific = calorific
        else:
            raise ValueError
        if Product.check(cost):
            self.cost = cost
        else:
            raise ValueError
    
    @staticmethod
    def check(element):
        return element > 0

          
class Ingredient():
    def __init__(self, product, weight):
        self.product = product
        if Ingredient.check_weight(weight):
            self.__weight = weight
        else:
            raise ValueError
    
    @staticmethod
    def check_weight(weight):
        return weight > 0

    @property
    def weight(self):
        return self.__weight
        
    @weight.setter
    def weight(self, weight):
        if Ingredient.check_weight(weight):
            self.__weight = weight
        else:
            raise ValueError   

    def get_calorific(self):
        return self.product.calorific * self.__weight / 100

    def get_cost(self):
        return self.product.cost * self.__weight / 100
        
class Pizza(Title):
    def __init__(self, name, ingredient):
        super().__init__(name)
        self.ingredient = ingredient
       

# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы
pizza_calorific = 0
pizza_cost = 0
print(f'Состав пиццы "{pizza_margarita.name}":')
for each in pizza_margarita.ingredient:
    ingredient_calorific = each.get_calorific()
    ingredient_cost = each.get_cost()
    print(f'{each.product.name} ({ingredient_calorific} Ккал)  -  {ingredient_cost} руб.')
    pizza_calorific +=ingredient_calorific
    pizza_cost +=ingredient_cost
print('-----------------------------------------')
print(f'{pizza_margarita.name} ({pizza_calorific} Ккал)  -  {pizza_cost} руб.')
