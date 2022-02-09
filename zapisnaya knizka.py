import pandas as pd

def append_work(data):
    inp = input("Введите заплонированные дела через запятую: ").split(",")
    csv_file = pd.read_csv("note.csv")

    data['Дела'] = inp
    data['Статус'] = ["Не выполнено"] * len(inp)

    tmp = input("Введите время через запятую: ").split(",")
    data['Время'] = tmp

    df = pd.concat([csv_file, pd.DataFrame(data)], ignore_index=True)

    df.to_csv("note.csv", index=None)

    print(df)

data = {"Дела":[], "Статус":[], "Время":[]}

append_work(data)

while True:
    what = input("1-добавить новые дела, 2-поменять статус дела, 3-стоп: ")
    if what == "1":
        append_work(data)

    elif what == "2":
        sts = input("Введите индекс и статус дела через пробел: ").split(" ")
        csv_file = pd.read_csv("note.csv")

        df = dict(pd.concat([csv_file, pd.DataFrame(data)], ignore_index=True))

        status = list(df['Статус'])
        status[int(sts[0])] = sts[1]
        df['Статус'] = status

        pd.DataFrame(df).to_csv("note.csv", index=None)
        print(pd.DataFrame(df))

    elif what == "3":
        break