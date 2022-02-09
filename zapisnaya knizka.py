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

