from LINKfile import file_link


class mobile_phone:
    telephone_number = 112

    def new_number(self):
        number = int(input("Введите номер телефона  "))
        self.telephone_number = number
    #   устанавливает номер телефона

    def what_number(self):
        print(self.telephone_number)
    # показывает номер телефона

    def call_number(self):
        print("вы позвонили на nokia3310")


class smart_phone(mobile_phone):
    wifi = True

    def wifi_on(self):
        smart_phone.wifi = True

    def wifi_off(self):
        smart_phone.wifi = False

    def follow_the_link(file_link):
        if smart_phone.wifi == True:
            print("Перейти по ссылке получилось")
        else:
            print("Нет подключения к Интернету")


nokia3310 = mobile_phone()
iphone13 = mobile_phone()
samsung5S = mobile_phone()

huaweiNova8 = smart_phone()
xiaomi11T = smart_phone()
pocoX3 = smart_phone()

iphone13.call_number()

huaweiNova8.follow_the_link()
xiaomi11T.follow_the_link()
pocoX3.follow_the_link()

