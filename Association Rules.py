import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

plik = 1

if plik == 1:
    sup = 0.025  # nasze zbiory częste, wsparcie 2.5%
    rul = 0.10  # reguły asocjacyjne, wiarygodności 10%
    dane = pd.read_csv("Police_deaths.csv")
    #normalnie wczytuje plik csv jako dataframe
    dane.drop(['person','dept','eow','cause','date','canine'], inplace=True, axis=1)
    #usuwa kolumny takie jak imiona, powtarzające się dane, dokładne daty co do dnia, czy był to K9
    #pozostawia przyczynę zgonu, rok, stan, nazwę departamentu policji
    print(dane)
    dane['All_together'] = dane[dane.columns[0:]].apply(
        lambda x: ','.join(x.dropna().astype(str)),
        axis=1
    )
    print(dane)
    #łączy wszystkie kolumny w jedną
    dane.drop(dane.iloc[:, 0:-1], inplace = True, axis = 1)
    print(dane)
    #usuwa pozostałe kolumny oprócz nowej
    dane = dane["All_together"].apply(lambda x: x.split(","))
    #tworzy dataframe odpowiedni dla encodera
    print(dane)

encoder = TransactionEncoder()
lista = encoder.fit(dane).transform(dane)
#tworzymy obiekt - programowanie obiektowe

lista = pd.DataFrame(lista, columns=encoder.columns_)
#budowanie dataframe'u z listy list, nazwy kolumn znajdują się w encoderze

czeste_zbiory = apriori(lista, sup, use_colnames=True, verbose=1)
#nasze zbiory częste

print (czeste_zbiory)

reguly = association_rules (czeste_zbiory, metric="confidence", min_threshold=rul)
#reguły asocjacyjne

print (reguly)