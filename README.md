# Cooling Tower Control System

Este projeto implementa um sistema de controle para torres de resfriamento, permitindo iniciar e parar motores e ventiladores em sequência.

## Descrição

A classe `CoolingTower` gerencia o estado de dois motores e dois ventiladores. O sistema permite iniciar e parar os motores e ventiladores em uma sequência específica, simulando o tempo de partida e parada.

## Funcionalidades

- Iniciar e parar motores individualmente.
- Iniciar e parar ventiladores individualmente.
- Executar uma sequência de partida para todos os motores e ventiladores.
- Executar uma sequência de parada para todos os motores e ventiladores.

## Uso

### Inicialização

Para usar o sistema de controle de torres de resfriamento, primeiro crie uma instância da classe `CoolingTower`:

```python
tower = CoolingTower()

Sequência de Partida
Para iniciar os motores e ventiladores em sequência:

