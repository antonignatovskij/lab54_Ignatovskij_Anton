class PrdVld:
    @staticmethod
    def validate(product):
        flag = []
        print(product['image'])
        if product['title'] == '':
            flag.append('Поле для названия обязательно к заполнению')

        if product['price'] != '':
            dot_counter = 0
            for digit in product['price']:
                try:
                    int(digit)
                except ValueError:
                    if digit == '.':
                        dot_counter += 1
                    else:
                        flag.append('В поле для цены присутствуют не цифровые значения')
                        break
            if dot_counter > 1:
                flag.append('Больше двух точек в вашей цене')
        else:
            flag.append('Поле для цены обязательно к заполнению')

        if product['image'] == '':
            flag.append('Поле для юрл картинки обязательно к заполнению!')
        print(flag)
        print(131231321232312312332)
        if len(flag) == 0:
            return True
        return flag