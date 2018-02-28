import logging
logger = logging.getLogger("ModImp")
logger.setLevel(logging.INFO)

fh = logging.FileHandler("new_snake.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - '
                              '%(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

def greet(name):
	logger.info("Hello, " + name + ". Good morning!")

def abc(a,b):
    logger.info("Logger in Action")
    greet("Srini")

abc(11,22)