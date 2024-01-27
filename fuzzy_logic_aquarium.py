from matplotlib import pyplot as plt
import numpy as np
import skfuzzy  as fuzz
from skfuzzy import control as ctrl

class FuzzyLogicAquarium:
    def __init__(self) :
        self.create_fuzzy_logic()
        

    def create_fuzzy_logic(self):
        # Crear las variables de entrada difusas
        self.temperatura = ctrl.Antecedent(np.arange(0, 40, 1), 'temperatura')

        # Crear las variables de salida difusas
        self.potencia_ventilador = ctrl.Consequent(np.arange(0, 100, 1), 'potencia_ventilador')
        self.potencia_calentador = ctrl.Consequent(np.arange(0, 100, 1), 'potencia_calentador')

        # Definir las funciones de membresía difusa para la self.temperatura
        self.temperatura['muy fria'] = fuzz.trimf(self.temperatura.universe, [0, 0, 10])
        self.temperatura['fria'] = fuzz.trimf(self.temperatura.universe, [5, 15, 23])
        self.temperatura['optima'] = fuzz.trimf(self.temperatura.universe, [22, 24, 26])
        self.temperatura['caliente'] = fuzz.trimf(self.temperatura.universe, [24, 30, 35])
        self.temperatura['muy caliente'] = fuzz.trimf(self.temperatura.universe, [30, 40, 40])

        #self.temperatura['muy fria'].view()


        # Definir las funciones de membresía difusa para el potencia del ventilador
        self.potencia_ventilador['nula'] = fuzz.trimf(self.potencia_ventilador.universe, [0, 0, 15])
        self.potencia_ventilador['media alta'] = fuzz.trimf(self.potencia_ventilador.universe, [13, 37, 50])
        self.potencia_ventilador['alta'] = fuzz.trimf(self.potencia_ventilador.universe, [45, 60, 85])
        self.potencia_ventilador['muy alta'] = fuzz.trimf(self.potencia_ventilador.universe, [75, 100, 100])


        # Definir las funciones de membresía difusa para la potencia del calentador
        self.potencia_calentador['nula'] = fuzz.trimf(self.potencia_calentador.universe, [0, 0, 15])
        self.potencia_calentador['media alta'] = fuzz.trimf(self.potencia_calentador.universe, [13, 37, 50])
        self.potencia_calentador['alta'] = fuzz.trimf(self.potencia_calentador.universe,  [45, 60, 85])
        self.potencia_calentador['muy alta'] = fuzz.trimf(self.potencia_calentador.universe,[75, 100, 100])

        #self.potencia_calentador.view();
        plt.show(block=True)

        # Definir las reglas difusas
        regla1 = ctrl.Rule(self.temperatura['muy fria'] | self.temperatura['fria'] | self.temperatura['optima'], self.potencia_ventilador['nula'])
        regla2 = ctrl.Rule(self.temperatura['caliente'], self.potencia_ventilador['media alta'] )
        regla3 = ctrl.Rule(self.temperatura['muy caliente'], self.potencia_ventilador['muy alta'])

        #regla1.view()

        regla4 = ctrl.Rule(self.temperatura['muy caliente'] | self.temperatura['caliente'] | self.temperatura['optima'], self.potencia_calentador['nula'])
        regla5 = ctrl.Rule(self.temperatura['fria'] , self.potencia_calentador['media alta'])
        regla6 = ctrl.Rule(self.temperatura['muy fria'] , self.potencia_calentador['muy alta'])

        # Crear el sistema de control difuso
        aquarium_ctrl = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6])
        self.aquarium = ctrl.ControlSystemSimulation(aquarium_ctrl)
       
        
    def new_temperature(self, temperature:int):
        self.aquarium.input['temperatura'] = temperature
        self.aquarium.compute()
        self.potencia_ventilador = self.aquarium.output['potencia_ventilador']
        self.potencia_calentador = self.aquarium.output['potencia_calentador']



