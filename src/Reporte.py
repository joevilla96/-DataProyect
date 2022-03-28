import pandas as pd
import pandas_profiling as ppr
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport


df = pd.read_csv("Data/Data_limpia.csv", na_values=['='])




profile = ProfileReport(df,

                        title="Salario Data",

        dataset={

        "description": "This profiling report was generated for Analytics",

        "copyright_holder": "Analisis por Joel Landaveri",

        "copyright_year": "2022",

        #"url": "https://www.analyticsvidhya.com/blog/",

    },

    variables={

        "descriptions": {

            #"timestamp": "Name of the state",

            "company": "Nombres de las compañías",

            #"title": "Títulos",

            "totalyearlycompensation": "Compensación total anual",

            #"location": "locación",

            #"yearsofexperience": "Años de experiencia",

            #"yearsatcompany": "Años en la compañía",

            #"tag": "Etiqueta",

            "basesalary": "Salario base",

            #"stockgrantvalue": "How much production?",

            #"bonus": "How much production?",

            "gender": "How much production?",

            "Race": "How much production?",
            
            "Education": "How much production?"

        }

    }

)




st.title("Pandas Profiling in Streamlit!")

st.write(df)

st_profile_report(profile)