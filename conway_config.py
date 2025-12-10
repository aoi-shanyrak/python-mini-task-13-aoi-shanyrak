
DENSITY_MODES = {
    "very_sparse": 0.02,    # 2% - почти пустое поле
    "sparse": 0.05,         # 5% - для стабильных конфигураций
    "optimal": 0.1,         # 10% - оптимально для игры Жизнь
    "dense": 0.15,          # 15% - более активная игра
    "chaos": 0.25,          # 25% - хаотичное поведение
    "random": None,         # Случайная плотность от 2% до 25%
}

USE_NUMPY = False

DENSITY_MODE = "optimal"
DENSITY_VALUE = None
TEST_DIR = "fields"
FIELD_SIZE = 256
STEPS = 128

FIELD_NUMBER = None

VERBOSE = True
