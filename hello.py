#この行はコメントです。
print(1 + 2);
price = 510;
count = input('数字を入力してください：');

total = price * int(count);

print('合計金額は' + str(total) + '円です。');

testbox = ['apple','orange','banana'];

print('1つ目の箱の中に入っているのは' + testbox[0] + 'です。');

print('箱の中にgrapeを追加します');
print('変更前：' + str(testbox));
testbox.append('grape');
print('変更後：' + str(testbox));

for test in testbox:
    print('箱の中は' + test + 'です。');
