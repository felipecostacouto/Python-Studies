import re

def cpf_generator():
    print("##### Gerador de CPF #####")
    cpf = input("Digite os nove primeiros digitos do CPF com o .: \n")

    cpf_formated = re.sub(r"[^0-9]", "",cpf)
    cpf_int = int(cpf_formated)
    print(cpf_formated)

cpf_generator()
