import streamlit as st
import json
from src.person import Person


with open("data/person_db.json", "r", encoding="utf-8") as f:
    data = json.load(f)

name_to_id = {
    f'{p["lastname"]}, {p["firstname"]}': p["id"]
    for p in data
}

selected_name = st.selectbox(
    "Person auswählen",
    list(name_to_id.keys())
)

selected_id = name_to_id[selected_name]

person = Person.load_by_id(selected_id)


st.title(person.get_full_name())

st.image(person.get_image())

st.write("Alter:", person.calc_age())
st.write("Max HF:", person.calc_max_heart_rate())
st.write("Geschlecht:", person.gender)