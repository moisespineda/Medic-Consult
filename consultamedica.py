# Programa en donde se pregunta al usuario por el motivo de la consulta entre ah1n1, covid, 
# gripe comun, sarampion o dengue. Tambien se pregunta por la edad y el sexo del paciente.
# Al final, se muestra la cantidad de pacientes que consulta paracada enfermedad, la cantidad
# total de pacientes, el promedio de edad de los pacientes y el porcentaje de pacientes hombres
# y pacientes mujeres.

# Program where the user is asked about the reason for the consultation between ah1n1, covid, 
# common flu, measles or dengue. It also asks about the age and sex of the patient. At the end,
# the number of patients consulting for each disease, the total number of patients, the average age 
# of the patients and the percentage of male and female patients are displayed.

covid=0
ah1n1=0
common=0
measles=0
dengue=0
persons=0
ages=0
men=0
women=0
option=(input("Ingrese la razon por cual consulta: \n \n1. Covid-19 \n2. AH1N1 \n3. Gripe Común \n4. Sarampion \n5. Dengue \n \nOpcion: "))

while option=="1" or option=="2" or option=="3" or option=="4" or option=="5":
    
    if option=="1":
        covid=covid+1
    if option=="2":
        ah1n1=ah1n1+1
    if option=="3":
        common=common+1
    if option=="4":
        measles=measles+1
    if option=="5":
        dengue=dengue+1
    sex=input("Ingrese si el paciente es hombre(H) o mujer(M): ").title()
    if sex=="H":
        men+=1
    else:
        women+=1
    age=int(input("Ingrese su edad: "))
    ages+=age
    persons=persons+1
    option=(input("Ingrese la razon por cual consulta: \n \n1. Covid-19 \n2. AH1N1 \n3. Gripe Común \n4. Sarampion \n5. Dengue \n \nOpcion: "))

meanage=ages/persons
percm=(men*100)/persons
percw=(women*100)/persons

print("RESUMEN \n \n")

print("Cantidad de pacientes con COVID-19: ", covid)
print("Cantidad de pacientes con AH1N1:", ah1n1)
print("Cantidad de pacientes con Gripe Común:", common)
print("Cantidad de pacientes con Sarampion:", measles)
print("Cantidad de pacientes con Dengue:", dengue)
print("Cantidad de pacientes: ", persons)
print("Promedio de edades: ", meanage)
print("Porcentaje de hombres: ", percm, "%")
print("Porcentaje de mujeres: ", percw, "%")