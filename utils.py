"""Question 1 - Python Graded Assignment"""
import logging,re
from datetime import datetime
from logging.handlers import (RotatingFileHandler)

formatter = logging.Formatter('%(asctime)s %(name)-8s %(module)s %(lineno)d %(levelname)-8s %(message)s')
def setup_logger(name, log_file, level="DEBUG"):
    handler = RotatingFileHandler(log_file, maxBytes=120000, backupCount=1, delay=False)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

# first file logger
log = setup_logger('LOG', 'utils.log')


class checkPasswordUtility:
    def __init__(self) -> bool:
        log.warning(f"============== INIT START {datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S')} ==============")
        print("Processing Data .............")
        
    def checkPasswordStrength(self,password):
        result,stringVal = None,None
        self.password = password
        log.info(f'Password provided :-> {self.password}')
        try:
            step1 = self.checkLength()
            #! Checking Password Minimum Length
            if not step1:
                stringVal = "be at least 8 characters long"
                raise Exception('Step 1')
            
            step2 = self.checkCase()
            if not step2:
                stringVal = "contains both uppercase(A-Z) and lowercase letters(a-z)"
                raise Exception('Step 2')

            step3 = self.checkDigit()
            if not step3:
                stringVal = "contains at least one digit (0-9)"
                raise Exception('Step 3')
            
            step4 = self.checkSpecialCharacter()
            if not step4:
                stringVal = "contains at least one special character (e.g., !, @, #, $, %)"
                raise Exception('Step 4')
            
            if step4:
                result = True
                if len(self.password) >= 8:
                    stringVal = "Weak"
                if len(self.password) >= 11:
                    stringVal = "Strong"
                if len(self.password) >= 15:
                    stringVal = "Difficult"
            
        except Exception as e:
            log.exception(e)
            if stringVal is None:
                stringVal = "Oops!! Some Error Has been Occured"
            result,stringVal = False,stringVal
        finally:
            log.info(f"=============== INIT END {datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S')} ===============")
            return result,stringVal
    
    #! Checking 8  Character Length    
    def checkLength(self):
        if len(self.password) < 8:
            log.error(f'Below 8 | Length is {len(self.password)}')
            return False
        else:
            log.warn(f'Above 8 | Length is {len(self.password)}')
            return True
    #! Checking Both Uppercase(A-Z) & Lowercase(a-z)
    def checkCase(self):
        pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z]).+$')
        result = pattern.match(self.password)
        log.warning(f"{bool(result)} | CheckCase Result :-> {result}")
        return bool(result)
    # Checking Digit  (0-9)
    def checkDigit(self):
        pattern = re.compile(r'^(?=.*[0-9]).+$')
        result = pattern.match(self.password)
        log.warning(f"{bool(result)} | CheckDigit Result :-> {result}")
        return bool(result)
    # Checking Special Characters  (, !, @, #, $, %)
    def checkSpecialCharacter(self):
        pattern = re.compile(r'^(?=.*[!@#$%]).+$')
        result = pattern.match(self.password)
        log.warning(f"{bool(result)} | CheckSpecialCharacter Result :-> {result}")
        return bool(result)