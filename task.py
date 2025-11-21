import rich

film = input("Hochesh snytisy v filme? [Da/Net]:")

if (film.lower() == "da") or (film.lower() == "да") or (film.lower() == "вф"):
    rich.print("У нас есть две свободные роли. [bold green] Hulk[/bold green]/[bold green]Loki[/bold green]")
    roly = input("Какая тебе интересна? ")
    
    if roly.lower() == "hulk":
        volume = float(input('Какой у тебя объем бицепса? '))
        
        if volume >= 60:
            rich.print('[bold green]Ты принят!!![/bold green]')
        elif 1 <= volume < 60:
            rich.print('[bold red]Тебе надо ещё поднабрать для этой роли[/bold red]')
        else:
            rich.print('Объем бицепса измеряется по-другому')
    
    elif roly.lower() == "loki":
        mofather = input("Кого ты любишь больше [маму] или [папу]? ")
        
        if mofather == "маму":
            print('Предлагаю сходить к папе и ответить ему на этот вопрос')
        elif mofather == "папу":
            rich.print('[bold blue]Можешь тогда идти домой')
        else:
            rich.print('[bold red]Кажется, ты написал что-то не то')
    
    else:
        rich.print('[bold red]Я не предлагал такую роль. Ты уверен, что всё правильно написал?')        
    
    
elif film.lower() == "net":
    print("Мне кажется, что тебе бы точно подошла одна из наших ролей")
    
else:
    print("bro, a chto s umeniem vvodit text s pomoshiy klaviaturi")
    