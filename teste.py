import openpyxl

wb = openpyxl.load_workbook('teste.xlsx')
ws = wb.active

print(f"Total de linhas: {str(ws.max_row)} e Colunas totais: {ws.max_column}")