goukei = 0

#iの値を1から1ずつ増やして11になったらループから抜ける
#for i in range(1,11):
#for i in range(11):
for i in range(0, 11, 1):
    print(i);
    goukei = goukei + i;

#合計を文字列に変換して表示
print("合計は" + str(goukei) + "です");
