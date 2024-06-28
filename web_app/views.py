import pandas as pd
from django.shortcuts import render
from .models import *
from web_app import graphics_function as gf
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os

def home(request):
    return render(request, "home.html")

def macro(request):
    x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
           2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    y =[14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13,
           11, 4, 2, 1]
    
    x_title = ''
    
    y_title = ''
    
    fig = gf.graph(x, y, x_title, y_title)
    
    macro_html_1 = fig.to_html()
    macro_html_2 = fig.to_html()

    context = {'macro1': macro_html_1, 
               'macro2': macro_html_2
              }
    
    return render(request, "macro.html", context)

def datos_demograficos(request):
    return render(request, "demograficos.html")

def ciclos_economicos(request):
    x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
           2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    y =[14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13,
           11, 4, 2, 1]
    
    x_title = ''
    y_title = ''
    
    fig = gf.graph(x, y, x_title, y_title)
    
    ciclos_economicos = fig.to_html()
    
    context = {'ciclos_economicos': ciclos_economicos}
    return render(request, "ciclos_economicos.html", context)
    
def indicadores(request):
    df = pd.read_csv('src/data/indicadores.csv')
    df_x = df.melt(var_name='Year')
    df_y = df.melt(value_name='Value')
    
    x = df_x['Year']
    y = df_y['Value']
    
    x_1 = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]
    y_1 = [14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 12]
    
    x_title = 'Años'
    y_title = 'Indices'
    
    fig = gf.graph(x, y, x_title, y_title)
    fig_1 = gf.graph(x_1, y_1, x_title, y_title)
    
    indicadores_html = fig.to_html()
    indicadores_html2 = fig_1.to_html()
    indicadores_html3 = fig.to_html()
    indicadores_html4 = fig.to_html()
    indicadores_html5 = fig.to_html()
    indicadores_html6 = fig.to_html()
    indicadores_html7 = fig.to_html()
    indicadores_html8 = fig.to_html()
    indicadores_html9 = fig.to_html()
    indicadores_html10 = fig.to_html()
    indicadores_html11 = fig.to_html()
    indicadores_html12 = fig.to_html()
    indicadores_html13 = fig.to_html()
    indicadores_html14 = fig.to_html()
    indicadores_html15 = fig.to_html()
    indicadores_html16 = fig.to_html()
    indicadores_html17 = fig.to_html()
    indicadores_html18 = fig.to_html()

    context = {'indicadores': indicadores_html, 
               'indicadores2': indicadores_html2, 
               'indicadores3': indicadores_html3, 
               'indicadores4': indicadores_html4, 
               'indicadores5': indicadores_html5, 
               'indicadores6': indicadores_html6,
               'indicadores7': indicadores_html7,
               'indicadores8': indicadores_html8,
               'indicadores9': indicadores_html9,
               'indicadores10': indicadores_html10,
               'indicadores11': indicadores_html11,
               'indicadores12': indicadores_html12,
               'indicadores13': indicadores_html13,
               'indicadores14': indicadores_html14,
               'indicadores15': indicadores_html15,
               'indicadores16': indicadores_html16,
               'indicadores17': indicadores_html17,
               'indicadores18': indicadores_html18,
               }
    return render(request, "indicadores.html", context)

def JP_304(request):
    if request.method == "POST":
        # Retrieve form data
        start_month = request.POST.get('start_month')
        end_month = request.POST.get('end_month')
        year = request.POST.get('year')
        name = request.POST.get('name')
        direction = request.POST.get('direction')
        liaison_officer = request.POST.get('liaison_officer')
        title = request.POST.get('title')
        tel = request.POST.get('tel')
        nombre_agencia_federal = request.POST.get('nombre_agencia_federal')
        catalogo_federal = request.POST.get('catalogo_federal')
        sai_federal = request.POST.get('sai_federal')
        titulo_federal = request.POST.get('titulo_federal')
        aportacion_aprobada_federal = request.POST.get('aportacion_aprobada_federal')
        fecha_aprobacion_federal = request.POST.get('fecha_aprobacion_federal')
        aportacion_recibida_federal = request.POST.get('aportacion_recibida_federal')
        fecha_recibo_federal = request.POST.get('fecha_recibo_federal')
        aportacion_gastada_federal = request.POST.get('aportacion_gastada_federal')
        fecha_gasto_federal = request.POST.get('fecha_gasto_federal')
        agencia_local_table_box = request.POST.get('agencia_local_table_box')
        catalogo_local = request.POST.get('catalogo_local')
        programa_local = request.POST.get('programa_local')
        aportacion_federal_aprobada_local = request.POST.get('aportacion_federal_aprobada_local')
        fecha_aprobacion_local = request.POST.get('fecha_aprobacion_local')
        aportacion_federal_recibida_local = request.POST.get('aportacion_federal_recibida_local')
        fecha_recibo_local = request.POST.get('fecha_recibo_local')
        aportacion_federal_gastada_local = request.POST.get('aportacion_federal_gastada_local')
        fecha_gasto_local = request.POST.get('fecha_gasto_local')
        numero_cuenta_local = request.POST.get('numero_cuenta_local')
        
        csv_file_path = 'data/cuestionarios/balanza_de_pago/JP-304.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['start_month', 'end_month', 'year', 'name',
                                'direction', 'liaison_officer', 'title', 'tel',
                                'nombre_agencia_federal', 'catalogo_federal', 'sai_federal',
                                'titulo_federal', 'aportacion_aprobada_federal', 'fecha_aprobacion_federal',
                                'aportacion_recibida_federal', 'fecha_recibo_federal', 'aportacion_gastada_federal',
                                'fecha_gasto_federal', 'agencia_local_table_box', 'catalogo_local', 'programa_local',
                                'aportacion_federal_aprobada_local', 'fecha_aprobacion_local', 'aportacion_federal_recibida_local',
                                'fecha_recibo_local', 'aportacion_federal_gastada_local', 'fecha_gasto_local', 'numero_cuenta_local'
                                ])
            
            writer.writerow([start_month, end_month, year, name,
                             direction, liaison_officer, title, tel,
                             nombre_agencia_federal, catalogo_federal, sai_federal,
                             titulo_federal, aportacion_aprobada_federal, fecha_aprobacion_federal,
                             aportacion_recibida_federal, fecha_recibo_federal, aportacion_gastada_federal,
                             fecha_gasto_federal, agencia_local_table_box, catalogo_local, programa_local,
                             aportacion_federal_aprobada_local, fecha_aprobacion_local, aportacion_federal_recibida_local,
                             fecha_recibo_local, aportacion_federal_gastada_local, fecha_gasto_local, numero_cuenta_local
                             ])  

        return render(request, "cuestionarios/succesfull.html")
    
    return render(request, "cuestionarios/balanza_de_pagos/JP-304.html")

def JP_361(request):
    if request.method == "POST":
        # Retrieve form data
        income_expenses_year_1 = request.POST.get('income_expenses_year_1')
        income_expenses_year_2 = request.POST.get('income_expenses_year_2')
        income_life_1 = request.POST.get('income_life_1')
        income_life_2 = request.POST.get('income_life_2')
        income_disability_1 = request.POST.get('income_disability_1')
        income_disability_2 = request.POST.get('income_disability_2')
        income_auto_1 = request.POST.get('income_auto_1')
        income_auto_2 = request.POST.get('income_auto_2')
        income_other_1 = request.POST.get('income_other_1')
        income_other_2 = request.POST.get('income_other_2')
        income_interest_1 = request.POST.get('income_interest_1')
        income_interest_2 = request.POST.get('income_interest_2')
        income_rent_1 = request.POST.get('income_rent_1')
        income_rent_2 = request.POST.get('income_rent_2')
        income_other_2_1 = request.POST.get('income_other_2_1')
        income_other_2_2 = request.POST.get('income_other_2_2')
        total_income_1 = request.POST.get('total_income_1')
        total_income_2 = request.POST.get('total_income_2')
        expenses_life_1 = request.POST.get('expenses_life_1')
        expenses_life_2 = request.POST.get('expenses_life_2')
        expenses_disability_1 = request.POST.get('expenses_disability_1')
        expenses_disability_2 = request.POST.get('expenses_disability_2')
        expenses_auto_1 = request.POST.get('expenses_auto_1')
        expenses_auto_2 = request.POST.get('expenses_auto_2')
        expenses_other_1 = request.POST.get('expenses_other_1')
        expenses_other_2 = request.POST.get('expenses_other_2')
        expenses_salaries_1 = request.POST.get('expenses_salaries_1')
        expenses_salaries_2 = request.POST.get('expenses_salaries_2')
        expenses_interes_1 = request.POST.get('expenses_interes_1')
        expenses_interes_2 = request.POST.get('expenses_interes_2')
        expenses_rent_1 = request.POST.get('expenses_rent_1')
        expenses_rent_2 = request.POST.get('expenses_rent_2')
        expenses_depreciation_1 = request.POST.get('expenses_depreciation_1')
        expenses_depreciation_2 = request.POST.get('expenses_depreciation_2')
        expenses_donations_1 = request.POST.get('expenses_donations_1')
        expenses_donations_2 = request.POST.get('expenses_donations_2')
        expenses_commissions_1 = request.POST.get('expenses_commissions_1')
        expenses_commissions_2 = request.POST.get('expenses_commissions_2')
        expenses_employees_1 = request.POST.get('expenses_employees_1')
        expenses_employees_2 = request.POST.get('expenses_employees_2')
        expenses_brokers_1 = request.POST.get('expenses_brokers_1')
        expenses_brokers_2 = request.POST.get('expenses_brokers_2')
        expenses_other_operational_1 = request.POST.get('expenses_other_operational_1')
        expenses_other_operational_2 = request.POST.get('expenses_other_operational_2')
        total_expenses_1 = request.POST.get('total_expenses_1')
        total_expenses_2 = request.POST.get('total_expenses_2')
        net_profit_1 = request.POST.get('net_profit_1')
        net_profit_2 = request.POST.get('net_profit_2')
        balance_year_1 = request.POST.get('balance_year_1')
        balance_year_2 = request.POST.get('balance_year_2')
        guaranteed_1 = request.POST.get('guaranteed_1')
        guaranteed_2 = request.POST.get('guaranteed_2')
        guaranteed_3 = request.POST.get('guaranteed_3')
        guaranteed_4 = request.POST.get('guaranteed_4')
        veterans_1 = request.POST.get('veterans_1')
        veterans_2 = request.POST.get('veterans_2')
        veterans_3 = request.POST.get('veterans_3')
        veterans_4 = request.POST.get('veterans_4')
        conventional_1 = request.POST.get('conventional_1')
        conventional_2 = request.POST.get('conventional_2')
        conventional_3 = request.POST.get('conventional_3')
        conventional_4 = request.POST.get('conventional_4')
        other_1 = request.POST.get('other_1')
        other_2 = request.POST.get('other_2')
        other_3 = request.POST.get('other_3')
        other_4 = request.POST.get('other_4')
        policy_loans_1 = request.POST.get('policy_loans_1')
        policy_loans_2 = request.POST.get('policy_loans_2')
        policy_loans_3 = request.POST.get('policy_loans_3')
        policy_loans_4 = request.POST.get('policy_loans_4')
        other_specify_1 = request.POST.get('other_specify_1')
        other_specify_2 = request.POST.get('other_specify_2')
        other_specify_3 = request.POST.get('other_specify_3')
        other_specify_4 = request.POST.get('other_specify_4')
        policy_reserves_1 = request.POST.get('policy_reserves_1')
        policy_reserves_2 = request.POST.get('policy_reserves_2')
        accrued_dividends_1 = request.POST.get('accrued_dividends_1')
        accrued_dividends_2 = request.POST.get('accrued_dividends_2')
        signature = request.POST.get('signature')
        date = request.POST.get('date')
        phone = request.POST.get('phone')
        position = request.POST.get('position')
        
        csv_file_path = 'data/cuestionarios/balanza_de_pago/JP-361.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['income_expenses_year_1', 'income_expenses_year_2',
                                'income_life_1', 'income_life_2', 'income_disability_1',
                                'income_disability_2', 'income_auto_1', 'income_auto_2',
                                'income_other_1', 'income_other_2', 'income_interest_1', 
                                'income_interest_2', 'income_rent_1', 'income_rent_2',
                                'income_other_2_1', 'income_other_2_2', 'total_income_1', 
                                'total_income_2', 'expenses_life_1', 'expenses_life_2',
                                'expenses_disability_1', 'expenses_disability_2', 
                                'expenses_auto_1', 'expenses_auto_2', 'expenses_other_1',
                                'expenses_other_2', 'expenses_salaries_1', 'expenses_salaries_2',
                                'expenses_interes_1', 'expenses_interes_2', 'expenses_rent_1',  
                                'expenses_rent_2', 'expenses_depreciation_1', 'expenses_depreciation_2',
                                'expenses_donations_1', 'expenses_donations_2', 'expenses_commissions_1',
                                'expenses_commissions_2', 'expenses_employees_1', 'expenses_employees_2',
                                'expenses_brokers_1', 'expenses_brokers_2', 'expenses_other_operational_1',
                                'expenses_other_operational_2', 'total_expenses_1', 'total_expenses_2',
                                'net_profit_1', 'net_profit_2', 'balance_year_1', 'balance_year_2',
                                'guaranteed_1', 'guaranteed_2', 'guaranteed_3', 'guaranteed_4',
                                'veterans_1', 'veterans_2', 'veterans_3', 'veterans_4', 
                                'conventional_1', 'conventional_2', 'conventional_3', 'conventional_4',
                                'other_1', 'other_2', 'other_3', 'other_4', 'policy_loans_1',
                                'policy_loans_2', 'policy_loans_3', 'policy_loans_4', 'other_specify_1',
                                'other_specify_2', 'other_specify_3', 'other_specify_4', 'policy_reserves_1',
                                'policy_reserves_2', 'accrued_dividends_1', 'accrued_dividends_2',
                                'signature', 'date', 'phone', 'position'
                                ])
            
            writer.writerow([
                            income_expenses_year_1, income_expenses_year_2,
                            income_life_1, income_life_2, income_disability_1, 
                            income_disability_2, income_auto_1, income_auto_2, 
                            income_other_1, income_other_2, income_interest_1, 
                            income_interest_2, income_rent_1, income_rent_2,
                            income_other_2_1, income_other_2_2, total_income_1,
                            total_income_2, expenses_life_1, expenses_life_2,
                            expenses_disability_1, expenses_disability_2,
                            expenses_auto_1, expenses_auto_2, expenses_other_1,
                            expenses_other_2, expenses_salaries_1, expenses_salaries_2,
                            expenses_interes_1, expenses_interes_2, expenses_rent_1,
                            expenses_rent_2, expenses_depreciation_1, expenses_depreciation_2,
                            expenses_donations_1, expenses_donations_2, expenses_commissions_1,
                            expenses_commissions_2, expenses_employees_1, expenses_employees_2,
                            expenses_brokers_1, expenses_brokers_2, expenses_other_operational_1,
                            expenses_other_operational_2, total_expenses_1, total_expenses_2,
                            net_profit_1, net_profit_2, balance_year_1, balance_year_2,
                            guaranteed_1, guaranteed_2, guaranteed_3, guaranteed_4,
                            veterans_1, veterans_2, veterans_3, veterans_4,
                            conventional_1, conventional_2, conventional_3, conventional_4,
                            other_1, other_2, other_3, other_4, policy_loans_1,
                            policy_loans_2, policy_loans_3, policy_loans_4, other_specify_1,
                            other_specify_2, other_specify_3, other_specify_4, policy_reserves_1,
                            policy_reserves_2, accrued_dividends_1, accrued_dividends_2,
                            signature, date, phone, position
                            ])  

        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/balanza_de_pagos/JP-361.html")

