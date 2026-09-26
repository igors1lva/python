def soma(a, b):
  return a + b

def mult(a, b):
  return a * b

def div(a, b):
  if b == 0:
   return "Não há divisão por 0"
  return a / b # Corrigido para garantir a execução correta após a verificação

def sub(a, b):
  if a < 0 or b < 0:
   return a + b
  else:
   return a - b

def calculadora():
  print("====> CALCULADORA PYTHON <====")
  print("====Digite 'Sair' para sair da calculadora")
  operacoes = {
      "+": soma,
      "-": sub,
      "/": div,
      "*": mult,
  }

  while True:
    operador = input("Escolha alguma operaçao: (+, -, *, /)").strip().lower()
    if operador == "sair": # Removido o 'break' incondicional
      print("Encerrando a calculadora")
      break
    if operador not in operacoes:
      print("Operação Inválida.")
      continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
      print("Por favor, digite números válidos.")
      continue

    resultado = operacoes[operador](num1, num2)
    print(f"O resultado é: {resultado}\n")

if __name__ == "__main__":
 calculadora()