import phone_book
#import view

pb = phone_book.PhoneBook("phone_db.txt")


while True:
    print(pb.main_menu())
    choice = int(input('Выберите пункт меню: '))
    match choice:
        case 1:
            phone_book.print_pb(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите телефон: ')
            comment = input('Введите коментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите поисковый запрос: ')
            phone_book.print_pb(pb.show_contacts(word))
        case 4:
            phone_book.print_pb(pb)
            index = int(input('Введите индекс контакта который будем изменять: '))
            name = input('Введите имя ( или Enter - оставить без изменений: ')
            phone = input('Введите номер телефона ( или Enter - оставить без изменений:')
            comment = input('Введите коментарий ( или Enter - оставить без изменений: ')
            pb.change(index-1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input('Введите индекс контакта который хотите удалить: '))
            pb.remove_contact(index-1)
        case 6:
            pb.save()
        case 7:
            break
