from pywebio.input import input as pw_input
from pywebio.output import put_code

food = pw_input('Яка твоя улюбленна страва?').lower()
put_code(f'О, я теж люблю {food}!\U0001F60E')
