import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px  # interactive charts


st.set_page_config(
    page_title="Water - contaminants and levels Dashboard",
    #page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")


# dashboard title
st.title("Water - contaminants and levels Dashboard")
st.markdown("---------------------------------------------------------------")


#read the file
Mod_data = pd.read_csv('integrated_water_related_data.csv')


st.markdown("""
<style>
.big-font {  font-size:25px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.mid-font {  font-size:20px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="mid-font">Study of water contaminants has shed light on the pivotal role of wastewater as the strongest global metric impacting various facets of the environment and human health</p>', unsafe_allow_html=True)

st.markdown('<p class="big-font">Wastewater discharge comprises of three different sources </p>', unsafe_allow_html=True )
st.markdown('<p class="mid-font">1. Agricultural</p>', unsafe_allow_html=True )
st.markdown('<p class="mid-font">2. Urban</p>', unsafe_allow_html=True )
st.markdown('<p class="mid-font">3. Industrial</p>', unsafe_allow_html=True )
st.subheader("")
st.subheader("")

st.markdown('<p class="big-font">Breakdown of Total Wastewater discharged without treatment</p>', unsafe_allow_html=True)

st.bar_chart(Mod_data, x='Entity', y = ["Agricultural (incl. forestry + fisheries) wastewater, all sources, direct discharges(million m3)", "Urban wastewater, all sources, discharged without treatment(million m3)","Industrial wastewater, all sources, discharged without treatment(million m3)"] )


st.subheader("Interconnectedness between Wastewater contamination and adverse impacts")

st.markdown("")
st.markdown("")


#button_col1, button_col2 = st.columns(2)
#with button_col1:
#                if st.button("Public health"):
 #                   st.switch_page("//Pages//Public_Health.py")
#with button_col2:
 #               if st.button("Ecosystem"):
 #                    st.switch_page("//Pages//Ecosystem.py")



st.subheader("Countries having Wastewater discharged without treatment")
st.map(Mod_data)

st.markdown("")

st.subheader("Histogram of Total Wastewater discharged without treatment")
fig2 = px.histogram(data_frame=Mod_data, x="Year", y ="Total Wastewater" )
st.write(fig2)

st.markdown("")

st.title("Public Health impacted due to Wastewater")
st.markdown("---------------------------------------------------------------")



#Create a sidebar for year dropdown selection
with st.sidebar:
     st.title('Water - contaminants and levels Dashboard')
    
     years = list(Mod_data.Year.unique())[::-1]
    
     selected_year = st.selectbox('Select year to view', years)
     df_year_selected = Mod_data[Mod_data.Year == selected_year]
     df_year_selected_sorted = df_year_selected.sort_values(by="Entity", ascending=False)




st.markdown("It was found that by increasing the volume of urban wastewater premature deaths rise by approximately 0.844, highlighting significant health risks from inadequate wastewater management.")
st.markdown("")



st.subheader("Correlation between Premature Deaths and Total Wastewater discharged without treatment for selected year")
st.markdown("")
st.line_chart(df_year_selected, x="Entity", y=["Total Wastewater","Premature_Death_Count" ], color=["#FF0000", "#0000FF"]  # Optional
)
st.markdown("")
st.markdown("")


st.subheader("Correlation between Premature Deaths and Urban Wastewater discharged without treatment for selected year")
st.markdown("")
st.line_chart(df_year_selected, x="Entity", y=["Urban wastewater, all sources, discharged without treatment(million m3)","Premature_Death_Count" ], color=["#FF0000", "#0000FF"]  # Optional
)
st.markdown("")
st.markdown("")

st.subheader("Correlation between Premature Deaths and Agricultural Wastewater discharged without treatment for selected year")
st.markdown("")
st.line_chart(df_year_selected, x="Entity", y=["Agricultural (incl. forestry + fisheries) wastewater, all sources, direct discharges(million m3)","Premature_Death_Count" ], color=["#FF0000", "#0000FF"]  # Optional
)
st.markdown("")
st.markdown("")

st.subheader("Correlation between Premature Deaths and Agricultural Wastewater discharged without treatment for selected year")
st.markdown("")
st.line_chart(df_year_selected, x="Entity", y=["Industrial wastewater, all sources, discharged without treatment(million m3)","Premature_Death_Count" ], color=["#FF0000", "#0000FF"]  # Optional
)


st.subheader("Correlation between Premature Deaths and Total Wastewater discharged without treatment from 2015-2019")
st.markdown("")
st.scatter_chart(Mod_data, x="Entity", y=["Total Wastewater","Premature_Death_Count" ], color=["#FF0000", "#0000FF"]  # Optional
)

st.markdown("")
st.markdown("")
st.markdown("")


st.title("Ecosystem impacted due to Wastewater")
st.markdown("---------------------------------------------------------------")

st.subheader("Correlation between Total Wastewater discharged without treatment and Total discharges to Inland waters for selected year")
st.markdown("")
st.line_chart(df_year_selected, x="Entity", y=["Total Wastewater","Total discharges to Inland waters(million m3)" ], color=["#FF0000", "#0000FF"]  # Optional
)
st.markdown("")
st.markdown("")


st.subheader("Correlation between Total Wastewater discharged without treatment and Total discharges to the sea for selected year")
st.markdown("")
st.line_chart(df_year_selected, x="Entity", y=["Total Wastewater","Total discharges to the sea(million m3)" ], color=["#FF0000", "#0000FF"]  # Optional
)
st.markdown("")
st.markdown("")

st.subheader("Correlation between  Total Wastewater, Total discharges to the sea and Total discharges to Inland waters from 2015-2019")
st.markdown("")
st.scatter_chart(Mod_data, x="Entity", y=["Total Wastewater","Total discharges to the sea(million m3)","Total discharges to Inland waters(million m3)" ], color=["#FF0000", "#0000FF","#0CC80C"]  # Optional
)

st.markdown("")


st.subheader('Thank you for visiting :smiley:')

