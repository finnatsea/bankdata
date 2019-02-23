file = open(doc.txt, "w")
test = "Loans and discounts.. $12, 978, 293 52           $12,445,004     92 $12, 977, 234 44       $13,253,701     16   $13, 523, 420   47"
for y in
    test = list(test)
    c1 = test[0:22]
    c2 = test[23:40]
    c3 = test[73:93]
    c4 = test[93:111]
    c5 = test[112:130]
    columns = [c1, c2, c3, c4, c5]
    clean = []
    for x in columns:
        str1 = ''.join(x)
        str1 = str1.replace(" ", "")
        str1 = str1.replace(",","")
        str1 = str1.replace("$","")
        print(str1)
        clean.append(str1)

        df=pd.DataFrame(list,columns=['col1','col2'])

        res = pd.DataFrame(clean, columns=('label', '1', '2', '3', '4', '5'))
        df = pd.DataFrame(clean[0:5]).T