def JP_362(request):
    if request.method == "POST":
        # Retrieve form data
        year_1 = request.POST.get('year_1')
        year_2 = request.POST.get('year_2')
        
        company_name = request.POST.get('company_name')
        
        debts_balance = request.POST.get('debts_balance')
        debts_emision = request.POST.get('debts_emision')
        debts_amortizacion = request.POST.get('debts_amortizacion')
        debts_final = request.POST.get('debts_final')
        debts_interes = request.POST.get('debts_interes')
        debts_acreedor = request.POST.get('debts_acreedor')
        
        debts_bond_balance = request.POST.get('debts_bond_balance')
        debts_bond_emision = request.POST.get('debts_bond_emision')
        debts_bond_amortizacion = request.POST.get('debts_bond_amortizacion')
        debts_bond_final = request.POST.get('debts_bond_final')
        debts_bond_interes = request.POST.get('debts_bond_interes')
        debts_bond_acreedor = request.POST.get('debts_bond_acreedor')
        
        debts_promossory_notes_balance = request.POST.get('debts_promossory_notes_balance')
        debts_promossory_notes_emision = request.POST.get('debts_promossory_notes_emision')
        debts_promossory_notes_amortizacion = request.POST.get('debts_promossory_notes_amortizacion')
        debts_promossory_notes_final = request.POST.get('debts_promossory_notes_final')
        debts_promossory_notes_interes = request.POST.get('debts_promossory_notes_interes')
        debts_promossory_notes_acreedor = request.POST.get('debts_promossory_notes_acreedor')
        
        debts_others_balance = request.POST.get('debts_others_balance')
        debts_others_emision = request.POST.get('debts_others_emision')
        debts_others_amortizacion = request.POST.get('debts_others_amortizacion')
        debts_others_final = request.POST.get('debts_others_final')
        debts_others_interes = request.POST.get('debts_others_interes')
        debts_others_acreedor = request.POST.get('debts_others_acreedor')
        
        short_promossory_balance = request.POST.get('short_promossory_balance')
        short_promossory_emision = request.POST.get('short_promossory_emision')
        short_promossory_amortizacion = request.POST.get('short_promossory_amortizacion')
        short_promossory_final = request.POST.get('short_promossory_final')
        short_promossory_interes = request.POST.get('short_promossory_interes')
        short_promossory_acreedor = request.POST.get('short_promossory_acreedor')
        
        short_account_balance = request.POST.get('short_account_balance')
        short_account_emision = request.POST.get('short_account_emision')
        short_account_amortizacion = request.POST.get('short_account_amortizacion')
        short_account_final = request.POST.get('short_account_final')
        short_account_interes = request.POST.get('short_account_interes')
        short_account_acreedor = request.POST.get('short_account_acreedor')
        
        short_others_balance = request.POST.get('short_others_balance')
        short_others_emision = request.POST.get('short_others_emision')
        short_others_amortizacion = request.POST.get('short_others_amortizacion')
        short_others_final = request.POST.get('short_others_final')
        short_others_interes = request.POST.get('short_others_interes')
        short_others_acreedor = request.POST.get('short_others_acreedor')
        
        short_term_balance = request.POST.get('short_term_balance')
        short_term_emision = request.POST.get('short_term_emision')
        short_term_amortizacion = request.POST.get('short_term_amortizacion')
        short_term_final = request.POST.get('short_term_final')
        short_term_interes = request.POST.get('short_term_interes')
        short_term_acreedor = request.POST.get('short_term_acreedor')
        
        assets_balance = request.POST.get('assets_balance')
        assets_emision = request.POST.get('assets_emision')
        assets_amortizacion = request.POST.get('assets_amortizacion')
        assets_final = request.POST.get('assets_final')
        assets_interes = request.POST.get('assets_interes')
        
        assets_values_balance = request.POST.get('assets_values_balance')
        assets_values_emision = request.POST.get('assets_values_emision')
        assets_values_amortizacion = request.POST.get('assets_values_amortizacion')
        assets_values_final = request.POST.get('assets_values_final')
        assets_values_interes = request.POST.get('assets_values_interes')
        
        assets_others_balance = request.POST.get('assets_others_balance')
        assets_others_emision = request.POST.get('assets_others_emision')
        assets_others_amortizacion = request.POST.get('assets_others_amortizacion')
        assets_others_final = request.POST.get('assets_others_final')
        assets_others_interes = request.POST.get('assets_others_interes')
        
        short_balance = request.POST.get('short_balance')
        short_emision = request.POST.get('short_emision')
        short_amortizacion = request.POST.get('short_amortizacion')
        short_final = request.POST.get('short_final')
        short_interes = request.POST.get('short_interes')
        
        short_balance_balance = request.POST.get('short_balance_balance')
        short_balance_emision = request.POST.get('short_balance_emision')
        short_balance_amortizacion = request.POST.get('short_balance_amortizacion')
        short_balance_final = request.POST.get('short_balance_final')
        short_balance_interes = request.POST.get('short_balance_interes')
        
        short_accouts_balance = request.POST.get('short_accouts_balance')
        short_accouts_emision = request.POST.get('short_accouts_emision')
        short_accouts_amortizacion = request.POST.get('short_accouts_amortizacion')
        short_accouts_final = request.POST.get('short_accouts_final')
        short_accouts_interes = request.POST.get('short_accouts_interes')
        
        short_others_balance_2 = request.POST.get('short_others_balance_2')
        short_others_emision_2 = request.POST.get('short_others_emision_2')
        short_others_amortizacion_2 = request.POST.get('short_others_amortizacion_2')
        short_others_final_2 = request.POST.get('short_others_final_2')
        short_others_interes_2 = request.POST.get('short_others_interes_2')
        
        name_signature = request.POST.get('name_signature')
        position_signature = request.POST.get('position_signature')
        date_signature = request.POST.get('date_signature')
        phone = request.POST.get('phone')
        
        
        csv_file_path = 'data/cuestionarios/balanza_de_pagos/JP-362.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['year_1', 'year_2', 'company_name', 'debts_balance', 'debts_emision', 'debts_amortizacion',
                                'debts_final', 'debts_interes', 'debts_acreedor', 'debts_bond_balance', 'debts_bond_emision',
                                'debts_bond_amortizacion', 'debts_bond_final', 'debts_bond_interes', 'debts_bond_acreedor',
                                'debts_promossory_notes_balance', 'debts_promossory_notes_emision', 'debts_promossory_notes_amortizacion',
                                'debts_promossory_notes_final', 'debts_promossory_notes_interes', 'debts_promossory_notes_acreedor',
                                'debts_others_balance', 'debts_others_emision', 'debts_others_amortizacion', 'debts_others_final',
                                'debts_others_interes', 'debts_others_acreedor', 'short_term_balance', 'short_term_emision',
                                'short_term_amortizacion', 'short_term_final', 'short_term_interes', 'short_term_acreedor',
                                'short_promossory_balance', 'short_promossory_emision', 'short_promossory_amortizacion', 'short_promossory_final',
                                'short_promossory_interes', 'short_promossory_acreedor', 'short_account_balance', 'short_account_emision',
                                'short_account_amortizacion', 'short_account_final', 'short_account_interes', 'short_account_acreedor',
                                'short_others_balance', 'short_others_emision', 'short_others_amortizacion', 'short_others_final',
                                'short_others_interes', 'short_others_acreedor', 'assets_balance', 'assets_emision', 'assets_amortizacion',
                                'assets_final', 'assets_interes', 'assets_values_balance', 'assets_values_emision', 'assets_values_amortizacion',
                                'assets_values_final', 'assets_values_interes', 'assets_others_balance', 'assets_others_emision',
                                'assets_others_amortizacion', 'assets_others_final', 'assets_others_interes', 'short_balance',
                                'short_emision', 'short_amortizacion', 'short_final', 'short_interes',
                                'short_balance_balance', 'short_balance_emision', 'short_balance_amortizacion', 'short_balance_final', 'short_balance_interes',
                                'short_accouts_balance', 'short_accouts_emision', 'short_accouts_amortizacion', 'short_accouts_final',
                                'short_accouts_interes', 'short_others_balance_2', 'short_others_emision_2', 'short_others_amortizacion_2',
                                'short_others_final_2', 'short_others_interes_2', 'name_signature', 'position_signature', 'date_signature', 'phone'
                                ])
            
            writer.writerow([year_1, year_2, company_name, debts_balance, debts_emision, debts_amortizacion,
                            debts_final, debts_interes, debts_acreedor, debts_bond_balance, debts_bond_emision,
                            debts_bond_amortizacion, debts_bond_final, debts_bond_interes, debts_bond_acreedor,
                            debts_promossory_notes_balance, debts_promossory_notes_emision, debts_promossory_notes_amortizacion,
                            debts_promossory_notes_final, debts_promossory_notes_interes, debts_promossory_notes_acreedor,
                            debts_others_balance, debts_others_emision, debts_others_amortizacion, debts_others_final,
                            debts_others_interes, debts_others_acreedor, short_term_balance, short_term_emision,
                            short_term_amortizacion, short_term_final, short_term_interes, short_term_acreedor,
                            short_promossory_balance, short_promossory_emision, short_promossory_amortizacion, short_promossory_final,
                            short_promossory_interes, short_promossory_acreedor, short_account_balance, short_account_emision,
                            short_account_amortizacion, short_account_final, short_account_interes, short_account_acreedor,
                            short_others_balance, short_others_emision, short_others_amortizacion, short_others_final,
                            short_others_interes, short_others_acreedor, assets_balance, assets_emision, assets_amortizacion,
                            assets_final, assets_interes, assets_values_balance, assets_values_emision, assets_values_amortizacion,
                            assets_values_final, assets_values_interes, assets_others_balance, assets_others_emision,
                            assets_others_amortizacion, assets_others_final, assets_others_interes, short_balance,
                            short_emision, short_amortizacion, short_final, short_interes,
                            short_balance_balance, short_balance_emision, short_balance_amortizacion, short_balance_final, short_balance_interes,
                            short_accouts_balance, short_accouts_emision, short_accouts_amortizacion, short_accouts_final,
                            short_accouts_interes, short_others_balance_2, short_others_emision_2, short_others_amortizacion_2,
                            short_others_final_2, short_others_interes_2, name_signature, position_signature, date_signature, phone
                            ])  

        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/balanza_de_pagos/JP-362.html")

def JP_364(request):
    if request.method == "POST":
        # Retrieve form data
        year_bono1 = request.POST.get('year_bono1')
        year_bono2 = request.POST.get('year_bono2')
        year_paga1 = request.POST.get('year_paga1')
        year_paga2 = request.POST.get('year_paga2')
        ELA_bono1 = request.POST.get('ELA_bono1')
        ELA_bono2 = request.POST.get('ELA_bono2')
        ELA_paga1 = request.POST.get('ELA_paga1')
        ELA_paga2 = request.POST.get('ELA_paga2')
        ELA_agente = request.POST.get('ELA_agente')
        municipio_bono1 = request.POST.get('municipio_bono1')
        municipio_bono2 = request.POST.get('municipio_bono2')
        municipio_paga1 = request.POST.get('municipio_paga1')
        municipio_paga2 = request.POST.get('municipio_paga2')
        municipio_agente = request.POST.get('municipio_agente')
        corp_publicas_bono1 = request.POST.get('corp_publicas_bono1')
        corp_publicas_bono2 = request.POST.get('corp_publicas_bono2')
        corp_publicas_paga1 = request.POST.get('corp_publicas_paga1')
        corp_publicas_paga2 = request.POST.get('corp_publicas_paga2')
        corp_publicas_agente = request.POST.get('corp_publicas_agente')
        AEE_bono1 = request.POST.get('AEE_bono1')
        AEE_bono2 = request.POST.get('AEE_bono2')
        AEE_paga1 = request.POST.get('AEE_paga1')
        AEE_paga2 = request.POST.get('AEE_paga2')
        AEE_agente = request.POST.get('AEE_agente')
        Acarreteras_bono1 = request.POST.get('Acarreteras_bono1')
        Acarreteras_bono2 = request.POST.get('Acarreteras_bono2')
        Acarreteras_paga1 = request.POST.get('Acarreteras_paga1')
        Acarreteras_paga2 = request.POST.get('Acarreteras_paga2')
        Acarreteras_agente = request.POST.get('Acarreteras_agente')
        AAA_bono1 = request.POST.get('AAA_bono1')
        AAA_bono2 = request.POST.get('AAA_bono2')
        AAA_paga1 = request.POST.get('AAA_paga1')
        AAA_paga2 = request.POST.get('AAA_paga2')
        AAA_agente = request.POST.get('AAA_agente')
        AEP_bono1 = request.POST.get('AEP_bono1')
        AEP_bono2 = request.POST.get('AEP_bono2')
        AEP_paga1 = request.POST.get('AEP_paga1')
        AEP_paga2 = request.POST.get('AEP_paga2')
        AEP_agente = request.POST.get('AEP_agente')
        AP_bono1 = request.POST.get('AP_bono1') 
        AP_bono2 = request.POST.get('AP_bono2')
        AP_paga1 = request.POST.get('AP_paga1')
        AP_paga2 = request.POST.get('AP_paga2')
        AP_agente = request.POST.get('AP_agente')
        AT_bono1 = request.POST.get('AT_bono1')
        AT_bono2 = request.POST.get('AT_bono2')
        AT_paga1 = request.POST.get('AT_paga1')
        AT_paga2 = request.POST.get('AT_paga2')
        AT_agente = request.POST.get('AT_agente')
        CFI_bono1 = request.POST.get('CFI_bono1')
        CFI_bono2 = request.POST.get('CFI_bono2')
        CFI_paga1 = request.POST.get('CFI_paga1')
        CFI_paga2 = request.POST.get('CFI_paga2')
        CFI_agente = request.POST.get('CFI_agente')
        BGF_bono1 = request.POST.get('BGF_bono1')
        BGF_bono2 = request.POST.get('BGF_bono2')
        BGF_paga1 = request.POST.get('BGF_paga1')
        BGF_paga2 = request.POST.get('BGF_paga2')
        BGF_agente = request.POST.get('BGF_agente')
        CFV_bono1 = request.POST.get('CFV_bono1')
        CFV_bono2 = request.POST.get('CFV_bono2')
        CFV_paga1 = request.POST.get('CFV_paga1')
        CFV_paga2 = request.POST.get('CFV_paga2')
        CFV_agente = request.POST.get('CFV_agente')
        otherk_title = request.POST.get('otherk_title')
        otherk_bono1 = request.POST.get('otherk_bono1')
        otherk_bono2 = request.POST.get('otherk_bono2')
        otherk_paga1 = request.POST.get('otherk_paga1')
        otherk_paga2 = request.POST.get('otherk_paga2')
        otherk_agente = request.POST.get('otherk_agente')
        otherl_title = request.POST.get('otherl_title')
        otherl_bono1 = request.POST.get('otherl_bono1')
        otherl_bono2 = request.POST.get('otherl_bono2')
        otherl_paga1 = request.POST.get('otherl_paga1')
        otherl_paga2 = request.POST.get('otherl_paga2')
        otherl_agente = request.POST.get('otherl_agente')
        otherm_title = request.POST.get('otherm_title')
        otherm_bono1 = request.POST.get('otherm_bono1')
        otherm_bono2 = request.POST.get('otherm_bono2')
        otherm_paga1 = request.POST.get('otherm_paga1')
        otherm_paga2 = request.POST.get('otherm_paga2')
        otherm_agente = request.POST.get('otherm_agente')
        
        year_balance1 = request.POST.get('year_balance1')
        year_balance2 = request.POST.get('year_balance2')
        FHA_balance1 = request.POST.get('FHA_balance1')
        FHA_balance2 = request.POST.get('FHA_balance2')
        FHA_agente = request.POST.get('FHA_agente')
        GAV_balance1 = request.POST.get('GAV_balance1')
        GAV_balance2 = request.POST.get('GAV_balance2')
        GAV_agente = request.POST.get('GAV_agente')
        convencionales_balance1 = request.POST.get('convencionales_balance1')
        convencionales_balance2 = request.POST.get('convencionales_balance2')
        convencionales_agente = request.POST.get('convencionales_agente')
        otras_instituciones_balance1 = request.POST.get('otras_instituciones_balance1')
        otras_instituciones_balance2 = request.POST.get('otras_instituciones_balance2')
        otras_instituciones_agente = request.POST.get('otras_instituciones_agente')
        prestamos_hipo_balance1 = request.POST.get('prestamos_hipo_balance1')
        prestamos_hipo_balance2 = request.POST.get('prestamos_hipo_balance2')
        prestamos_hipo_agente = request.POST.get('prestamos_hipo_agente')
        prestamos_comerciales_industriales_balance1 = request.POST.get('prestamos_comerciales_industriales_balance1')
        prestamos_comerciales_industriales_balance2 = request.POST.get('prestamos_comerciales_industriales_balance2')
        prestamos_comerciales_industriales_agente = request.POST.get('prestamos_comerciales_industriales_agente')
        prestamos_poliza_balance1 = request.POST.get('prestamos_poliza_balance1')
        prestamos_poliza_balance2 = request.POST.get('prestamos_poliza_balance2')
        prestamos_poliza_agente = request.POST.get('prestamos_poliza_agente')
        reservas_poliza_balance1 = request.POST.get('reservas_poliza_balance1')
        reservas_poliza_balance2 = request.POST.get('reservas_poliza_balance2')
        reservas_poliza_agente = request.POST.get('reservas_poliza_agente')
        dividendos_poliza_balance1 = request.POST.get('dividendos_poliza_balance1')
        dividendos_poliza_balance2 = request.POST.get('dividendos_poliza_balance2')
        dividendos_poliza_agente = request.POST.get('dividendos_poliza_agente')
        nombre_firma = request.POST.get('nombre_firma')
        phone = request.POST.get('phone')
        nombre_persona = request.POST.get('nombre_persona')
        
        csv_file_path = 'data/cuestionarios/balanza_de_pagos/JP-364.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow([
                                'year_bono1', 'year_bono2', 'year_paga1', 'year_paga2', 'ELA_bono1', 'ELA_bono2',
                                'ELA_paga1', 'ELA_paga2', 'ELA_agente', 'municipio_bono1', 'municipio_bono2',
                                'municipio_paga1', 'municipio_paga2', 'municipio_agente', 'corp_publicas_bono1',
                                'corp_publicas_bono2', 'corp_publicas_paga1', 'corp_publicas_paga2', 'corp_publicas_agente',
                                'AEE_bono1', 'AEE_bono2', 'AEE_paga1', 'AEE_paga2', 'AEE_agente', 'Acarreteras_bono1',
                                'Acarreteras_bono2', 'Acarreteras_paga1', 'Acarreteras_paga2', 'Acarreteras_agente', 'AAA_bono1',
                                'AAA_bono2', 'AAA_paga1', 'AAA_paga2', 'AAA_agente', 'AEP_bono1', 'AEP_bono2', 'AEP_paga1',
                                'AEP_paga2', 'AEP_agente', 'AP_bono1', 'AP_bono2', 'AP_paga1', 'AP_paga2', 'AP_agente',
                                'AT_bono1', 'AT_bono2', 'AT_paga1', 'AT_paga2', 'AT_agente', 'CFI_bono1', 'CFI_bono2',
                                'CFI_paga1', 'CFI_paga2', 'CFI_agente', 'BGF_bono1', 'BGF_bono2', 'BGF_paga1', 'BGF_paga2',
                                'BGF_agente', 'CFV_bono1', 'CFV_bono2', 'CFV_paga1', 'CFV_paga2', 'CFV_agente', 'otherk_title',
                                'otherk_bono1', 'otherk_bono2', 'otherk_paga1', 'otherk_paga2', 'otherk_agente', 'otherl_title',
                                'otherl_bono1', 'otherl_bono2', 'otherl_paga1', 'otherl_paga2', 'otherl_agente', 'otherm_title',
                                'otherm_bono1', 'otherm_bono2', 'otherm_paga1', 'otherm_paga2', 'otherm_agente', 'year_balance1',
                                'year_balance2', 'FHA_balance1', 'FHA_balance2', 'FHA_agente', 'GAV_balance1', 'GAV_balance2',
                                'GAV_agente', 'convencionales_balance1', 'convencionales_balance2', 'convencionales_agente',
                                'otras_instituciones_balance1', 'otras_instituciones_balance2', 'otras_instituciones_agente',
                                'prestamos_hipo_balance1', 'prestamos_hipo_balance2', 'prestamos_hipo_agente',
                                'prestamos_comerciales_industriales_balance1', 'prestamos_comerciales_industriales_balance2',
                                'prestamos_comerciales_industriales_agente', 'prestamos_poliza_balance1', 'prestamos_poliza_balance2',
                                'prestamos_poliza_agente', 'reservas_poliza_balance1', 'reservas_poliza_balance2', 'reservas_poliza_agente',
                                'dividendos_poliza_balance1', 'dividendos_poliza_balance2', 'dividendos_poliza_agente', 'nombre_firma',
                                'phone', 'nombre_persona'
                                ])
            
            writer.writerow([
                            year_bono1, year_bono2, year_paga1, year_paga2, ELA_bono1, ELA_bono2,
                            ELA_paga1, ELA_paga2, ELA_agente, municipio_bono1, municipio_bono2,
                            municipio_paga1, municipio_paga2, municipio_agente, corp_publicas_bono1,
                            corp_publicas_bono2, corp_publicas_paga1, corp_publicas_paga2, corp_publicas_agente,
                            AEE_bono1, AEE_bono2, AEE_paga1, AEE_paga2, AEE_agente, Acarreteras_bono1,
                            Acarreteras_bono2, Acarreteras_paga1, Acarreteras_paga2, Acarreteras_agente, AAA_bono1,
                            AAA_bono2, AAA_paga1, AAA_paga2, AAA_agente, AEP_bono1, AEP_bono2, AEP_paga1,
                            AEP_paga2, AEP_agente, AP_bono1, AP_bono2, AP_paga1, AP_paga2, AP_agente,
                            AT_bono1, AT_bono2, AT_paga1, AT_paga2, AT_agente, CFI_bono1, CFI_bono2,
                            CFI_paga1, CFI_paga2, CFI_agente, BGF_bono1, BGF_bono2, BGF_paga1, BGF_paga2,
                            BGF_agente, CFV_bono1, CFV_bono2, CFV_paga1, CFV_paga2, CFV_agente, otherk_title,
                            otherk_bono1, otherk_bono2, otherk_paga1, otherk_paga2, otherk_agente, otherl_title,
                            otherl_bono1, otherl_bono2, otherl_paga1, otherl_paga2, otherl_agente, otherm_title,
                            otherm_bono1, otherm_bono2, otherm_paga1, otherm_paga2, otherm_agente, year_balance1,
                            year_balance2, FHA_balance1, FHA_balance2, FHA_agente, GAV_balance1, GAV_balance2,
                            GAV_agente, convencionales_balance1, convencionales_balance2, convencionales_agente,
                            otras_instituciones_balance1, otras_instituciones_balance2, otras_instituciones_agente,
                            prestamos_hipo_balance1, prestamos_hipo_balance2, prestamos_hipo_agente,
                            prestamos_comerciales_industriales_balance1, prestamos_comerciales_industriales_balance2,
                            prestamos_comerciales_industriales_agente, prestamos_poliza_balance1, prestamos_poliza_balance2,
                            prestamos_poliza_agente, reservas_poliza_balance1, reservas_poliza_balance2, reservas_poliza_agente,
                            dividendos_poliza_balance1, dividendos_poliza_balance2, dividendos_poliza_agente, nombre_firma,
                            phone, nombre_persona
                            ])  

        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/balanza_de_pagos/JP-364.html")

def JP_383(request):
    return render(request, "cuestionarios/balanza_de_pagos/JP-383.html")

