from django import forms
from config_ui.settings import TEMPLATES

class IP_110(forms.Form):
    company_name = forms.CharField(label='Nombre compañía / Company Name', max_length=100)
    address = forms.CharField(label='Dirección / Address', max_length=200)
    email = forms.EmailField(label='Correo electrónico / Email')
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    ssn = forms.CharField(label='Numero de Seguro Social / Social Security Number', max_length=11)
    tel = forms.CharField(label='Tel', max_length=20)
    fax = forms.CharField(label='Fax', max_length=20)
    legal_form = forms.ChoiceField(
        label='Forma legal de organización / Legal form of organization', 
        choices=[('Corporación', 'Corporación'), ('Sociedad', 'Sociedad'), ('Cooperativa', 'Cooperativa'), ('Empresa Individual', 'Empresa Individual'), ('Empresa sin fines pecuniarios', 'Empresa sin fines pecuniarios')]
    )
    cfc = forms.ChoiceField(label='CEC', choices=[('Si', 'Si'), ('No', 'No')])
    business_type = forms.CharField(label='Clase de negocio / Type of business', max_length=200)
    business_function = forms.CharField(
        label='Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity', 
        widget=forms.Textarea
    )
    branches = forms.ChoiceField(label='¿Opera sucursuales esta firma? / Do you have branch operations?', choices=[('Si', 'Si'), ('No', 'No')])
    closing_date = forms.DateField(label='Fecha de cierre de sus libros / Your accounting period closing date', widget=forms.SelectDateWidget)
    services_revenues_12 = forms.CharField(label='Ingresos por servicios - Services rendered'),
    services_revenues_13 = forms.CharField(label='Ingresos por servicios - Services rendered'),
    industries_businesses_12 = forms.CharField(label='Ingresos por industrias y negocios - From industries and businesses'),
    industries_businesses_13 = forms.CharField(label='Ingresos por industrias y negocios - From industries and businesses'),
    people_12 = forms.CharField(label='Ingresos por personas - From people'),
    people_13 = forms.CharField(label='Ingresos por personas - From people'),
    sales_12 = forms.CharField(label='2. Ventas - From sale of merchandise'),
    sales_13 = forms.CharField(label='2. Ventas - From sale of merchandise'),
    incomes_rents_12 = forms.CharField(label='3. Alquileres - From rents'),
    incomes_rents_13 = forms.CharField(label='3. Alquileres - From rents'),
    incomes_interests_12 = forms.CharField(label='4. Intereses - Interests'),
    incomes_interests_13 = forms.CharField(label='4. Intereses - Interests'),
    dividends_12 = forms.CharField(label='5. Ganancia o pérdida de capital - Capital gain or loss'),
    dividends_13 = forms.CharField(label='5. Ganancia o pérdida de capital - Capital gain or loss'),
    others_incomes_12 = forms.CharField(label='6. Otros ingresos de operación - Other operating income'),
    others_incomes_13 = forms.CharField(label='6. Otros ingresos de operación - Other operating income'),
    total_income_12 = forms.CharField(label='7. Total de ingresos - Total income'),
    total_income_13 = forms.CharField(label='7. Total de ingresos - Total income'),
    expenses_2012 = forms.CharField(label='B. Gastos - Expenses'),
    expenses_2012 = forms.CharField(label='B. Gastos - Expenses'),
    salaries_2012 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    salaries_2013 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    expenses_interests_12 = forms.CharField(label='2. Intereses - Interests'),
    expenses_interests_13 = forms.CharField(label='2. Intereses - Interests'),
    expenses_rents_12 = forms.CharField(label='3. Renta de terreno y edificio - Rent of land and building'),
    expenses_rents_13 = forms.CharField(label='3. Renta de terreno y edificio - Rent of land and building'),
    depreciation_12 = forms.CharField(label='4. Depreciación - Depreciation'),
    depreciation_13 = forms.CharField(label='4. Depreciación - Depreciation'),
    bad_debts_12 = forms.CharField(label='5. Cuentas incobrables - Bad debts'),
    bad_debts_13 = forms.CharField(label='5. Cuentas incobrables - Bad debts'),
    donations_12 = forms.CharField(label='6. Donativos - Donations'),
    donations_13 = forms.CharField(label='6. Donativos - Donations'),
    sales_tax_12 = forms.CharField(label='7. Impuesto sobre la venta y uso - sales and use tax'),
    sales_tax_13 = forms.CharField(label='7. Impuesto sobre la venta y uso - sales and use tax'),
    machinery_12 = forms.CharField(label='a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment'),
    machinery_13 = forms.CharField(label='a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment'),
    other_purchases_12 = forms.CharField(label='b. Por otras compras - On other purchases'),
    other_purchases_13 = forms.CharField(label='b. Por otras compras - On other purchases'),
    licenses_12 = forms.CharField(label='8. Licencias y patentes - Licenses and patents'),
    licenses_13 = forms.CharField(label='8. Licencias y patentes - Licenses and patents'),
    other_expenses_12 = forms.CharField(label='9. Otros gastos de operación - Other operating expenses'),
    other_expenses_13 = forms.CharField(label='9. Otros gastos de operación - Other operating expenses'),
    total_expenses_12 = forms.CharField(label='10. Total de gastos - Total expenses'),
    total_expenses_13 = forms.CharField(label='10. Total de gastos - Total expenses'),
    net_profit_12 = forms.CharField(label='C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    net_profit_13 = forms.CharField(label='C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    income_tax_12 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    income_tax_13 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    profit_after_tax_12 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    profit_after_tax_13 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    withheld_tax_12 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld'),
    withheld_tax_13 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld'),
    signature = forms.CharField(label='Nombre de persona que suministra la información - Name of person furnishing information', max_length=100)
    rank = forms.CharField(label='Rango - Title')
    

class JP_304(forms.Form):
    MONTH_CHOICES = [
        ('mes', 'mes'),
        ('enero', 'enero'),
        ('febrero', 'febrero'),
        ('marzo', 'marzo'),
        ('abril', 'abril'),
        ('mayo', 'mayo'),
        ('junio', 'junio'),
        ('julio', 'julio'),
        ('agosto', 'agosto'),
        ('septiembre', 'septiembre'),
        ('octubre', 'octubre'),
        ('noviembre', 'noviembre'),
        ('diciembre', 'diciembre'),
    ]

    start_month = forms.ChoiceField(choices=MONTH_CHOICES, required=True)
    end_month = forms.ChoiceField(choices=MONTH_CHOICES, required=True)
    year = forms.IntegerField(required=True)
    name = forms.CharField(label='Nombre / Name', max_length=100)
    direction = forms.CharField(label='Dirección / Address', max_length=200)
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    title = forms.CharField(label='Título / Title', max_length=100)
    tel = forms.CharField(label='Tel', max_length=20)
    nombre_agencia_federal = forms.CharField(label='Nombre de la agencia federal / Name of federal agency', max_length=100)
    catalogo_federal = forms.CharField(label='Número de catálogo federal / Federal catalog number', max_length=100)
    sai_federal = forms.CharField(label='Número de SAI federal / Federal SAI number', max_length=100)
    titulo_federal = forms.CharField(label='Título federal / Federal title', max_length=100)
    aportacion_aprobada_federal = forms.CharField(label='Aportación aprobada federal / Federal approved contribution', max_length=100)
    fecha_aprobacion_federal = forms.DateField(label='Fecha de aprobación federal / Federal approval date', widget=forms.SelectDateWidget)
    aportacion_recibida_federal = forms.CharField(label='Aportación recibida federal / Federal contribution received', max_length=100)
    fecha_recibo_federal = forms.DateField(label='Fecha de recibo federal / Federal receipt date', widget=forms.SelectDateWidget)
    aportacion_gastada_federal = forms.CharField(label='Aportación gastada federal / Federal contribution spent', max_length=100)
    fecha_gasto_federal = forms.DateField(label='Fecha de gasto federal / Federal spending date', widget=forms.SelectDateWidget)
    agencia_local_table_box = forms.CharField(label='Agencia local / Local agency', max_length=100)
    catalogo_local = forms.CharField(label='Número de catálogo local / Local catalog number', max_length=100)
    programa_local = forms.CharField(label='Programa local / Local program', max_length=100)
    aportacion_federal_aprobada_local = forms.CharField(label='Aportación aprobada federal local / Local federal approved contribution', max_length=100)
    fecha_aprobacion_local = forms.DateField(label='Fecha de aprobación local / Local approval date', widget=forms.SelectDateWidget)
    aportacion_federal_recibida_local = forms.CharField(label='Aportación recibida federal local / Local federal contribution received', max_length=100)
    fecha_recibo_local = forms.DateField(label='Fecha de recibo federal local / Local federal receipt date', widget=forms.SelectDateWidget)
    aportacion_federal_gastada_local = forms.CharField(label='Aportación gastada federal local / Local federal contribution spent', max_length=100)
    fecha_gasto_local = forms.DateField(label='Fecha de gasto federal local / Local federal spending date', widget=forms.SelectDateWidget)
    numero_cuenta_local = forms.CharField(label='Número de cuenta local / Local account number', max_length=100)


class JP_541(forms.Form):
    COMPANT_TYPE_CHOICES = [
        ('Corporación', 'Corporación'),
        ('Administración', 'Administración'),
    ]
    
    #TABLE 1
    form_1 = forms.CharField(label='Encuesta :', max_length=100)
    fiscal_year_1 = forms.CharField(label='Año Fiscal :', max_length=100)
    company_name_1 = forms.CharField(label='Nombre de la Empresa:', max_length=100)
    liaison_officer_1 = forms.CharField(label='Persona de Contacto:', max_length=100)
    tel_1 = forms.CharField(label='Teléfono::', max_length=100)
    project_1 = forms.CharField(label='Proyecto por::', max_length=100)
    branches_1 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)
    
    project_name_1_1 = forms.CharField(label='', max_length=100)
    city_1_1 = forms.CharField(label='', max_length=100)
    total_number_project_1_1 = forms.CharField(label='', max_length=100)
    total_cost_1_1 = forms.CharField(label='', max_length=100)
    start_date_1_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_1 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_1 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_1 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_1 = forms.CharField(label='', max_length=100)
    
    project_name_1_2 = forms.CharField(label='', max_length=100)
    city_1_2 = forms.CharField(label='', max_length=100)
    total_number_project_1_2 = forms.CharField(label='', max_length=100)
    total_cost_1_2 = forms.CharField(label='', max_length=100)
    start_date_1_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_2 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_2 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_2 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_2 = forms.CharField(label='', max_length=100)
    
    project_name_1_3 = forms.CharField(label='', max_length=100)
    city_1_3 = forms.CharField(label='', max_length=100)
    total_number_project_1_3 = forms.CharField(label='', max_length=100)
    total_cost_1_3 = forms.CharField(label='', max_length=100)
    start_date_1_3 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_3 =  forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_3 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_3 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_3 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_3 = forms.CharField(label='', max_length=100)
    
    project_name_1_4 = forms.CharField(label='', max_length=100)
    city_1_4 = forms.CharField(label='', max_length=100)
    total_number_project_1_4 = forms.CharField(label='', max_length=100)
    total_cost_1_4 = forms.CharField(label='', max_length=100)
    start_date_1_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_4 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_4 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_4 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_4 = forms.CharField(label='', max_length=100)
    
    project_name_1_5 = forms.CharField(label='', max_length=100)
    city_1_5 = forms.CharField(label='', max_length=100)
    total_number_project_1_5 = forms.CharField(label='', max_length=100)
    total_cost_1_5 = forms.CharField(label='', max_length=100)
    start_date_1_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_5 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_5 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_5 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_5 = forms.CharField(label='', max_length=100)
    
    
    project_name_1_6 = forms.CharField(label='', max_length=100)
    city_1_6 = forms.CharField(label='', max_length=100)
    total_number_project_1_6 = forms.CharField(label='', max_length=100)
    total_cost_1_6 = forms.CharField(label='', max_length=100)
    start_date_1_6 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_6 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_6 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_6 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_6 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_6 = forms.CharField(label='', max_length=100)
    
    project_name_1_7 = forms.CharField(label='', max_length=100)
    city_1_7 = forms.CharField(label='', max_length=100)
    total_number_project_1_7 = forms.CharField(label='', max_length=100)
    total_cost_1_7 = forms.CharField(label='', max_length=100)
    start_date_1_7 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_7 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_7 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_7 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_7 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_7 = forms.CharField(label='', max_length=100)
    
    project_name_1_8 = forms.CharField(label='', max_length=100)
    city_1_8 = forms.CharField(label='', max_length=100)
    total_number_project_1_8 = forms.CharField(label='', max_length=100)
    total_cost_1_8 = forms.CharField(label='', max_length=100)
    start_date_1_8 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_8 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_8 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_8 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_8 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_8 = forms.CharField(label='', max_length=100)
    
    project_name_1_9 = forms.CharField(label='', max_length=100)
    city_1_9 = forms.CharField(label='', max_length=100)
    total_number_project_1_9 = forms.CharField(label='', max_length=100)
    total_cost_1_9 = forms.CharField(label='', max_length=100)
    start_date_1_9 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_9 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_9 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_9 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_9 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_9 = forms.CharField(label='', max_length=100)
    
    project_name_1_10 = forms.CharField(label='', max_length=100)
    city_1_10 = forms.CharField(label='', max_length=100)
    total_number_project_1_10 = forms.CharField(label='', max_length=100)
    total_cost_1_10 = forms.CharField(label='', max_length=100)
    start_date_1_10 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_1_10 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_1_10 = forms.CharField(label='', max_length=100)
    value_second_trimester_1_10 = forms.CharField(label='', max_length=100)
    value_third_trimester_1_10 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_1_10 = forms.CharField(label='', max_length=100)
    
    
    #TABLE 2
    form_2 = forms.CharField(label='Encuesta :', max_length=100)
    fiscal_year_2 = forms.CharField(label='Año Fiscal :', max_length=100)
    company_name_2 = forms.CharField(label='Nombre de la Empresa:', max_length=100)
    liaison_officer_2 = forms.CharField(label='Persona de Contacto:', max_length=100)
    tel_2 = forms.CharField(label='Teléfono::', max_length=100)
    project_2 = forms.CharField(label='Proyecto por::', max_length=100)
    branches_2 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)
    
    project_name_2_1 = forms.CharField(label='', max_length=100)
    city_2_1 = forms.CharField(label='', max_length=100)
    total_number_project_2_1 = forms.CharField(label='', max_length=100)
    total_cost_2_1 = forms.CharField(label='', max_length=100)
    start_date_2_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_1 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_1 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_1 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_1 = forms.CharField(label='', max_length=100)
    
    project_name_2_2 = forms.CharField(label='', max_length=100)
    city_2_2 = forms.CharField(label='', max_length=100)
    total_number_project_2_2 = forms.CharField(label='', max_length=100)
    total_cost_2_2 = forms.CharField(label='', max_length=100)
    start_date_2_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_2 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_2 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_2 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_2 = forms.CharField(label='', max_length=100)
    
    project_name_2_3 = forms.CharField(label='', max_length=100)
    city_2_3 = forms.CharField(label='', max_length=100)
    total_number_project_2_3 = forms.CharField(label='', max_length=100)
    total_cost_2_3 = forms.CharField(label='', max_length=100)
    start_date_2_3 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_3 =  forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_3 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_3 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_3 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_3 = forms.CharField(label='', max_length=100)
    
    project_name_2_4 = forms.CharField(label='', max_length=100)
    city_2_4 = forms.CharField(label='', max_length=100)
    total_number_project_2_4 = forms.CharField(label='', max_length=100)
    total_cost_2_4 = forms.CharField(label='', max_length=100)
    start_date_2_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_4 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_4 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_4 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_4 = forms.CharField(label='', max_length=100)
    
    project_name_2_5 = forms.CharField(label='', max_length=100)
    city_2_5 = forms.CharField(label='', max_length=100)
    total_number_project_2_5 = forms.CharField(label='', max_length=100)
    total_cost_2_5 = forms.CharField(label='', max_length=100)
    start_date_2_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_5 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_5 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_5 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_5 = forms.CharField(label='', max_length=100)
    
    project_name_2_6 = forms.CharField(label='', max_length=100)
    city_2_6 = forms.CharField(label='', max_length=100)
    total_number_project_2_6 = forms.CharField(label='', max_length=100)
    total_cost_2_6 = forms.CharField(label='', max_length=100)
    start_date_2_6 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_6 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_6 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_6 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_6 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_6 = forms.CharField(label='', max_length=100)
    
    project_name_2_7 = forms.CharField(label='', max_length=100)
    city_2_7 = forms.CharField(label='', max_length=100)
    total_number_project_2_7 = forms.CharField(label='', max_length=100)
    total_cost_2_7 = forms.CharField(label='', max_length=100)
    start_date_2_7 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_7 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_7 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_7 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_7 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_7 = forms.CharField(label='', max_length=100)
    
    project_name_2_8 = forms.CharField(label='', max_length=100)
    city_2_8 = forms.CharField(label='', max_length=100)
    total_number_project_2_8 = forms.CharField(label='', max_length=100)
    total_cost_2_8 = forms.CharField(label='', max_length=100)
    start_date_2_8 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_8 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_8 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_8 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_8 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_8 = forms.CharField(label='', max_length=100)
    
    project_name_2_9 = forms.CharField(label='', max_length=100)
    city_2_9 = forms.CharField(label='', max_length=100)
    total_number_project_2_9 = forms.CharField(label='', max_length=100)
    total_cost_2_9 = forms.CharField(label='', max_length=100)
    start_date_2_9 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_9 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_9 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_9 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_9 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_9 = forms.CharField(label='', max_length=100)
    
    project_name_2_10 = forms.CharField(label='', max_length=100)
    city_2_10 = forms.CharField(label='', max_length=100)
    total_number_project_2_10 = forms.CharField(label='', max_length=100)
    total_cost_2_10 = forms.CharField(label='', max_length=100)
    start_date_2_10 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_2_10 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_2_10 = forms.CharField(label='', max_length=100)
    value_second_trimester_2_10 = forms.CharField(label='', max_length=100)
    value_third_trimester_2_10 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_2_10 = forms.CharField(label='', max_length=100)
    
    
    #TABLE 3
    form_3 = forms.CharField(label='Encuesta :', max_length=100)
    fiscal_year_3 = forms.CharField(label='Año Fiscal :', max_length=100)
    company_name_3 = forms.CharField(label='Nombre de la Empresa:', max_length=100)
    liaison_officer_3 = forms.CharField(label='Persona de Contacto:', max_length=100)
    tel_3 = forms.CharField(label='Teléfono::', max_length=100)
    project_3 = forms.CharField(label='Proyecto por::', max_length=100)
    branches_3 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)
    
    project_name_3_1 = forms.CharField(label='', max_length=100)
    city_3_1 = forms.CharField(label='', max_length=100)
    total_number_project_3_1 = forms.CharField(label='', max_length=100)
    total_cost_3_1 = forms.CharField(label='', max_length=100)
    start_date_3_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_1 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_1 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_1 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_1 = forms.CharField(label='', max_length=100)
    
    project_name_3_2 = forms.CharField(label='', max_length=100)
    city_3_2 = forms.CharField(label='', max_length=100)
    total_number_project_3_2 = forms.CharField(label='', max_length=100)
    total_cost_3_2 = forms.CharField(label='', max_length=100)
    start_date_3_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_2 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_2 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_2 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_2 = forms.CharField(label='', max_length=100)
    
    project_name_3_3 = forms.CharField(label='', max_length=100)
    city_3_3 = forms.CharField(label='', max_length=100)
    total_number_project_3_3 = forms.CharField(label='', max_length=100)
    total_cost_3_3 = forms.CharField(label='', max_length=100)
    start_date_3_3 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_3 =  forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_3 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_3 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_3 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_3 = forms.CharField(label='', max_length=100)
    
    project_name_3_4 = forms.CharField(label='', max_length=100)
    city_3_4 = forms.CharField(label='', max_length=100)
    total_number_project_3_4 = forms.CharField(label='', max_length=100)
    total_cost_3_4 = forms.CharField(label='', max_length=100)
    start_date_3_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_4 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_4 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_4 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_4 = forms.CharField(label='', max_length=100)
    
    project_name_3_5 = forms.CharField(label='', max_length=100)
    city_3_5 = forms.CharField(label='', max_length=100)
    total_number_project_3_5 = forms.CharField(label='', max_length=100)
    total_cost_3_5 = forms.CharField(label='', max_length=100)
    start_date_3_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_5 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_5 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_5 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_5 = forms.CharField(label='', max_length=100)
    
    project_name_3_6 = forms.CharField(label='', max_length=100)
    city_3_6 = forms.CharField(label='', max_length=100)
    total_number_project_3_6 = forms.CharField(label='', max_length=100)
    total_cost_3_6 = forms.CharField(label='', max_length=100)
    start_date_3_6 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_6 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_6 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_6 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_6 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_6 = forms.CharField(label='', max_length=100)
    
    project_name_3_7 = forms.CharField(label='', max_length=100)
    city_3_7 = forms.CharField(label='', max_length=100)
    total_number_project_3_7 = forms.CharField(label='', max_length=100)
    total_cost_3_7 = forms.CharField(label='', max_length=100)
    start_date_3_7 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_7 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_7 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_7 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_7 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_7 = forms.CharField(label='', max_length=100)
    
    project_name_3_8 = forms.CharField(label='', max_length=100)
    city_3_8 = forms.CharField(label='', max_length=100)
    total_number_project_3_8 = forms.CharField(label='', max_length=100)
    total_cost_3_8 = forms.CharField(label='', max_length=100)
    start_date_3_8 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_8 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_8 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_8 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_8 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_8 = forms.CharField(label='', max_length=100)
    
    project_name_3_9 = forms.CharField(label='', max_length=100)
    city_3_9 = forms.CharField(label='', max_length=100)
    total_number_project_3_9 = forms.CharField(label='', max_length=100)
    total_cost_3_9 = forms.CharField(label='', max_length=100)
    start_date_3_9 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_9 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_9 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_9 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_9 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_9 = forms.CharField(label='', max_length=100)
    
    project_name_3_10 = forms.CharField(label='', max_length=100)
    city_3_10 = forms.CharField(label='', max_length=100)
    total_number_project_3_10 = forms.CharField(label='', max_length=100)
    total_cost_3_10 = forms.CharField(label='', max_length=100)
    start_date_3_10 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_3_10 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_3_10 = forms.CharField(label='', max_length=100)
    value_second_trimester_3_10 = forms.CharField(label='', max_length=100)
    value_third_trimester_3_10 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_3_10 = forms.CharField(label='', max_length=100)
    
    
    #TABLE 4
    form_4 = forms.CharField(label='Encuesta :', max_length=100)
    fiscal_year_4 = forms.CharField(label='Año Fiscal :', max_length=100)
    company_name_4 = forms.CharField(label='Nombre de la Empresa:', max_length=100)
    liaison_officer_4 = forms.CharField(label='Persona de Contacto:', max_length=100)
    tel_4 = forms.CharField(label='Teléfono::', max_length=100)
    project_4 = forms.CharField(label='Proyecto por::', max_length=100)
    branches_4 = forms.CharField(choice=COMPANT_TYPE_CHOICES, max_length=100)
    
    project_name_4_1 = forms.CharField(label='', max_length=100)
    city_4_1 = forms.CharField(label='', max_length=100)
    total_number_project_4_1 = forms.CharField(label='', max_length=100)
    total_cost_4_1 = forms.CharField(label='', max_length=100)
    start_date_4_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_1 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_1 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_1 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_1 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_1 = forms.CharField(label='', max_length=100)
    
    project_name_4_2 = forms.CharField(label='', max_length=100)
    city_4_2 = forms.CharField(label='', max_length=100)
    total_number_project_4_2 = forms.CharField(label='', max_length=100)
    total_cost_4_2 = forms.CharField(label='', max_length=100)
    start_date_4_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_2 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_2 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_2 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_2 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_2 = forms.CharField(label='', max_length=100)
    
    project_name_4_3 = forms.CharField(label='', max_length=100)
    city_4_3 = forms.CharField(label='', max_length=100)
    total_number_project_4_3 = forms.CharField(label='', max_length=100)
    total_cost_4_3 = forms.CharField(label='', max_length=100)
    start_date_4_3 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_3 =  forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_3 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_3 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_3 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_3 = forms.CharField(label='', max_length=100)
    
    project_name_4_4 = forms.CharField(label='', max_length=100)
    city_4_4 = forms.CharField(label='', max_length=100)
    total_number_project_4_4 = forms.CharField(label='', max_length=100)
    total_cost_4_4 = forms.CharField(label='', max_length=100)
    start_date_4_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_4 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_4 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_4 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_4 = forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_4 = forms.CharField(label='', max_length=100)
    
    project_name_4_5 = forms.CharField(label='', max_length=100)
    city_4_5 = forms.CharField(label='', max_length=100)
    total_number_project_4_5 = forms.CharField(label='', max_length=100)
    total_cost_4_5 = forms.CharField(label='', max_length=100)
    start_date_4_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_5 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_5 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_5 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_5 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_5 = forms.CharField(label='', max_length=100)
    
    

    project_name_4_6 = forms.CharField(label='', max_length=100)
    city_4_6 = forms.CharField(label='', max_length=100)
    total_number_project_4_6 = forms.CharField(label='', max_length=100)
    total_cost_4_6 = forms.CharField(label='', max_length=100)
    start_date_4_6 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_6 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_6 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_6 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_6 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_6 = forms.CharField(label='', max_length=100)
    
    project_name_4_7 = forms.CharField(label='', max_length=100)
    city_4_7 = forms.CharField(label='', max_length=100)
    total_number_project_4_7 = forms.CharField(label='', max_length=100)
    total_cost_4_7 = forms.CharField(label='', max_length=100)
    start_date_4_7 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_7 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_7 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_7 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_7 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_7 = forms.CharField(label='', max_length=100)
    
    project_name_4_8 = forms.CharField(label='', max_length=100)
    city_4_8 = forms.CharField(label='', max_length=100)
    total_number_project_4_8 = forms.CharField(label='', max_length=100)
    total_cost_4_8 = forms.CharField(label='', max_length=100)
    start_date_4_8 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_8 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_8 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_8 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_8 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_8 = forms.CharField(label='', max_length=100)
    
    project_name_4_9 = forms.CharField(label='', max_length=100)
    city_4_9 = forms.CharField(label='', max_length=100)
    total_number_project_4_9 = forms.CharField(label='', max_length=100)
    total_cost_4_9 = forms.CharField(label='', max_length=100)
    start_date_4_9 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_9 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_9 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_9 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_9 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_9 = forms.CharField(label='', max_length=100)
    
    project_name_4_10 = forms.CharField(label='', max_length=100)
    city_4_10 = forms.CharField(label='', max_length=100)
    total_number_project_4_10 = forms.CharField(label='', max_length=100)
    total_cost_4_10 = forms.CharField(label='', max_length=100)
    start_date_4_10 = forms.DateField(label='', widget=forms.SelectDateWidget)
    end_date_4_10 = forms.DateField(label='', widget=forms.SelectDateWidget)
    value_first_trimester_4_10 = forms.CharField(label='', max_length=100)
    value_second_trimester_4_10 = forms.CharField(label='', max_length=100)
    value_third_trimester_4_10 =  forms.CharField(label='', max_length=100)
    value_fourth_trimester_4_10 = forms.CharField(label='', max_length=100)
    

