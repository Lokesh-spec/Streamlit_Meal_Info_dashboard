import pandas as pd
import time
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from streamlit.proto.Balloons_pb2 import Balloons



st.balloons()

st.markdown("# Titanic Data Visualization")

@st.cache
def load_dataset(data_link):
    dataset = pd.read_csv(data_link)
    return dataset

titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data = load_dataset(titanic_link)

st.dataframe(titanic_data)

selected_class = st.radio('Select Class', titanic_data['class'].unique())
st.write("Selected Class:", selected_class)
st.write("Selected Class Type:", type(selected_class))

selected_sex = st.selectbox("Select Sex",
titanic_data["sex"].unique())
st.write(f'Selected Option: {selected_sex!r}')

selected_decks = st.multiselect("Select Decks",
titanic_data['deck'].unique())
st.write("Selected Decks:", selected_decks)

age_columns = st.beta_columns(2)
age_min = age_columns[0].number_input("Minimum Age", value=titanic_data['age'].min())
age_max = age_columns[0].number_input("Maximum Age", value=titanic_data['age'].max())

if age_max < age_min:
    st.error("The maximum age can't be smaller than the minimum age!")
else:
    st.success("Congratulations! Correct Parameters!")
    subset_age = titanic_data[(titanic_data['age'] <= age_max) & (age_min <= titanic_data['age'])]
    st.write(f'Number of Records With Age Between {age_min} and {age_max}: {subset_age.shape[0]}')


optionals = st.beta_expander("Optional Configurations", True)
fare_min = optionals.slider(
    "Minimum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Maximum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]
st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")

with st.echo('below'):
    balloons = st.text_area('Please enter awesome to see some ballons')
    if balloons == 'awesome':
        st.balloons()

st.write("This is a large text area.")
st.text_area('A very big area', height=300)



start_button = st.button("Start the Progress")

if start_button:
    progress_bar = st.progress(0)
    progress_text = st.empty()
    for i in range(101):
        time.sleep(0.1)
        progress_bar.progress(i)
        progress_text.text(f'Progress: {i}%')
else:
    st.write("The progress will be starting by clicking the button.")
st.markdown("____")

with st.echo():
    st.markdown("## Level 2 header")
    st.markdown("This is a _markdown_ comment, which is *great* and _**awesome**_. Above the separator.")
    st.markdown("___")
    st.markdown("Here's the link to [Streamlit](https://www.streamlit.io/). Below the separator.")
    st.markdown("```python\nnumbers = [1, 2, 3, 4, 5]\ntexts = ['a', 'b', 'c']")


st.write("Survival By Class")
st.dataframe(pd.crosstab(titanic_data['class'], titanic_data['survived'], normalize='index'))
st.write("Here's the code to generate this table:")
st.code("pd.crosstab(titanic_data['class'], titanic_data['survived'], normalize='index')")

st.write(px.histogram(titanic_data['fare']))


st.markdown("# Food Demand Prediction")

@st.cache
def load_data(nrows):
    data = pd.read_csv('/home/lokesh/Streamlit/App1/train.csv', nrows=nrows)
    return data

@st.cache
def load_center_data(nrows):
    data = pd.read_csv('/home/lokesh/Streamlit/App1/fulfilment_center_info.csv', nrows=nrows)
    return data


@st.cache
def load_meal_data(nrows):
    data = pd.read_csv('/home/lokesh/Streamlit/App1/meal_info.csv', nrows=nrows)
    return data

data_load_state = st.text('Loading Data...')
weekly_data = load_data(1000)
center_info_data = load_center_data(1000)
meal_data = load_meal_data(1000)

st.subheader("Weekly Demand Data")
st.write(weekly_data)

#Bar Chart
st.bar_chart(weekly_data["num_orders"])
df = pd.DataFrame(weekly_data[:200], columns=["num_orders", 'checkout_price', 'base_price'])
df.hist()
plt.show()
st.pyplot()

## Line Chart
st.line_chart(df)

chart_data = pd.DataFrame(weekly_data[:40], columns=['num_orders', 'base_price'])
st.area_chart(chart_data)

st.subheader('Fulfillment Center Information')
if st.checkbox('Show Center Information data'):
    st.subheader('Center Information data')
    st.write(center_info_data)

st.bar_chart(center_info_data['region_code'])
st.bar_chart(center_info_data['center_type'])

#hist_data = [center_info_data['center_id'], center_info_data['region_code']]
#group_labels =['center Id', 'Region Code']
#fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25])
#st.plotly_chart(fig, use_container_width=True)



st.subheader('Meal Information')
st.write(meal_data)

st.bar_chart(meal_data['cuisine'])

agree = st.button('Click to see Categories of Meal')
if agree:
    st.bar_chart(meal_data['category'])