def IP_110(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        liaison_officer = request.POST.get('liaison_officer')
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        legal_form = request.POST.get('legal_form')
        cfc = request.POST.get('cfc')
        business_type = request.POST.get('business_type')
        business_function = request.POST.get('business_function')
        branches = request.POST.get('branches')
        closing_date = request.POST.get('closing_date')
        services_revenues_12 = request.POST.get('services_revenues_12')
        services_revenues_13 = request.POST.get('services_revenues_13')
        industries_businesses_12 = request.POST.get('industries_businesses_12')
        industries_businesses_13 = request.POST.get('industries_businesses_13')
        people_12 = request.POST.get('people_12')
        people_13 = request.POST.get('people_13')
        sales_12 = request.POST.get('sales_12')
        sales_13 = request.POST.get('sales_13')
        incomes_rents_12 = request.POST.get('incomes_rents_12')
        incomes_rents_13 = request.POST.get('incomes_rents_12')
        incomes_interests_12 = request.POST.get('incomes_interests_12')
        incomes_interests_13 = request.POST.get('incomes_interests_13')
        dividends_12 = request.POST.get('dividends_12')
        dividends_13 = request.POST.get('dividends_13')
        others_incomes_12 = request.POST.get('others_incomes_12')
        others_incomes_13 = request.POST.get('others_incomes_13')
        total_income_12 = request.POST.get('total_income_12')
        total_income_13 = request.POST.get('total_income_13')
        expenses_12 = request.POST.get('expenses_12')
        expenses_13 = request.POST.get('expenses_13')
        salaries_2012 = request.POST.get('salaries_2012') 
        salaries_2013 = request.POST.get('salaries_2013')
        expenses_interests_12 = request.POST.get('expenses_interests_12')
        expenses_interests_13 = request.POST.get('expenses_interests_13')
        expenses_rents_12 = request.POST.get('expenses_rents_12')
        expenses_rents_13 = request.POST.get('expenses_rents_13')
        depreciation_12 = request.POST.get('depreciation_12')
        depreciation_13 = request.POST.get('depreciation_13')
        bad_debts_12 = request.POST.get('bad_debts_12')
        bad_debts_13 = request.POST.get('bad_debts_13')
        donations_12 = request.POST.get('donations_12')
        donations_13 = request.POST.get('donations_13')
        sales_tax_12 = request.POST.get('sales_tax_12')
        sales_tax_13 = request.POST.get('sales_tax_13')
        machinery_12 = request.POST.get('machinery_12')
        machinery_13 = request.POST.get('machinery_13')
        other_purchases_12 = request.POST.get('other_purchases_12')
        other_purchases_13 = request.POST.get('other_purchases_13')
        licenses_12 = request.POST.get('licenses_12')
        licenses_13 = request.POST.get('licenses_13')
        other_expenses_12 = request.POST.get('other_expenses_12')
        other_expenses_13 = request.POST.get('other_expenses_13')
        total_expenses_12 = request.POST.get('total_expenses_12')
        total_expenses_13 = request.POST.get('total_expenses_13')
        net_profit_12 = request.POST.get('net_profit_12')
        net_profit_13 = request.POST.get('net_profit_13')
        income_tax_12 = request.POST.get('income_tax_12')
        income_tax_13 = request.POST.get('income_tax_13')
        profit_after_tax_12 = request.POST.get('profit_after_tax_12')
        profit_after_tax_13 = request.POST.get('profit_after_tax_13')
        withheld_tax_12 = request.POST.get('withheld_tax_12')
        withheld_tax_13 = request.POST.get('withheld_tax_13')
        signature = request.POST.get('signature')
        rank = request.POST.get('rank')
        
        
        csv_file_path = 'data/cuestionarios/ingreso_neto/IP_110.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['company_name','address','email','liaison_officer','ssn','tel','fax',
                                 'legal_form','cfc','business_type','business_function','branches',
                                 'closing_date','services_revenues_12','services_revenues_13',
                                 'industries_businesses_12','industries_businesses_13','people_12',
                                 'people_13','sales_12','sales_13','incomes_rents_12','incomes_rents_13'
                                 ,'incomes_interests_12','incomes_interests_13','dividends_12','dividends_13',
                                 'others_incomes_12','others_incomes_13','total_income_12','total_income_13',
                                 'expenses_12','expenses_13','salaries_2012','salaries_2013','expenses_interests_12'
                                 ,'expenses_interests_13','expenses_rents_12','expenses_rents_13','depreciation_12',
                                 'depreciation_13','bad_debts_12','bad_debts_13','donations_12','donations_13','sales_tax_12'
                                 ,'sales_tax_13','machinery_12','machinery_13','other_purchases_12','other_purchases_13',
                                 'licenses_12','licenses_13','other_expenses_12','other_expenses_13','total_expenses_12',
                                 'total_expenses_13','net_profit_12','net_profit_13','income_tax_12','income_tax_13',
                                 'profit_after_tax_12','profit_after_tax_13','withheld_tax_12','withheld_tax_13',
                                 'signature','rank'
                                ])
            
            writer.writerow([company_name, address, email, liaison_officer, 
                             ssn, tel, fax, legal_form, cfc, business_type,
                             business_function, branches, closing_date,
                             services_revenues_12, services_revenues_13,
                             industries_businesses_12, industries_businesses_13,
                             people_12, people_13, sales_12, sales_13,
                             incomes_rents_12, incomes_rents_13,
                             incomes_interests_12, incomes_interests_13,
                             dividends_12, dividends_13,
                             others_incomes_12, others_incomes_13,
                             total_income_12, total_income_13,
                             expenses_12, expenses_13,
                             salaries_2012, salaries_2013,
                             expenses_interests_12, expenses_interests_13,
                             expenses_rents_12, expenses_rents_13,
                             depreciation_12, depreciation_13,
                             bad_debts_12, bad_debts_13,
                             donations_12, donations_13,
                             sales_tax_12, sales_tax_13,
                             machinery_12, machinery_13,
                             other_purchases_12, other_purchases_13,
                             licenses_12, licenses_13,
                             other_expenses_12, other_expenses_13,
                             total_expenses_12, total_expenses_13,
                             net_profit_12, net_profit_13,
                             income_tax_12, income_tax_13,
                             profit_after_tax_12, profit_after_tax_13,
                             withheld_tax_12, withheld_tax_13,
                             signature, rank
                            ])  

        return render(request, "cuestionarios/succesfull.html")

    return render(request, "cuestionarios/ingreso_neto/IP-110.html")

