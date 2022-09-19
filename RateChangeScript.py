import streamlit as st
import pandas as pd



# function definition to highlight columns
def highlight_cols(x):

                   
    df = x.copy()
    df.loc[:, :] = 'background-color: lightgrey' 
    df[['Projected IFP Rate Change']] = 'background-color: cornflowerblue'
    df.style.hide_index()
    return df 

st.markdown(
    """
<style>
span[data-baseweb="tag"] {
  background-color: blue !important;
}
</style>
""",
    unsafe_allow_html=True,
)


def convert_df(df):
    return df.to_csv().encode('utf-8')


st.image('zizzl health logo 22.png')

st.title('Projected IFP Rate Changes 2023')



df = pd.read_csv(r'2023RateChangeData.csv')

#Selector
States = st.multiselect('Pick States', ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Conneticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hamshire', 'New Jersey', 'New Mexico', 'New York', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'])

final_df = pd.DataFrame()

for i in States:
    st.subheader(i)
    choice = df.loc[df['State'] == i]
    
    for j in choice.count(axis=0):
        x = choice['Projected IFP Rate Change'].str.slice(0, -1, 1).astype(float)
    st.write("Average Rate Change : " ,str(round(x.sum()/j,2)), "%")

    choice = choice.set_index('Insurer')

    st.table(choice[['Projected IFP Rate Change', 'Minimum Rate Change', 'Maximum Rate Change']].style.apply(highlight_cols, axis = None))

    final_df = pd.concat([final_df, choice[['State','Projected IFP Rate Change','Minimum Rate Change','Maximum Rate Change']]], axis=0)  # This line concatonates 


csv = convert_df(final_df)

if len(final_df) != 0:

    st.download_button(
        label = "Download data as CSV",
        data = csv,
        file_name = 'Rate_Changes.csv',
        mime='text/csv'
    )
with st.expander("KEY"):
    st.write("""
        **IFP** =  Individual & Family Plan (health insurance)
    """)

    st.write("""
        **Projected 2023 IFP Rate Change** =  The average health insurance premium increase or decrease applied from the 2022 to 2023 plan years for ACA regulated IFP health insurance products.
    """)
st.subheader('Disclaimer:')
st.write(' **This tool is for internal zizzl health reseller use ONLY and is not to be shared with anyone outside of an approved reseller organization.** Data for the analysis was provided by healthcare.gov and reflects proposed health insurance rate changes for ACA-compliant Individual & Family Plans (IFPs) for the upcoming plan year. This tool does not reflect finalized 2023 IFP rates as only proposed rates are available at the time of publishing. The analysis is for informational purposes and does not constitute opinions or guidance from zizzl health. The health insurance carrier names above represent entity names on file with healthcare.gov. Insurers may market their products under multiple unique brand names. ')


    