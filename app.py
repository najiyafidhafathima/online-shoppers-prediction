import streamlit as st
import pandas as pd
import joblib
model=joblib.load('online_shoppers_model.pkl')
month_encoder=joblib.load('month_encoder.pkl')
visitor_encoder=joblib.load('visitor_encoder.pkl')
st.title('Online Shoppers Purchasing Intention Prediction')
st.write('Enter the visitor details to predict whether the visitor will make a purchase.')
Administrative=st.number_input('Administrative',min_value=0,value=0)
Administrative_Duration=st.number_input(
    'Administrative Duration',min_value=0.0,value=0.0
)
Informational=st.number_input('Informational',min_value=0,value=0)
Informational_Duration=st.number_input(
    'Informational Duration',min_value=0.0,value=0.0
)
Product_Related=st.number_input('Product Related',min_value=0,value=0)
Product_Related_Duration=st.number_input(
    'Product Related Duration',min_value=0.0,value=0.0
)
BounceRates=st.number_input(
    'Bounce Rate',min_value=0.0,value=0.0
)
ExitRates=st.number_input(
    'Exit Rate',min_value=0.0,value=0.0
)
PageValues=st.number_input(
    'Page Values',min_value=0.0,value=0.0
)
SpecialDay=st.number_input(
    'Special Day',min_value=0.0,value=0.0
)
Month = st.selectbox(
    "Month",
    month_encoder.classes_
)

OperatingSystems = st.number_input(
    "Operating Systems", min_value=1, value=1
)

Browser = st.number_input(
    "Browser", min_value=1, value=1
)

Region = st.number_input(
    "Region", min_value=1, value=1
)

TrafficType = st.number_input(
    "Traffic Type", min_value=1, value=1
)

VisitorType = st.selectbox(
    "Visitor Type",
    visitor_encoder.classes_
)

Weekend = st.selectbox(
    "Weekend",
    [False, True])

if st.button("Predict Purchase"):

    Month_encoded = month_encoder.transform([Month])[0]
    VisitorType_encoded = visitor_encoder.transform([VisitorType])[0]

    input_data = pd.DataFrame([[
        Administrative,
        Administrative_Duration,
        Informational,
        Informational_Duration,
        Product_Related,
        Product_Related_Duration,
        BounceRates,
        ExitRates,
        PageValues,
        SpecialDay,
        Month_encoded,
        OperatingSystems,
        Browser,
        Region,
        TrafficType,
        VisitorType_encoded,
        Weekend
    ]], columns=[
        'Administrative',
        'Administrative_Duration',
        'Informational',
        'Informational_Duration',
        'ProductRelated',
        'ProductRelated_Duration',
        'BounceRates',
        'ExitRates',
        'PageValues',
        'SpecialDay',
        'Month',
        'OperatingSystems',
        'Browser',
        'Region',
        'TrafficType',
        'VisitorType',
        'Weekend'
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("The visitor is likely to make a purchase.")
    else:
        st.info("The visitor is unlikely to make a purchase.")