def JP_541(request):
    if request.method == "POST":
        # Retrieve form data
        
        #TABLE 1
        encuesta_1 = request.POST.get('encuesta_1')
        trimestre_1 = request.POST.get('trimestre_1')
        company_name_1 = request.POST.get('company_name_1')
        liaison_officer_1 = request.POST.get('liaison_officer_1')
        tel_1 = request.POST.get('tel_1')
        project_1 = request.POST.get('project_1')
        branches_1 = request.POST.get('branches_1')
        
        project_name_1_1 = request.POST.get('project_name_1_1')
        city_1_1 = request.POST.get('city_1_1')
        total_number_project_1_1 = request.POST.get('total_number_project_1_1')
        total_cost_1_1 = request.POST.get('total_cost_1_1')
        start_date_1_1 = request.POST.get('start_date_1_1')
        end_date_1_1 = request.POST.get('end_date_1_1')
        value_first_trimester_1_1 = request.POST.get('value_first_trimester_1_1')
        value_second_trimester_1_1 = request.POST.get('value_second_trimester_1_1')
        value_third_trimester_1_1 = request.POST.get('value_third_trimester_1_1')
        value_fourth_trimester_1_1 = request.POST.get('value_fourth_trimester_1_1')
        
        project_name_1_2 = request.POST.get('project_name_1_2')
        city_1_2 = request.POST.get('city_1_2')
        total_number_project_1_2 = request.POST.get('total_number_project_1_2')
        total_cost_1_2 = request.POST.get('total_cost_1_2')
        start_date_1_2 = request.POST.get('start_date_1_2')
        end_date_1_2 = request.POST.get('end_date_1_2')
        value_first_trimester_1_2 = request.POST.get('value_first_trimester_1_2')
        value_second_trimester_1_2 = request.POST.get('value_second_trimester_1_2')
        value_third_trimester_1_2 = request.POST.get('value_third_trimester_1_2')
        value_fourth_trimester_1_2 = request.POST.get('value_fourth_trimester_1_2')
        
        project_name_1_3 = request.POST.get('project_name_1_3')
        city_1_3 = request.POST.get('city_1_3')
        total_number_project_1_3 = request.POST.get('total_number_project_1_3')
        total_cost_1_3 = request.POST.get('total_cost_1_3')
        start_date_1_3 = request.POST.get('start_date_1_3')
        end_date_1_3 = request.POST.get('end_date_1_3')
        value_first_trimester_1_3 = request.POST.get('value_first_trimester_1_3')
        value_second_trimester_1_3 = request.POST.get('value_second_trimester_1_3')
        value_third_trimester_1_3 = request.POST.get('value_third_trimester_1_3')
        value_fourth_trimester_1_3 = request.POST.get('value_fourth_trimester_1_3')
        
        project_name_1_4 = request.POST.get('project_name_1_4')
        city_1_4 = request.POST.get('city_1_4')
        total_number_project_1_4 = request.POST.get('total_number_project_1_4')
        total_cost_1_4 = request.POST.get('total_cost_1_4')
        start_date_1_4 = request.POST.get('start_date_1_4')
        end_date_1_4 = request.POST.get('end_date_1_4')
        value_first_trimester_1_4 = request.POST.get('value_first_trimester_1_4')
        value_second_trimester_1_4 = request.POST.get('value_second_trimester_1_4')
        value_third_trimester_1_4 = request.POST.get('value_third_trimester_1_4')
        value_fourth_trimester_1_4 = request.POST.get('value_fourth_trimester_1_4')
        
        project_name_1_5 = request.POST.get('project_name_1_5')
        city_1_5 = request.POST.get('city_1_5')
        total_number_project_1_5 = request.POST.get('total_number_project_1_5')
        total_cost_1_5 = request.POST.get('total_cost_1_5')
        start_date_1_5 = request.POST.get('start_date_1_5')
        end_date_1_5 = request.POST.get('end_date_1_5')
        value_first_trimester_1_5 = request.POST.get('value_first_trimester_1_5')
        value_second_trimester_1_5 = request.POST.get('value_second_trimester_1_5')
        value_third_trimester_1_5 = request.POST.get('value_third_trimester_1_5')
        value_fourth_trimester_1_5 = request.POST.get('value_fourth_trimester_1_5')
        
        project_name_1_6 = request.POST.get('project_name_1_6')
        city_1_6 = request.POST.get('city_1_6')
        total_number_project_1_6 = request.POST.get('total_number_project_1_6')
        total_cost_1_6 = request.POST.get('total_cost_1_6')
        start_date_1_6 = request.POST.get('start_date_1_6')
        end_date_1_6 = request.POST.get('end_date_1_6')
        value_first_trimester_1_6 = request.POST.get('value_first_trimester_1_6')
        value_second_trimester_1_6 = request.POST.get('value_second_trimester_1_6')
        value_third_trimester_1_6 = request.POST.get('value_third_trimester_1_6')
        value_fourth_trimester_1_6 = request.POST.get('value_fourth_trimester_1_6')
        
        project_name_1_7 = request.POST.get('project_name_1_7')
        city_1_7 = request.POST.get('city_1_7')
        total_number_project_1_7 = request.POST.get('total_number_project_1_7')
        total_cost_1_7 = request.POST.get('total_cost_1_7')
        start_date_1_7 = request.POST.get('start_date_1_7')
        end_date_1_7 = request.POST.get('end_date_1_7')
        value_first_trimester_1_7 = request.POST.get('value_first_trimester_1_7')
        value_second_trimester_1_7 = request.POST.get('value_second_trimester_1_7')
        value_third_trimester_1_7 = request.POST.get('value_third_trimester_1_7')
        value_fourth_trimester_1_7 = request.POST.get('value_fourth_trimester_1_7')
        
        project_name_1_8 = request.POST.get('project_name_1_8')
        city_1_8 = request.POST.get('city_1_8')
        total_number_project_1_8 = request.POST.get('total_number_project_1_8')
        total_cost_1_8 = request.POST.get('total_cost_1_8')
        start_date_1_8 = request.POST.get('start_date_1_8')
        end_date_1_8 = request.POST.get('end_date_1_8')
        value_first_trimester_1_8 = request.POST.get('value_first_trimester_1_8')
        value_second_trimester_1_8 = request.POST.get('value_second_trimester_1_8')
        value_third_trimester_1_8 = request.POST.get('value_third_trimester_1_8')
        value_fourth_trimester_1_8 = request.POST.get('value_fourth_trimester_1_8')
        
        project_name_1_9 = request.POST.get('project_name_1_9')
        city_1_9 = request.POST.get('city_1_9')
        total_number_project_1_9 = request.POST.get('total_number_project_1_9')
        total_cost_1_9 = request.POST.get('total_cost_1_9')
        start_date_1_9 = request.POST.get('start_date_1_9')
        end_date_1_9 = request.POST.get('end_date_1_9')
        value_first_trimester_1_9 = request.POST.get('value_first_trimester_1_9')
        value_second_trimester_1_9 = request.POST.get('value_second_trimester_1_9')
        value_third_trimester_1_9 = request.POST.get('value_third_trimester_1_9')
        value_fourth_trimester_1_9 = request.POST.get('value_fourth_trimester_1_9')
        
        project_name_1_10 = request.POST.get('project_name_1_10')
        city_1_10 = request.POST.get('city_1_10')
        total_number_project_1_10 = request.POST.get('total_number_project_1_10')
        total_cost_1_10 = request.POST.get('total_cost_1_10')
        start_date_1_10 = request.POST.get('start_date_1_10')
        end_date_1_10 = request.POST.get('end_date_1_10')
        value_first_trimester_1_10 = request.POST.get('value_first_trimester_1_10')
        value_second_trimester_1_10 = request.POST.get('value_second_trimester_1_10')
        value_third_trimester_1_10 = request.POST.get('value_third_trimester_1_10')
        value_fourth_trimester_1_10 = request.POST.get('value_fourth_trimester_1_10')
        
        
        
        #TABLE 2
        encuesta_2 = request.POST.get('encuesta_2')
        trimestre_2 = request.POST.get('trimestre_2')
        company_name_2 = request.POST.get('company_name_2')
        liaison_officer_2 = request.POST.get('liaison_officer_2')
        tel_2 = request.POST.get('tel_2')
        project_2 = request.POST.get('project_2')
        branches_2 = request.POST.get('branches_2')
        
        project_name_2_1 = request.POST.get('project_name_2_1')
        city_2_1 = request.POST.get('city_2_1')
        total_number_project_2_1 = request.POST.get('total_number_project_2_1')
        total_cost_2_1 = request.POST.get('total_cost_2_1')
        start_date_2_1 = request.POST.get('start_date_2_1')
        end_date_2_1 = request.POST.get('end_date_2_1')
        value_first_trimester_2_1 = request.POST.get('value_first_trimester_2_1')
        value_second_trimester_2_1 = request.POST.get('value_second_trimester_2_1')
        value_third_trimester_2_1 = request.POST.get('value_third_trimester_2_1')
        value_fourth_trimester_2_1 = request.POST.get('value_fourth_trimester_2_1')
        
        project_name_2_2 = request.POST.get('project_name_2_2')
        city_2_2 = request.POST.get('city_2_2')
        total_number_project_2_2 = request.POST.get('total_number_project_2_2')
        total_cost_2_2 = request.POST.get('total_cost_2_2')
        start_date_2_2 = request.POST.get('start_date_2_2')
        end_date_2_2 = request.POST.get('end_date_2_2')
        value_first_trimester_2_2 = request.POST.get('value_first_trimester_2_2')
        value_second_trimester_2_2 = request.POST.get('value_second_trimester_2_2')
        value_third_trimester_2_2 = request.POST.get('value_third_trimester_2_2')
        value_fourth_trimester_2_2 = request.POST.get('value_fourth_trimester_2_2')
        
        project_name_2_3 = request.POST.get('project_name_2_3')
        city_2_3 = request.POST.get('city_2_3')
        total_number_project_2_3 = request.POST.get('total_number_project_2_3')
        total_cost_2_3 = request.POST.get('total_cost_2_3')
        start_date_2_3 = request.POST.get('start_date_2_3')
        end_date_2_3 = request.POST.get('end_date_2_3')
        value_first_trimester_2_3 = request.POST.get('value_first_trimester_2_3')
        value_second_trimester_2_3 = request.POST.get('value_second_trimester_2_3')
        value_third_trimester_2_3 = request.POST.get('value_third_trimester_2_3')
        value_fourth_trimester_2_3 = request.POST.get('value_fourth_trimester_2_3')
        
        project_name_2_4 = request.POST.get('project_name_2_4')
        city_2_4 = request.POST.get('city_2_4')
        total_number_project_2_4 = request.POST.get('total_number_project_2_4')
        total_cost_2_4 = request.POST.get('total_cost_2_4')
        start_date_2_4 = request.POST.get('start_date_2_4')
        end_date_2_4 = request.POST.get('end_date_2_4')
        value_first_trimester_2_4 = request.POST.get('value_first_trimester_2_4')
        value_second_trimester_2_4 = request.POST.get('value_second_trimester_2_4')
        value_third_trimester_2_4 = request.POST.get('value_third_trimester_2_4')
        value_fourth_trimester_2_4 = request.POST.get('value_fourth_trimester_2_4')
        
        project_name_2_5 = request.POST.get('project_name_2_5')
        city_2_5 = request.POST.get('city_2_5')
        total_number_project_2_5 = request.POST.get('total_number_project_2_5')
        total_cost_2_5 = request.POST.get('total_cost_2_5')
        start_date_2_5 = request.POST.get('start_date_2_5')
        end_date_2_5 = request.POST.get('end_date_2_5')
        value_first_trimester_2_5 = request.POST.get('value_first_trimester_2_5')
        value_second_trimester_2_5 = request.POST.get('value_second_trimester_2_5')
        value_third_trimester_2_5 = request.POST.get('value_third_trimester_2_5')
        value_fourth_trimester_2_5 = request.POST.get('value_fourth_trimester_2_5')
        
        project_name_2_6 = request.POST.get('project_name_2_6')
        city_2_6 = request.POST.get('city_2_6')
        total_number_project_2_6 = request.POST.get('total_number_project_2_6')
        total_cost_2_6 = request.POST.get('total_cost_2_6')
        start_date_2_6 = request.POST.get('start_date_2_6')
        end_date_2_6 = request.POST.get('end_date_2_6')
        value_first_trimester_2_6 = request.POST.get('value_first_trimester_2_6')
        value_second_trimester_2_6 = request.POST.get('value_second_trimester_2_6')
        value_third_trimester_2_6 = request.POST.get('value_third_trimester_2_6')
        value_fourth_trimester_2_6 = request.POST.get('value_fourth_trimester_2_6')
        
        project_name_2_7 = request.POST.get('project_name_2_7')
        city_2_7 = request.POST.get('city_2_7')
        total_number_project_2_7 = request.POST.get('total_number_project_2_7')
        total_cost_2_7 = request.POST.get('total_cost_2_7')
        start_date_2_7 = request.POST.get('start_date_2_7')
        end_date_2_7 = request.POST.get('end_date_2_7')
        value_first_trimester_2_7 = request.POST.get('value_first_trimester_2_7')
        value_second_trimester_2_7 = request.POST.get('value_second_trimester_2_7')
        value_third_trimester_2_7 = request.POST.get('value_third_trimester_2_7')
        value_fourth_trimester_2_7 = request.POST.get('value_fourth_trimester_2_7')
        
        project_name_2_8 = request.POST.get('project_name_2_8')
        city_2_8 = request.POST.get('city_2_8')
        total_number_project_2_8 = request.POST.get('total_number_project_2_8')
        total_cost_2_8 = request.POST.get('total_cost_2_8')
        start_date_2_8 = request.POST.get('start_date_2_8')
        end_date_2_8 = request.POST.get('end_date_2_8')
        value_first_trimester_2_8 = request.POST.get('value_first_trimester_2_8')
        value_second_trimester_2_8 = request.POST.get('value_second_trimester_2_8')
        value_third_trimester_2_8 = request.POST.get('value_third_trimester_2_8')
        value_fourth_trimester_2_8 = request.POST.get('value_fourth_trimester_2_8')
        
        project_name_2_9 = request.POST.get('project_name_2_9')
        city_2_9 = request.POST.get('city_2_9')
        total_number_project_2_9 = request.POST.get('total_number_project_2_9')
        total_cost_2_9 = request.POST.get('total_cost_2_9')
        start_date_2_9 = request.POST.get('start_date_2_9')
        end_date_2_9 = request.POST.get('end_date_2_9')
        value_first_trimester_2_9 = request.POST.get('value_first_trimester_2_9')
        value_second_trimester_2_9 = request.POST.get('value_second_trimester_2_9')
        value_third_trimester_2_9 = request.POST.get('value_third_trimester_2_9')
        value_fourth_trimester_2_9 = request.POST.get('value_fourth_trimester_2_9')
        
        project_name_2_10 = request.POST.get('project_name_2_10')
        city_2_10 = request.POST.get('city_2_10')
        total_number_project_2_10 = request.POST.get('total_number_project_2_10')
        total_cost_2_10 = request.POST.get('total_cost_2_10')
        start_date_2_10 = request.POST.get('start_date_2_10')
        end_date_2_10 = request.POST.get('end_date_2_10')
        value_first_trimester_2_10 = request.POST.get('value_first_trimester_2_10')
        value_second_trimester_2_10 = request.POST.get('value_second_trimester_2_10')
        value_third_trimester_2_10 = request.POST.get('value_third_trimester_2_10')
        value_fourth_trimester_2_10 = request.POST.get('value_fourth_trimester_2_10')
        
        
        #TABLE 3
        encuesta_3 = request.POST.get('encuesta_3')
        trimestre_3 = request.POST.get('trimestre_3')
        company_name_3 = request.POST.get('company_name_3')
        liaison_officer_3 = request.POST.get('liaison_officer_3')
        tel_3 = request.POST.get('tel_3')
        project_3 = request.POST.get('project_3')
        branches_3 = request.POST.get('branches_3')
        
        project_name_3_1 = request.POST.get('project_name_3_1')
        city_3_1 = request.POST.get('city_3_1')
        total_number_project_3_1 = request.POST.get('total_number_project_3_1')
        total_cost_3_1 = request.POST.get('total_cost_3_1')
        start_date_3_1 = request.POST.get('start_date_3_1')
        end_date_3_1 = request.POST.get('end_date_3_1')
        value_first_trimester_3_1 = request.POST.get('value_first_trimester_3_1')
        value_second_trimester_3_1 = request.POST.get('value_second_trimester_3_1')
        value_third_trimester_3_1 = request.POST.get('value_third_trimester_3_1')
        value_fourth_trimester_3_1 = request.POST.get('value_fourth_trimester_3_1')
        
        project_name_3_2 = request.POST.get('project_name_3_2')
        city_3_2 = request.POST.get('city_3_2')
        total_number_project_3_2 = request.POST.get('total_number_project_3_2')
        total_cost_3_2 = request.POST.get('total_cost_3_2')
        start_date_3_2 = request.POST.get('start_date_3_2')
        end_date_3_2 = request.POST.get('end_date_3_2')
        value_first_trimester_3_2 = request.POST.get('value_first_trimester_3_2')
        value_second_trimester_3_2 = request.POST.get('value_second_trimester_3_2')
        value_third_trimester_3_2 = request.POST.get('value_third_trimester_3_2')
        value_fourth_trimester_3_2 = request.POST.get('value_fourth_trimester_3_2')
        
        project_name_3_3 = request.POST.get('project_name_3_3')
        city_3_3 = request.POST.get('city_3_3')
        total_number_project_3_3 = request.POST.get('total_number_project_3_3')
        total_cost_3_3 = request.POST.get('total_cost_3_3')
        start_date_3_3 = request.POST.get('start_date_3_3')
        end_date_3_3 = request.POST.get('end_date_3_3')
        value_first_trimester_3_3 = request.POST.get('value_first_trimester_3_3')
        value_second_trimester_3_3 = request.POST.get('value_second_trimester_3_3')
        value_third_trimester_3_3 = request.POST.get('value_third_trimester_3_3')
        value_fourth_trimester_3_3 = request.POST.get('value_fourth_trimester_3_3')
        
        project_name_3_4 = request.POST.get('project_name_3_4')
        city_3_4 = request.POST.get('city_3_4')
        total_number_project_3_4 = request.POST.get('total_number_project_3_4')
        total_cost_3_4 = request.POST.get('total_cost_3_4')
        start_date_3_4 = request.POST.get('start_date_3_4')
        end_date_3_4 = request.POST.get('end_date_3_4')
        value_first_trimester_3_4 = request.POST.get('value_first_trimester_3_4')
        value_second_trimester_3_4 = request.POST.get('value_second_trimester_3_4')
        value_third_trimester_3_4 = request.POST.get('value_third_trimester_3_4')
        value_fourth_trimester_3_4 = request.POST.get('value_fourth_trimester_3_4')
        
        project_name_3_5 = request.POST.get('project_name_3_5')
        city_3_5 = request.POST.get('city_3_5')
        total_number_project_3_5 = request.POST.get('total_number_project_3_5')
        total_cost_3_5 = request.POST.get('total_cost_3_5')
        start_date_3_5 = request.POST.get('start_date_3_5')
        end_date_3_5 = request.POST.get('end_date_3_5')
        value_first_trimester_3_5 = request.POST.get('value_first_trimester_3_5')
        value_second_trimester_3_5 = request.POST.get('value_second_trimester_3_5')
        value_third_trimester_3_5 = request.POST.get('value_third_trimester_3_5')
        value_fourth_trimester_3_5 = request.POST.get('value_fourth_trimester_3_5')
        
        project_name_3_6 = request.POST.get('project_name_3_6')
        city_3_6 = request.POST.get('city_3_6')
        total_number_project_3_6 = request.POST.get('total_number_project_3_6')
        total_cost_3_6 = request.POST.get('total_cost_3_6')
        start_date_3_6 = request.POST.get('start_date_3_6')
        end_date_3_6 = request.POST.get('end_date_3_6')
        value_first_trimester_3_6 = request.POST.get('value_first_trimester_3_6')
        value_second_trimester_3_6 = request.POST.get('value_second_trimester_3_6')
        value_third_trimester_3_6 = request.POST.get('value_third_trimester_3_6')
        value_fourth_trimester_3_6 = request.POST.get('value_fourth_trimester_3_6')
        
        project_name_3_7 = request.POST.get('project_name_3_7')
        city_3_7 = request.POST.get('city_3_7')
        total_number_project_3_7 = request.POST.get('total_number_project_3_7')
        total_cost_3_7 = request.POST.get('total_cost_3_7')
        start_date_3_7 = request.POST.get('start_date_3_7')
        end_date_3_7 = request.POST.get('end_date_3_7')
        value_first_trimester_3_7 = request.POST.get('value_first_trimester_3_7')
        value_second_trimester_3_7 = request.POST.get('value_second_trimester_3_7')
        value_third_trimester_3_7 = request.POST.get('value_third_trimester_3_7')
        value_fourth_trimester_3_7 = request.POST.get('value_fourth_trimester_3_7')
        
        project_name_3_8 = request.POST.get('project_name_3_8')
        city_3_8 = request.POST.get('city_3_8')
        total_number_project_3_8 = request.POST.get('total_number_project_3_8')
        total_cost_3_8 = request.POST.get('total_cost_3_8')
        start_date_3_8 = request.POST.get('start_date_3_8')
        end_date_3_8 = request.POST.get('end_date_3_8')
        value_first_trimester_3_8 = request.POST.get('value_first_trimester_3_8')
        value_second_trimester_3_8 = request.POST.get('value_second_trimester_3_8')
        value_third_trimester_3_8 = request.POST.get('value_third_trimester_3_8')
        value_fourth_trimester_3_8 = request.POST.get('value_fourth_trimester_3_8')
        
        project_name_3_9 = request.POST.get('project_name_3_9')
        city_3_9 = request.POST.get('city_3_9')
        total_number_project_3_9 = request.POST.get('total_number_project_3_9')
        total_cost_3_9 = request.POST.get('total_cost_3_9')
        start_date_3_9 = request.POST.get('start_date_3_9')
        end_date_3_9 = request.POST.get('end_date_3_9')
        value_first_trimester_3_9 = request.POST.get('value_first_trimester_3_9')
        value_second_trimester_3_9 = request.POST.get('value_second_trimester_3_9')
        value_third_trimester_3_9 = request.POST.get('value_third_trimester_3_9')
        value_fourth_trimester_3_9 = request.POST.get('value_fourth_trimester_3_9')
        
        project_name_3_10 = request.POST.get('project_name_3_10')
        city_3_10 = request.POST.get('city_3_10')
        total_number_project_3_10 = request.POST.get('total_number_project_3_10')
        total_cost_3_10 = request.POST.get('total_cost_3_10')
        start_date_3_10 = request.POST.get('start_date_3_10')
        end_date_3_10 = request.POST.get('end_date_3_10')
        value_first_trimester_3_10 = request.POST.get('value_first_trimester_3_10')
        value_second_trimester_3_10 = request.POST.get('value_second_trimester_3_10')
        value_third_trimester_3_10 = request.POST.get('value_third_trimester_3_10')
        value_fourth_trimester_3_10 = request.POST.get('value_fourth_trimester_3_10')
        
        
        #TABLE 4
        encuesta_4 = request.POST.get('encuesta_4')
        trimestre_4 = request.POST.get('trimestre_4')
        company_name_4 = request.POST.get('company_name_4')
        liaison_officer_4 = request.POST.get('liaison_officer_4')
        tel_4 = request.POST.get('tel_4')
        project_4 = request.POST.get('project_4')
        branches_4 = request.POST.get('branches_4')
        
        project_name_4_1 = request.POST.get('project_name_4_1')
        city_4_1 = request.POST.get('city_4_1')
        total_number_project_4_1 = request.POST.get('total_number_project_4_1')
        total_cost_4_1 = request.POST.get('total_cost_4_1')
        start_date_4_1 = request.POST.get('start_date_4_1')
        end_date_4_1 = request.POST.get('end_date_4_1')
        value_first_trimester_4_1 = request.POST.get('value_first_trimester_4_1')
        value_second_trimester_4_1 = request.POST.get('value_second_trimester_4_1')
        value_third_trimester_4_1 = request.POST.get('value_third_trimester_4_1')
        value_fourth_trimester_4_1 = request.POST.get('value_fourth_trimester_4_1')
        
        project_name_4_2 = request.POST.get('project_name_4_2')
        city_4_2 = request.POST.get('city_4_2')
        total_number_project_4_2 = request.POST.get('total_number_project_4_2')
        total_cost_4_2 = request.POST.get('total_cost_4_2')
        start_date_4_2 = request.POST.get('start_date_4_2')
        end_date_4_2 = request.POST.get('end_date_4_2')
        value_first_trimester_4_2 = request.POST.get('value_first_trimester_4_2')
        value_second_trimester_4_2 = request.POST.get('value_second_trimester_4_2')
        value_third_trimester_4_2 = request.POST.get('value_third_trimester_4_2')
        value_fourth_trimester_4_2 = request.POST.get('value_fourth_trimester_4_2')
        
        project_name_4_3 = request.POST.get('project_name_4_3')
        city_4_3 = request.POST.get('city_4_3')
        total_number_project_4_3 = request.POST.get('total_number_project_4_3')
        total_cost_4_3 = request.POST.get('total_cost_4_3')
        start_date_4_3 = request.POST.get('start_date_4_3')
        end_date_4_3 = request.POST.get('end_date_4_3')
        value_first_trimester_4_3 = request.POST.get('value_first_trimester_4_3')
        value_second_trimester_4_3 = request.POST.get('value_second_trimester_4_3')
        value_third_trimester_4_3 = request.POST.get('value_third_trimester_4_3')
        value_fourth_trimester_4_3 = request.POST.get('value_fourth_trimester_4_3')
        
        project_name_4_4 = request.POST.get('project_name_4_4')
        city_4_4 = request.POST.get('city_4_4')
        total_number_project_4_4 = request.POST.get('total_number_project_4_4')
        total_cost_4_4 = request.POST.get('total_cost_4_4')
        start_date_4_4 = request.POST.get('start_date_4_4')
        end_date_4_4 = request.POST.get('end_date_4_4')
        value_first_trimester_4_4 = request.POST.get('value_first_trimester_4_4')
        value_second_trimester_4_4 = request.POST.get('value_second_trimester_4_4')
        value_third_trimester_4_4 = request.POST.get('value_third_trimester_4_4')
        value_fourth_trimester_4_4 = request.POST.get('value_fourth_trimester_4_4')
        
        project_name_4_5 = request.POST.get('project_name_4_5')
        city_4_5 = request.POST.get('city_4_5')
        total_number_project_4_5 = request.POST.get('total_number_project_4_5')
        total_cost_4_5 = request.POST.get('total_cost_4_5')
        start_date_4_5 = request.POST.get('start_date_4_5')
        end_date_4_5 = request.POST.get('end_date_4_5')
        value_first_trimester_4_5 = request.POST.get('value_first_trimester_4_5')
        value_second_trimester_4_5 = request.POST.get('value_second_trimester_4_5')
        value_third_trimester_4_5 = request.POST.get('value_third_trimester_4_5')
        value_fourth_trimester_4_5 = request.POST.get('value_fourth_trimester_4_5')
        
        
        
        project_name_4_6 = request.POST.get('project_name_4_6')
        city_4_6 = request.POST.get('city_4_6')
        total_number_project_4_6 = request.POST.get('total_number_project_4_6')
        total_cost_4_6 = request.POST.get('total_cost_4_6')
        start_date_4_6 = request.POST.get('start_date_4_6')
        end_date_4_6 = request.POST.get('end_date_4_6')
        value_first_trimester_4_6 = request.POST.get('value_first_trimester_4_6')
        value_second_trimester_4_6 = request.POST.get('value_second_trimester_4_6')
        value_third_trimester_4_6 = request.POST.get('value_third_trimester_4_6')
        value_fourth_trimester_4_6 = request.POST.get('value_fourth_trimester_4_6')
        
        project_name_4_7 = request.POST.get('project_name_4_7')
        city_4_7 = request.POST.get('city_4_7')
        total_number_project_4_7 = request.POST.get('total_number_project_4_7')
        total_cost_4_7 = request.POST.get('total_cost_4_7')
        start_date_4_7 = request.POST.get('start_date_4_7')
        end_date_4_7 = request.POST.get('end_date_4_7')
        value_first_trimester_4_7 = request.POST.get('value_first_trimester_4_7')
        value_second_trimester_4_7 = request.POST.get('value_second_trimester_4_7')
        value_third_trimester_4_7 = request.POST.get('value_third_trimester_4_7')
        value_fourth_trimester_4_7 = request.POST.get('value_fourth_trimester_4_7')
        
        
        project_name_4_8 = request.POST.get('project_name_4_8')
        city_4_8 = request.POST.get('city_4_8')
        total_number_project_4_8 = request.POST.get('total_number_project_4_8')
        total_cost_4_8 = request.POST.get('total_cost_4_8')
        start_date_4_8 = request.POST.get('start_date_4_8')
        end_date_4_8 = request.POST.get('end_date_4_8')
        value_first_trimester_4_8 = request.POST.get('value_first_trimester_4_8')
        value_second_trimester_4_8 = request.POST.get('value_second_trimester_4_8')
        value_third_trimester_4_8 = request.POST.get('value_third_trimester_4_8')
        value_fourth_trimester_4_8 = request.POST.get('value_fourth_trimester_4_8')
        
        
        project_name_4_9 = request.POST.get('project_name_4_9')
        city_4_9 = request.POST.get('city_4_9')
        total_number_project_4_9 = request.POST.get('total_number_project_4_9')
        total_cost_4_9 = request.POST.get('total_cost_4_9')
        start_date_4_9 = request.POST.get('start_date_4_9')
        end_date_4_9 = request.POST.get('end_date_4_9')
        value_first_trimester_4_9 = request.POST.get('value_first_trimester_4_9')
        value_second_trimester_4_9 = request.POST.get('value_second_trimester_4_9')
        value_third_trimester_4_9 = request.POST.get('value_third_trimester_4_9')
        value_fourth_trimester_4_9 = request.POST.get('value_fourth_trimester_4_9')
        
        
        project_name_4_10 = request.POST.get('project_name_4_10')
        city_4_10 = request.POST.get('city_4_10')
        total_number_project_4_10 = request.POST.get('total_number_project_4_10')
        total_cost_4_10 = request.POST.get('total_cost_4_10')
        start_date_4_10 = request.POST.get('start_date_4_10')
        end_date_4_10 = request.POST.get('end_date_4_10')
        value_first_trimester_4_10 = request.POST.get('value_first_trimester_4_10')
        value_second_trimester_4_10 = request.POST.get('value_second_trimester_4_10')
        value_third_trimester_4_10 = request.POST.get('value_third_trimester_4_10')
        value_fourth_trimester_4_10 = request.POST.get('value_fourth_trimester_4_10')
        
        
        csv_file_path = 'data/cuestionarios/construcción/JP-541.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow([   
                                    'encuesta_1', 'trimestre_1', 'company_name_1', 'liaison_officer_1', 'tel_1', 'project_1', 'branches_1',
                                    'project_name_1_1', 'city_1_1', 'total_number_project_1_1', 'total_cost_1_1', 'start_date_1_1', 'end_date_1_1', 'value_first_trimester_1_1', 'value_second_trimester_1_1', 'value_third_trimester_1_1', 'value_fourth_trimester_1_1',
                                    'project_name_1_2', 'city_1_2', 'total_number_project_1_2', 'total_cost_1_2', 'start_date_1_2', 'end_date_1_2', 'value_first_trimester_1_2', 'value_second_trimester_1_2', 'value_third_trimester_1_2', 'value_fourth_trimester_1_2',
                                    'project_name_1_3', 'city_1_3', 'total_number_project_1_3', 'total_cost_1_3', 'start_date_1_3', 'end_date_1_3', 'value_first_trimester_1_3', 'value_second_trimester_1_3', 'value_third_trimester_1_3', 'value_fourth_trimester_1_3',
                                    'project_name_1_4', 'city_1_4', 'total_number_project_1_4', 'total_cost_1_4', 'start_date_1_4', 'end_date_1_4', 'value_first_trimester_1_4', 'value_second_trimester_1_4', 'value_third_trimester_1_4', 'value_fourth_trimester_1_4',
                                    'project_name_1_5', 'city_1_5', 'total_number_project_1_5', 'total_cost_1_5', 'start_date_1_5', 'end_date_1_5', 'value_first_trimester_1_5', 'value_second_trimester_1_5', 'value_third_trimester_1_5', 'value_fourth_trimester_1_5',
                                    'project_name_1_6', 'city_1_6', 'total_number_project_1_6', 'total_cost_1_6', 'start_date_1_6', 'end_date_1_6', 'value_first_trimester_1_6', 'value_second_trimester_1_6', 'value_third_trimester_1_6', 'value_fourth_trimester_1_6',
                                    'project_name_1_7', 'city_1_7', 'total_number_project_1_7', 'total_cost_1_7', 'start_date_1_7', 'end_date_1_7', 'value_first_trimester_1_7', 'value_second_trimester_1_7', 'value_third_trimester_1_7', 'value_fourth_trimester_1_7',
                                    'project_name_1_8', 'city_1_8', 'total_number_project_1_8', 'total_cost_1_8', 'start_date_1_8', 'end_date_1_8', 'value_first_trimester_1_8', 'value_second_trimester_1_8', 'value_third_trimester_1_8', 'value_fourth_trimester_1_8',
                                    'project_name_1_9', 'city_1_9', 'total_number_project_1_9', 'total_cost_1_9', 'start_date_1_9', 'end_date_1_9', 'value_first_trimester_1_9', 'value_second_trimester_1_9', 'value_third_trimester_1_9', 'value_fourth_trimester_1_9',
                                    'project_name_1_10', 'city_1_10', 'total_number_project_1_10', 'total_cost_1_10', 'start_date_1_10', 'end_date_1_10', 'value_first_trimester_1_10', 'value_second_trimester_1_10', 'value_third_trimester_1_10', 'value_fourth_trimester_1_10',
                                    
                                    'encuesta_2', 'trimestre_2', 'company_name_2', 'liaison_officer_2', 'tel_2', 'project_2', 'branches_2',
                                    'project_name_2_1', 'city_2_1', 'total_number_project_2_1', 'total_cost_2_1', 'start_date_2_1', 'end_date_2_1', 'value_first_trimester_2_1', 'value_second_trimester_2_1', 'value_third_trimester_2_1', 'value_fourth_trimester_2_1',
                                    'project_name_2_2', 'city_2_2', 'total_number_project_2_2', 'total_cost_2_2', 'start_date_2_2', 'end_date_2_2', 'value_first_trimester_2_2', 'value_second_trimester_2_2', 'value_third_trimester_2_2', 'value_fourth_trimester_2_2',
                                    'project_name_2_3', 'city_2_3', 'total_number_project_2_3', 'total_cost_2_3', 'start_date_2_3', 'end_date_2_3', 'value_first_trimester_2_3', 'value_second_trimester_2_3', 'value_third_trimester_2_3', 'value_fourth_trimester_2_3',
                                    'project_name_2_4', 'city_2_4', 'total_number_project_2_4', 'total_cost_2_4', 'start_date_2_4', 'end_date_2_4', 'value_first_trimester_2_4', 'value_second_trimester_2_4', 'value_third_trimester_2_4', 'value_fourth_trimester_2_4',
                                    'project_name_2_5', 'city_2_5', 'total_number_project_2_5', 'total_cost_2_5', 'start_date_2_5', 'end_date_2_5', 'value_first_trimester_2_5', 'value_second_trimester_2_5', 'value_third_trimester_2_5', 'value_fourth_trimester_2_5',
                                    'project_name_2_6', 'city_2_6', 'total_number_project_2_6', 'total_cost_2_6', 'start_date_2_6', 'end_date_2_6', 'value_first_trimester_2_6', 'value_second_trimester_2_6', 'value_third_trimester_2_6', 'value_fourth_trimester_2_6',
                                    'project_name_2_7', 'city_2_7', 'total_number_project_2_7', 'total_cost_2_7', 'start_date_2_7', 'end_date_2_7', 'value_first_trimester_2_7', 'value_second_trimester_2_7', 'value_third_trimester_2_7', 'value_fourth_trimester_2_7',
                                    'project_name_2_8', 'city_2_8', 'total_number_project_2_8', 'total_cost_2_8', 'start_date_2_8', 'end_date_2_8', 'value_first_trimester_2_8', 'value_second_trimester_2_8', 'value_third_trimester_2_8', 'value_fourth_trimester_2_8',
                                    'project_name_2_9', 'city_2_9', 'total_number_project_2_9', 'total_cost_2_9', 'start_date_2_9', 'end_date_2_9', 'value_first_trimester_2_9', 'value_second_trimester_2_9', 'value_third_trimester_2_9', 'value_fourth_trimester_2_9',
                                    'project_name_2_10', 'city_2_10', 'total_number_project_2_10', 'total_cost_2_10', 'start_date_2_10', 'end_date_2_10', 'value_first_trimester_2_10', 'value_second_trimester_2_10', 'value_third_trimester_2_10', 'value_fourth_trimester_2_10',
                                    
                                    'encuesta_3', 'trimestre_3', 'company_name_3', 'liaison_officer_3', 'tel_3', 'project_3', 'branches_3',
                                    'project_name_3_1', 'city_3_1', 'total_number_project_3_1', 'total_cost_3_1', 'start_date_3_1', 'end_date_3_1', 'value_first_trimester_3_1', 'value_second_trimester_3_1', 'value_third_trimester_3_1', 'value_fourth_trimester_3_1',
                                    'project_name_3_2', 'city_3_2', 'total_number_project_3_2', 'total_cost_3_2', 'start_date_3_2', 'end_date_3_2', 'value_first_trimester_3_2', 'value_second_trimester_3_2', 'value_third_trimester_3_2', 'value_fourth_trimester_3_2',
                                    'project_name_3_3', 'city_3_3', 'total_number_project_3_3', 'total_cost_3_3', 'start_date_3_3', 'end_date_3_3', 'value_first_trimester_3_3', 'value_second_trimester_3_3', 'value_third_trimester_3_3', 'value_fourth_trimester_3_3',
                                    'project_name_3_4', 'city_3_4', 'total_number_project_3_4', 'total_cost_3_4', 'start_date_3_4', 'end_date_3_4', 'value_first_trimester_3_4', 'value_second_trimester_3_4', 'value_third_trimester_3_4', 'value_fourth_trimester_3_4',
                                    'project_name_3_5', 'city_3_5', 'total_number_project_3_5', 'total_cost_3_5', 'start_date_3_5', 'end_date_3_5', 'value_first_trimester_3_5', 'value_second_trimester_3_5', 'value_third_trimester_3_5', 'value_fourth_trimester_3_5',
                                    'project_name_3_6', 'city_3_6', 'total_number_project_3_6', 'total_cost_3_6', 'start_date_3_6', 'end_date_3_6', 'value_first_trimester_3_6', 'value_second_trimester_3_6', 'value_third_trimester_3_6', 'value_fourth_trimester_3_6',
                                    'project_name_3_7', 'city_3_7', 'total_number_project_3_7', 'total_cost_3_7', 'start_date_3_7', 'end_date_3_7', 'value_first_trimester_3_7', 'value_second_trimester_3_7', 'value_third_trimester_3_7', 'value_fourth_trimester_3_7',
                                    'project_name_3_8', 'city_3_8', 'total_number_project_3_8', 'total_cost_3_8', 'start_date_3_8', 'end_date_3_8', 'value_first_trimester_3_8', 'value_second_trimester_3_8', 'value_third_trimester_3_8', 'value_fourth_trimester_3_8',
                                    'project_name_3_9', 'city_3_9', 'total_number_project_3_9', 'total_cost_3_9', 'start_date_3_9', 'end_date_3_9', 'value_first_trimester_3_9', 'value_second_trimester_3_9', 'value_third_trimester_3_9', 'value_fourth_trimester_3_9',
                                    'project_name_3_10', 'city_3_10', 'total_number_project_3_10', 'total_cost_3_10', 'start_date_3_10', 'end_date_3_10', 'value_first_trimester_3_10', 'value_second_trimester_3_10', 'value_third_trimester_3_10', 'value_fourth_trimester_3_10',
                                    
                                    'encuesta_4', 'trimestre_4', 'company_name_4', 'liaison_officer_4', 'tel_4', 'project_4', 'branches_4',
                                    'project_name_4_1', 'city_4_1', 'total_number_project_4_1', 'total_cost_4_1', 'start_date_4_1', 'end_date_4_1', 'value_first_trimester_4_1', 'value_second_trimester_4_1', 'value_third_trimester_4_1', 'value_fourth_trimester_4_1',
                                    'project_name_4_2', 'city_4_2', 'total_number_project_4_2', 'total_cost_4_2', 'start_date_4_2', 'end_date_4_2', 'value_first_trimester_4_2', 'value_second_trimester_4_2', 'value_third_trimester_4_2', 'value_fourth_trimester_4_2',
                                    'project_name_4_3', 'city_4_3', 'total_number_project_4_3', 'total_cost_4_3', 'start_date_4_3', 'end_date_4_3', 'value_first_trimester_4_3', 'value_second_trimester_4_3', 'value_third_trimester_4_3', 'value_fourth_trimester_4_3',
                                    'project_name_4_4', 'city_4_4', 'total_number_project_4_4', 'total_cost_4_4', 'start_date_4_4', 'end_date_4_4', 'value_first_trimester_4_4', 'value_second_trimester_4_4', 'value_third_trimester_4_4', 'value_fourth_trimester_4_4',
                                    'project_name_4_5', 'city_4_5', 'total_number_project_4_5', 'total_cost_4_5', 'start_date_4_5', 'end_date_4_5', 'value_first_trimester_4_5', 'value_second_trimester_4_5', 'value_third_trimester_4_5', 'value_fourth_trimester_4_5',
                                    'project_name_4_6', 'city_4_6', 'total_number_project_4_6', 'total_cost_4_6', 'start_date_4_6', 'end_date_4_6', 'value_first_trimester_4_6', 'value_second_trimester_4_6', 'value_third_trimester_4_6', 'value_fourth_trimester_4_6',
                                    'project_name_4_7', 'city_4_7', 'total_number_project_4_7', 'total_cost_4_7', 'start_date_4_7', 'end_date_4_7', 'value_first_trimester_4_7', 'value_second_trimester_4_7', 'value_third_trimester_4_7', 'value_fourth_trimester_4_7',
                                    'project_name_4_8', 'city_4_8', 'total_number_project_4_8', 'total_cost_4_8', 'start_date_4_8', 'end_date_4_8', 'value_first_trimester_4_8', 'value_second_trimester_4_8', 'value_third_trimester_4_8', 'value_fourth_trimester_4_8',
                                    'project_name_4_9', 'city_4_9', 'total_number_project_4_9', 'total_cost_4_9', 'start_date_4_9', 'end_date_4_9', 'value_first_trimester_4_9', 'value_second_trimester_4_9', 'value_third_trimester_4_9', 'value_fourth_trimester_4_9',
                                    'project_name_4_10', 'city_4_10', 'total_number_project_4_10', 'total_cost_4_10', 'start_date_4_10', 'end_date_4_10', 'value_first_trimester_4_10', 'value_second_trimester_4_10', 'value_third_trimester_4_10', 'value_fourth_trimester_4_10',
                                ])
            
            writer.writerow([   
                                encuesta_1, trimestre_1, company_name_1, liaison_officer_1, tel_1, project_1, branches_1,
                                project_name_1_1, city_1_1, total_number_project_1_1, total_cost_1_1, start_date_1_1, end_date_1_1, value_first_trimester_1_1, value_second_trimester_1_1, value_third_trimester_1_1, value_fourth_trimester_1_1,
                                project_name_1_2, city_1_2, total_number_project_1_2, total_cost_1_2, start_date_1_2, end_date_1_2, value_first_trimester_1_2, value_second_trimester_1_2, value_third_trimester_1_2, value_fourth_trimester_1_2,
                                project_name_1_3, city_1_3, total_number_project_1_3, total_cost_1_3, start_date_1_3, end_date_1_3, value_first_trimester_1_3, value_second_trimester_1_3, value_third_trimester_1_3, value_fourth_trimester_1_3,
                                project_name_1_4, city_1_4, total_number_project_1_4, total_cost_1_4, start_date_1_4, end_date_1_4, value_first_trimester_1_4, value_second_trimester_1_4, value_third_trimester_1_4, value_fourth_trimester_1_4,
                                project_name_1_5, city_1_5, total_number_project_1_5, total_cost_1_5, start_date_1_5, end_date_1_5, value_first_trimester_1_5, value_second_trimester_1_5, value_third_trimester_1_5, value_fourth_trimester_1_5,
                                project_name_1_6, city_1_6, total_number_project_1_6, total_cost_1_6, start_date_1_6, end_date_1_6, value_first_trimester_1_6, value_second_trimester_1_6, value_third_trimester_1_6, value_fourth_trimester_1_6,
                                project_name_1_7, city_1_7, total_number_project_1_7, total_cost_1_7, start_date_1_7, end_date_1_7, value_first_trimester_1_7, value_second_trimester_1_7, value_third_trimester_1_7, value_fourth_trimester_1_7,
                                project_name_1_8, city_1_8, total_number_project_1_8, total_cost_1_8, start_date_1_8, end_date_1_8, value_first_trimester_1_8, value_second_trimester_1_8, value_third_trimester_1_8, value_fourth_trimester_1_8,
                                project_name_1_9, city_1_9, total_number_project_1_9, total_cost_1_9, start_date_1_9, end_date_1_9, value_first_trimester_1_9, value_second_trimester_1_9, value_third_trimester_1_9, value_fourth_trimester_1_9,
                                project_name_1_10, city_1_10, total_number_project_1_10, total_cost_1_10, start_date_1_10, end_date_1_10, value_first_trimester_1_10, value_second_trimester_1_10, value_third_trimester_1_10, value_fourth_trimester_1_10,
                                
                                encuesta_2, trimestre_2, company_name_2, liaison_officer_2, tel_2, project_2, branches_2,
                                project_name_2_1, city_2_1, total_number_project_2_1, total_cost_2_1, start_date_2_1, end_date_2_1, value_first_trimester_2_1, value_second_trimester_2_1, value_third_trimester_2_1, value_fourth_trimester_2_1,
                                project_name_2_2, city_2_2, total_number_project_2_2, total_cost_2_2, start_date_2_2, end_date_2_2, value_first_trimester_2_2, value_second_trimester_2_2, value_third_trimester_2_2, value_fourth_trimester_2_2,
                                project_name_2_3, city_2_3, total_number_project_2_3, total_cost_2_3, start_date_2_3, end_date_2_3, value_first_trimester_2_3, value_second_trimester_2_3, value_third_trimester_2_3, value_fourth_trimester_2_3,
                                project_name_2_4, city_2_4, total_number_project_2_4, total_cost_2_4, start_date_2_4, end_date_2_4, value_first_trimester_2_4, value_second_trimester_2_4, value_third_trimester_2_4, value_fourth_trimester_2_4,
                                project_name_2_5, city_2_5, total_number_project_2_5, total_cost_2_5, start_date_2_5, end_date_2_5, value_first_trimester_2_5, value_second_trimester_2_5, value_third_trimester_2_5, value_fourth_trimester_2_5,
                                project_name_2_6, city_2_6, total_number_project_2_6, total_cost_2_6, start_date_2_6, end_date_2_6, value_first_trimester_2_6, value_second_trimester_2_6, value_third_trimester_2_6, value_fourth_trimester_2_6,
                                project_name_2_7, city_2_7, total_number_project_2_7, total_cost_2_7, start_date_2_7, end_date_2_7, value_first_trimester_2_7, value_second_trimester_2_7, value_third_trimester_2_7, value_fourth_trimester_2_7,
                                project_name_2_8, city_2_8, total_number_project_2_8, total_cost_2_8, start_date_2_8, end_date_2_8, value_first_trimester_2_8, value_second_trimester_2_8, value_third_trimester_2_8, value_fourth_trimester_2_8,
                                project_name_2_9, city_2_9, total_number_project_2_9, total_cost_2_9, start_date_2_9, end_date_2_9, value_first_trimester_2_9, value_second_trimester_2_9, value_third_trimester_2_9, value_fourth_trimester_2_9,
                                project_name_2_10, city_2_10, total_number_project_2_10, total_cost_2_10, start_date_2_10, end_date_2_10, value_first_trimester_2_10, value_second_trimester_2_10, value_third_trimester_2_10, value_fourth_trimester_2_10,
                                
                                encuesta_3, trimestre_3, company_name_3, liaison_officer_3, tel_3, project_3, branches_3,
                                project_name_3_1, city_3_1, total_number_project_3_1, total_cost_3_1, start_date_3_1, end_date_3_1, value_first_trimester_3_1, value_second_trimester_3_1, value_third_trimester_3_1, value_fourth_trimester_3_1,
                                project_name_3_2, city_3_2, total_number_project_3_2, total_cost_3_2, start_date_3_2, end_date_3_2, value_first_trimester_3_2, value_second_trimester_3_2, value_third_trimester_3_2, value_fourth_trimester_3_2,
                                project_name_3_3, city_3_3, total_number_project_3_3, total_cost_3_3, start_date_3_3, end_date_3_3, value_first_trimester_3_3, value_second_trimester_3_3, value_third_trimester_3_3, value_fourth_trimester_3_3,
                                project_name_3_4, city_3_4, total_number_project_3_4, total_cost_3_4, start_date_3_4, end_date_3_4, value_first_trimester_3_4, value_second_trimester_3_4, value_third_trimester_3_4, value_fourth_trimester_3_4,
                                project_name_3_5, city_3_5, total_number_project_3_5, total_cost_3_5, start_date_3_5, end_date_3_5, value_first_trimester_3_5, value_second_trimester_3_5, value_third_trimester_3_5, value_fourth_trimester_3_5,
                                project_name_3_6, city_3_6, total_number_project_3_6, total_cost_3_6, start_date_3_6, end_date_3_6, value_first_trimester_3_6, value_second_trimester_3_6, value_third_trimester_3_6, value_fourth_trimester_3_6,
                                project_name_3_7, city_3_7, total_number_project_3_7, total_cost_3_7, start_date_3_7, end_date_3_7, value_first_trimester_3_7, value_second_trimester_3_7, value_third_trimester_3_7, value_fourth_trimester_3_7,
                                project_name_3_8, city_3_8, total_number_project_3_8, total_cost_3_8, start_date_3_8, end_date_3_8, value_first_trimester_3_8, value_second_trimester_3_8, value_third_trimester_3_8, value_fourth_trimester_3_8,
                                project_name_3_9, city_3_9, total_number_project_3_9, total_cost_3_9, start_date_3_9, end_date_3_9, value_first_trimester_3_9, value_second_trimester_3_9, value_third_trimester_3_9, value_fourth_trimester_3_9,
                                project_name_3_10, city_3_10, total_number_project_3_10, total_cost_3_10, start_date_3_10, end_date_3_10, value_first_trimester_3_10, value_second_trimester_3_10, value_third_trimester_3_10, value_fourth_trimester_3_10,
                                
                
                                encuesta_4, trimestre_4, company_name_4, liaison_officer_4, tel_4, project_4, branches_4,
                                project_name_4_1, city_4_1, total_number_project_4_1, total_cost_4_1, start_date_4_1, end_date_4_1, value_first_trimester_4_1, value_second_trimester_4_1, value_third_trimester_4_1, value_fourth_trimester_4_1,
                                project_name_4_2, city_4_2, total_number_project_4_2, total_cost_4_2, start_date_4_2, end_date_4_2, value_first_trimester_4_2, value_second_trimester_4_2, value_third_trimester_4_2, value_fourth_trimester_4_2,
                                project_name_4_3, city_4_3, total_number_project_4_3, total_cost_4_3, start_date_4_3, end_date_4_3, value_first_trimester_4_3, value_second_trimester_4_3, value_third_trimester_4_3, value_fourth_trimester_4_3,
                                project_name_4_4, city_4_4, total_number_project_4_4, total_cost_4_4, start_date_4_4, end_date_4_4, value_first_trimester_4_4, value_second_trimester_4_4, value_third_trimester_4_4, value_fourth_trimester_4_4,
                                project_name_4_5, city_4_5, total_number_project_4_5, total_cost_4_5, start_date_4_5, end_date_4_5, value_first_trimester_4_5, value_second_trimester_4_5, value_third_trimester_4_5, value_fourth_trimester_4_5,
                                project_name_4_6, city_4_6, total_number_project_4_6, total_cost_4_6, start_date_4_6, end_date_4_6, value_first_trimester_4_6, value_second_trimester_4_6, value_third_trimester_4_6, value_fourth_trimester_4_6,
                                project_name_4_7, city_4_7, total_number_project_4_7, total_cost_4_7, start_date_4_7, end_date_4_7, value_first_trimester_4_7, value_second_trimester_4_7, value_third_trimester_4_7, value_fourth_trimester_4_7,
                                project_name_4_8, city_4_8, total_number_project_4_8, total_cost_4_8, start_date_4_8, end_date_4_8, value_first_trimester_4_8, value_second_trimester_4_8, value_third_trimester_4_8, value_fourth_trimester_4_8,
                                project_name_4_9, city_4_9, total_number_project_4_9, total_cost_4_9, start_date_4_9, end_date_4_9, value_first_trimester_4_9, value_second_trimester_4_9, value_third_trimester_4_9, value_fourth_trimester_4_9,
                                project_name_4_10, city_4_10, total_number_project_4_10, total_cost_4_10, start_date_4_10, end_date_4_10, value_first_trimester_4_10, value_second_trimester_4_10, value_third_trimester_4_10, value_fourth_trimester_4_10,
                             ])  

        return render(request, "cuestionarios/succesfull.html")
    
    return render(request, "cuestionarios/construcción/JP-541.html")

