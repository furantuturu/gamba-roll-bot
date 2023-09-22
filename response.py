import random

def get_roll_response(message) -> str:
    rollnum = []
    
    if message == "!roll":
        rollnum.append(random.randint(0, 9))
        rollnum.append(random.randint(0, 9))
        rollnum.append(random.randint(0, 9))
        
        return f"({rollnum[0]}) ({rollnum[1]}) ({rollnum[2]})"