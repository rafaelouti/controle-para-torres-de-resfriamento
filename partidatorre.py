import time

class CoolingTower:
    def __init__(self):
        self.motor1 = False
        self.motor2 = False
        self.fan1 = False
        self.fan2 = False
    
    def start_motor(self, motor):
        if motor == 1:
            self.motor1 = True
            print("Motor 1 iniciado.")
        elif motor == 2:
            self.motor2 = True
            print("Motor 2 iniciado.")
        else:
            print("Motor inválido.")
    
    def stop_motor(self, motor):
        if motor == 1:
            self.motor1 = False
            print("Motor 1 desligado.")
        elif motor == 2:
            self.motor2 = False
            print("Motor 2 desligado.")
        else:
            print("Motor inválido.")
    
    def start_fan(self, fan):
        if fan == 1:
            self.fan1 = True
            print("Ventilador 1 iniciado.")
        elif fan == 2:
            self.fan2 = True
            print("Ventilador 2 iniciado.")
        else:
            print("Ventilador inválido.")
    
    def stop_fan(self, fan):
        if fan == 1:
            self.fan1 = False
            print("Ventilador 1 desligado.")
        elif fan == 2:
            self.fan2 = False
            print("Ventilador 2 desligado.")
        else:
            print("Ventilador inválido.")
    
    def start_sequence(self):
        print("Iniciando sequência de partida das torres de resfriamento...")
        
        # Iniciar o Motor 1 e Ventilador 1
        self.start_motor(1)
        time.sleep(2)  # Simulando tempo de partida
        self.start_fan(1)
        time.sleep(1)
        
        # Iniciar o Motor 2 e Ventilador 2
        self.start_motor(2)
        time.sleep(2)
        self.start_fan(2)
        time.sleep(1)
        
        print("Todos os motores e ventiladores estão em operação.")
    
    def stop_sequence(self):
        print("Iniciando sequência de parada das torres de resfriamento...")
        
        # Desligar o Motor 1 e Ventilador 1
        self.stop_fan(1)
        time.sleep(1)
        self.stop_motor(1)
        time.sleep(1)
        
        # Desligar o Motor 2 e Ventilador 2
        self.stop_fan(2)
        time.sleep(1)
        self.stop_motor(2)
        time.sleep(1)
        
        print("Todos os motores e ventiladores foram desligados.")

# Exemplo de uso:
tower = CoolingTower()

# Iniciar os motores e ventiladores em sequência
tower.start_sequence()

# Simular a operação por algum tempo
time.sleep(5)

# Parar os motores e ventiladores em sequência
tower.stop_sequence()
