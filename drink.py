from menu_item import MenuItem

class Drink(MenuItem):
    # インスタンス時初期化処理を追加
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

    # info メソッドを定義してください
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'
