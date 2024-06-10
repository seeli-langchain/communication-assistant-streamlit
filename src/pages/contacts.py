import streamlit as st
import persisting as repo

if "contact_id" not in st.session_state:
    st.session_state.contact_id = 0

st.title("Contacts")

pid = 0
contacts = repo.get_contacts()

if contacts is None or len(contacts) == 0:
    st.warning("No contacts found")
    if st.button("Add Contact"):
        st.session_state.contact_idrepo.create_contact(first_name="First Name", last_name="Last Name").id
        st.success("Added")
        st.experimental_rerun()
else:
    if (st.session_state.contact_id != 0):
        pid = st.session_state.contact_id
    else:
        pid = contacts[0].id

    idx = 0
    for (index, contact) in enumerate(contacts):
        if (contact.id == pid):
            idx = index

    contact_id = st.selectbox("Select Persona to edit", [contact.id for contact in contacts], 
                            format_func=lambda x: repo.get_person_by_id(x).__repr__(), index=idx)

    st.session_state.contact_id = contact_id
    contact = repo.get_person_by_id(contact_id)

    first_name = st.text_input("First Name", value=contact.first_name)
    last_name = st.text_input("Last Name", value=contact.last_name)

    text = st.text_area("Text", value=contact.text, height=300)


    col1, col2, col3 = st.columns(3)

    if col1.button("Save Contact"):
        repo.save_person(contact_id, first_name=first_name, last_name=last_name, text=text)
        st.success("Saved")
        st.experimental_rerun()

    if col2.button("New Contact"):
        st.session_state.contact_id = repo.create_contact(first_name="First Name", last_name="Last Name").id
        st.success("Added")
        st.experimental_rerun()

    if (contact_id):
        if col3.button("Delete Contact"):
            repo.delete_person(person_id)
            st.success("Deleted")
            st.session_state.contact_id = 0
            st.experimental_rerun()