def JP_363(request):    
    if request.method == "POST":
        # Retrieve form data
        bonds_year_left = request.POST.get('bonds_year_left')
        bonds_year_right = request.POST.get('bonds_year_right')
        notes_year_left = request.POST.get('notes_year_left')
        notes_year_right = request.POST.get('notes_year_right')
        CG_bonds_left = request.POST.get('CG_bonds_left')
        CG_bonds_right = request.POST.get('CG_bonds_right')
        CG_notes_left = request.POST.get('CG_notes_left')
        CG_notes_right = request.POST.get('CG_notes_right')
        CG_name_service = request.POST.get('CG_name_service')
        town_bonds_left = request.POST.get('town_bonds_left')
        town_bonds_right = request.POST.get('town_bonds_right')
        town_notes_left = request.POST.get('town_notes_left')
        town_notes_right = request.POST.get('town_notes_right')
        town_name_service = request.POST.get('town_name_service')
        PC_bonds_left = request.POST.get('PC_bonds_left')
        PC_bonds_right = request.POST.get('PC_bonds_right')
        PC_notes_left = request.POST.get('PC_notes_left')
        PC_notes_right = request.POST.get('PC_notes_right')
        PC_name_service = request.POST.get('PC_name_service')
        EPA_bonds_left = request.POST.get('EPA_bonds_left')
        EPA_bonds_right = request.POST.get('EPA_bonds_right')
        EPA_notes_left = request.POST.get('EPA_notes_left')
        EPA_notes_right = request.POST.get('EPA_notes_right')
        EPA_name_service = request.POST.get('EPA_name_service')
        HA_bonds_left = request.POST.get('HA_bonds_left')
        HA_bonds_right = request.POST.get('HA_bonds_right')
        HA_notes_left = request.POST.get('HA_notes_left')
        HA_notes_right = request.POST.get('HA_notes_right')
        HA_name_service = request.POST.get('HA_name_service')
        ASA_bonds_left = request.POST.get('ASA_bonds_left')
        ASA_bonds_right = request.POST.get('ASA_bonds_right')
        ASA_notes_left = request.POST.get('ASA_notes_left')
        ASA_notes_right = request.POST.get('ASA_notes_right')
        ASA_name_service = request.POST.get('ASA_name_service')
        PBA_bonds_left = request.POST.get('PBA_bonds_left')
        PBA_bonds_right = request.POST.get('PBA_bonds_right')
        PBA_notes_left = request.POST.get('PBA_notes_left')
        PBA_notes_right = request.POST.get('PBA_notes_right')
        PBA_name_service = request.POST.get('PBA_name_service')
        PA_bonds_left = request.POST.get('PA_bonds_left')
        PA_bonds_right = request.POST.get('PA_bonds_right')
        PA_notes_left = request.POST.get('PA_notes_left')
        PA_notes_right = request.POST.get('PA_notes_right')
        PA_name_service = request.POST.get('PA_name_service')
        TA_bonds_left = request.POST.get('TA_bonds_left')
        TA_bonds_right = request.POST.get('TA_bonds_right')
        TA_notes_left = request.POST.get('TA_notes_left')
        TA_notes_right = request.POST.get('TA_notes_right')
        TA_name_service = request.POST.get('TA_name_service')
        IDC_bonds_left = request.POST.get('IDC_bonds_left')
        IDC_bonds_right = request.POST.get('IDC_bonds_right')
        IDC_notes_left = request.POST.get('IDC_notes_left')
        IDC_notes_right = request.POST.get('IDC_notes_right')
        IDC_name_service = request.POST.get('IDC_name_service')
        GDB_bonds_left = request.POST.get('GDB_bonds_left')
        GDB_bonds_right = request.POST.get('GDB_bonds_right')
        GDB_notes_left = request.POST.get('GDB_notes_left')
        GDB_notes_right = request.POST.get('GDB_notes_right')
        GDB_name_service = request.POST.get('GDB_name_service')
        HFC_bonds_left = request.POST.get('HFC_bonds_left')
        HFC_bonds_right = request.POST.get('HFC_bonds_right')
        HFC_notes_left = request.POST.get('HFC_notes_left')
        HFC_notes_right = request.POST.get('HFC_notes_right')
        HFC_name_service = request.POST.get('HFC_name_service')
        other = request.POST.get('other')
        other_bonds_left = request.POST.get('other_bonds_left')
        other_bonds_right = request.POST.get('other_bonds_right')
        other_notes_left = request.POST.get('other_notes_left')
        other_notes_right = request.POST.get('other_notes_right')
        other_name_service = request.POST.get('other_name_service')
        other_PC_1 = request.POST.get('other_PC_1')
        other_PC_1_bonds_left = request.POST.get('other_PC_1_bonds_left')
        other_PC_1_bonds_right = request.POST.get('other_PC_1_bonds_right')
        other_PC_1_notes_left = request.POST.get('other_PC_1_notes_left')
        other_PC_1_notes_right = request.POST.get('other_PC_1_notes_right')
        other_PC_1_name_service = request.POST.get('other_PC_1_name_service')
        other_PC_2 = request.POST.get('other_PC_2')
        other_PC_2_bonds_left = request.POST.get('other_PC_2_bonds_left')
        other_PC_2_bonds_right = request.POST.get('other_PC_2_bonds_right')
        other_PC_2_notes_left = request.POST.get('other_PC_2_notes_left')
        other_PC_2_notes_right = request.POST.get('other_PC_2_notes_right')
        other_PC_2_name_service = request.POST.get('other_PC_2_name_service')
        GNMA_bonds_left = request.POST.get('GNMA_bonds_left')
        GNMA_bonds_right = request.POST.get('GNMA_bonds_right')
        GNMA_notes_left = request.POST.get('GNMA_notes_left')
        GNMA_notes_right = request.POST.get('GNMA_notes_right')
        GNMA_name_service = request.POST.get('GNMA_name_service')
        other5 = request.POST.get('other5')
        other5_bonds_left = request.POST.get('other5_bonds_left')
        other5_bonds_right = request.POST.get('other5_bonds_right')
        other5_notes_left = request.POST.get('other5_notes_left')
        other5_notes_right = request.POST.get('other5_notes_right')
        other5_name_service = request.POST.get('other5_name_service')
        signature = request.POST.get('signature')
        position = request.POST.get('position')
        date = request.POST.get('date')
        phone = request.POST.get('phone')
        
        csv_file_path = 'data/cuestionarios/balanza_de_pago/JP-363.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(["bonds_year_left", "bonds_year_right", "notes_year_left", "notes_year_right", 
                                "CG_bonds_left", "CG_bonds_right", "CG_notes_left", "CG_notes_right", "CG_name_service",
                                "town_bonds_left", "town_bonds_right", "town_notes_left", "town_notes_right", 
                                "town_name_service", "PC_bonds_left", "PC_bonds_right", "PC_notes_left", 
                                "PC_notes_right", "PC_name_service", "EPA_bonds_left", "EPA_bonds_right", 
                                "EPA_notes_left", "EPA_notes_right", "EPA_name_service", "HA_bonds_left", 
                                "HA_bonds_right", "HA_notes_left", "HA_notes_right", "HA_name_service", 
                                "ASA_bonds_left", "ASA_bonds_right", "ASA_notes_left", "ASA_notes_right", 
                                "ASA_name_service", "PBA_bonds_left", "PBA_bonds_right", "PBA_notes_left", 
                                "PBA_notes_right", "PBA_name_service", "PA_bonds_left", "PA_bonds_right", 
                                "PA_notes_left", "PA_notes_right", "PA_name_service", "TA_bonds_left", 
                                "TA_bonds_right", "TA_notes_left", "TA_notes_right", "TA_name_service", 
                                "IDC_bonds_left", "IDC_bonds_right", "IDC_notes_left", "IDC_notes_right", 
                                "IDC_name_service", "GDB_bonds_left", "GDB_bonds_right", "GDB_notes_left", 
                                "GDB_notes_right", "GDB_name_service", "HFC_bonds_left", "HFC_bonds_right", 
                                "HFC_notes_left", "HFC_notes_right", "HFC_name_service", "other", "other_bonds_left",
                                "other_bonds_right", "other_notes_left", "other_notes_right", "other_name_service", 
                                "other_PC_1", "other_PC_1_bonds_left", "other_PC_1_bonds_right", "other_PC_1_notes_left", 
                                "other_PC_1_notes_right", "other_PC_1_name_service", "other_PC_2", "other_PC_2_bonds_left",
                                "other_PC_2_bonds_right", "other_PC_2_notes_left", "other_PC_2_notes_right", 
                                "other_PC_2_name_service", "GNMA_bonds_left", "GN", "GNMA_notes_left", "GNMA_notes_right",
                                "GNMA_name_service", "other5", "other5_bonds_left", "other5_bonds_right", "other5_notes_left",
                                "other5_notes_right", "other5_name_service", "signature", "position", "date", "phone"
                                ])
            
            writer.writerow([
                            bonds_year_left, bonds_year_right, notes_year_left, notes_year_right,
                            CG_bonds_left, CG_bonds_right, CG_notes_left, CG_notes_right, CG_name_service,
                            town_bonds_left, town_bonds_right, town_notes_left, town_notes_right,
                            town_name_service, PC_bonds_left, PC_bonds_right, PC_notes_left,
                            PC_notes_right, PC_name_service, EPA_bonds_left, EPA_bonds_right,
                            EPA_notes_left, EPA_notes_right, EPA_name_service, HA_bonds_left,
                            HA_bonds_right, HA_notes_left, HA_notes_right, HA_name_service,
                            ASA_bonds_left, ASA_bonds_right, ASA_notes_left, ASA_notes_right,
                            ASA_name_service, PBA_bonds_left, PBA_bonds_right, PBA_notes_left,
                            PBA_notes_right, PBA_name_service, PA_bonds_left, PA_bonds_right,
                            PA_notes_left, PA_notes_right, PA_name_service, TA_bonds_left,
                            TA_bonds_right, TA_notes_left, TA_notes_right, TA_name_service,
                            IDC_bonds_left, IDC_bonds_right, IDC_notes_left, IDC_notes_right,
                            IDC_name_service, GDB_bonds_left, GDB_bonds_right, GDB_notes_left,
                            GDB_notes_right, GDB_name_service, HFC_bonds_left, HFC_bonds_right,
                            HFC_notes_left, HFC_notes_right, HFC_name_service, other, other_bonds_left,
                            other_bonds_right, other_notes_left, other_notes_right, other_name_service,
                            other_PC_1, other_PC_1_bonds_left, other_PC_1_bonds_right, other_PC_1_notes_left,
                            other_PC_1_notes_right, other_PC_1_name_service, other_PC_2, other_PC_2_bonds_left,
                            other_PC_2_bonds_right, other_PC_2_notes_left, other_PC_2_notes_right,
                            other_PC_2_name_service, GNMA_bonds_left, GNMA_bonds_right, GNMA_notes_left,
                            GNMA_notes_right, GNMA_name_service, other5, other5_bonds_left, other5_bonds_right,
                            other5_notes_left, other5_notes_right, other5_name_service, signature, position,
                            date, phone
                            ])  

        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/balanza_de_pagos/JP-363.html")

