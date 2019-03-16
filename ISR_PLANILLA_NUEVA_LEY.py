
# coding: utf-8

# In[1]:


planilla = {"Alberto": 3000000, "Lucía": 1100000, "Felipe": 800000,"Erick":5000000}

def calcular_ISR(planilla):
 for item in planilla:
    salario = planilla[item]
      
    if (salario >= 0) and (salario <= 817000):ISR = (0*salario)

    elif (salario > 817000) and (salario <= 1199000):ISR = (0.1 * (salario-817000))
        
    elif (salario > 1199000) and (salario <= 2103000):ISR = (0.1 * (1199000-817000)) + (0.15 * (salario-1199000))
        
    elif (salario > 2103000) and (salario <= 4205000):ISR = (0.1 * (1199000-817000)) + (0.15 * (2103000-1199000))+(0.2 * (salario-2103000))

    elif (salario > 4205000):ISR = (0.1 * (1199000-817000)) + (0.15 * (2103000-1199000))+(0.2 * (4205000-2103000))+(0.25 * (salario-4205000))

    else:
            pass
    planilla [item] = int(ISR)
 return planilla


# In[2]:


print(calcular_ISR(planilla))

