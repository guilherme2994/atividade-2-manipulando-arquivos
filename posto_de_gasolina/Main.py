from Veiculo import Veiculo
from Combustivel import Combustivel
from Abastecimento import Abastecimento

# ==========================================
# COMBUSTÍVEIS
# ==========================================
etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")

# ==========================================
# VEÍCULOS
# ==========================================
carro = Veiculo("Carro", "ABC-1234")
moto = Veiculo("Moto", "DEF-5678")
van = Veiculo("Van Escolar", "GHI-9012")

# ==========================================
# ABASTECIMENTOS
# ==========================================
abastecimento1 = Abastecimento(carro,etanol,50)
abastecimento2 = Abastecimento(moto,gasolina,25)
abastecimento3 = Abastecimento(van,diesel,200)

# ==========================================
# LISTA DE ABASTECIMENTOS
# ==========================================
abastecimentos = [abastecimento1, abastecimento2, abastecimento3]

# ==========================================
# MOSTRANDO OS ABASTECIMENTOS
# ==========================================
print("========== ABASTECIMENTOS DO DIA ==========")

for abastecimento in abastecimentos:
    abastecimento.mostrar_abastecimento()

# ==========================================
# TOTAL DE VENDAS POR COMBUSTÍVEL
# ==========================================
total_etanol = 0
total_gasolina = 0
total_diesel = 0

for abastecimento in abastecimentos:
    if abastecimento.combustivel.nome == "Etanol":
        total_etanol += abastecimento.valor
    elif abastecimento.combustivel.nome == "Gasolina":
        total_gasolina += abastecimento.valor
    elif abastecimento.combustivel.nome == "Diesel":
        total_diesel += abastecimento.valor

# ==========================================
# TOTAL DO DIA
# ==========================================
total_dia = (total_etanol + total_gasolina + total_diesel)

from Veiculo import Veiculo
from Combustivel import Combustivel
from Abastecimento import Abastecimento

# COMBUSTÍVEIS

etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")

# VEÍCULOS INICIAIS

carro = Veiculo("Carro", "ABC-1234")
moto = Veiculo("Moto", "DEF-5678")
van = Veiculo("Van Escolar", "GHI-9012")

# NOVOS VEÍCULOS

caminhao = Veiculo("Caminhão", "JKL-3456")
onibus = Veiculo("Ônibus", "MNO-7890")
pickup = Veiculo("Pickup", "PQR-1122")
suv = Veiculo("SUV", "STU-3344")
trator = Veiculo("Trator", "VWX-5566")

# ABASTECIMENTOS INICIAIS

abastecimento1 = Abastecimento(carro, etanol, 50)
abastecimento2 = Abastecimento(moto, gasolina, 25)
abastecimento3 = Abastecimento(van, diesel, 200)

# NOVOS ABASTECIMENTOS

abastecimento4 = Abastecimento(caminhao, diesel, 350)
abastecimento5 = Abastecimento(onibus, diesel, 300)
abastecimento6 = Abastecimento(pickup, gasolina, 100)
abastecimento7 = Abastecimento(suv, gasolina, 80)
abastecimento8 = Abastecimento(trator, etanol, 150)


# LISTA PRINCIPAL

abastecimentos = [
    abastecimento1,
    abastecimento2,
    abastecimento3,
    abastecimento4,
    abastecimento5,
    abastecimento6,
    abastecimento7,
    abastecimento8
]

# CALCULANDO TOTAIS

total_etanol = 0
total_gasolina = 0
total_diesel = 0

for abastecimento in abastecimentos:

    if abastecimento.combustivel.nome == "Etanol":
        total_etanol += abastecimento.valor

    elif abastecimento.combustivel.nome == "Gasolina":
        total_gasolina += abastecimento.valor

    elif abastecimento.combustivel.nome == "Diesel":
        total_diesel += abastecimento.valor


total_dia = total_etanol + total_gasolina + total_diesel

# ETAPA 1 E 2 - GERANDO/ATUALIZANDO TXT

with open("recibo_posto.txt", "w", encoding="utf-8") as arquivo:

    arquivo.write("========== POSTO DE GASOLINA ==========\n")

    for abastecimento in abastecimentos:

        arquivo.write(
            f"{abastecimento.veiculo}\n"
        )

        arquivo.write(
            f"Combustível: {abastecimento.combustivel}\n"
        )

        arquivo.write(
            f"Valor: R$ {abastecimento.valor:.2f}\n\n"
        )

    arquivo.write("========================================\n")
    arquivo.write(f"Etanol: R$ {total_etanol:.2f}\n")
    arquivo.write(f"Gasolina: R$ {total_gasolina:.2f}\n")
    arquivo.write(f"Diesel: R$ {total_diesel:.2f}\n")
    arquivo.write(f"TOTAL DO DIA: R$ {total_dia:.2f}\n")

# ETAPA 3 - LENDO O ARQUIVO

with open("recibo_posto.txt", "r", encoding="utf-8") as arquivo:

    conteudo = arquivo.read()

    print("\n========== RECIBO LIDO DO ARQUIVO ==========")
    print(conteudo)

# ENCONTRANDO OS TOTAIS DENTRO DO TEXTO

for linha in conteudo.splitlines():

    if linha.startswith("Etanol:"):
        print("Total gasto com Etanol:", linha)

    elif linha.startswith("Gasolina:"):
        print("Total gasto com Gasolina:", linha)

    elif linha.startswith("Diesel:"):
        print("Total gasto com Diesel:", linha)

    elif linha.startswith("TOTAL DO DIA:"):
        print("Valor total gasto no dia:", linha)
