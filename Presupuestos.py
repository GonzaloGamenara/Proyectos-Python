class Category:

    #Metodo de Inicializacion
    def __init__(self,name):

        self.ledger=[]
        self.name=name

    #Metodo para depositar un amount(cantidad) de dinero en una categoria(name)
    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount, 'description': description})

    #Metodo para extraer un amount(cantidad) de dinero de una categoria(name)
    def withdraw(self,amount,description=""):


        #Comprobar con el metodo check_funds() si el amount(cantidad) de dinero a extraer es menor a la cantidad de dinero que dispone la categoria
        if self.check_funds(amount):
            
            #agregar el diccionario con la cantidad (negativa) y la descripcion a la lista[ledger]
            self.ledger.append(

                {'amount': -amount, 'description': description}
                
                ) 
            return True
        else: return False

    #Metodo para obtener el balance de la categoria
    def get_balance(self):
        balance=0

        #recorrer la categoria sumando los movimientos de dinero
        for bal in self.ledger:
            balance += bal['amount']
        return balance

    #Metodo para transferir de una categoria a otra dinero
    def transfer(self,amount,category):

        #chequear fondos nuevamente para no transferir fondos inexistentes
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    #Metodo para chequear fondos en la categoria utilizando get_balance()
    def check_funds(self,amount):
        return self.get_balance() >= amount

    #Metodo para imprimir por pantalla el ticket final
    def __str__(self):
        # Título centrado
        title = f"{self.name:*^30}\n"
        
        # Detalle de transacciones
        items = ""
        for entry in self.ledger:
            description = entry['description'][:23].ljust(23)  # Alinear a la izquierda
            amount = f"{entry['amount']:.2f}"[:7].rjust(7)     # Alinear a la derecha
            items += f"{description}{amount}\n"

        # Total
        total = f"Total: {self.get_balance():.2f}"
        
        # Resultado completo
        return title + items + total


def create_spend_chart(categories):
    # Título
    title = "Percentage spent by category\n"
    
    # Calcular el total de gastos y porcentajes por categoría
    total_spent = 0
    spent_by_category = []
    
    for category in categories:
        spent = sum(-entry['amount'] for entry in category.ledger if entry['amount'] < 0)
        spent_by_category.append(spent)
        total_spent += spent
    
    percentages = [int((spent / total_spent) * 100 // 10) * 10 for spent in spent_by_category]
    
    # Crear el gráfico
    chart = ""
    for i in range(100, -1, -10):  # De 100 a 0, decreciendo de a 10
        chart += f"{i:>3}| "  # Alinear los números a la derecha y agregar la barra vertical
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"
    
    # Línea horizontal
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Nombres de las categorías, verticalmente
    max_name_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_name_length) for category in categories]
    
    for i in range(max_name_length):
        chart += "     "  #agregamos un espacio inicial
        for name in names:
            chart += name[i] + "  "
        chart += "\n"
    
    return title + chart.rstrip("\n")