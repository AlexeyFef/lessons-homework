# импортируем класс User, создаем новый экземпляр my_user, вызываем все три метода

from user import User

my_user = User('Alex', 'Fef')
my_user.sayFirstName()
my_user.sayLastName()
my_user.sayFirstNameLastName()