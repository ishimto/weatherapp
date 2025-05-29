#import logging
#from datetime import datetime

#current_time = datetime.now()

#logging.basicConfig(filename=f'server_logs/record-{current_time.strftime("%d-%m-%Y__%H_%M_%S")}.log',
#					level=logging.DEBUG,
#					format="%(asctime)s %(levelname)s %(message)s")


#contact_logger = logging.getLogger("ContactLogger")
#contact_logger.setLevel(logging.INFO)

#contact_handler = logging.FileHandler(f'server_logs/contact-{current_time.strftime("%d-%m-%Y__%H_%M_%S")}.log')
#contact_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

#contact_handler.setFormatter(contact_formatter)
#contact_logger.addHandler(contact_handler)
