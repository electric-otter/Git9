import os
import streamlit as st
from git import Repo

# Set the title of the Streamlit app
st.title("Git9 Home")

# Function to list repositories
def list_repositories():
    return [d for d in os.listdir('.') if os.path.isdir(d) and os.path.exists(os.path.join(d, '.git'))]

# Display existing repositories
st.header("Repositories")
repos = list_repositories()
if repos:
    for repo in repos:
        st.write(repo)
else:
    st.write("No repositories found.")

# Form to create a new repository
st.header("Create a New Repository")
with st.form("create_repo_form"):
    repo_name = st.text_input("Repository Name", "")
    submitted = st.form_submit_button("Create")
    if submitted and repo_name:
        os.makedirs(repo_name, exist_ok=True)
        Repo.init(repo_name)
        st.success(f"Repository '{repo_name}' created successfully.")
        repos = list_repositories()

# Rerun to update the list of repositories after creation
if submitted and repo_name:
    st.experimental_rerun()
