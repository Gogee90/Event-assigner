# Event-assigner
http://event-assigner.francecentral.cloudapp.azure.com/api/events/ - посмотреть все ивенты, которые есть. <br>
http://event-assigner.francecentral.cloudapp.azure.com/api/events/1 - посмотреть конкретный ивент по первичному ключу. <br>
http://event-assigner.francecentral.cloudapp.azure.com/api/events/1/create-request/ - оставить заявку или отправить отклик, в зависимости от типа события. <br>
Там используется одна форма для двух видов событий, просто в одном случае произойдёт отправка письма с файлом, в другом без. <br>
http://event-assigner.francecentral.cloudapp.azure.com/api/events/requests/ - все заявки и отклики. <br>
http://event-assigner.francecentral.cloudapp.azure.com/api/events/requests/1 - одна конретная заявка, по первичному клюу. <br> <hr>
http://event-assigner.francecentral.cloudapp.azure.com/users/accounts/ - посмотреть всех созданных пользователей, тут же можно создать нового пользователя. В этом случае после создания юзера, юзер логинится сразу (сделано чисто в целях демонстрации. По хорошему надо было сделать отдельную форму). Создавайте юзера с реальными имейлами, чтобы проверить отправку писем. <br>
http://event-assigner.francecentral.cloudapp.azure.com/users/accounts/user-account/ - что-то типа личного кабинет, где можно посмотреть все события, для залогиненного пользователя, и все отклики и заявки к событиям. <br>
Стоит упомянуть группы пользователей: там создано две группы - assigners и participants. Assigners - могут создавать события, participants - могут оставлять заявки или отклики. В любом случае в админке можно группам права изменить. <br>
Задача по напоминанию запускается каждый день в 12:00. В events/tasks можно посмотреть как реализовано.<br>
Размещено на AZURE.
