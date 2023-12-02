class Name():

    def reading():
        f=[]
        for i in range(0,178):
            try:
                with open(f'data/allCars/{i}.txt','r',encoding='utf-8') as file:
                    f.append(file.readlines()[0].replace('\n',''))
            except(FileNotFoundError):
                continue
        return f


    headers = ['Гос. номер автомобиля','Цвет','Марка','Модель','Год выпуска','Мощность двигателя\n(л.с.)','Фары(on/off)','Двери\n(открыты/закрыты)']
    Comand = ['Создать новый профиль(1)\n','Изменить профиль(2)\n','Удалить профиль(3)\n','Очистить базу данных(4)\n','Закрыть программу(5)']
    nomer_simv='ABEKMHOPCTYX'+'АВЕКМНОРСТУХ'
    nomer_nums='0123456789'
    status1 = ['off','on']
    status2=['открыты','закрыты']
    models_car = ['Nissan', 'Toyota', 'BMW', 'Mersedec']
    color = ['Бежевый', 'Белый','Жёлтый','Зелёный',
             'Коричневый','Красный','Оранжевый','Розовый'
              ,'Серебристый','Серый','Синий','Чёрный','Фиолетовый']
    marks = reading()
    years = [i for i in range(1970,2023)]
    on_off=['on','off']

    with open('cars.txt', 'r', encoding='utf-8') as file:
        allTable = file.readlines()
    file.close()

    # def updateAvtoNomer(self):
    avtoNomers =[]
    for i in range(len(allTable)):
        with open('cars.txt', 'r', encoding='utf-8') as file:
            str = file.readlines()
        file.close()
        a=str[i].split(' ')
        avtoNomers.append(a[0])