class JP_361(forms.Form):
    income_expenses_year_1 = forms.CharField(label='Year', max_length=4)
    income_expenses_year_2 = forms.CharField(label='Year', max_length=4)
    income_life_1 = forms.CharField(label='a) Life', max_length=100)
    income_life_2 = forms.CharField(label='a) Life', max_length=100)
    income_disability_1 = forms.CharField(label='b) Disability', max_length=100)
    income_disability_2 = forms.CharField(label='b) Disability', max_length=100)
    income_auto_1 = forms.CharField(label='c) Auto', max_length=100)
    income_auto_2 = forms.CharField(label='c) Auto', max_length=100)
    income_other_1 = forms.CharField(label='d) Other', max_length=100)
    income_other_2 = forms.CharField(label='d) Other', max_length=100)
    income_interest_1 = forms.CharField(label='2. Interest', max_length=100)
    income_interest_2 = forms.CharField(label='2. Interest', max_length=100)
    income_rent_1 = forms.CharField(label='3. Rent of land and building', max_length=100)
    income_rent_2 = forms.CharField(label='3. Rent of land and building', max_length=100)
    income_other_2_1 = forms.CharField(label='4. Other', max_length=100)
    income_other_2_2 = forms.CharField(label='4. Other', max_length=100)
    total_income_1 = forms.CharField(label='Total Income', max_length=100)
    total_income_2 = forms.CharField(label='Total Income', max_length=100)
    expenses_life_1 = forms.CharField(label='a) Life', max_length=100)
    expenses_life_2 = forms.CharField(label='a) Life', max_length=100)
    expenses_disability_1 = forms.CharField(label='b) Disability', max_length=100)
    expenses_disability_2 = forms.CharField(label='b) Disability', max_length=100)
    expenses_auto_1 = forms.CharField(label='c) Auto', max_length=100)
    expenses_auto_2 = forms.CharField(label='c) Auto', max_length=100)
    expenses_other_1 = forms.CharField(label='d) Other', max_length=100)
    expenses_other_2 = forms.CharField(label='d) Other', max_length=100)
    expenses_salaries_1 = forms.CharField(label='2. Salaries', max_length=100)
    expenses_salaries_2 = forms.CharField(label='2. Salaries', max_length=100)
    expenses_interes_1 = forms.CharField(label='3. Interest', max_length=100)
    expenses_interes_2 = forms.CharField(label='3. Interest', max_length=100)
    expenses_rent_1 = forms.CharField(label='4. Rent of land and building', max_length=100)
    expenses_rent_2 = forms.CharField(label='4. Rent of land and building', max_length=100)
    expenses_depreciation_1 = forms.CharField(label='5. Depreciation', max_length=100)
    expenses_depreciation_2 = forms.CharField(label='5. Depreciation', max_length=100)
    expenses_donations_1 = forms.CharField(label='6. Donations', max_length=100)
    expenses_donations_2 = forms.CharField(label='6. Donations', max_length=100)
    expenses_commissions_1 = forms.CharField(label='7. Commissions', max_length=100)
    expenses_commissions_2 = forms.CharField(label='7. Commissions', max_length=100)
    expenses_employees_1 = forms.CharField(label='a) To employees', max_length=100)
    expenses_employees_2 = forms.CharField(label='a) To employees', max_length=100)
    expenses_brokers_1 = forms.CharField(label='b) To local brokers', max_length=100)
    expenses_brokers_2 = forms.CharField(label='b) To local brokers', max_length=100)
    expenses_other_operational_1 = forms.CharField(label='8. Other operational expenses', max_length=100)
    expenses_other_operational_2 = forms.CharField(label='8. Other operational expenses', max_length=100)
    total_expenses_1 = forms.CharField(label='Total Expenses', max_length=100)
    total_expenses_2 = forms.CharField(label='Total Expenses', max_length=100)
    net_profit_1 = forms.CharField(label='Net profit or loss', max_length=100)
    net_profit_2 = forms.CharField(label='Net profit or loss', max_length=100)
    balance_year_1 = forms.CharField(label='As of 6/30/', max_length=4)
    balance_year_2 = forms.CharField(label='Estimated as of 6/30/', max_length=4)
    guaranteed_1 = forms.CharField(label='1. F.H.A. guaranteed', max_length=100)
    guaranteed_2 = forms.CharField(label='1. F.H.A. guaranteed', max_length=100)
    guaranteed_3 = forms.CharField(label='1. F.H.A. guaranteed', max_length=100)
    guaranteed_4 = forms.CharField(label='1. F.H.A. guaranteed', max_length=100)
    veterans_1 = forms.CharField(label='2. Veterans Administration', max_length=100)
    veterans_2 = forms.CharField(label='2. Veterans Administration', max_length=100)
    veterans_3 = forms.CharField(label='2. Veterans Administration', max_length=100)
    veterans_4 = forms.CharField(label='2. Veterans Administration', max_length=100)
    conventional_1 = forms.CharField(label='3. Conventional', max_length=100)
    conventional_2 = forms.CharField(label='3. Conventional', max_length=100)
    conventional_3 = forms.CharField(label='3. Conventional', max_length=100)
    conventional_4 = forms.CharField(label='3. Conventional', max_length=100)
    other_1 = forms.CharField(label='4. Other', max_length=100)
    other_2 = forms.CharField(label='4. Other', max_length=100)
    other_3 = forms.CharField(label='4. Other', max_length=100)
    other_4 = forms.CharField(label='4. Other', max_length=100)
    policy_loans_1 = forms.CharField(label='1. Policy loans', max_length=100)
    policy_loans_2 = forms.CharField(label='1. Policy loans', max_length=100)
    policy_loans_3 = forms.CharField(label='1. Policy loans', max_length=100)
    policy_loans_4 = forms.CharField(label='1. Policy loans', max_length=100)
    other_specify_1 = forms.CharField(label='5. Other (Specify)', max_length=100)
    other_specify_2 = forms.CharField(label='5. Other (Specify)', max_length=100)
    other_specify_3 = forms.CharField(label='5. Other (Specify)', max_length=100)
    other_specify_4 = forms.CharField(label='5. Other (Specify)', max_length=100)
    policy_reserves_1 = forms.CharField(label='1. Policy reserves of Puerto Rican residents', max_length=100)
    policy_reserves_2 = forms.CharField(label='1. Policy reserves of Puerto Rican residents', max_length=100)
    accrued_dividends_1 = forms.CharField(label='2. Accrued dividends on life insurance policies held by Puerto Rican residents', max_length=100)
    accrued_dividends_2 = forms.CharField(label='2. Accrued dividends on life insurance policies held by Puerto Rican residents', max_length=100)
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    date = forms.CharField(label='Date', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    position = forms.CharField(label='Position', max_length=100)
    
class JP_363(forms.Form):
    bonds_year_left = forms.CharField(label='Año', max_length=4)
    bonds_year_right = forms.CharField(label='Año', max_length=4)
    notes_year_left = forms.CharField(label='Año', max_length=4)
    notes_year_right = forms.CharField(label='Año', max_length=4)

    town_bonds_left = forms.CharField(label='Bonos Municipales', max_length=100)
    town_bonds_right = forms.CharField(label='Bonos Municipales', max_length=100)
    town_notes_left = forms.CharField(label='Notas Municipales', max_length=100)
    town_notes_right = forms.CharField(label='Notas Municipales', max_length=100)
    town_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    PC_bonds_left = forms.CharField(label='Bonos Corporativos', max_length=100)
    PC_bonds_right = forms.CharField(label='Bonos Corporativos', max_length=100)
    PC_notes_left  = forms.CharField(label='Notas Corporativas', max_length=100)
    PC_notes_right = forms.CharField(label='Notas Corporativas', max_length=100)
    PC_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    EPA_bonds_left = forms.CharField(label='Bonos de la EPA', max_length=100)
    EPA_bonds_right = forms.CharField(label='Bonos de la EPA', max_length=100)
    EPA_notes_left = forms.CharField(label='Notas de la EPA', max_length=100)
    EPA_notes_right = forms.CharField(label='Notas de la EPA', max_length=100)
    EPA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    HA_bonds_left = forms.CharField(label='Bonos de la HA', max_length=100)
    HA_bonds_right = forms.CharField(label='Bonos de la HA', max_length=100)
    HA_notes_left = forms.CharField(label='Notas de la HA', max_length=100)
    HA_notes_right = forms.CharField(label='Notas de la HA', max_length=100)
    HA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    ASA_bonds_left = forms.CharField(label='Bonos de la ASA', max_length=100)
    ASA_bonds_right = forms.CharField(label='Bonos de la ASA', max_length=100)
    ASA_notes_left = forms.CharField(label='Notas de la ASA', max_length=100)
    ASA_notes_right = forms.CharField(label='Notas de la ASA', max_length=100)
    ASA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    PBA_bonds_left = forms.CharField(label='Bonos de la PBA', max_length=100)
    PBA_bonds_right = forms.CharField(label='Bonos de la PBA', max_length=100)
    PBA_notes_left = forms.CharField(label='Notas de la PBA', max_length=100)
    PBA_notes_right = forms.CharField(label='Notas de la PBA', max_length=100)
    PBA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    PA_bonds_left = forms.CharField(label='Bonos de la PA', max_length=100)
    PA_bonds_right = forms.CharField(label='Bonos de la PA', max_length=100)
    PA_notes_left = forms.CharField(label='Notas de la PA', max_length=100)
    PA_notes_right = forms.CharField(label='Notas de la PA', max_length=100)
    PA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    IDC_bonds_left = forms.CharField(label='Bonos de la IDC', max_length=100)
    IDC_bonds_right = forms.CharField(label='Bonos de la IDC', max_length=100)
    IDC_notes_left = forms.CharField(label='Notas de la IDC', max_length=100)
    IDC_notes_right = forms.CharField(label='Notas de la IDC', max_length=100)
    IDC_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    GDB_bonds_left = forms.CharField(label='Bonos del GDB', max_length=100)
    GDB_bonds_right = forms.CharField(label='Bonos del GDB', max_length=100)
    GDB_notes_left = forms.CharField(label='Notas del GDB', max_length=100)
    GDB_notes_right = forms.CharField(label='Notas del GDB', max_length=100)
    GDB_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    HFC_bonds_left = forms.CharField(label='Bonos de la HFC', max_length=100)
    HFC_bonds_right = forms.CharField(label='Bonos de la HFC', max_length=100)
    HFC_notes_left = forms.CharField(label='Notas de la HFC', max_length=100)
    HFC_notes_right = forms.CharField(label='Notas de la HFC', max_length=100)
    HFC_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    other = forms.CharField(label='Otros', max_length=100)
    other_bonds_left = forms.CharField(label='Otros Bonos', max_length=100)
    other_bonds_right = forms.CharField(label='Otros Bonos', max_length=100)
    other_notes_left = forms.CharField(label='Otras Notas', max_length=100)
    other_notes_right = forms.CharField(label='Otras Notas', max_length=100)
    other_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    other_PC_1 = forms.CharField(label='Otros Corporativos', max_length=100)
    other_PC_1_bonds_left = forms.CharField(label='Bonos', max_length=100)
    other_PC_1_bonds_right = forms.CharField(label='Bonos', max_length=100)
    other_PC_1_notes_left = forms.CharField(label='Notas', max_length=100)
    other_PC_1_notes_right = forms.CharField(label='Notas', max_length=100)
    other_PC_1_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    other_PC_2 = forms.CharField(label='Otros Corporativos', max_length=100)
    other_PC_2_bonds_left = forms.CharField(label='Bonos', max_length=100)
    other_PC_2_bonds_right = forms.CharField(label='Bonos', max_length=100)
    other_PC_2_notes_left = forms.CharField(label='Notas', max_length=100)
    other_PC_2_notes_right = forms.CharField(label='Notas', max_length=100)
    other_PC_2_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    GNMA_bonds_left = forms.CharField(label='Bonos de la GNMA', max_length=100)
    GNMA_bonds_right = forms.CharField(label='Bonos de la GNMA', max_length=100)
    GNMA_notes_left = forms.CharField(label='Notas de la GNMA', max_length=100)
    GNMA_notes_right = forms.CharField(label='Notas de la GNMA', max_length=100)
    GNMA_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)

    other5 = forms.CharField(label='Otros', max_length=100)
    other5_bonds_left = forms.CharField(label='Otros', max_length=100)
    other5_bonds_right = forms.CharField(label='Otros', max_length=100)
    other5_notes_left = forms.CharField(label='Otros', max_length=100)
    other5_notes_right = forms.CharField(label='Otros', max_length=100)
    other5_name_service = forms.CharField(label='Nombre del Servicio', max_length=100)
    
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    position = forms.CharField(label='Position', max_length=100)
    date = forms.CharField(label='Date', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    
class JP_560_63110(forms.Forms):
    ssn = forms.CharField(label='Social Security Number', max_length=100)
    tel = forms.CharField(label='Telephone Number', max_length=100)
    fax = forms.CharField(label='Fax Number', max_length=100)
    sales_1 = forms.CharField(label='Sales', max_length=100)
    sales_2 = forms.CharField(label='Sales', max_length=100)
    disability_1 = forms.CharField(label='Disability', max_length=100)
    disability_2 = forms.CharField(label='Disability', max_length=100)
    life_1 = forms.CharField(label='Life', max_length=100)
    life_2 = forms.CharField(label='Life', max_length=100)
    interest_1 = forms.CharField(label='Interest', max_length=100)
    interest_2 = forms.CharField(label='Interest', max_length=100)
    other_income_1 = forms.CharField(label='Other Income', max_length=100)
    other_income_2 = forms.CharField(label='Other Income', max_length=100)
    total_income_1 = forms.CharField(label='Total Income', max_length=100)
    total_income_2 = forms.CharField(label='Total Income', max_length=100)
    interest_paid_1 = forms.CharField(label='Interest Paid', max_length=100)
    interest_paid_2 = forms.CharField(label='Interest Paid', max_length=100)
    disability_paid_1 = forms.CharField(label='Disability Paid', max_length=100)
    disability_paid_2 = forms.CharField(label='Disability Paid', max_length=100)
    life_paid_1 = forms.CharField(label='Life Paid', max_length=100)
    life_paid_2 = forms.CharField(label='Life Paid', max_length=100)
    other_expenditures_1 = forms.CharField(label='Other Expenditures', max_length=100)
    other_expenditures_2 = forms.CharField(label='Other Expenditures', max_length=100)
    total_expenditures_1 = forms.CharField(label='Total Expenditures', max_length=100)
    total_expenditures_2 = forms.CharField(label='Total Expenditures', max_length=100)
    net_profit_1 = forms.CharField(label='Net Profit', max_length=100)
    net_profit_2 = forms.CharField(label='Net Profit', max_length=100)
    initial_inventory_1 = forms.CharField(label='Initial Inventory', max_length=100)
    initial_inventory_2 = forms.CharField(label='Initial Inventory', max_length=100)
    final_inventory_1 = forms.CharField(label='Final Inventory', max_length=100)
    final_inventory_2 = forms.CharField(label='Final Inventory', max_length=100)
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    rank = forms.CharField(label='Rank', max_length=100)

class IP_210(forms.Form):
    company_name = forms.CharField(label='Nombre compañía / Company Name', max_length=100)
    address = forms.CharField(label='Dirección / Address', max_length=200)
    email = forms.EmailField(label='Correo electrónico / Email')
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    ssn = forms.CharField(label='Numero de Seguro Social / Social Security Number', max_length=11)
    tel = forms.CharField(label='Tel', max_length=20)
    fax = forms.CharField(label='Fax', max_length=20)
    legal_form = forms.ChoiceField(
        label='Forma legal de organización / Legal form of organization', 
        choices=[('Corporación', 'Corporación'), ('Sociedad', 'Sociedad'), ('Cooperativa', 'Cooperativa'), ('Empresa Individual', 'Empresa Individual'), ('Empresa sin fines pecuniarios', 'Empresa sin fines pecuniarios')]
    )
    cfc = forms.ChoiceField(label='CEC', choices=[('Si', 'Si'), ('No', 'No')])
    business_type = forms.CharField(label='Clase de negocio / Type of business', max_length=200)
    business_function = forms.CharField(
        label='Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity', 
        widget=forms.Textarea
    )
    branches = forms.ChoiceField(label='¿Opera sucursuales esta firma? / Do you have branch operations?', choices=[('Si', 'Si'), ('No', 'No')])
    closing_date = forms.DateField(label='Fecha de cierre de sus libros / Your accounting period closing date', widget=forms.SelectDateWidget)
    income_operations_12 = forms.CharField(label='1. Ingresos por operaciones - Income from operations'),
    income_operations_13 = forms.CharField(label='1. Ingresos por operaciones - Income from operations'),
    income_interests_12 = forms.CharField(label='2. Interese - Interests'),
    income_interests_13 = forms.CharField(label='2. Interese - Interests'),
    incomes_rents_12 = forms.CharField(label='3. Alquileres - From rents'),
    incomes_rents_13 = forms.CharField(label='3. Alquileres - From rents'),
    income_rent_land_12 = forms.CharField(label='4. Ganancia o pérdida de capital - Rent of land and building'),
    income_rent_land_13 = forms.CharField(label='4. Ganancia o pérdida de capital - Rent of land and building'),
    other_income_12 = forms.CharField(label='5. Otros ingresos - Other income'),
    other_income_13 = forms.CharField(label='5. Otros ingresos - Other income'),
    total_incomes_12 = forms.CharField(label='6. Total de ingresos - Other income'),
    total_incomes_13 = forms.CharField(label='6. Total de ingresos - Other income'),
    total_income_12 = forms.CharField(label='7. Total de ingresos - Total income'),
    total_income_13 = forms.CharField(label='7. Total de ingresos - Total income'),
    expenses_2012 = forms.CharField(label='B. Gastos - Expenses'),
    expenses_2012 = forms.CharField(label='B. Gastos - Expenses'),
    salaries_2012 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    salaries_2013 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    expenses_interests_12 = forms.CharField(label='2. Intereses - Interests'),
    expenses_interests_13 = forms.CharField(label='2. Intereses - Interests'),
    depreciation_12 = forms.CharField(label='3. Depreciación - Depreciation'),
    depreciation_13 = forms.CharField(label='3. Depreciación - Depreciation'),
    expenses_rent_12 = forms.CharField(label='4. Renta de terreno y edificio - Rent of land and building'),
    expenses_rent_13 = forms.CharField(label='4. Renta de terreno y edificio - Rent of land and building'),
    bad_debts_12 = forms.CharField(label='5. Cuentas incobrables - Bad debts'),
    bad_debts_13 = forms.CharField(label='5. Cuentas incobrables - Bad debts'),
    donations_12 = forms.CharField(label='6. Donativos - Donations'),
    donations_13 = forms.CharField(label='6. Donativos - Donations'),
    sales_tax_12 = forms.CharField(label='7. Impuesto sobre la venta y uso - sales and use tax'),
    sales_tax_13 = forms.CharField(label='7. Impuesto sobre la venta y uso - sales and use tax'),
    machinery_12 = forms.CharField(label='a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment'),
    machinery_13 = forms.CharField(label='a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment'),
    other_purchases_12 = forms.CharField(label='b. Por otras compras - On other purchases'),
    other_purchases_13 = forms.CharField(label='b. Por otras compras - On other purchases'),
    licenses_12 = forms.CharField(label='8. Licencias y patentes - Licenses and patents'),
    licenses_13 = forms.CharField(label='8. Licencias y patentes - Licenses and patents'),
    other_expenses_12 = forms.CharField(label='9. Otros gastos de operación - Other operating expenses'),
    other_expenses_13 = forms.CharField(label='9. Otros gastos de operación - Other operating expenses'),
    total_expenses_12 = forms.CharField(label='10. Total de gastos - Total expenses'),
    total_expenses_13 = forms.CharField(label='10. Total de gastos - Total expenses'),
    net_profit_12 = forms.CharField(label='C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    net_profit_13 = forms.CharField(label='C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    income_tax_12 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    income_tax_13 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    profit_after_tax_12 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    profit_after_tax_13 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    withheld_tax_12 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld'),
    withheld_tax_13 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld'),
    signature = forms.CharField(label='Nombre de persona que suministra la información - Name of person furnishing information', max_length=100)
    rank = forms.CharField(label='Rango - Title')

class IP_220(forms.Form):
    company_name = forms.CharField(label='Nombre compañía / Company Name', max_length=100)
    address = forms.CharField(label='Dirección / Address', max_length=200)
    email = forms.EmailField(label='Correo electrónico / Email')
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    ssn = forms.CharField(label='Numero de Seguro Social / Social Security Number', max_length=11)
    tel = forms.CharField(label='Tel', max_length=20)
    fax = forms.CharField(label='Fax', max_length=20)
    legal_form = forms.ChoiceField(
        label='Forma legal de organización / Legal form of organization', 
        choices=[('Corporación', 'Corporación'), ('Sociedad', 'Sociedad'), ('Cooperativa', 'Cooperativa'), ('Empresa Individual', 'Empresa Individual'), ('Empresa sin fines pecuniarios', 'Empresa sin fines pecuniarios')]
    )
    cfc = forms.ChoiceField(label='CEC', choices=[('Si', 'Si'), ('No', 'No')])
    business_type = forms.CharField(label='Clase de negocio / Type of business', max_length=200)
    business_function = forms.CharField(
        label='Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity', 
        widget=forms.Textarea
    )
    branches = forms.ChoiceField(label='¿Opera sucursuales esta firma? / Do you have branch operations?', choices=[('Si', 'Si'), ('No', 'No')])
    branches_yes = forms.ChoiceField(label='afirmativo a branches', choices=[('todas las sucursales', 'todas las sucursales'), ('este establecimiento', 'este establecimiento')])
    closing_date = forms.DateField(label='Fecha de cierre de sus libros / Your accounting period closing date', widget=forms.SelectDateWidget)
    services_revenues_12 = forms.CharField(label='Ingresos por servicios - Services rendered'),
    services_revenues_13 = forms.CharField(label='Ingresos por servicios - Services rendered'),
    residential_consumers_12 = forms.CharField(label='a. Abonados residenciales - Residential consumers'),
    residential_consumers_13 = forms.CharField(label='a. A industrias y negocios - To industries and businesses'),
    other_consumers_12 = forms.CharField(label='b. Otros abonados - Other consumers'),
    other_consumers_13 = forms.CharField(label='b. A personas - To persons'),
    sales_12 = forms.CharField(label='2. Ventas - From sale of merchandise'),
    sales_13 = forms.CharField(label='2. Ventas - From sale of merchandise'),
    incomes_rents_12 = forms.CharField(label='3. Alquileres - From rents'),
    incomes_rents_13 = forms.CharField(label='3. Alquileres - From rents'),
    incomes_interests_12 = forms.CharField(label='4. Intereses - Interests'),
    incomes_interests_13 = forms.CharField(label='4. Intereses - Interests'),
    dividends_12 = forms.CharField(label='5. Ganancia o pérdida de capital - Capital gain or loss'),
    dividends_13 = forms.CharField(label='5. Ganancia o pérdida de capital - Capital gain or loss'),
    others_incomes_12 = forms.CharField(label='6. Otros ingresos de operación - Other operating income'),
    others_incomes_13 = forms.CharField(label='6. Otros ingresos de operación - Other operating income'),
    total_income_12 = forms.CharField(label='7. Total de ingresos - Total income'),
    total_income_13 = forms.CharField(label='7. Total de ingresos - Total income'),
    salaries_2012 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    salaries_2013 = forms.CharField(label='1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    expenses_interests_12 = forms.CharField(label='2. Intereses - Interests'),
    expenses_interests_13 = forms.CharField(label='2. Intereses - Interests'),
    expenses_rents_12 = forms.CharField(label='3. Renta de terreno y edificio - Rent of land and building'),
    expenses_rents_13 = forms.CharField(label='3. Renta de terreno y edificio - Rent of land and building'),
    depreciation_12 = forms.CharField(label='4. Depreciación - Depreciation'),
    depreciation_13 = forms.CharField(label='4. Depreciación - Depreciation'),
    bad_debts_12 = forms.CharField(label='5. Cuentas incobrables - Bad debts'),
    bad_debts_13 = forms.CharField(label='5. Cuentas incobrables - Bad debts'),
    donations_12 = forms.CharField(label='6. Donativos - Donations'),
    donations_13 = forms.CharField(label='6. Donativos - Donations'),
    sales_tax_12 = forms.CharField(label='7. Impuesto sobre la venta y uso - sales and use tax'),
    sales_tax_13 = forms.CharField(label='7. Impuesto sobre la venta y uso - sales and use tax'),
    machinery_12 = forms.CharField(label='a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment'),
    machinery_13 = forms.CharField(label='a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment'),
    other_purchases_12 = forms.CharField(label='b. Por otras compras - On other purchases'),
    other_purchases_13 = forms.CharField(label='b. Por otras compras - On other purchases'),
    licenses_12 = forms.CharField(label='8. Licencias y patentes - Licenses and patents'),
    licenses_13 = forms.CharField(label='8. Licencias y patentes - Licenses and patents'),
    other_expenses_12 = forms.CharField(label='9. Otros gastos de operación - Other operating expenses'),
    other_expenses_13 = forms.CharField(label='9. Otros gastos de operación - Other operating expenses'),
    total_expenses_12 = forms.CharField(label='10. Total de gastos - Total expenses'),
    total_expenses_13 = forms.CharField(label='10. Total de gastos - Total expenses'),
    net_profit_12 = forms.CharField(label='C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    net_profit_13 = forms.CharField(label='C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    income_tax_12 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    income_tax_13 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    profit_after_tax_12 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    profit_after_tax_13 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    withheld_tax_12 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld'),
    withheld_tax_13 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld'),
    signature = forms.CharField(label='Nombre de persona que suministra la información - Name of person furnishing information', max_length=100)
    rank = forms.CharField(label='Rango - Title')


class JP_560_63111(forms.Form):
    ssn = forms.CharField(label='Social Security Number', max_length=100)
    tel = forms.CharField(label='Telephone Number', max_length=100)
    fax = forms.CharField(label='Fax Number', max_length=100)
    sales_1 = forms.CharField(label='Sales', max_length=100)
    sales_2 = forms.CharField(label='Sales', max_length=100)
    premiums_1 = forms.CharField(label='Premiums', max_length=100)
    premiums_2 = forms.CharField(label='Premiums', max_length=100)
    interest_received_1 = forms.CharField(label='Interest Received', max_length=100)
    interest_received_2 = forms.CharField(label='Interest Received', max_length=100)
    other_income_1 = forms.CharField(label='Other Income', max_length=100)
    other_income_2 = forms.CharField(label='Other Income', max_length=100)
    total_income_1 = forms.CharField(label='Total Income', max_length=100)
    total_income_2 = forms.CharField(label='Total Income', max_length=100)
    interest_paid_1 = forms.CharField(label='Interest Paid', max_length=100)
    interest_paid_2 = forms.CharField(label='Interest Paid', max_length=100)
    claims_paid_1 = forms.CharField(label='Claims Paid', max_length=100)
    claims_paid_2 = forms.CharField(label='Claims Paid', max_length=100)
    other_expenditures_1 = forms.CharField(label='Other Expenditures', max_length=100)
    other_expenditures_2 = forms.CharField(label='Other Expenditures', max_length=100)
    total_expenditures_1 = forms.CharField(label='Total Expenditures', max_length=100)
    total_expenditures_2 = forms.CharField(label='Total Expenditures', max_length=100)
    net_profit_loss_1 = forms.CharField(label='Net Profit/Loss', max_length=100)
    net_profit_loss_2 = forms.CharField(label='Net Profit/Loss', max_length=100)
    initial_inventory_1 = forms.CharField(label='Initial Inventory', max_length=100)
    initial_inventory_2 = forms.CharField(label='Initial Inventory', max_length=100)
    final_inventory_1 = forms.CharField(label='Final Inventory', max_length=100)
    final_inventory_2 = forms.CharField(label='Final Inventory', max_length=100)
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    
class IP_230(forms.Form):
    company_name = forms.CharField(label='Nombre compañía / Company Name', max_length=100)
    address = forms.CharField(label='Dirección / Address', max_length=200)
    email = forms.EmailField(label='Correo electrónico / Email') 
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    ssn = forms.CharField(label='Numero de Seguro Social / Social Security Number', max_length=11)
    tel = forms.CharField(label='Tel', max_length=20)
    fax = forms.CharField(label='Fax', max_length=20)
    legal_form = forms.ChoiceField(
        label='Forma legal de organización / Legal form of organization', 
        choices=[('Corporación', 'Corporación'), ('Sociedad', 'Sociedad'), ('Cooperativa', 'Cooperativa'), ('Empresa Individual', 'Empresa Individual'), ('Empresa sin fines pecuniarios', 'Empresa sin fines pecuniarios')]
    )
    cfc = forms.ChoiceField(label='CEC', choices=[('Si', 'Si'), ('No', 'No')])
    business_function = forms.CharField(
        label='Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity', 
        widget=forms.Textarea
    )
    closing_date = forms.DateField(label='Fecha de cierre de sus libros / Your accounting period closing date', widget=forms.SelectDateWidget)
    income_project_A_12 = forms.CharField(label='1. Ingresos por proyecto - Income from project'),
    income_project_A_13 = forms.CharField(label='1. Ingresos por proyecto - Income from project'),
    people_A_12 = forms.CharField(label='2. A personas - To persons'),
    people_A_13 = forms.CharField(label='2. A personas - To persons'),
    industries_businesses_A_12 = forms.CharField(label='3. A industrias y negocios - To industries and businesses'),
    industries_businesses_A_13 = forms.CharField(label='3. A industrias y negocios - To industries and businesses'),
    direct_indirect_B_12 = forms.CharField(label='4. Costos directos e indirectos - Direct and indirect costs'),
    direct_indirect_B_13 = forms.CharField(label='4. Costos directos e indirectos - Direct and indirect costs'),
    direct_christmas_vacation_B_12 = forms.CharField(label='a. Por bono de Navidad y vacaciones - On Christmas bonus and vacation'),
    direct_christmas_vacation_B_13 = forms.CharField(label='a. Por bono de Navidad y vacaciones - On Christmas bonus and vacation'),
    rent_land_building_B_12 = forms.CharField(label='b. Por renta de terreno y edificio - On rent of land and building'),
    rent_land_building_B_13 = forms.CharField(label='b. Por renta de terreno y edificio - On rent of land and building'),
    rent_equipment_B_12 = forms.CharField(label='c. Por renta de equipo - On rent of equipment'),
    rent_equipment_B_13 = forms.CharField(label='c. Por renta de equipo - On rent of equipment'),
    depreciation_B_12 = forms.CharField(label='d. Por depreciación - On depreciation'),
    depreciation_B_13 = forms.CharField(label='d. Por depreciación - On depreciation'),
    sales_tax_B_12 = forms.CharField(label='e. Por impuesto sobre la venta y uso - On sales and use tax'),
    sales_tax_B_13 = forms.CharField(label='e. Por impuesto sobre la venta y uso - On sales and use tax'),
    purchases_machinery_equipment_B_12 = forms.CharField(label='f. Por compra de maquinaria y equipo - On purchases of machinery and equipment'),
    purchases_machinery_equipment_B_13 = forms.CharField(label='f. Por compra de maquinaria y equipo - On purchases of machinery and equipment'),
    other_purchases_B_12 = forms.CharField(label='g. Por otras compras - On other purchases'),
    other_purchases_B_13 = forms.CharField(label='g. Por otras compras - On other purchases'),
    licenses_patent_B_12 = forms.CharField(label='h. Por licencias y patentes - On licenses and patents'),
    licenses_patent_B_13 = forms.CharField(label='h. Por licencias y patentes - On licenses and patents'),
    other_costs_direct_indirect_B_12 = forms.CharField(label='i. Otros costos directos e indirectos - Other direct and indirect costs'),
    other_costs_direct_indirect_B_13 = forms.CharField(label='i. Otros costos directos e indirectos - Other direct and indirect costs'),
    gross_profit_C_12 = forms.CharField(label='5. Utilidad bruta - Gross profit'),
    gross_profit_C_13 = forms.CharField(label='5. Utilidad bruta - Gross profit'),
    other_income_D_12 = forms.CharField(label='6. Otros ingresos - Other income'),
    other_income_D_13 = forms.CharField(label='6. Otros ingresos - Other income'),
    interest_D_12 = forms.CharField(label='7. Intereses - Interests'),
    interest_D_13 = forms.CharField(label='7. Intereses - Interests'),
    rent_land_building_D_12 = forms.CharField(label='8. Renta de terreno y edificio - Rent of land and building'),
    rent_land_building_D_13 = forms.CharField(label='8. Renta de terreno y edificio - Rent of land and building'),
    gain_loss_D_12 = forms.CharField(label='9. Ganancia o pérdida de capital - Capital gain or loss'),
    gain_loss_D_13 = forms.CharField(label='9. Ganancia o pérdida de capital - Capital gain or loss'),
    other_D_12 = forms.CharField(label='10. Otros - Other'),
    other_D_13 = forms.CharField(label='10. Otros - Other'),
    gross_profit_E_12 = forms.CharField(label='11. Utilidad bruta - Gross profit'),
    gross_profit_E_13 = forms.CharField(label='11. Utilidad bruta - Gross profit'),
    administrative_F_12 = forms.CharField(label='1. Gastos administrativos - Administrative expenses'),
    administrative_F_13 = forms.CharField(label='1. Gastos administrativos - Administrative expenses'),
    salaries_wages_bonus_commissions_F_12 = forms.CharField(label='2. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    salaries_wages_bonus_commissions_F_13 = forms.CharField(label='2. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions'),
    interest_F_12 = forms.CharField(label='3. Intereses - Interests'),
    interest_F_13 = forms.CharField(label='3. Intereses - Interests'),
    rent_land_building_F_12 = forms.CharField(label='4. Renta de terreno y edificio - Rent of land and building'),
    rent_land_building_F_13 = forms.CharField(label='4. Renta de terreno y edificio - Rent of land and building'),
    depreciation_F_12 = forms.CharField(label='5. Depreciación - Depreciation'),
    depreciation_F_13 = forms.CharField(label='5. Depreciación - Depreciation'),
    bad_depts_F_12 = forms.CharField(label='6. Cuentas incobrables - Bad debts'),
    bad_depts_F_13 = forms.CharField(label='6. Cuentas incobrables - Bad debts'),
    donation_F_12 = forms.CharField(label='7. Donativos - Donations'),
    donation_F_13 = forms.CharField(label='7. Donativos - Donations'),
    other_expenses_F_12 = forms.CharField(label='8. Otros gastos - Other expenses'),
    other_expenses_F_13 = forms.CharField(label='8. Otros gastos - Other expenses'),
    net_profit_G_12 = forms.CharField(label='9. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    net_profit_G_13 = forms.CharField(label='9. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )'),
    income_tax_G_12 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    income_tax_G_13 = forms.CharField(label='1. Contribución sobre ingresos - Income tax'),
    profit_after_tax_G_12 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    profit_after_tax_G_13 = forms.CharField(label='2. Ganancia después de contribución sobre ingresos - Profit after income tax'),
    sales_tax_H_12 = forms.CharField(label='3. Impuesto sobre la venta y uso - sales and use tax'),
    sales_tax_H_13 = forms.CharField(label='3. Impuesto sobre la venta y uso - sales and use tax'),
    biginning_year_HA = forms.CharField(label='Año Inicial', max_length=100)
    end_year_HB = forms.CharField(label='Año Final', max_length=100)
    biginning_year_HC = forms.CharField(label='Año Inicial', max_length=100)
    end_year_HD = forms.CharField(label='Año Final', max_length=100)
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    rank = forms.CharField(label='Rank', max_length=100)
    
class JP_560_63210(forms.Form):
    ssn = forms.CharField(label='Social Security Number', max_length=100)
    tel = forms.CharField(label='Telephone Number', max_length=100)
    fax = forms.CharField(label='Fax Number', max_length=100)
    sales_1 = forms.CharField(label='Sales', max_length=100)
    sales_2 = forms.CharField(label='Sales', max_length=100)
    premiums_1 = forms.CharField(label='Premiums', max_length=100)
    premiums_2 = forms.CharField(label='Premiums', max_length=100)
    disability_A_1 = forms.CharField(label='Disability', max_length=100)
    disability_A_2 = forms.CharField(label='Disability', max_length=100)
    cars_A_1 = forms.CharField(label='Cars', max_length=100)
    cars_A_2 = forms.CharField(label='Cars', max_length=100)
    other_A_1 = forms.CharField(label='Other', max_length=100)
    other_A_2 = forms.CharField(label='Other', max_length=100)
    interest_received_1 = forms.CharField(label='Interest Received', max_length=100)
    interest_received_2 = forms.CharField(label='Interest Received', max_length=100)
    other_income_1 = forms.CharField(label='Other Income', max_length=100)
    other_income_2 = forms.CharField(label='Other Income', max_length=100)
    total_income_1 = forms.CharField(label='Total Income', max_length=100)
    total_income_2 = forms.CharField(label='Total Income', max_length=100)
    interest_paid_1 = forms.CharField(label='Interest Paid', max_length=100)
    interest_paid_2 = forms.CharField(label='Interest Paid', max_length=100)
    claims_paid_1 = forms.CharField(label='Claims Paid', max_length=100)
    claims_paid_2 = forms.CharField(label='Claims Paid', max_length=100)
    disability_B_1 = forms.CharField(label='Disability', max_length=100)
    disability_B_2 = forms.CharField(label='Disability', max_length=100)
    cars_B_1 = forms.CharField(label='Cars', max_length=100)
    cars_B_2 = forms.CharField(label='Cars', max_length=100)
    other_B_1 = forms.CharField(label='Other', max_length=100)
    other_B_2 = forms.CharField(label='Other', max_length=100)
    other_expenditures_1 = forms.CharField(label='Other Expenditures', max_length=100)
    other_expenditures_2 = forms.CharField(label='Other Expenditures', max_length=100)
    total_expenditures_1 = forms.CharField(label='Total Expenditures', max_length=100)
    total_expenditures_2 = forms.CharField(label='Total Expenditures', max_length=100)
    net_profit_loss_1 = forms.CharField(label='Net Profit/Loss', max_length=100)
    net_profit_loss_2 = forms.CharField(label='Net Profit/Loss', max_length=100)
    initial_inventory_1 = forms.CharField(label='Initial Inventory', max_length=100)
    initial_inventory_2 = forms.CharField(label='Initial Inventory', max_length=100)
    final_inventory_1 = forms.CharField(label='Final Inventory', max_length=100)
    final_inventory_2 = forms.CharField(label='Final Inventory', max_length=100)
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    rank = forms.CharField(label='Rank', max_length=100)
    
class JP_362(forms.Form):
    year_1 = forms.CharField(label='Año / Year', max_length=100)
    year_2 = forms.CharField(label='Año / Year', max_length=100)
    
    company_name = forms.CharField(label='Nombre de Empresa Pública', max_length=100)
    
    debts_balance = forms.CharField(label='1. Deudas en el Exterios De Largo Plazo, Total', max_length=100)
    debts_emision = forms.CharField(label='1. Deudas en el Exterios De Largo Plazo, Emisión', max_length=100)
    debts_amortizacion = forms.CharField(label='1. Deudas en el Exterios De Largo Plazo, Amortización', max_length=100)
    debts_final = forms.CharField(label='1. Deudas en el Exterios De Largo Plazo, Final', max_length=100)
    debts_interes = forms.CharField(label='1. Deudas en el Exterios De Largo Plazo, Interés', max_length=100)
    debts_acreedor = forms.CharField(label='1. Deudas en el Exterios De Largo Plazo, Acreedor', max_length=100)
    
    debts_bond_balance = forms.CharField(label='Bonos, Valor Par', max_length=100)
    debts_bond_emision = forms.CharField(label='Bonos, Valor Par', max_length=100)
    debts_bond_amortizacion = forms.CharField(label='Bonos, Valor Par', max_length=100)
    debts_bond_final = forms.CharField(label='Bonos, Valor Par', max_length=100)
    debts_bond_interes = forms.CharField(label='Bonos, Valor Par', max_length=100)
    debts_bond_acreedor = forms.CharField(label='Bonos, Valor Par', max_length=100)
    
    debts_promossory_notes_balance = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    debts_promossory_notes_emision = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    debts_promossory_notes_amortizacion = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    debts_promossory_notes_final = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    debts_promossory_notes_interes = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    debts_promossory_notes_acreedor = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    
    debts_others_balance = forms.CharField(label='Otras (especifique)', max_length=100)
    debts_others_emision = forms.CharField(label='Otras (especifique)', max_length=100)
    debts_others_amortizacion = forms.CharField(label='Otras (especifique)', max_length=100)
    debts_others_final = forms.CharField(label='Otras (especifique)', max_length=100)
    debts_others_interes = forms.CharField(label='Otras (especifique)', max_length=100)
    debts_others_acreedor = forms.CharField(label='Otras (especifique)', max_length=100)
    
    short_promossory_balance = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    short_promossory_emision = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    short_promossory_amortizacion = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    short_promossory_final = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    short_promossory_interes = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    short_promossory_acreedor = forms.CharField(label='Pagarés, Valor Par', max_length=100)
    
    short_account_balance = forms.CharField(label='Cuentas por pagar', max_length=100)
    short_account_emision = forms.CharField(label='Cuentas por pagar', max_length=100)
    short_account_amortizacion = forms.CharField(label='Cuentas por pagar', max_length=100)
    short_account_final = forms.CharField(label='Cuentas por pagar', max_length=100)
    short_account_interes = forms.CharField(label='Cuentas por pagar', max_length=100)
    short_account_acreedor = forms.CharField(label='Cuentas por pagar', max_length=100)
    
    short_others_balance = forms.CharField(label='Otras (especifique)', max_length=100)
    short_others_emision = forms.CharField(label='Otras (especifique)', max_length=100)
    short_others_amortizacion = forms.CharField(label='Otras (especifique)', max_length=100)
    short_others_final = forms.CharField(label='Otras (especifique)', max_length=100)
    short_others_interes = forms.CharField(label='Otras (especifique)', max_length=100)
    short_others_acreedor = forms.CharField(label='Otras (especifique)', max_length=100)
    
    short_term_balance = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    short_term_emision = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    short_term_amortizacion = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    short_term_final = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    short_term_interes = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    short_term_acreedor = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    
    assets_balance = forms.CharField(label='2. Activos en el Exterior De Largo Plazo, Total', max_length=100)
    assets_emision = forms.CharField(label='2. Activos en el Exterior De Largo Plazo, Total', max_length=100)
    assets_amortizacion = forms.CharField(label='2. Activos en el Exterior De Largo Plazo, Total', max_length=100)
    assets_final = forms.CharField(label='2. Activos en el Exterior De Largo Plazo, Total', max_length=100)
    assets_interes = forms.CharField(label='2. Activos en el Exterior De Largo Plazo, Total', max_length=100)
    
    assets_values_balance = forms.CharField(label='Valores del Gobierno de E.E.U.U., Valor Par', max_length=100)
    assets_values_emision = forms.CharField(label='Valores del Gobierno de E.E.U.U., Valor Par', max_length=100)
    assets_values_amortizacion = forms.CharField(label='Valores del Gobierno de E.E.U.U., Valor Par', max_length=100)
    assets_values_final = forms.CharField(label='Valores del Gobierno de E.E.U.U., Valor Par', max_length=100)
    assets_values_interes = forms.CharField(label='Valores del Gobierno de E.E.U.U., Valor Par', max_length=100)
    
    assets_others_balance = forms.CharField(label='Otros, Valor Par (especifique)', max_length=100)
    assets_others_emision = forms.CharField(label='Otros, Valor Par (especifique)', max_length=100)
    assets_others_amortizacion = forms.CharField(label='Otros, Valor Par (especifique)', max_length=100)
    assets_others_final = forms.CharField(label='Otros, Valor Par (especifique)', max_length=100)
    assets_others_interes = forms.CharField(label='Otros, Valor Par (especifique)', max_length=100)
    
    short_balance = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    short_emision = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    short_amortizacion = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    short_final = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    short_interes = forms.CharField(label='De Corto Plazo, Total', max_length=100)
    
    short_balance_balance = forms.CharField(label='Balances Bancarios', max_length=100)
    short_balance_emision = forms.CharField(label='Balances Bancarios', max_length=100)
    short_balance_amortizacion = forms.CharField(label='Balances Bancarios', max_length=100)
    short_balance_final = forms.CharField(label='Balances Bancariosl', max_length=100)
    short_balance_interes = forms.CharField(label='Balances Bancarios', max_length=100)
    
    short_accouts_balance = forms.CharField(label='Cuentas por Cobrar', max_length=100)
    short_accouts_emision = forms.CharField(label='Cuentas por Cobrar', max_length=100)
    short_accouts_amortizacion = forms.CharField(label='Cuentas por Cobrar', max_length=100)
    short_accouts_final = forms.CharField(label='Cuentas por Cobrar', max_length=100)
    short_accouts_interes = forms.CharField(label='Cuentas por Cobrar', max_length=100)
    
    short_others_balance_2 = forms.CharField(label='Otros (especifique)', max_length=100)
    short_others_emision_2 = forms.CharField(label='Otros (especifique)', max_length=100)
    short_others_amortizacion_2 = forms.CharField(label='Otros (especifique)', max_length=100)
    short_others_final_2 = forms.CharField(label='Otros (especifique)', max_length=100)
    short_others_interes_2 = forms.CharField(label='Otros (especifique)', max_length=100)

    name_signature = forms.CharField(label='Name', max_length=100)
    position_signature = forms.CharField(label='Position', max_length=100)
    date_signature = forms.CharField(label='Date', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    
class JP_560_2(forms.Form):
    company_name = forms.CharField(label='Nombre compañía / Company Name', max_length=100)
    address = forms.CharField(label='Dirección / Address', max_length=200)
    email = forms.EmailField(label='Correo electrónico / Email')
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    ssn = forms.CharField(label='Numero de Seguro Social / Social Security Number', max_length=11)
    tel = forms.CharField(label='Tel', max_length=20)
    fax = forms.CharField(label='Fax', max_length=20)
    sales_1 = forms.CharField(label='Sales', max_length=100)
    sales_2 = forms.CharField(label='Sales', max_length=100)
    interest_received_1 = forms.CharField(label='Interest Received', max_length=100)
    interest_received_2 = forms.CharField(label='Interest Received', max_length=100)
    other_income_1 = forms.CharField(label='Other Income', max_length=100)
    other_income_2 = forms.CharField(label='Other Income', max_length=100)
    total_income_1 = forms.CharField(label='Total Income', max_length=100)
    total_income_2 = forms.CharField(label='Total Income', max_length=100)
    interest_paid_1 = forms.CharField(label='Interest Paid', max_length=100)
    interest_paid_2 = forms.CharField(label='Interest Paid', max_length=100)
    other_expenditures_1_1 = forms.CharField(label='Other Expenditures', max_length=100)
    other_expenditures_2_1 = forms.CharField(label='Other Expenditures', max_length=100)
    other_expenditures_1_2 = forms.CharField(label='Other Expenditures', max_length=100)
    other_expenditures_2_2 = forms.CharField(label='Other Expenditures', max_length=100)
    net_profit_loss_1 = forms.CharField(label='Net Profit/Loss', max_length=100)
    net_profit_loss_2 = forms.CharField(label='Net Profit/Loss', max_length=100)
    initial_inventory_1 = forms.CharField(label='Initial Inventory', max_length=100)
    initial_inventory_2 = forms.CharField(label='Initial Inventory', max_length=100)
    final_inventory_1 = forms.CharField(label='Final Inventory', max_length=100)
    final_inventory_2 = forms.CharField(label='Final Inventory', max_length=100)
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    rank = forms.CharField(label='Rank', max_length=100)    
class JP_364(forms.Form):
    year_bono1 = forms.CharField(label='Año / Year', max_length=100)
    year_bono2 = forms.CharField(label='Año / Year', max_length=100)
    year_paga1 = forms.CharField(label='Año / Year', max_length=100)
    year_paga2 = forms.CharField(label='Año / Year', max_length=100)
    ELA_bono1 = forms.CharField(label='ELA', max_length=100)
    ELA_bono2 = forms.CharField(label='ELA', max_length=100)
    ELA_paga1 = forms.CharField(label='ELA', max_length=100)
    ELA_paga2 = forms.CharField(label='ELA', max_length=100)
    ELA_agente = forms.CharField(label='ELA', max_length=100)
    municipio_bono1 = forms.CharField(label='Municipio', max_length=100)
    municipio_bono2 = forms.CharField(label='Municipio', max_length=100)
    municipio_paga1 = forms.CharField(label='Municipio', max_length=100)
    municipio_paga2 = forms.CharField(label='Municipio', max_length=100)
    municipio_agente = forms.CharField(label='Municipio', max_length=100)
    corp_publicas_bono1 = forms.CharField(label='Corporaciones Públicas', max_length=100)
    corp_publicas_bono2 = forms.CharField(label='Corporaciones Públicas', max_length=100)
    corp_publicas_paga1 = forms.CharField(label='Corporaciones Públicas', max_length=100)
    corp_publicas_paga2 = forms.CharField(label='Corporaciones Públicas', max_length=100)
    corp_publicas_agente = forms.CharField(label='Corporaciones Públicas', max_length=100)
    AEE_bono1 = forms.CharField(label='AEE', max_length=100)
    AEE_bono2 = forms.CharField(label='AEE', max_length=100)
    AEE_paga1 = forms.CharField(label='AEE', max_length=100)
    AEE_paga2 = forms.CharField(label='AEE', max_length=100)
    AEE_agente = forms.CharField(label='AEE', max_length=100)
    Acarreteras_bono1 = forms.CharField(label='Acarreteras', max_length=100)
    Acarreteras_bono2 = forms.CharField(label='Acarreteras', max_length=100)
    Acarreteras_paga1 = forms.CharField(label='Acarreteras', max_length=100)
    Acarreteras_paga2 = forms.CharField(label='Acarreteras', max_length=100)
    Acarreteras_agente = forms.CharField(label='Acarreteras', max_length=100)
    AAA_bono1 = forms.CharField(label='AAA', max_length=100)
    AAA_bono2 = forms.CharField(label='AAA', max_length=100)
    AAA_paga1 = forms.CharField(label='AAA', max_length=100)
    AAA_paga2 = forms.CharField(label='AAA', max_length=100)
    AAA_agente = forms.CharField(label='AAA', max_length=100)
    AEP_bono1 = forms.CharField(label='AFA', max_length=100)
    AEP_bono2 = forms.CharField(label='AFA', max_length=100)
    AEP_paga1 = forms.CharField(label='AFA', max_length=100)
    AEP_paga2 = forms.CharField(label='AFA', max_length=100)
    AEP_agente = forms.CharField(label='AFA', max_length=100)
    AP_bono1 = forms.CharField(label='AP', max_length=100)
    AP_bono2 = forms.CharField(label='AP', max_length=100)
    AP_paga1 = forms.CharField(label='AP', max_length=100)
    AP_paga2 = forms.CharField(label='AP', max_length=100)
    AP_agente = forms.CharField(label='AP', max_length=100)
    AT_bono1 = forms.CharField(label='AT', max_length=100)
    AT_bono2 = forms.CharField(label='AT', max_length=100)
    AT_paga1 = forms.CharField(label='AT', max_length=100)
    AT_paga2 = forms.CharField(label='AT', max_length=100)
    AT_agente = forms.CharField(label='AT', max_length=100)
    CFI_bono1 = forms.CharField(label='CFI', max_length=100)
    CFI_bono2 = forms.CharField(label='CFI', max_length=100)
    CFI_paga1 = forms.CharField(label='CFI', max_length=100)
    CFI_paga2 = forms.CharField(label='CFI', max_length=100)
    CFI_agente = forms.CharField(label='CFI', max_length=100)
    BGF_bono1 = forms.CharField(label='BGF', max_length=100)
    BGF_bono2 = forms.CharField(label='BGF', max_length=100)
    BGF_paga1 = forms.CharField(label='BGF', max_length=100)
    BGF_paga2 = forms.CharField(label='BGF', max_length=100)
    BGF_agente = forms.CharField(label='BGF', max_length=100)
    CFV_bono1 = forms.CharField(label='CFV', max_length=100)
    CFV_bono2 = forms.CharField(label='CFV', max_length=100)
    CFV_paga1 = forms.CharField(label='CFV', max_length=100)
    CFV_paga2 = forms.CharField(label='CFV', max_length=100)
    CFV_agente = forms.CharField(label='CFV', max_length=100)
    otherk_title = forms.CharField(label='Otros', max_length=100)
    otherk_bono1 = forms.CharField(label='Otros', max_length=100)
    otherk_bono2 = forms.CharField(label='Otros', max_length=100)
    otherk_paga1 = forms.CharField(label='Otros', max_length=100)
    otherk_paga2 = forms.CharField(label='Otros', max_length=100)
    otherk_agente = forms.CharField(label='Otros', max_length=100)
    otherl_title = forms.CharField(label='Otros', max_length=100)
    otherl_bono1 = forms.CharField(label='Otros', max_length=100)
    otherl_bono2 = forms.CharField(label='Otros', max_length=100)
    otherl_paga1 = forms.CharField(label='Otros', max_length=100)
    otherl_paga2 = forms.CharField(label='Otros', max_length=100)
    otherl_agente = forms.CharField(label='Otros', max_length=100)
    otherm_title = forms.CharField(label='Otros', max_length=100)
    otherm_bono1 = forms.CharField(label='Otros', max_length=100)
    otherm_bono2 = forms.CharField(label='Otros', max_length=100)
    otherm_paga1 = forms.CharField(label='Otros', max_length=100)
    otherm_paga2 = forms.CharField(label='Otros', max_length=100)
    otherm_agente = forms.CharField(label='Otros', max_length=100)
    
    year_balance1 = forms.CharField(label='Año / Year', max_length=100)
    year_balance2 = forms.CharField(label='Año / Year', max_length=100)
    FHA_balance1 = forms.CharField(label='FHA', max_length=100)
    FHA_balance2 = forms.CharField(label='FHA', max_length=100)
    FHA_agente = forms.CharField(label='FHA', max_length=100)
    GAV_balance1 = forms.CharField(label='GAV', max_length=100)
    GAV_balance2 = forms.CharField(label='GAV', max_length=100)
    GAV_agente = forms.CharField(label='GAV', max_length=100)
    convencionales_balance1 = forms.CharField(label='Convencionales', max_length=100)
    convencionales_balance2 = forms.CharField(label='Convencionales', max_length=100)
    convencionales_agente = forms.CharField(label='Convencionales', max_length=100)
    otras_instituciones_balance1 = forms.CharField(label='Otras Instituciones', max_length=100)
    otras_instituciones_balance2 = forms.CharField(label='Otras Instituciones', max_length=100)
    otras_instituciones_agente = forms.CharField(label='Otras Instituciones', max_length=100)
    prestamos_hipo_balance1 = forms.CharField(label='Préstamos Hipotecarios', max_length=100)
    prestamos_hipo_balance2 = forms.CharField(label='Préstamos Hipotecarios', max_length=100)
    prestamos_hipo_agente = forms.CharField(label='Préstamos Hipotecarios', max_length=100)
    prestamos_comerciales_industriales_balance1 = forms.CharField(label='Préstamos Comerciales e Industriales', max_length=100)
    prestamos_comerciales_industriales_balance2 = forms.CharField(label='Préstamos Comerciales e Industriales', max_length=100)
    prestamos_comerciales_industriales_agente = forms.CharField(label='Préstamos Comerciales e Industriales', max_length=100)
    prestamos_poliza_balance1 = forms.CharField(label='Préstamos con Póliza', max_length=100)
    prestamos_poliza_balance2 = forms.CharField(label='Préstamos con Póliza', max_length=100)
    prestamos_poliza_agente = forms.CharField(label='Préstamos con Póliza', max_length=100)
    reservas_poliza_balance1 = forms.CharField(label='Reservas con Póliza', max_length=100)
    reservas_poliza_balance2 = forms.CharField(label='Reservas con Póliza', max_length=100)
    reservas_poliza_agente = forms.CharField(label='Reservas con Póliza', max_length=100)
    dividendos_poliza_balance1 = forms.CharField(label='Dividendos con Póliza', max_length=100)
    dividendos_poliza_balance2 = forms.CharField(label='Dividendos con Póliza', max_length=100)
    dividendos_poliza_agente = forms.CharField(label='Dividendos con Póliza', max_length=100)
    nombre_firma = forms.CharField(label='Nombre', max_length=100)
    phone = forms.CharField(label='Teléfono', max_length=100)
    nombre_persona = forms.CharField(label='Nombre de la persona que llena el cuestionario', max_length=100)
    


class JP_375(forms.Form):
    year_1 = forms.CharField(label='Año / Year', max_length=100)
    year_2 = forms.CharField(label='Año / Year', max_length=100)
    year_3 = forms.CharField(label='Año / Year', max_length=100)
    
    FHA_1 = forms.CharField(label='1. F.H.A.', max_length=100)
    FHA_2 = forms.CharField(label='1. F.H.A.', max_length=100)
    FHA_3 = forms.CharField(label='1. F.H.A.', max_length=100)
    
    veteran_1 = forms.CharField(label='2. Adm. de Veteranos', max_length=100)
    veteran_2 = forms.CharField(label='2. Adm. de Veteranos', max_length=100)
    veteran_3 = forms.CharField(label='2. Adm. de Veteranos', max_length=100)
    
    bank_1 = forms.CharField(label='3. Banco de la Vivienda', max_length=100)
    bank_2 = forms.CharField(label='3. Banco de la Vivienda', max_length=100)
    bank_3 = forms.CharField(label='3. Banco de la Vivienda', max_length=100)
    
    conventional_1 = forms.CharField(label='4. Convencionales', max_length=100)
    conventional_2 = forms.CharField(label='4. Convencionales', max_length=100)
    conventional_3 = forms.CharField(label='4. Convencionales', max_length=100)
    
    other_1 = forms.CharField(label='5. Otras', max_length=100)
    other_2 = forms.CharField(label='5. Otras', max_length=100)
    other_3 = forms.CharField(label='5. Otras', max_length=100)
    
    FHA_2_1 = forms.CharField(label='1) F.H.A.', max_length=100)
    FHA_2_2 = forms.CharField(label='1) F.H.A.', max_length=100)
    FHA_2_3 = forms.CharField(label='1) F.H.A.', max_length=100)
    
    veteran_2_1 = forms.CharField(label='2) Adm. de Veteranos', max_length=100)
    veteran_2_2 = forms.CharField(label='2) Adm. de Veteranos', max_length=100)
    veteran_2_3 = forms.CharField(label='2) Adm. de Veteranos', max_length=100)
    
    conventional_2_1 = forms.CharField(label='3) Convencionales', max_length=100)
    conventional_2_2 = forms.CharField(label='3) Convencionales', max_length=100)
    conventional_2_3 = forms.CharField(label='3) Convencionales', max_length=100)
    
    others_2_1 = forms.CharField(label='4) Otras', max_length=100)
    others_2_2 = forms.CharField(label='4) Otras', max_length=100)
    others_2_3 = forms.CharField(label='4) Otras', max_length=100)
    
    FHA_3_1 = forms.CharField(label='1) F.H.A.', max_length=100)
    FHA_3_2 = forms.CharField(label='1) F.H.A.', max_length=100)
    FHA_3_3 = forms.CharField(label='1) F.H.A.', max_length=100)
    
    veteran_3_1 = forms.CharField(label='2) Adm. de Veteranos', max_length=100)
    veteran_3_2 = forms.CharField(label='2) Adm. de Veteranos', max_length=100)
    veteran_3_3 = forms.CharField(label='2) Adm. de Veteranos', max_length=100)
    
    bank_2_1 = forms.CharField(label='3) Banco de la Vivienda', max_length=100)
    bank_2_2 = forms.CharField(label='3) Banco de la Vivienda', max_length=100)
    bank_2_3 = forms.CharField(label='3) Banco de la Vivienda', max_length=100)
    
    conventional_3_1 = forms.CharField(label='4) Convencionales', max_length=100)
    conventional_3_2 = forms.CharField(label='4) Convencionales', max_length=100)
    conventional_3_3 = forms.CharField(label='4) Convencionales', max_length=100)
    
    others_3_1 = forms.CharField(label='5) Otras', max_length=100) 
    others_3_2 = forms.CharField(label='5) Otras', max_length=100)
    others_3_3 = forms.CharField(label='5) Otras', max_length=100)

    FHA_4_1 = forms.CharField(label='1) F.H.A.', max_length=100)
    FHA_4_2 = forms.CharField(label='1) F.H.A.', max_length=100)
    FHA_4_3 = forms.CharField(label='1) F.H.A.', max_length=100)
    
    veteran_4_1 = forms.CharField(label='2) Adm. de Veteranos', max_length=100)
    veteran_4_2 = forms.CharField(label='2) Adm. de Veteranos', max_length=100)
    veteran_4_3 = forms.CharField(label='2) Adm. de Veteranos', max_length=100)
    
    conventional_4_1 = forms.CharField(label='3) Convencionales', max_length=100)
    conventional_4_2 = forms.CharField(label='3) Convencionales', max_length=100)
    conventional_4_3 = forms.CharField(label='3) Convencionales', max_length=100)
    
    others_4_1 = forms.CharField(label='4) Otras', max_length=100)
    others_4_2 = forms.CharField(label='4) Otras', max_length=100)
    others_4_3 = forms.CharField(label='4) Otras', max_length=100)

    commissions_1 = forms.CharField(label='b) Comisiones Recibidas de No-Residentes 3/', max_length=100)
    commissions_2 = forms.CharField(label='b) Comisiones Recibidas de No-Residentes 3/', max_length=100)
    commissions_3 = forms.CharField(label='b) Comisiones Recibidas de No-Residentes 3/', max_length=100)
    
    phone = forms.CharField(label='Phone Number', max_length=100)
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    position = forms.CharField(label='Position', max_length=100)
    
class IP_480(forms.Form):
    company_name = forms.CharField(label='Nombre compañía / Company Name', max_length=100)
    address = forms.CharField(label='Dirección / Address', max_length=200)
    email = forms.EmailField(label='Correo electrónico / Email') 
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    ssn = forms.CharField(label='Numero de Seguro Social / Social Security Number', max_length=11)
    tel = forms.CharField(label='Tel', max_length=20)
    fax = forms.CharField(label='Fax', max_length=20)
    legal_form = forms.ChoiceField(
        label='Forma legal de organización / Legal form of organization', 
        choices=[('Corporación', 'Corporación'), ('Sociedad', 'Sociedad'), ('Cooperativa', 'Cooperativa'), ('Empresa Individual', 'Empresa Individual'), ('Empresa sin fines pecuniarios', 'Empresa sin fines pecuniarios')]
    )
    cfc = forms.ChoiceField(label='CEC', choices=[('Si', 'Si'), ('No', 'No')])
    business_function = forms.CharField(
        label='Describa brevemente la función principal del negocio / Explain briefly the main function of the business activity', 
        widget=forms.Textarea
    )
    closing_date = forms.DateField(label='Fecha de cierre de sus libros / Your accounting period closing date', widget=forms.SelectDateWidget)
    operation_incomes_1 = forms.CharField(label='1. Ingresos por proyecto - Income from project'),
    operation_incomes_2 = forms.CharField(label='1. Ingresos por proyecto - Income from project'),
    people_A_1 = forms.CharField(label='2. A personas - To persons'),
    people_A_2 = forms.CharField(label='2. A personas - To persons'),
    industries_businesses_A_1 = forms.CharField(label='3. A industrias y negocios - To industries and businesses'),
    industries_businesses_A_2 = forms.CharField(label='3. A industrias y negocios - To industries and businesses'),
    incomes_interests_1 = forms.CharField(label='4. Ingresos por intereses - Income from interests'),
    incomes_interests_2 = forms.CharField(label='4. Ingresos por intereses - Income from interests'),
    incomes_rents_1 = forms.CharField(label='5. Ingresos por alquileres - Income from rents'),
    incomes_rents_2 = forms.CharField(label='5. Ingresos por alquileres - Income from rents'),
    dividends_1 = forms.CharField(label='6. Dividendos - Dividends'),
    dividends_2 = forms.CharField(label='6. Dividendos - Dividends'),
    others_incomes_1 = forms.CharField(label='7. Otros ingresos - Other incomes'),
    others_incomes_2 = forms.CharField(label='7. Otros ingresos - Other incomes'),
    total_incomes_1 = forms.CharField(label='Total de ingresos - Total incomes'),
    total_incomes_2 = forms.CharField(label='Total de ingresos - Total incomes'),
    expenses_1 = forms.CharField(label='1. Gastos - Expenses'),
    expenses_2 = forms.CharField(label='1. Gastos - Expenses'),
    salaries_1 = forms.CharField(label='2. Salarios - Salaries'),
    salaries_2 = forms.CharField(label='2. Salarios - Salaries'),
    expenses_interests_1 = forms.CharField(label='3. Gastos por intereses - Expenses from interests'),
    expenses_interests_2 = forms.CharField(label='3. Gastos por intereses - Expenses from interests'),
    expenses_rents_1 = forms.CharField(label='4. Gastos por alquileres - Expenses from rents'),
    expenses_rents_2 = forms.CharField(label='4. Gastos por alquileres - Expenses from rents'),
    depreciation_1 = forms.CharField(label='5. Depreciación - Depreciation'),
    depreciation_2 = forms.CharField(label='5. Depreciación - Depreciation'),
    donations_1 = forms.CharField(label='6. Donaciones - Donations'),
    donations_2 = forms.CharField(label='6. Donaciones - Donations'),
    sales_tax_1 = forms.CharField(label='7. Impuesto sobre ventas - Sales tax'),
    sales_tax_2 = forms.CharField(label='7. Impuesto sobre ventas - Sales tax'),
    machinery_1 = forms.CharField(label='8. Maquinaria - Machinery'),
    machinery_2 = forms.CharField(label='8. Maquinaria - Machinery'),
    other_purchases_1 = forms.CharField(label='9. Otras compras - Other purchases'),
    other_purchases_2 = forms.CharField(label='9. Otras compras - Other purchases'),
    licenses_1 = forms.CharField(label='10. Licencias - Licenses'),
    licenses_2 = forms.CharField(label='10. Licencias - Licenses'),
    other_expenses_1 = forms.CharField(label='11. Otros gastos - Other expenses'),
    other_expenses_2 = forms.CharField(label='11. Otros gastos - Other expenses'),
    total_expenses_1 = forms.CharField(label='Total de gastos - Total expenses'),
    total_expenses_2 = forms.CharField(label='Total de gastos - Total expenses'),
    net_profit_1 = forms.CharField(label='Utilidad neta - Net profit'),
    net_profit_2 = forms.CharField(label='Utilidad neta - Net profit'),
    income_tax_1 = forms.CharField(label='Impuesto sobre la renta - Income tax'),
    income_tax_2 = forms.CharField(label='Impuesto sobre la renta - Income tax'),
    profit_after_tax_1 = forms.CharField(label='Utilidad después de impuestos - Profit after tax'),
    profit_after_tax_2 = forms.CharField(label='Utilidad después de impuestos - Profit after tax'),
    withheld_tax_1 = forms.CharField(label='Impuesto retenido - Withheld tax'),
    withheld_tax_2 = forms.CharField(label='Impuesto retenido - Withheld tax'),
    signature = forms.CharField(label='Name of person filling the questionnaire', max_length=100)
    rank = forms.CharField(label='Rank', max_length=100)
    
    
class IP_420(forms.Form):
    company_name = forms.CharField(label='Nombre compañía / Company Name', max_length=100)
    address = forms.CharField(label='Dirección / Address', max_length=200)
    email = forms.EmailField(label='Correo electrónico / Email')
    liaison_officer = forms.CharField(label='Persona contacto / Liaison officer', max_length=100)
    ssn = forms.CharField(label='Numero de Seguro Social / Social Security Number', max_length=11)
    tel = forms.CharField(label='Tel', max_length=20)
    fax = forms.CharField(label='Fax', max_length=20)
    legal_form = forms.ChoiceField(
        label='Forma legal de organización / Legal form of organization', 
        choices=[('Corporación', 'Corporación'), ('Sociedad', 'Sociedad'), 
                 ('Cooperativa', 'Cooperativa'), ('Empresa Individual', 
                'Empresa Individual'), ('Empresa sin fines pecuniarios', 
                'Empresa sin fines pecuniarios')]
    )
    cfc = forms.ChoiceField(label='CEC', choices=[('Si', 'Si'), ('No', 'No')])
    main_line = forms.CharField(label='4. Línea principal de mercancía vendida por esta firma / Main line of merchandise sold by the firm:', max_length=200)
    business_type = forms.ChoiceField(
        label = "5. Clase de negocio / Type of business:",
        choices = [('Distribuidor', 'Distribuidor'), ('Representante', 
                'Representative'), ('Mayorista', 'Wholesaler'), 
                   ('Supermercado', 'Supermarket')]
    )
    other_business_type = forms.CharField(label='Otro (especifique) / Other (specify)', max_length=100)
    accounting_period = forms.CharField(label='6. Fecha de detallar la siguiente informacion / Your accounting period closing date:', max_length=100)
    
    sales_A_1 = forms.CharField(label='1. Ventas - Sales', max_length=100)
    sales_A_2 = forms.CharField(label='1. Ventas - Sales', max_length=100)
    
    people_A_1 = forms.CharField(label='a. De personas - To persons', max_length=100)
    people_A_2 = forms.CharField(label='a. De personas - To persons', max_length=100)
    
    industries_businesses_A_1 = forms.CharField(label='b. De industrias y negocios - To industries and businesses', max_length=100)
    industries_businesses_A_2 = forms.CharField(label='b. De industrias y negocios - To industries and businesses', max_length=100)
    
    less_cost_A_1 = forms.CharField(label='2. Menos costo de ventas - Less cost of sales', max_length=100)
    less_cost_A_2 = forms.CharField(label='2. Menos costo de ventas - Less cost of sales', max_length=100)
    
    inventory_beginning_1 = forms.CharField(label='a. Inventario al principio de año- Inventory at beginning of the year', max_length=100)
    inventory_beginning_2 = forms.CharField(label='a. Inventario al principio de año- Inventory at beginning of the year', max_length=100)
    
    purchases_A_1 = forms.CharField(label='b. Compras - Purchases', max_length=100)
    purchases_A_2 = forms.CharField(label='b. Compras - Purchases', max_length=100)
    
    inventory_end_1 = forms.CharField(label='c. Inventario al final año- Inventory at end of the year', max_length=100)
    inventory_end_2 = forms.CharField(label='c. Inventario al final año- Inventory at end of the year', max_length=100)
    
    gross_profit_A_1 = forms.CharField(label='3.Beneficio bruto (1 - 2) / Gross profit (1 - 2)', max_length=100)
    gross_profit_A_2 = forms.CharField(label='3.Beneficio bruto (1 - 2) / Gross profit (1 - 2)', max_length=100)
    
    other_income_A_1 = forms.CharField(label='4. Otros ingresos de operación / Other operationg income', max_length=100)
    other_income_A_2 = forms.CharField(label='4. Otros ingresos de operación / Other operationg income', max_length=100)
    
    interests_A_1 = forms.CharField(label='a. Intereses - Interests', max_length=100)
    interests_A_2 = forms.CharField(label='a. Intereses - Interests', max_length=100)
    
    rent_A_1 = forms.CharField(label='b. Renta de terreno y edificio / Rent of land and building', max_length=100)
    rent_A_2 = forms.CharField(label='b. Renta de terreno y edificio / Rent of land and building', max_length=100)
    
    capital_gain_A_1 = forms.CharField(label='c. Ganancia o pérdida de capital / Capital gain or loss', max_length=100)
    capital_gain_A_2 = forms.CharField(label='c. Ganancia o pérdida de capital / Capital gain or loss', max_length=100)
    
    dividends_A_1 = forms.CharField(label='d. Dividendos - Dividends', max_length=100)
    dividends_A_2 = forms.CharField(label='d. Dividendos - Dividends', max_length=100)
    
    total_gross_A_1 = forms.CharField(label='5. Total de ingresos brutos (3 + 4) / Total gross income (3 + 4)', max_length=100)
    total_gross_A_2 = forms.CharField(label='5. Total de ingresos brutos (3 + 4) / Total gross income (3 + 4)', max_length=100)
    
    cost_B_1 = forms.CharField(label='B. total costos directos e indirectos - Direct and indirect costs', max_length=100)
    cost_B_2 = forms.CharField(label='B. total costos directos e indirectos - Direct and indirect costs', max_length=100)
    
    salaries_B_1 = forms.CharField(label='1. Salario, jornales, bono de Navidad y comiciones / Salaries, wages, Christmas bonus and comissions', max_length=100)
    salaries_B_2 = forms.CharField(label='1. Salario, jornales, bono de Navidad y comiciones / Salaries, wages, Christmas bonus and comissions', max_length=100)
    
    interests_B_1 = forms.CharField(label='2. Intereses - Interests', max_length=100)
    interests_B_2 = forms.CharField(label='2. Intereses - Interests', max_length=100)
    
    depreciation_B_1 = forms.CharField(label='3. Depreciación - Depreciation', max_length=100)
    depreciation_B_2 = forms.CharField(label='3. Depreciación - Depreciation', max_length=100)
    
    rent_B_1 = forms.CharField(label='4. Renta de terreno y edificio - Rent of land and building', max_length=100)
    rent_B_2 = forms.CharField(label='4. Renta de terreno y edificio - Rent of land and building', max_length=100)
    
    bad_debts_B_1 = forms.CharField(label='5. Cuenta incobrables / bad debts', max_length=100)
    bad_debts_B_2 = forms.CharField(label='5. Cuenta incobrables / bad debts', max_length=100)
    
    donations_B_1 = forms.CharField(label='6. Donaciones - Donations', max_length=100)
    donations_B_2 = forms.CharField(label='6. Donaciones - Donations', max_length=100)
    
    sales_B_1 = forms.CharField(label='7. Impuesto sobre la venta y uso / Sales and use tax', max_length=100)
    sales_B_2 = forms.CharField(label='7. Impuesto sobre la venta y uso / Sales and use tax', max_length=100)
    
    purchases_B_1 = forms.CharField(label='a. Por Compra de maquinaria y equipo / On purchases of machinery and equipment', max_length=100)
    purchases_B_2 = forms.CharField(label='a. Por Compra de maquinaria y equipo / On purchases of machinery and equipment', max_length=100)
    
    other_purchases_B_1 = forms.CharField(label='b. Por otras compras / On other purchases', max_length=100)
    other_purchases_B_2 = forms.CharField(label='b. Por otras compras / On other purchases', max_length=100)
    
    licenses_B_1 = forms.CharField(label='8. Licencias y patentes - Licenses and patents', max_length=100)
    licenses_B_2 = forms.CharField(label='8. Licencias y patentes - Licenses and patents', max_length=100)
    
    other_operations_B_1 = forms.CharField(label='9. Otras operaciones - Other operations', max_length=100)
    other_operations_B_2 = forms.CharField(label='9. Otras operaciones - Other operations', max_length=100)
    
    gross_profit_C_1 = forms.CharField(label='C. Beneficio bruto (A-B) - Gross profit (A-B', max_length=100)
    gross_profit_C_2 = forms.CharField(label='C. Beneficio bruto (A-B) - Gross profit (A-B', max_length=100)
    
    income_C_1 = forms.CharField(label='1. Contribución sobre ingresos / Income tax', max_length=100)
    income_C_2 = forms.CharField(label='1. Contribución sobre ingresos / Income tax', max_length=100)
    
    profit_C_after_1 = forms.CharField(label='2. Ganacia después de contribución sobre ingresos / Profit after income tax', max_length=100)
    profit_C_after_2 = forms.CharField(label='2. Ganacia después de contribución sobre ingresos / Profit after income tax', max_length=100)
    
    sales_D_1 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido / Sales and use tax Withheld', max_length=100)
    sales_D_2 = forms.CharField(label='D. Impuesto sobre ventas y uso retenido / Sales and use tax Withheld', max_length=100)
    
    name = forms.CharField(label='Nombre de persona que suministra la información Name of person furnishing information', max_length=100)
    rank = forms.CharField(label='Rango o posición que ocupa en la empresa Rank or position', max_length=100)