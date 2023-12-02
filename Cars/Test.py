from Names import Name
import WindowCreate
import WindowChange
import WindowDelete
import WindowSearch
import WindowClear
import WindowMain

class UnitTest():


    def TestDoors(self):
        must = ['открыты','закрыты']
        with open('cars.txt','r',encoding='utf-8') as file:
            r = file.readlines()
        k=0
        for i in r:
            a= i.split(' ')
            for j in range(len(a)):
                a[j]=a[j].replace('\n','')
            for j in must:
                if a[7] == j:
                    k+=1
                    break
        if k == len(r):
            print(True)
        else: print(False)

    def TestLight(self):
        must = ['off','on']
        with open('cars.txt', 'r', encoding='utf-8') as file:
            r = file.readlines()
        k = 0
        for i in r:
            a = i.split(' ')
            for j in range(len(a)):
                a[j] = a[j].replace('\n', '')
            for j in must:
                if a[6] == j:
                    k += 1
                    break
        if k == len(r):
            print(True)
        else:
            print(False)


class IntegrationTest():
    def TestChange(self,car):
        # Проверка,что изменённый автомобиль соответствует изменению
        k=0
        with open('cars.txt','r',encoding='utf-8') as file:
            datacar = file.readlines()
        for i in datacar:
            data = i.split(' ')
            if car==data:
                k+=1

        if k==1:
            print('Change True')
            return True
        else:
            print('Change False',k)
            return False

    def TestCreate(self,ln):
        with open('cars.txt', 'r', encoding='utf-8') as file:
            datacar = file.readlines()
        if len(datacar)==len(ln)+1:
            print('Create True')
            return True
        else:
            print('Create False')
            return False


if __name__ == '__main__':
    UnitTest().TestDoors()
    UnitTest().TestLight()

