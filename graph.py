graph = {
    "A": {
        "B": {"distance": 5, "time": 7, "traffic": 2, "difficulty": 1},
        "D": {"distance": 6, "time": 8, "traffic": 1, "difficulty": 1},
    },

    "B": {
        "A": {"distance": 5, "time": 7, "traffic": 2, "difficulty": 1},
        "C": {"distance": 4, "time": 6, "traffic": 2, "difficulty": 2},
        "E": {"distance": 5, "time": 7, "traffic": 1, "difficulty": 1},
    },

    "C": {
        "B": {"distance": 4, "time": 6, "traffic": 2, "difficulty": 2},
        "G": {"distance": 10, "time": 15, "traffic": 3, "difficulty": 2},
    },

    "D": {
        "A": {"distance": 6, "time": 8, "traffic": 1, "difficulty": 1},
        "F": {"distance": 7, "time": 9, "traffic": 1, "difficulty": 1},
    },

    "E": {
        "B": {"distance": 5, "time": 7, "traffic": 1, "difficulty": 1},
        "G": {"distance": 8, "time": 11, "traffic": 2, "difficulty": 1},
    },

    "F": {
        "D": {"distance": 7, "time": 9, "traffic": 1, "difficulty": 1},
        "G": {"distance": 7, "time": 10, "traffic": 1, "difficulty": 1},
    },

    "G": {
        "C": {"distance": 10, "time": 15, "traffic": 3, "difficulty": 2},
        "E": {"distance": 8, "time": 11, "traffic": 2, "difficulty": 1},
        "F": {"distance": 7, "time": 10, "traffic": 1, "difficulty": 1},
    }
}


locations = {
    "A": "Центр",
    "B": "Університет",
    "C": "Лікарня",
    "D": "Парк",
    "E": "Вокзал",
    "F": "Торговий центр",
    "G": "Аеропорт",
}