def succesfull_page(request):
    return render(request, "cuestionarios/succesfull.html")

def Forms(request):
    return render(request, "cuestionarios/forms.html")

def JP_560_63110(request):
    if request.method == "POST":
        # Retrieve form data
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        sales_1 = request.POST.get('sales_1')
        sales_2 = request.POST.get('sales_2')
        disability_1 = request.POST.get('disability_1')
        disability_2 = request.POST.get('disability_2')
        life_1 = request.POST.get('life_1')
        life_2 = request.POST.get('life_2')
        interest_1 = request.POST.get('interest_1')
        interest_2 = request.POST.get('interest_2')
        other_income_1 = request.POST.get('other_income_1')
        other_income_2 = request.POST.get('other_income_2')
        total_income_1 = request.POST.get('total_income_1')
        total_income_2 = request.POST.get('total_income_2')
        interest_paid_1 = request.POST.get('interest_paid_1')
        interest_paid_2 = request.POST.get('interest_paid_2')
        disability_paid_1 = request.POST.get('disability_paid_1')
        disability_paid_2 = request.POST.get('disability_paid_2')
        life_paid_1 = request.POST.get('life_paid_1')
        life_paid_2 = request.POST.get('life_paid_2')
        other_expenditures_1 = request.POST.get('other_expenditures_1')
        other_expenditures_2 = request.POST.get('other_expenditures_2')
        total_expenditures_1 = request.POST.get('total_expenditures_1')
        total_expenditures_2 = request.POST.get('total_expenditures_2')
        net_profit_1 = request.POST.get('net_profit_1')
        net_profit_2 = request.POST.get('net_profit_2')
        initial_inventory_1 = request.POST.get('initial_inventory_1')
        initial_inventory_2 = request.POST.get('initial_inventory_2')
        final_inventory_1 = request.POST.get('final_inventory_1')
        final_inventory_2 = request.POST.get('final_inventory_2')
        signature = request.POST.get('signature')
        rank = request.POST.get('rank')

        csv_file_path = 'data/cuestionarios/ingreso_neto/JP-560-63110.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow([
                                    "ssn", "tel", "fax", "sales_1", 
                                    "sales_2", "disability_1", "disability_2", 
                                    "life_1", "life_2", "interest_1", "interest_2", 
                                    "other_income_1", "other_income_2", "total_income_1", 
                                    "total_income_2", "interest_paid_1", "interest_paid_2",
                                    "disability_paid_1", "disability_paid_2", "life_paid_1", 
                                    "life_paid_2", "other_expenditures_1", "other_expenditures_2", 
                                    "total_expenditures_1", "total_expenditures_2", "net_profit_1", 
                                    "net_profit_2", "initial_inventory_1", "initial_inventory_2", 
                                    "final_inventory_1", "final_inventory_2", "signature", "rank"
                                    ])
                
            writer.writerow([
                                ssn, tel, fax, sales_1, sales_2, disability_1, disability_2, life_1, 
                                life_2, interest_1, interest_2, other_income_1, other_income_2, total_income_1, 
                                total_income_2, interest_paid_1, interest_paid_2, disability_paid_1, disability_paid_2, 
                                life_paid_1, life_paid_2, other_expenditures_1, other_expenditures_2, total_expenditures_1, 
                                total_expenditures_2, net_profit_1, net_profit_2, initial_inventory_1, initial_inventory_2, 
                                final_inventory_1, final_inventory_2, signature, rank
                            ])
            
        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/ingreso_neto/JP-560-63110.html")

def IP_210(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        liaison_officer = request.POST.get('liaison_officer')
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        legal_form = request.POST.get('legal_form')
        cfc = request.POST.get('cfc')
        business_type = request.POST.get('business_type')
        business_function = request.POST.get('business_function')
        branches = request.POST.get('branches')
        closing_date = request.POST.get('closing_date')
        income_operations_12 = request.POST.get('income_operations_12')
        income_operations_13 = request.POST.get('income_operations_13')
        income_interests_12 = request.POST.get('income_interests_12')
        income_interests_13 = request.POST.get('income_interests_13')
        incomes_rents_12 = request.POST.get('incomes_rents_12')
        incomes_rents_13 = request.POST.get('incomes_rents_12')
        income_rent_land_12 = request.POST.get('income_rent_land_12')
        income_rent_land_13 = request.POST.get('income_rent_land_13')
        other_income_12 = request.POST.get('other_income_12')
        other_income_13 = request.POST.get('other_income_13')
        total_incomes_12 = request.POST.get('total_incomes_12')
        total_incomes_13 = request.POST.get('total_incomes_13')
        total_income_12 = request.POST.get('total_income_12')
        total_income_13 = request.POST.get('total_income_13')
        expenses_12 = request.POST.get('expenses_12')
        expenses_13 = request.POST.get('expenses_13')
        salaries_2012 = request.POST.get('salaries_2012') 
        salaries_2013 = request.POST.get('salaries_2013')
        expenses_interests_12 = request.POST.get('expenses_interests_12')
        expenses_interests_13 = request.POST.get('expenses_interests_13')
        depreciation_12 = request.POST.get('depreciation_12')
        depreciation_13 = request.POST.get('depreciation_13')
        expenses_rent_12 = request.POST.get('expenses_rent_12')
        expenses_rent_13 = request.POST.get('expenses_rent_13')
        bad_debts_12 = request.POST.get('bad_debts_12')
        bad_debts_13 = request.POST.get('bad_debts_13')
        donations_12 = request.POST.get('donations_12')
        donations_13 = request.POST.get('donations_13')
        sales_tax_12 = request.POST.get('sales_tax_12')
        sales_tax_13 = request.POST.get('sales_tax_13')
        machinery_12 = request.POST.get('machinery_12')
        machinery_13 = request.POST.get('machinery_13')
        other_purchases_12 = request.POST.get('other_purchases_12')
        other_purchases_13 = request.POST.get('other_purchases_13')
        licenses_12 = request.POST.get('licenses_12')
        licenses_13 = request.POST.get('licenses_13')
        other_expenses_12 = request.POST.get('other_expenses_12')
        other_expenses_13 = request.POST.get('other_expenses_13')
        total_expenses_12 = request.POST.get('total_expenses_12')
        total_expenses_13 = request.POST.get('total_expenses_13')
        net_profit_12 = request.POST.get('net_profit_12')
        net_profit_13 = request.POST.get('net_profit_13')
        income_tax_12 = request.POST.get('income_tax_12')
        income_tax_13 = request.POST.get('income_tax_13')
        profit_after_tax_12 = request.POST.get('profit_after_tax_12')
        profit_after_tax_13 = request.POST.get('profit_after_tax_13')
        withheld_tax_12 = request.POST.get('withheld_tax_12')
        withheld_tax_13 = request.POST.get('withheld_tax_13')
        signature = request.POST.get('signature')
        rank = request.POST.get('rank')
        
        
        csv_file_path = 'data/cuestionarios/ingreso_neto/IP_210.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['company_name','address','email','liaison_officer','ssn','tel','fax',
                                 'legal_form','cfc','business_type','business_function','branches',
                                 'closing_date','income_operations_12','income_operations_13',
                                 'income_interests_12','income_interests_13','incomes_rents_12'
                                 ,'incomes_rents_13' ,'income_rent_land_12','income_rent_land_13','other_income_12','other_income_13',
                                 'total_incomes_12','total_incomes_13','total_income_12','total_income_13',
                                 'expenses_12','expenses_13','salaries_2012','salaries_2013','expenses_interests_12'
                                 ,'expenses_interests_13','depreciation_12', 'depreciation_13','bad_debts_12','bad_debts_13',
                                 'expenses_rent_12','expenses_rent_13','donations_12','donations_13','sales_tax_12'
                                 ,'sales_tax_13','machinery_12','machinery_13','other_purchases_12','other_purchases_13',
                                 'licenses_12','licenses_13','other_expenses_12','other_expenses_13','total_expenses_12',
                                 'total_expenses_13','net_profit_12','net_profit_13','income_tax_12','income_tax_13',
                                 'profit_after_tax_12','profit_after_tax_13','withheld_tax_12','withheld_tax_13',
                                 'signature','rank'
                                ])
            
            writer.writerow([company_name, address, email, liaison_officer, 
                             ssn, tel, fax, legal_form, cfc, business_type,
                             business_function, branches, closing_date,
                             income_operations_12, income_operations_13,
                             income_interests_12, income_interests_13,
                             incomes_rents_12, incomes_rents_13,
                             income_rent_land_12, income_rent_land_13,
                             other_income_12, other_income_13,
                             total_incomes_12, total_incomes_13,
                             total_income_12, total_income_13,
                             expenses_12, expenses_13,
                             salaries_2012, salaries_2013,
                             expenses_interests_12, expenses_interests_13,
                             depreciation_12, depreciation_13,
                             expenses_rent_12, expenses_rent_13,
                             bad_debts_12, bad_debts_13,
                             donations_12, donations_13,
                             sales_tax_12, sales_tax_13,
                             machinery_12, machinery_13,
                             other_purchases_12, other_purchases_13,
                             licenses_12, licenses_13,
                             other_expenses_12, other_expenses_13,
                             total_expenses_12, total_expenses_13,
                             net_profit_12, net_profit_13,
                             income_tax_12, income_tax_13,
                             profit_after_tax_12, profit_after_tax_13,
                             withheld_tax_12, withheld_tax_13,
                             signature, rank
                            ])  

        return render(request, "cuestionarios/succesfull.html")

    return render(request, "cuestionarios/ingreso_neto/IP-210.html")

def IP_220(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        liaison_officer = request.POST.get('liaison_officer')
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        legal_form = request.POST.get('legal_form')
        cfc = request.POST.get('cfc')
        business_type = request.POST.get('business_type')
        business_function = request.POST.get('business_function')
        branches = request.POST.get('branches')
        branches_yes = request.POST.get('branches_yes')
        closing_date = request.POST.get('closing_date')
        services_revenues_12 = request.POST.get('services_revenues_12')
        services_revenues_13 = request.POST.get('services_revenues_13')
        residential_consumers_12 = request.POST.get('residential_consumers_12')
        residential_consumers_13 = request.POST.get('residential_consumers_13')
        other_consumers_12 = request.POST.get('other_consumers_12')
        other_consumers_13 = request.POST.get('other_consumers_13')
        incomes_rents_12 = request.POST.get('incomes_rents_12')
        incomes_rents_13 = request.POST.get('incomes_rents_13')
        incomes_interests_12 = request.POST.get('incomes_interests_12')
        incomes_interests_13 = request.POST.get('incomes_interests_13')
        dividends_12 = request.POST.get('dividends_12')
        dividends_13 = request.POST.get('dividends_13')
        others_incomes_12 = request.POST.get('others_incomes_12')
        others_incomes_13 = request.POST.get('others_incomes_13')
        total_income_12 = request.POST.get('total_income_12')
        total_income_13 = request.POST.get('total_income_13')
        salaries_2012 = request.POST.get('salaries_2012') 
        salaries_2013 = request.POST.get('salaries_2013')
        expenses_interests_12 = request.POST.get('expenses_interests_12')
        expenses_interests_13 = request.POST.get('expenses_interests_13')
        expenses_rents_12 = request.POST.get('expenses_rents_12')
        expenses_rents_13 = request.POST.get('expenses_rents_13')
        depreciation_12 = request.POST.get('depreciation_12')
        depreciation_13 = request.POST.get('depreciation_13')
        bad_debts_12 = request.POST.get('bad_debts_12')
        bad_debts_13 = request.POST.get('bad_debts_13')
        donations_12 = request.POST.get('donations_12')
        donations_13 = request.POST.get('donations_13')
        sales_tax_12 = request.POST.get('sales_tax_12')
        sales_tax_13 = request.POST.get('sales_tax_13')
        machinery_12 = request.POST.get('machinery_12')
        machinery_13 = request.POST.get('machinery_13')
        other_purchases_12 = request.POST.get('other_purchases_12')
        other_purchases_13 = request.POST.get('other_purchases_13')
        licenses_12 = request.POST.get('licenses_12')
        licenses_13 = request.POST.get('licenses_13')
        other_expenses_12 = request.POST.get('other_expenses_12')
        other_expenses_13 = request.POST.get('other_expenses_13')
        total_expenses_12 = request.POST.get('total_expenses_12')
        total_expenses_13 = request.POST.get('total_expenses_13')
        net_profit_12 = request.POST.get('net_profit_12')
        net_profit_13 = request.POST.get('net_profit_13')
        income_tax_12 = request.POST.get('income_tax_12')
        income_tax_13 = request.POST.get('income_tax_13')
        profit_after_tax_12 = request.POST.get('profit_after_tax_12')
        profit_after_tax_13 = request.POST.get('profit_after_tax_13')
        withheld_tax_12 = request.POST.get('withheld_tax_12')
        withheld_tax_13 = request.POST.get('withheld_tax_13')
        signature = request.POST.get('signature')
        rank = request.POST.get('rank')

        csv_file_path = 'data/cuestionarios/ingreso_neto/IP_220.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['company_name','address','email','liaison_officer','ssn','tel','fax',
                                 'legal_form','cfc','business_type','business_function','branches','branches_yes',
                                 'closing_date','services_revenues_12','services_revenues_13',
                                 'residential_consumers_12','residential_consumers_13','other_consumers_12',
                                 'other_consumers_13','incomes_rents_12','incomes_rents_13','incomes_interests_12',
                                 'incomes_interests_13','dividends_12','dividends_13','others_incomes_12',
                                 'others_incomes_13','total_income_12','total_income_13','salaries_2012',
                                 'salaries_2013','expenses_interests_12','expenses_interests_13','expenses_rents_12',
                                 'expenses_rents_13','depreciation_12','depreciation_13','bad_debts_12','bad_debts_13',
                                 'donations_12','donations_13','sales_tax_12','sales_tax_13','machinery_12',
                                 'machinery_13','other_purchases_12','other_purchases_13','licenses_12','licenses_13',
                                 'other_expenses_12','other_expenses_13','total_expenses_12','total_expenses_13',
                                 'net_profit_12','net_profit_13','income_tax_12','income_tax_13','profit_after_tax_12',
                                 'profit_after_tax_13','withheld_tax_12','withheld_tax_13','signature','rank'
                                ])
            
            writer.writerow([company_name, address, email, liaison_officer, 
                             ssn, tel, fax, legal_form, cfc, business_type,
                             business_function, branches, branches_yes, closing_date,
                             services_revenues_12, services_revenues_13,
                             residential_consumers_12, residential_consumers_13,
                             other_consumers_12, other_consumers_13, incomes_rents_12,
                             incomes_rents_13, incomes_interests_12, incomes_interests_13,
                             dividends_12, dividends_13, others_incomes_12,
                             others_incomes_13, total_income_12, total_income_13,
                             salaries_2012, salaries_2013, expenses_interests_12,
                             expenses_interests_13, expenses_rents_12, expenses_rents_13,
                             depreciation_12, depreciation_13, bad_debts_12, bad_debts_13,
                             donations_12, donations_13, sales_tax_12, sales_tax_13,
                             machinery_12, machinery_13, other_purchases_12, other_purchases_13,
                             licenses_12, licenses_13, other_expenses_12, other_expenses_13,
                             total_expenses_12, total_expenses_13, net_profit_12, net_profit_13,
                             income_tax_12, income_tax_13, profit_after_tax_12, profit_after_tax_13,
                             withheld_tax_12, withheld_tax_13, signature, rank
                            ])  

        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/ingreso_neto/IP-220.html")

