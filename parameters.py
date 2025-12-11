import numpy as np

presets = {
    "Tc99m": {
        "tau": 6.0,              # h
        "gamma": 0.0075,         # µSv·m²/(MBq·h)  
        "A0": 740.0,             # MBq  (ejemplo típico)
        "N": 40,                 # pacientes/semana
        "d": 2.0                 # m
    },
    "F18": {
        "tau": 1.83,             # h
        "gamma": 0.16,           # µSv·m²/(MBq·h) 
        "A0": 370.0,             # MBq
        "N": 20,
        "d": 1.5
    },
    "I131": {
        "tau": 192.5,            # h (8.02 días)
        "gamma": 0.5,            # µSv·m²/(MBq·h)
        "A0": 3700.0,            # MBq 
        "N": 2,
        "d": 2.0
    },
    "Co60": {
        "tau": 4.62e4,           # h (≈5.27 años)
        "gamma": 0.38,           # µSv·m²/(MBq·h)
        "A0": 1e6,               # MBq
        "N": 0,
        "d": 5.0
    }
}


presets2 = {
    "Plomo": {
        "alpha": 1.543,           
        "beta": -0.4408,    
        "gamma": 2.136             
    },
    
    "Concreto": {
        "alpha": 0.1539,           
        "beta": -0.1161,    
        "gamma": 2.0752             
    },
    
    "Hierro": {
        "alpha": 0.5704,           
        "beta": -0.3063,    
        "gamma": 0.6326             
    },
}