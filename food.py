from menu_item import MenuItem

class Food(MenuItem):
    # __init__ メソッドを定義してください
    def __init__(self,name,price,calorie):

        #<<<upd_sta mnao 2021/9/12 super()メソッドを使う
        #※親クラスのメソッドを使う
        #self.name = name
        #self.price = price
        super().__init__(name,price)
        #>>>upd_end mnao 2021/9/12

        self.calorie = calorie

    # info メソッドを定義してください
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'

    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')
