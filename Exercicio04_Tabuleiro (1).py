#!/usr/bin/env python
# coding: utf-8

# In[1]:


from openpyxl import Workbook

def preencherTabuleiro(planilha1):
    graos = 1
    qtd_linhas = 8
    qtd_colunas = 8
    for lin in range(1, qtd_linhas+1):
        for col in range(1, qtd_colunas+1):
            planilha1.cell(row=lin, column=col, value=graos)
            graos *=2
    print("\nTabueiro preenchido com sucesso!")
    return planilha1
    
#ABRIR ARQUIVO   
arquivo_excel = Workbook()
planilha1 = arquivo_excel.active
planilha1.title = "Tabuleiro"

#PREENCHER O TABULEIRO
planilha1 = preencherTabuleiro(planilha1)

#SALVAR ARQUIVO
arquivo_excel.save("Tabuleiro.xlsx")


# In[ ]:





# In[ ]:




