import re  
import tkinter
 

def removerCeros(stock): 
    new_stock = re.sub(r'\b0+(\d)', r'\1', stock) 
    
    
    
      
    return new_stock  
      
      

  
  
stock ="001.200.001.004"
print(removerCeros(stock))


boton_leeme = Button(ventana, text="Léeme", command=leeme)
boton_leeme.grid(row=7, columnspan= 5, pady=10, padx=10, sticky=E)