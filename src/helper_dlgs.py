import streamlit as st
import persisting as repo

@st.experimental_dialog("Confirm Delete")
def confirm_delete(item):
    st.write(f"Are you sure you want to delete {item}?")
    c1, c2 = st.columns(2)
    if c1.button("✖️"):
       st.session_state.confirm_delete = False
       st.rerun()
       
    if c2.button("✔️"):
       st.session_state.confirm_delete = True
       st.rerun()

def manage_state():
   if "id" not in st.session_state or st.session_state.id is None:
      st.session_state.id = 0
   if "confirm_delete" not in st.session_state :
      st.session_state.confirm_delete = None
   if "deleting" not in st.session_state :
      st.session_state.deleting = False

   if st.session_state.deleting == False:
      st.session_state.confirm_delete = None

def add_buttons():
    col1, col2, col3, col4, col5 = st.columns(5)
    save = col3.form_submit_button("💾")
    new = col1.form_submit_button("➕")
    delete = col2.form_submit_button("🗑️")
    cancel = col4.form_submit_button("✖️")
    save_and_close = col5.form_submit_button("✔️")
    return save, new, delete, cancel, save_and_close

def do_cancel():
    print("do cancel")
    st.session_state.id = 0
    st.rerun()

def do_new(repo_class):
    st.session_state.id = repo_class.add_func().id
    st.rerun()

def handle_buttons(buttons, repo):
   if buttons[0]:   # new
      repo.save()

   if buttons[1]:   # new
      do_new(repo.__class__)

   if buttons[2] or st.session_state.deleting:   # delete
      st.session_state.deleting = True

      if (st.session_state.confirm_delete is None):
         confirm_delete(repo.item)
         st.stop()
   
      if st.session_state.confirm_delete:
         repo.__class__.delete_func(st.session_state.id)
         st.session_state.confirm_delete = None
         st.session_state.id = 0
         st.session_state.deleting = False
         st.rerun()
      else: 
         st.session_state.confirm_delete = None
         st.session_state.deleting = False

   if buttons[3]:  # cancel
      print("cancel")
      do_cancel()
      
   if buttons[4]:  # save and close
      repo.save()
      do_cancel()

def handle_no_items(repo_class):
    st.warning("No items found")
    if st.button("➕"):
        do_new(repo_class)
    st.stop()

def select_item_to_edit(repo_class):
      items = repo_class.read_all_func()

      if len(items) == 0 or items is None:
         handle_no_items(repo_class)
         st.stop()
         
      if (st.session_state.id == 0 and len(items) > 1):
         st.session_state.id = st.selectbox("", [item.id for item in items], 
                           format_func=lambda x: repo_class.read_one_func(x), index=None, 
                           placeholder="Select an Item to edit", label_visibility="collapsed")
         add = st.button("➕")
         if add:
               do_new(repo_class)
         
         if (st.session_state.id is None):
               st.stop()
   
         st.rerun()
   
      if (st.session_state.id == 0):
         st.session_state.id = items[0].id
   
      return repo_class.read_one_func(st.session_state.id)