def JP_560_63111(request):

    if request.method == "POST":
        # Retrieve form data
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        sales_1 = request.POST.get('sales_1')
        sales_2 = request.POST.get('sales_2')
        premiums_1 = request.POST.get('premiums_1')
        premiums_2 = request.POST.get('premiums_2')
        interest_received_1 = request.POST.get('interest_received_1')
        interest_received_2 = request.POST.get('interest_received_2')
        other_income_1 = request.POST.get('other_income_1')
        other_income_2 = request.POST.get('other_income_2')
        total_income_1 = request.POST.get('total_income_1')
        total_income_2 = request.POST.get('total_income_2')
        interest_paid_1 = request.POST.get('interest_paid_1')
        interest_paid_2 = request.POST.get('interest_paid_2')
        claims_paid_1 = request.POST.get('claims_paid_1')
        claims_paid_2 = request.POST.get('claims_paid_2')
        other_expenditures_1 = request.POST.get('other_expenditures_1')
        other_expenditures_2 = request.POST.get('other_expenditures_2')
        total_expenditures_1 = request.POST.get('total_expenditures_1')
        total_expenditures_2 = request.POST.get('total_expenditures_2')
        net_profit_loss_1 = request.POST.get('net_profit_loss_1')
        net_profit_loss_2 = request.POST.get('net_profit_loss_2')
        initial_inventory_1 = request.POST.get('initial_inventory_1')
        initial_inventory_2 = request.POST.get('initial_inventory_2')
        final_inventory_1 = request.POST.get('final_inventory_1')
        final_inventory_2 = request.POST.get('final_inventory_2')
        signature = request.POST.get('signature')
        rank = request.POST.get('rank')


        csv_file_path = 'data/cuestionarios/ingreso_neto/JP-560-63111.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(["ssn", "tel", "fax", "sales_1", "sales_2", "premiums_1", "premiums_2", "interest_received_1",
                                 "interest_received_2", "other_income_1", "other_income_2", "total_income_1", "total_income_2",
                                "interest_paid_1", "interest_paid_2", "claims_paid_1", "claims_paid_2", "other_expenditures_1",
                                "other_expenditures_2", "total_expenditures_1", "total_expenditures_2", "net_profit_loss_1",
                                "net_profit_loss_2", "initial_inventory_1", "initial_inventory_2", "final_inventory_1", "final_inventory_2",
                                "signature", "rank"])
                
            writer.writerow([
                            ssn, tel, fax, sales_1, sales_2, premiums_1, premiums_2, interest_received_1, interest_received_2,
                            other_income_1, other_income_2, total_income_1, total_income_2, interest_paid_1, interest_paid_2,
                            claims_paid_1, claims_paid_2, other_expenditures_1, other_expenditures_2, total_expenditures_1,
                            total_expenditures_2, net_profit_loss_1, net_profit_loss_2, initial_inventory_1, initial_inventory_2,
                            final_inventory_1, final_inventory_2, signature, rank
                            ])
            
        return render(request, "cuestionarios/succesfull.html")

    return render(request, "cuestionarios/ingreso_neto/JP-560-63111.html")

def IP_230(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        liaison_officer = request.POST.get('liaison_officer')
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        legal_form = request.POST.get('legal_form')
        cfc = request.POST.get('cfc')
        business_function = request.POST.get('business_function')
        closing_date = request.POST.get('closing_date')
        income_project_A_12 = request.POST.get('income_project_A_12')
        income_project_A_13 = request.POST.get('income_project_A_13')
        people_A_12 = request.POST.get('people_A_12')
        people_A_13 = request.POST.get('people_A_13')
        industries_businesses_A_12 = request.POST.get('industries_businesses_A_12')
        industries_businesses_A_13 = request.POST.get('industries_businesses_A_13')
        direct_indirect_B_12 = request.POST.get('direct_indirect_B_12')
        direct_indirect_B_13 = request.POST.get('direct_indirect_B_13')
        direct_christmas_vacation_B_12 = request.POST.get('direct_christmas_vacation_B_12')
        direct_christmas_vacation_B_13 = request.POST.get('direct_christmas_vacation_B_13')
        rent_land_building_B_12 = request.POST.get('rent_land_building_B_12')
        rent_land_building_B_13 = request.POST.get('rent_land_building_B_13')
        rent_equipment_B_12 = request.POST.get('rent_equipment_B_12')
        rent_equipment_B_13 = request.POST.get('rent_equipment_B_13')
        depreciation_B_12 = request.POST.get('depreciation_B_12')
        depreciation_B_13 = request.POST.get('depreciation_B_13')
        sales_tax_B_12 = request.POST.get('sales_tax_B_12')
        sales_tax_B_13 = request.POST.get('sales_tax_B_13')
        purchases_machinery_equipment_B_12 = request.POST.get('purchases_machinery_equipment_B_12')
        purchases_machinery_equipment_B_13 = request.POST.get('purchases_machinery_equipment_B_13')
        other_purchases_B_12 = request.POST.get('other_purchases_B_12')
        other_purchases_B_13 = request.POST.get('other_purchases_B_13')
        licenses_patent_B_12 = request.POST.get('licenses_patent_B_12')
        licenses_patent_B_13 = request.POST.get('licenses_patent_B_13')
        other_costs_direct_indirect_B_12 = request.POST.get('other_costs_direct_indirect_B_12')
        other_costs_direct_indirect_B_13 = request.POST.get('other_costs_direct_indirect_B_13')
        gross_profit_C_12 = request.POST.get('gross_profit_C_12')
        gross_profit_C_13 = request.POST.get('gross_profit_C_13')
        other_income_D_12 = request.POST.get('other_income_D_12')
        other_income_D_13 = request.POST.get('other_income_D_13')
        interest_D_12 = request.POST.get('interest_D_12')
        interest_D_13 = request.POST.get('interest_D_13')
        rent_land_building_D_12 = request.POST.get('rent_land_building_D_12')
        rent_land_building_D_13 = request.POST.get('rent_land_building_D_13')
        gain_loss_D_12 = request.POST.get('gain_loss_D_12')
        gain_loss_D_13 = request.POST.get('gain_loss_D_13')
        other_D_12 = request.POST.get('other_D_12')
        other_D_13 = request.POST.get('other_D_13')
        gross_profit_E_12 = request.POST.get('gross_profit_E_12')
        gross_profit_E_13 = request.POST.get('gross_profit_E_13')
        administrative_F_12 = request.POST.get('administrative_F_12')
        administrative_F_13 = request.POST.get('administrative_F_13')
        salaries_wages_bonus_commissions_F_12 = request.POST.get('salaries_wages_bonus_commissions_F_12')
        salaries_wages_bonus_commissions_F_13 = request.POST.get('salaries_wages_bonus_commissions_F_13')
        interest_F_12 = request.POST.get('interest_F_12')
        interest_F_13 = request.POST.get('interest_F_13')
        rent_land_building_F_12 = request.POST.get('rent_land_building_F_12')
        rent_land_building_F_13 = request.POST.get('rent_land_building_F_13')
        depreciation_F_12 = request.POST.get('depreciation_F_12')
        depreciation_F_13 = request.POST.get('depreciation_F_13')
        bad_depts_F_12 = request.POST.get('bad_depts_F_12')
        bad_depts_F_13 = request.POST.get('bad_depts_F_13')
        donation_F_12 = request.POST.get('donation_F_12')
        donation_F_13 = request.POST.get('donation_F_13')
        other_expenses_F_12 = request.POST.get('other_expenses_F_12')
        other_expenses_F_13 = request.POST.get('other_expenses_F_13')
        net_profit_G_12 = request.POST.get('net_profit_G_12')
        net_profit_G_13 = request.POST.get('net_profit_G_13')
        income_tax_G_12 = request.POST.get('income_tax_G_12')
        income_tax_G_13 = request.POST.get('income_tax_G_13')
        profit_after_tax_G_12 = request.POST.get('profit_after_tax_G_12')
        profit_after_tax_G_13 = request.POST.get('profit_after_tax_G_13')
        sales_tax_H_12 = request.POST.get('sales_tax_H_12')
        sales_tax_H_13 = request.POST.get('sales_tax_H_13')
        biginning_year_HA = request.POST.get('biginning_year_HA')
        end_year_HB = request.POST.get('end_year_HB')
        biginning_year_HC = request.POST.get('biginning_year_HC') 
        end_year_HD = request.POST.get('end_year_HD') 
        signature = request.POST.get('signature')
        rank = request.POST.get('rank')

        csv_file_path = 'data/cuestionarios/ingreso_neto/IP-230.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow([
                                "company_name","address","email","liaison_officer","ssn","tel","fax","legal_form",
                                "cfc","business_function","closing_date","income_project_A_12","income_project_A_13",
                                "people_A_12","people_A_13","industries_businesses_A_12","industries_businesses_A_13",
                                "direct_indirect_B_12","direct_indirect_B_13","direct_christmas_vacation_B_12",
                                "direct_christmas_vacation_B_13","rent_land_building_B_12","rent_land_building_B_13",
                                "rent_equipment_B_12","rent_equipment_B_13","depreciation_B_12","depreciation_B_13",
                                "sales_tax_B_12","sales_tax_B_13","purchases_machinery_equipment_B_12",
                                "purchases_machinery_equipment_B_13","other_purchases_B_12","other_purchases_B_13",
                                "licenses_patent_B_12","licenses_patent_B_13","other_costs_direct_indirect_B_12",
                                "other_costs_direct_indirect_B_13","gross_profit_C_12","gross_profit_C_13",
                                "other_income_D_12","other_income_D_13","interest_D_12","interest_D_13",
                                "rent_land_building_D_12","rent_land_building_D_13","gain_loss_D_12","gain_loss_D_13",
                                "other_D_12","other_D_13","gross_profit_E_12","gross_profit_E_13","administrative_F_12",
                                "administrative_F_13","salaries_wages_bonus_commissions_F_12","salaries_wages_bonus_commissions_F_13",
                                "interest_F_12","interest_F_13","rent_land_building_F_12","rent_land_building_F_13",
                                "depreciation_F_12","depreciation_F_13","bad_depts_F_12","bad_depts_F_13",
                                "donation_F_12","donation_F_13","other_expenses_F_12","other_expenses_F_13",
                                "net_profit_G_12","net_profit_G_13","income_tax_G_12","income_tax_G_13",
                                "profit_after_tax_G_12","profit_after_tax_G_13","sales_tax_H_12","sales_tax_H_13",
                                "biginning_year_HA","end_year_HB","biginning_year_HC","end_year_HD","signature","rank"
                                ])
                
            writer.writerow([
                            company_name, address, email, liaison_officer, ssn, tel, fax, legal_form,
                            cfc, business_function, closing_date, income_project_A_12, income_project_A_13,
                            people_A_12, people_A_13, industries_businesses_A_12, industries_businesses_A_13,
                            direct_indirect_B_12, direct_indirect_B_13, direct_christmas_vacation_B_12,
                            direct_christmas_vacation_B_13, rent_land_building_B_12, rent_land_building_B_13,
                            rent_equipment_B_12, rent_equipment_B_13, depreciation_B_12, depreciation_B_13,
                            sales_tax_B_12, sales_tax_B_13, purchases_machinery_equipment_B_12,
                            purchases_machinery_equipment_B_13, other_purchases_B_12, other_purchases_B_13,
                            licenses_patent_B_12, licenses_patent_B_13, other_costs_direct_indirect_B_12,
                            other_costs_direct_indirect_B_13, gross_profit_C_12, gross_profit_C_13,
                            other_income_D_12, other_income_D_13, interest_D_12, interest_D_13,
                            rent_land_building_D_12, rent_land_building_D_13, gain_loss_D_12, gain_loss_D_13,
                            other_D_12, other_D_13, gross_profit_E_12, gross_profit_E_13, administrative_F_12,
                            administrative_F_13, salaries_wages_bonus_commissions_F_12, salaries_wages_bonus_commissions_F_13,
                            interest_F_12, interest_F_13, rent_land_building_F_12, rent_land_building_F_13,
                            depreciation_F_12, depreciation_F_13, bad_depts_F_12, bad_depts_F_13,
                            donation_F_12, donation_F_13, other_expenses_F_12, other_expenses_F_13,
                            net_profit_G_12, net_profit_G_13, income_tax_G_12, income_tax_G_13,
                            profit_after_tax_G_12, profit_after_tax_G_13, sales_tax_H_12, sales_tax_H_13,
                            biginning_year_HA, end_year_HB, biginning_year_HC, end_year_HD, signature, rank
                            ])
            
        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/ingreso_neto/IP-230.html")

def JP_560_63210(request):
    if request.method == "POST":
        # Retrieve form data
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        sales_1 = request.POST.get('sales_1') 
        sales_2 = request.POST.get('sales_2')
        premiums_1 = request.POST.get('premiums_1')
        premiums_2 = request.POST.get('premiums_2')
        disability_A_1 = request.POST.get('disability_A_1') 
        disability_A_2 = request.POST.get('disability_A_2')
        cars_A_1 = request.POST.get('cars_A_1')
        cars_A_2 = request.POST.get('cars_A_2')
        other_A_1 = request.POST.get('other_A_1')
        other_A_2 = request.POST.get('other_A_2')
        interest_received_1 = request.POST.get('interest_received_1')
        interest_received_2 = request.POST.get('interest_received_2')
        other_income_1 = request.POST.get('other_income_1')
        other_income_2 = request.POST.get('other_income_2')
        total_income_1 = request.POST.get('total_income_1')
        total_income_2 = request.POST.get('total_income_2')
        interest_paid_1 = request.POST.get('interest_paid_1')
        interest_paid_2 = request.POST.get('interest_paid_2')
        claims_paid_1 = request.POST.get('claims_paid_1')
        claims_paid_2 = request.POST.get('claims_paid_2')
        disability_B_1 = request.POST.get('disability_B_1')
        disability_B_2 = request.POST.get('disability_B_2')
        cars_B_1 = request.POST.get('cars_B_1')
        cars_B_2 = request.POST.get('cars_B_2')
        other_B_1 = request.POST.get('other_B_1')
        other_B_2 = request.POST.get('other_B_2')
        other_expenditures_1 = request.POST.get('other_expenditures_1')
        other_expenditures_2 = request.POST.get('other_expenditures_2')
        total_expenditures_1 = request.POST.get('total_expenditures_1')
        total_expenditures_2 = request.POST.get('total_expenditures_2')
        net_profit_loss_1 = request.POST.get('net_profit_loss_1')
        net_profit_loss_2 = request.POST.get('net_profit_loss_2')
        initial_inventory_1 = request.POST.get('initial_inventory_1')
        initial_inventory_2 = request.POST.get('initial_inventory_2')
        final_inventory_1 = request.POST.get('final_inventory_1')
        final_inventory_2 = request.POST.get('final_inventory_2')
        signature = request.POST.get('signature')
        rank = request.POST.get('rank')

        csv_file_path = 'data/cuestionarios/ingreso_neto/JP-560-63210.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow([
                                "ssn","tel","fax","sales_1","sales_2","premiums_1","premiums_2","disability_A_1",
                                "disability_A_2","cars_A_1","cars_A_2","other_A_1","other_A_2","interest_received_1",
                                "interest_received_2","other_income_1","other_income_2","total_income_1","total_income_2",
                                "interest_paid_1","interest_paid_2","claims_paid_1","claims_paid_2","disability_B_1",
                                "disability_B_2","cars_B_1","cars_B_2","other_B_1","other_B_2","other_expenditures_1",
                                "other_expenditures_2","total_expenditures_1","total_expenditures_2","net_profit_loss_1",
                                "net_profit_loss_2","initial_inventory_1","initial_inventory_2","final_inventory_1",
                                "final_inventory_2","signature","rank"
                                ])
                
            writer.writerow([
                            ssn, tel, fax, sales_1, sales_2, premiums_1, premiums_2, disability_A_1,
                            disability_A_2, cars_A_1, cars_A_2, other_A_1, other_A_2, interest_received_1,
                            interest_received_2, other_income_1, other_income_2, total_income_1, total_income_2,
                            interest_paid_1, interest_paid_2, claims_paid_1, claims_paid_2, disability_B_1,
                            disability_B_2, cars_B_1, cars_B_2, other_B_1, other_B_2, other_expenditures_1,
                            other_expenditures_2, total_expenditures_1, total_expenditures_2, net_profit_loss_1,
                            net_profit_loss_2, initial_inventory_1, initial_inventory_2, final_inventory_1,
                            final_inventory_2, signature, rank
                            ])
            
        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/ingreso_neto/JP-560-63210.html")

def JP_560_2(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        liaison_officer = request.POST.get('liaison_officer')
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        sales_1 = request.POST.get('sales_1')
        sales_2 = request.POST.get('sales_2')
        interest_received_1 = request.POST.get('interest_received_1')
        interest_received_2 = request.POST.get('interest_received_2')
        other_income_1 = request.POST.get('other_income_1')
        other_income_2 = request.POST.get('other_income_2')
        total_income_1 = request.POST.get('total_income_1')
        total_income_2 = request.POST.get('total_income_2')
        interest_paid_1 = request.POST.get('interest_paid_1')
        interest_paid_2 = request.POST.get('interest_paid_2')
        other_expenditures_1_1 = request.POST.get('other_expenditures_1_1')
        other_expenditures_2_1 = request.POST.get('other_expenditures_1_2')
        other_expenditures_1_2 = request.POST.get('other_expenditures_2_1')
        other_expenditures_2_2 = request.POST.get('other_expenditures_2_2')
        net_profit_loss_1 = request.POST.get('net_profit_loss_1')
        net_profit_loss_2 = request.POST.get('net_profit_loss_2')
        initial_inventory_1 = request.POST.get('initial_inventory_1')
        initial_inventory_2 = request.POST.get('initial_inventory_2')
        final_inventory_1 = request.POST.get('final_inventory_1')
        final_inventory_2 = request.POST.get('final_inventory_2')
        signature = request.POST.get('signature')
        rank = request.POST.get('rank')


        csv_file_path = 'data/cuestionarios/ingreso_neto/JP-560-2.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(["company_name", "address", "email", "liaison_officer", 
                                "ssn", "tel", "fax", "sales_1", "sales_2", "interest_received_1", 
                                "interest_received_2", "other_income_1", "other_income_2", "total_income_1", 
                                "total_income_2", "interest_paid_1", "interest_paid_2", "other_expenditures_1_1",
                                "other_expenditures_2_1", "other_expenditures_1_2", "other_expenditures_2_2",
                                "net_profit_loss_1", "net_profit_loss_2", "initial_inventory_1", "initial_inventory_2",
                                "final_inventory_1", "final_inventory_2", "signature", "rank"
                                ])
                
            writer.writerow([company_name, address, email, liaison_officer, ssn, tel, fax, sales_1, sales_2, interest_received_1,
                            interest_received_2, other_income_1, other_income_2, total_income_1, total_income_2, interest_paid_1,
                            interest_paid_2, other_expenditures_1_1, other_expenditures_2_1, other_expenditures_1_2,
                            other_expenditures_2_2, net_profit_loss_1, net_profit_loss_2, initial_inventory_1, initial_inventory_2,
                            final_inventory_1, final_inventory_2, signature, rank
                            ])
            
        return render(request, "cuestionarios/succesfull.html")

    return render(request, "cuestionarios/ingreso_neto/JP-560-2.html")

