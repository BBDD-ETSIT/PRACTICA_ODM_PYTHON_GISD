# encoding: utf-8

from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine
import json
import uuid
import os

from models import Hospital, Patient, Doctor, sparql

# Buscar todos los hospitales
def show_hospitals():
    #Complete aquí el contenido de la función
    return all_hospitals

# Filtra los hospitales por ciudad
def filterHospitalsByCity(city):
    #Complete aquí el contenido de la función
    return list_hospitals

# Buscar pacientes de un hospital ordenadors por el nombre (de la A a la Z)
def list_hospital_patients(hospital_id):
    #Complete aquí el contenido de la función
    return patients

# Muestra la informacion de un paciente
def read_patient(patient_id):
    #Complete aquí el contenido de la función
    return patient

# Crea un paciente en un hospital
def create_patient(hospital_id,body):
    #Complete aquí el contenido de la función


    
    return new_patient

# Obtiene el formulario para actualizar un paciente
def create_edited_patient(patient_id):
    #Complete aquí el contenido de la función
    return patient

# Actualiza un paciente
def update_patient(patient_id,body):
    #Complete aquí el contenido de la función
    return patient

# Borra un paciente
def delete_patient(patient_id):
    #Complete aquí el contenido de la función
    return patient
# Asigna un doctor y devuelve los datos del paciente
def assign_doctor(patient_id,doctor_id):
    #Complete aquí el contenido de la función
    return patient

# Muestras los medicos de un paciente
def show_patient_doctors(patient_id):
    #Complete aquí el contenido de la función
    return doctors

# Mostrar la información registrada para un hospital    
def show_hospital(hospital_id):
    #Complete aquí el contenido de la función
    hospital = Hospital.objects.get(id=hospital_id)
    query = f'''
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT DISTINCT ?nombre # ...
    # ¡ATENCIÓN!
    # Hay que utilizar doble corchete en estas consultas, porque es una f-string
            WHERE {{
                <{hospital.iri}> rdfs:label ?nombre .
            }}

    '''
    hospital_info = sparql(query, endpoint='https://es.dbpedia.org/sparql')
    return hospital_info, hospital.iri
