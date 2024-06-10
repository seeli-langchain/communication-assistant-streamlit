import streamlit as st
import persisting as repo

@st.experimental_dialog("Confirm Delete")
def confirm_delete(item):
    st.write(f"Are you sure you want to delete {item.title}?")
    c1, c2 = st.columns(2)
    if c1.button("✖️"):
       st.session_state.confirm_delete = False
       st.rerun()
       
    if c2.button("✔️"):
       st.session_state.confirm_delete = True
       st.rerun()


main_person = repo.get_main_person()


if "persona_id" not in st.session_state or st.session_state.persona_id is None:
    st.session_state.persona_id = 0
if "confirm_delete" not in st.session_state :
    st.session_state.confirm_delete = None
if "deleting" not in st.session_state :
    st.session_state.deleting = False

if st.session_state.deleting == False:
    st.session_state.confirm_delete = None

##st.session_state.confirm_delete
#st.session_state.deleting

st.title(f"Personas of {main_person.first_name} {main_person.last_name}")


personas = repo.get_personas_of_main_person()

if personas is None or len(personas) == 0:
    st.warning("No personas found")
    if st.button("➕"):
        new_id = repo.add_persona_for_main_person("").id
        st.session_state.persona_id = new_id
        st.success("Added")
        st.rerun()
    st.stop()


if (st.session_state.persona_id == 0 and len(personas) > 1):
    # we have to show the selection box
    persona_id = st.selectbox("", [persona.id for persona in personas], 
                          format_func=lambda x: repo.get_persona_by_id(x).title, index=None, 
                          placeholder="Select a Persona to edit", label_visibility="collapsed")
    addPersona = st.button("➕")
    if addPersona:
        st.session_state.persona_id = repo.add_persona_for_main_person("").id
        st.success("Added")
        st.rerun()
        
    if (persona_id is None):
        st.stop()
    st.session_state.persona_id = persona_id
    st.rerun()


if (st.session_state.persona_id != 0):
    pid = st.session_state.persona_id
else:
    pid = personas[0].id

persona = repo.get_persona_by_id(pid)


with st.form(key="persona_form"):
    title = st.text_input("Title", value=persona.title)
    text = st.text_area("Text", value=persona.text, height=200)
    col1, col2, col3, col4, col5 = st.columns(5)
    save = col3.form_submit_button("💾")
    new = col1.form_submit_button("➕")
    delete = col2.form_submit_button("🗑️")
    cancel = col4.form_submit_button("✖️")
    save_and_close = col5.form_submit_button("✔️")

if save:
    repo.save_persona(pid, text, title)
    st.success("Saved")

if new:
    st.session_state.persona_id = repo.add_persona_for_main_person("").id
    st.success("Added")
    st.rerun()


if delete or st.session_state.deleting :
    #'Delete Persona'
    st.session_state.deleting = True
    # st.session_state.confirm_delete
    if (st.session_state.confirm_delete is None):
        #'Confirm Delete'
        confirm_delete(persona)
        st.stop()
    
    if st.session_state.confirm_delete:
        #'Now we can delete the persona'
        repo.delete_persona(pid)
        st.session_state.confirm_delete = None
        st.success("Deleted")
        st.session_state.persona_id = 0
        st.session_state.deleting = False
        st.rerun()
    else: 
        #'Cancel Delete'
        st.session_state.confirm_delete = None
        st.session_state.deleting = False



if cancel:
    st.session_state.persona_id = 0
    st.rerun()

if save_and_close: 
    repo.save_persona(pid, text, title)
    st.session_state.persona_id = 0
    st.rerun()