def JP_375(request):
    if request.method == "POST":
        # Retrieve form data
        year_1 = request.POST.get('year_1')
        year_2 = request.POST.get('year_2')
        year_3 = request.POST.get('year_3')
        
        FHA_1 = request.POST.get('FHA_1')
        FHA_2 = request.POST.get('FHA_2')
        FHA_3 = request.POST.get('FHA_3')
        
        veteran_1 = request.POST.get('veteran_1')
        veteran_2 = request.POST.get('veteran_2')
        veteran_3 = request.POST.get('veteran_3')
        
        bank_1 = request.POST.get('bank_1')
        bank_2 = request.POST.get('bank_2')
        bank_3 = request.POST.get('bank_3')
        
        conventional_1 = request.POST.get('conventional_1')
        conventional_2 = request.POST.get('conventional_2')
        conventional_3 = request.POST.get('conventional_3')
        
        other_1 = request.POST.get('other_1')
        other_2 = request.POST.get('other_2')
        other_3 = request.POST.get('other_3')
        
        FHA_2_1  = request.POST.get('FHA_2_1')
        FHA_2_2  = request.POST.get('FHA_2_2')
        FHA_2_3  = request.POST.get('FHA_2_3')
        
        veteran_2_1 = request.POST.get('veteran_2_1')
        veteran_2_2 = request.POST.get('veteran_2_2')
        veteran_2_3 = request.POST.get('veteran_2_3')
        
        conventional_2_1 = request.POST.get('conventional_2_1')
        conventional_2_2 = request.POST.get('conventional_2_2')
        conventional_2_3 = request.POST.get('conventional_2_3')
        
        others_2_1 = request.POST.get('others_2_1')
        others_2_2 = request.POST.get('others_2_2')
        others_2_3 = request.POST.get('others_2_3')
        
        FHA_3_1 = request.POST.get('FHA_3_1')
        FHA_3_2 = request.POST.get('FHA_3_2')
        FHA_3_3 = request.POST.get('FHA_3_3')
        
        veteran_3_1 = request.POST.get('veteran_3_1')
        veteran_3_2 = request.POST.get('veteran_3_2')
        veteran_3_3 = request.POST.get('veteran_3_3')
        
        bank_2_1 = request.POST.get('bank_2_1')
        bank_2_2 = request.POST.get('bank_2_2')
        bank_2_3 = request.POST.get('bank_2_3')
        
        conventional_3_1 = request.POST.get('conventional_3_1')
        conventional_3_2 = request.POST.get('conventional_3_2')
        conventional_3_3 = request.POST.get('conventional_3_3')
        
        others_3_1 = request.POST.get('others_3_1')
        others_3_2 = request.POST.get('others_3_2')
        others_3_3 = request.POST.get('others_3_3')
        
        FHA_4_1 = request.POST.get('FHA_4_1')
        FHA_4_2 = request.POST.get('FHA_4_2')
        FHA_4_3 = request.POST.get('FHA_4_3')
        
        veteran_4_1 = request.POST.get('veteran_4_1')
        veteran_4_2 = request.POST.get('veteran_4_2')
        veteran_4_3 = request.POST.get('veteran_4_3')
        
        conventional_4_1 = request.POST.get('conventional_4_1')
        conventional_4_2 = request.POST.get('conventional_4_2')
        conventional_4_3 = request.POST.get('conventional_4_3')
        
        others_4_1 = request.POST.get('others_4_1')
        others_4_2 = request.POST.get('others_4_2')
        others_4_3 = request.POST.get('others_4_3')
        
        commissions_1 = request.POST.get('commissions_1')
        commissions_2 = request.POST.get('commissions_2')
        commissions_3 = request.POST.get('commissions_3')
        
        phone = request.POST.get('phone')
        signature = request.POST.get('signature')
        position = request.POST.get('position')
        

        csv_file_path = 'data/cuestionarios/balanza_de_pagos/JP-375.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['year_1', 'year_2', 'year_3','FHA_1', 'FHA_2', 'FHA_3', 'veteran_1', 'veteran_2', 'veteran_3', 'bank_1', 'bank_2', 'bank_3',
                                'conventional_1', 'conventional_2', 'conventional_3', 'other_1', 'other_2', 'other_3',
                                'FHA_2_1', 'FHA_2_2', 'FHA_2_3', 'veteran_2_1', 'veteran_2_2', 'veteran_2_3', 'conventional_2_1',
                                'conventional_2_2', 'conventional_2_3', 'others_2_1', 'others_2_2', 'others_2_3', 'FHA_3_1',
                                'FHA_3_2', 'FHA_3_3', 'veteran_3_1', 'veteran_3_2', 'veteran_3_3', 'bank_2_1', 'bank_2_2',
                                'bank_2_3', 'conventional_3_1', 'conventional_3_2', 'conventional_3_3', 'others_3_1',
                                'others_3_2', 'others_3_3', 'FHA_4_1', 'FHA_4_2', 'FHA_4_3', 'veteran_4_1', 'veteran_4_2',
                                'veteran_4_3', 'conventional_4_1', 'conventional_4_2', 'conventional_4_3', 'others_4_1',
                                'others_4_2', 'others_4_3', 'commissions_1', 'commissions_2', 'commissions_3',
                                'phone', 'signature', 'position'
                                ])
                
            writer.writerow([year_1, year_2, year_3, FHA_1, FHA_2, FHA_3, veteran_1, veteran_2, veteran_3, bank_1, bank_2, bank_3,
                            conventional_1, conventional_2, conventional_3, other_1, other_2, other_3,
                            FHA_2_1, FHA_2_2, FHA_2_3, veteran_2_1, veteran_2_2, veteran_2_3, conventional_2_1,
                            conventional_2_2, conventional_2_3, others_2_1, others_2_2, others_2_3, FHA_3_1,
                            FHA_3_2, FHA_3_3, veteran_3_1, veteran_3_2, veteran_3_3, bank_2_1, bank_2_2,
                            bank_2_3, conventional_3_1, conventional_3_2, conventional_3_3, others_3_1,
                            others_3_2, others_3_3, FHA_4_1, FHA_4_2, FHA_4_3, veteran_4_1, veteran_4_2,
                            veteran_4_3, conventional_4_1, conventional_4_2, conventional_4_3, others_4_1,
                            others_4_2, others_4_3, commissions_1, commissions_2, commissions_3,
                            phone, signature, position
                            ])
            
        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/balanza_de_pagos/JP-375.html")

def IP_480(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        liaison_officer = request.POST.get('liaison_officer')
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        legal_form = request.POST.get('legal_form')
        cfc = request.POST.get('cfc')
        business_function = request.POST.get('business_function')
        closing_date = request.POST.get('closing_date')
        operation_incomes_1 = request.POST.get('operation_incomes_1')
        operation_incomes_2 = request.POST.get('operation_incomes_2')
        people_A_1 = request.POST.get('people_A_1')
        people_A_2 = request.POST.get('people_A_2')
        industries_businesses_A_1 = request.POST.get('industries_businesses_A_1')
        industries_businesses_A_2 = request.POST.get('industries_businesses_A_2')
        incomes_interests_1 = request.POST.get('incomes_interests_1')
        incomes_interests_2 = request.POST.get('incomes_interests_2')
        incomes_rents_1 = request.POST.get('incomes_rents_1')
        incomes_rents_2 = request.POST.get('incomes_rents_2')
        dividends_1 = request.POST.get('dividends_1')
        dividends_2 = request.POST.get('dividends_2')
        others_incomes_1 = request.POST.get('others_incomes_1')
        others_incomes_2 = request.POST.get('others_incomes_2')
        total_incomes_1 = request.POST.get('total_incomes_1')
        total_incomes_2 = request.POST.get('total_incomes_2')
        expenses_1 = request.POST.get('expenses_1')
        expenses_2 = request.POST.get('expenses_2')
        salaries_1 = request.POST.get('salaries_1')
        salaries_2 = request.POST.get('salaries_2')
        expenses_interests_1 = request.POST.get('expenses_interests_1')
        expenses_interests_2 = request.POST.get('expenses_interests_2')
        expenses_rents_1 = request.POST.get('expenses_rents_1')
        expenses_rents_2 = request.POST.get('expenses_rents_2')
        depreciation_1 = request.POST.get('depreciation_1')
        depreciation_2 = request.POST.get('depreciation_2')
        donations_1 = request.POST.get('donations_1')
        donations_2 = request.POST.get('donations_2')
        sales_tax_1 = request.POST.get('sales_tax_1')
        sales_tax_2 = request.POST.get('sales_tax_2')
        machinery_1 = request.POST.get('machinery_1')
        machinery_2 = request.POST.get('machinery_2')
        other_purchases_1 = request.POST.get('other_purchases_1')
        other_purchases_2 = request.POST.get('other_purchases_2')
        licenses_1 = request.POST.get('licenses_1')
        licenses_2 = request.POST.get('licenses_2')
        other_expenses_1 = request.POST.get('other_expenses_1')
        other_expenses_2 = request.POST.get('other_expenses_2')
        total_expenses_1 = request.POST.get('total_expenses_1')
        total_expenses_2 = request.POST.get('total_expenses_2')
        net_profit_1 = request.POST.get('net_profit_1')
        net_profit_2 = request.POST.get('net_profit_2')
        income_tax_1 = request.POST.get('income_tax_1')
        income_tax_2 = request.POST.get('income_tax_2')
        profit_after_tax_1 = request.POST.get('profit_after_tax_1')
        profit_after_tax_2 = request.POST.get('profit_after_tax_2')
        withheld_tax_1 = request.POST.get('withheld_tax_1')
        withheld_tax_2 = request.POST.get('withheld_tax_2')
        signature = request.POST.get('signature')
        rank = request.POST.get('rank')

        csv_file_path = 'data/cuestionarios/ingreso_neto/IP-480.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow([
                                "company_name","address","email","liaison_officer","ssn","tel","fax","legal_form",
                                "cfc","business_function","closing_date","operation_incomes_1","operation_incomes_2",
                                "people_A_1","people_A_2","industries_businesses_A_1","industries_businesses_A_2",
                                "incomes_interests_1","incomes_interests_2","incomes_rents_1","incomes_rents_2",
                                "dividends_1","dividends_2","others_incomes_1","others_incomes_2","total_incomes_1",
                                "total_incomes_2","expenses_1","expenses_2","salaries_1","salaries_2",
                                "expenses_interests_1","expenses_interests_2","expenses_rents_1","expenses_rents_2",
                                "depreciation_1","depreciation_2","donations_1","donations_2","sales_tax_1",
                                "sales_tax_2","machinery_1","machinery_2","other_purchases_1","other_purchases_2",
                                "licenses_1","licenses_2","other_expenses_1","other_expenses_2","total_expenses_1",
                                "total_expenses_2","net_profit_1","net_profit_2","income_tax_1","income_tax_2",
                                "profit_after_tax_1","profit_after_tax_2","withheld_tax_1","withheld_tax_2","signature","rank"
                                ])
                
            writer.writerow([
                            company_name, address, email, liaison_officer, ssn, tel, fax, legal_form,
                            cfc, business_function, closing_date, operation_incomes_1, operation_incomes_2,
                            people_A_1, people_A_2, industries_businesses_A_1, industries_businesses_A_2,
                            incomes_interests_1, incomes_interests_2, incomes_rents_1, incomes_rents_2,
                            dividends_1, dividends_2, others_incomes_1, others_incomes_2, total_incomes_1,
                            total_incomes_2, expenses_1, expenses_2, salaries_1, salaries_2,
                            expenses_interests_1, expenses_interests_2, expenses_rents_1, expenses_rents_2,
                            depreciation_1, depreciation_2, donations_1, donations_2, sales_tax_1,
                            sales_tax_2, machinery_1, machinery_2, other_purchases_1, other_purchases_2,
                            licenses_1, licenses_2, other_expenses_1, other_expenses_2, total_expenses_1,
                            total_expenses_2, net_profit_1, net_profit_2, income_tax_1, income_tax_2,
                            profit_after_tax_1, profit_after_tax_2, withheld_tax_1, withheld_tax_2, signature, rank
                            ])
            
        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/ingreso_neto/IP-480.html")


def IP_420(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        liaison_officer = request.POST.get('liaison_officer')
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        legal_form = request.POST.get('legal_form')
        cfc = request.POST.get('cfc')
        main_line = request.POST.get('main_line')
        business_type = request.POST.get('business_type')
        accounting_period = request.POST.get('accounting_period')
        
        sales_A_1 = request.POST.get('sales_A_1')
        sales_A_2 = request.POST.get('sales_A_2')
        
        people_A_1 = request.POST.get('people_A_1')
        people_A_2 = request.POST.get('people_A_2')
        
        industries_businesses_A_1 = request.POST.get('industries_businesses_A_1')
        industries_businesses_A_2 = request.POST.get('industries_businesses_A_2')
        
        less_cost_A_1 = request.POST.get('less_cost_A_1')
        less_cost_A_2 = request.POST.get('less_cost_A_2')
        
        inventory_beginning_1 = request.POST.get('inventory_beginning_1')
        inventory_beginning_2 = request.POST.get('inventory_beginning_2')
        
        purchases_A_1 = request.POST.get('purchases_A_1')
        purchases_A_2 = request.POST.get('purchases_A_2')
        
        inventory_end_1 = request.POST.get('inventory_end_1')
        inventory_end_2 = request.POST.get('inventory_end_2')
        
        gross_profit_A_1 = request.POST.get('gross_profit_A_1')
        gross_profit_A_2 = request.POST.get('gross_profit_A_2')
        
        other_income_A_1 = request.POST.get('other_income_A_1')
        other_income_A_2 = request.POST.get('other_income_A_2')
        
        interests_A_1 = request.POST.get('interests_A_1')
        interests_A_2 = request.POST.get('interests_A_2')
        
        rent_A_1 = request.POST.get('rent_A_1')
        rent_A_2 = request.POST.get('rent_A_2')
        
        capital_gain_A_1 = request.POST.get('capital_gain_A_1')
        capital_gain_A_2 = request.POST.get('capital_gain_A_2')
        
        dividends_A_1 = request.POST.get('dividends_A_1')
        dividends_A_2 = request.POST.get('dividends_A_2')
        
        total_gross_A_1 = request.POST.get('total_gross_A_1')
        total_gross_A_2 = request.POST.get('total_gross_A_2')
        
        cost_B_1 = request.POST.get('cost_B_1')
        cost_B_2 = request.POST.get('cost_B_2')
        
        salaries_B_1 = request.POST.get('salaries_B_1')
        salaries_B_2 = request.POST.get('salaries_B_2')
        
        interests_B_1 = request.POST.get('interests_B_1')
        interests_B_2 = request.POST.get('interests_B_2')
        
        depreciation_B_1 = request.POST.get('depreciation_B_1')
        depreciation_B_2 = request.POST.get('depreciation_B_2')
        
        rent_B_1 = request.POST.get('rent_B_1')
        rent_B_2 = request.POST.get('rent_B_2')
        
        bad_debts_B_1 = request.POST.get('bad_debts_B_1')
        bad_debts_B_2 = request.POST.get('bad_debts_B_2')
        
        donations_B_1 = request.POST.get('donations_B_1')
        donations_B_2 = request.POST.get('donations_B_2')
        
        sales_B_1 = request.POST.get('sales_B_1')
        sales_B_2 = request.POST.get('sales_B_2')
        
        purchases_B_1 = request.POST.get('purchases_B_1')
        purchases_B_2 = request.POST.get('purchases_B_2')
        
        other_purchases_B_1 = request.POST.get('other_purchases_B_1')
        other_purchases_B_2 = request.POST.get('other_purchases_B_2')
        
        licenses_B_1 = request.POST.get('licenses_B_1')
        licenses_B_2 = request.POST.get('licenses_B_2')
        
        other_operations_B_1 = request.POST.get('other_operations_B_1')
        other_operations_B_2 = request.POST.get('other_operations_B_2')
        
        gross_profit_C_1 = request.POST.get('gross_profit_C_1')
        gross_profit_C_2 = request.POST.get('gross_profit_C_2')
        
        income_C_1 = request.POST.get('income_C_1')
        income_C_2 = request.POST.get('income_C_2')
        
        profit_C_after_1 = request.POST.get('profit_C_after_1')
        profit_C_after_2 = request.POST.get('profit_C_after_2')
        
        sales_D_1 = request.POST.get('sales_D_1')
        sales_D_2 = request.POST.get('sales_D_2')
        
        name = request.POST.get('name')
        rank = request.POST.get('rank')
        
        
        csv_file_path = 'data/cuestionarios/ingreso_neto/IP_420.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['company_name','address','email','liaison_officer','ssn','tel','fax',
                                'legal_form','cfc', 'main_line','business_type','accounting_period',
                                'sales_A_1','sales_A_2','people_A_1','people_A_2','industries_businesses_A_1',
                                'industries_businesses_A_2','less_cost_A_1','less_cost_A_2','inventory_beginning_1',
                                'inventory_beginning_2','purchases_A_1','purchases_A_2','inventory_end_1',
                                'inventory_end_2','gross_profit_A_1','gross_profit_A_2','other_income_A_1',
                                'other_income_A_2','interests_A_1','interests_A_2','rent_A_1','rent_A_2',
                                'capital_gain_A_1','capital_gain_A_2','dividends_A_1','dividends_A_2',
                                'total_gross_A_1','total_gross_A_2','cost_B_1', 'cost_B_1','salaries_B_1','salaries_B_2',
                                'interests_B_1','interests_B_2','depreciation_B_1','depreciation_B_2',
                                'rent_B_1','rent_B_2','bad_debts_B_1','bad_debts_B_2','donations_B_1',
                                'donations_B_2','sales_B_1','sales_B_2','purchases_B_1','purchases_B_2',
                                'other_purchases_B_1','other_purchases_B_2','licenses_B_1','licenses_B_2',
                                'other_operations_B_1','other_operations_B_2','gross_profit_C_1','gross_profit_C_1','income_C_1',
                                'income_C_2','profit_C_after_1','profit_C_after_2','sales_D_1', 'sales_D_1', 'name','rank'
                                ])
            
            writer.writerow([company_name, address, email, liaison_officer, 
                            ssn, tel, fax, legal_form, cfc, main_line, business_type,
                            accounting_period, sales_A_1, sales_A_2, people_A_1,
                            people_A_2, industries_businesses_A_1, industries_businesses_A_2, less_cost_A_1,
                            less_cost_A_2, inventory_beginning_1, inventory_beginning_2, purchases_A_1,
                            purchases_A_2, inventory_end_1, inventory_end_2, gross_profit_A_1, gross_profit_A_2,
                            other_income_A_1, other_income_A_2, interests_A_1, interests_A_2, rent_A_1,
                            rent_A_2, capital_gain_A_1, capital_gain_A_2, dividends_A_1, dividends_A_2,
                            total_gross_A_1, total_gross_A_2, cost_B_1, cost_B_2, salaries_B_1, salaries_B_2,
                            interests_B_1, interests_B_2, depreciation_B_1, depreciation_B_2, rent_B_1,
                            rent_B_2, bad_debts_B_1, bad_debts_B_2, donations_B_1, donations_B_2,
                            sales_B_1, sales_B_2, purchases_B_1, purchases_B_2, other_purchases_B_1,
                            other_purchases_B_2, licenses_B_1, licenses_B_2, other_operations_B_1,
                            other_operations_B_2, gross_profit_C_1, gross_profit_C_2, income_C_1, income_C_2, profit_C_after_1,
                            profit_C_after_2, sales_D_1, sales_D_2, name, rank
                            ])  

        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/ingreso_neto/IP-420.html")