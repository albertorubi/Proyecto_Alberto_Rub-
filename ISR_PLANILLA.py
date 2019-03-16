
# coding: utf-8

# In[26]:


planilla = {"Alberto": 3000000, "Lucía": 1100000, "Felipe": 800000}

def calcular_ISR(planilla):
 for item in planilla:
    salario = planilla[item]
      
    if (salario >= 0) and (salario <= 817000):ISR = (0*salario)

    elif (salario > 817000) and (salario <= 1226000):ISR = (0.1 * (salario-817000))

    elif (salario > 1226000):ISR = (0.1 * (1226000-817000)) + (0.15*(salario-1226000))  
    else:
            pass
    planilla [item] = int(ISR)
 return planilla


# In[27]:


print(calcular_ISR(planilla))

