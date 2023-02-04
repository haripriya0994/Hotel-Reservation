import streamlit as st
import pandas as pd
st.title('Hotel Booking Cancellation Predictor 🏨')
import pickle 

# Step 1: load the pickled model
model = open('rf.pickle','rb')
rfmodel=pickle.load(model)
model.close()

# Step 2: create a UI for front end user
from PIL import Image
no_of_adults = st.sidebar.slider('Enter Number of adults',1,25)
no_of_children=st.sidebar.slider('Enter Number of children',1,20)
no_of_weekend_nights=st.sidebar.slider('Enter number of Weekend stays',1,30)
no_of_week_nights= st.sidebar.slider('Enter number of Weekday stays',1,30)
type_of_meal_plan=st.sidebar.selectbox('Enter the type of meal',('Meal Plan 1', 'Not Selected', 'Meal Plan 2', 'Meal Plan 3'))
required_car_parking_space= st.sidebar.radio('Enter whether space for car parking is required',(1,0))
room_type_reserved = st.sidebar.selectbox('Enter the type of room you want',('Room_Type 1', 'Room_Type 4', 'Room_Type 2', 'Room_Type 6',
       'Room_Type 5', 'Room_Type 7', 'Room_Type 3'))
lead_time = st.sidebar.slider('Enter Lead Time',1,400)
arrival_year =  st.sidebar.radio('Select the arrival year',(2017,2018))
arrival_month =  st.sidebar.radio('Select the arrival month',(1,2,3,4,5,6,7,8,9,10,11,12))
arrival_date =  st.sidebar.slider('Select the arrival date',1,31)
market_segment_type=  st.sidebar.radio('Select the market segment type ',('Offline', 'Online', 'Corporate', 'Aviation', 'Complementary'))
repeated_guest=  st.sidebar.radio('Are you a repeated guest',(1,0))
no_of_previous_cancellations=  st.sidebar.slider('Enter the previous canellations',1,35)
no_of_previous_bookings_not_canceled= st.sidebar.slider('Enter the previous booking that are not cancelled',1,35)
avg_price_per_room=st.sidebar.slider('Enter the average price per room',10,700)
no_of_special_requests = st.sidebar.slider('Enter the number of special guests',1,15)


# Step 3: Change user input as models input data
data={
'no_of_adults' : no_of_adults,
'no_of_children': no_of_children,
'no_of_weekend_nights': no_of_weekend_nights,
'no_of_week_nights': no_of_week_nights,
'type_of_meal_plan': type_of_meal_plan,
'required_car_parking_space': required_car_parking_space,
'room_type_reserved' : room_type_reserved,
'lead_time' : lead_time,
'arrival_year' : arrival_year,
'arrival_month': arrival_month,
'arrival_date': arrival_date,
'market_segment_type':market_segment_type,
'repeated_guest': repeated_guest,
'no_of_previous_cancellations': no_of_previous_cancellations ,
'no_of_previous_bookings_not_canceled' : no_of_previous_bookings_not_canceled,                   
'avg_price_per_room': avg_price_per_room,
'no_of_special_requests':  no_of_special_requests
}

input_data = pd.DataFrame([data])
predictions = rfmodel.predict(input_data)
if st.button('Predict'):
    if predictions=='Not_Canceled':
        st.success('This Person is not likely to cancel')
    if predictions=='Canceled':
        st.error('High Chances of customer cancellation')
