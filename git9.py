import os
import streamlit as st
from git import Repo

# Set the title of the Streamlit app
st.title("Git9 Home")

# Function to list repositories
def list_repositories():
    return [d for d in os.listdir('.') if os.path.isdir(d) and os.path.exists(os.path.join(d, '.git'))]

# Function to set the Git remote URL
def set_git_remote(repo_path, remote_url):
    repo = Repo(repo_path)
    if "origin" in repo.remotes:
        repo.delete_remote("origin")
    repo.create_remote("origin", remote_url)

# Display existing repositories
st.header("Repositories")
repos = list_repositories()
if repos:
    for repo in repos:
        st.write(repo)
        vscode_url = f"https://vscode.dev/{os.path.abspath(repo)}"
        st.markdown(f"[Edit in VSCode]({vscode_url})")
        set_git_remote(repo, "https://git9website.streamlit.app")
else:
    st.write("No repositories found.")

# Form to create a new repository
st.header("Create a New Repository")
with st.form("create_repo_form"):
    repo_name = st.text_input("Repository Name", "")
    submitted = st.form_submit_button("Create")
    if submitted and repo_name:
        os.makedirs(repo_name, exist_ok=True)
        new_repo = Repo.init(repo_name)
        set_git_remote(repo_name, "https://git9website.streamlit.app")
        st.success(f"Repository '{repo_name}' created successfully.")
        repos = list_repositories()

# Rerun to update the list of repositories after creation
if submitted and repo_name:
    st.experimental_rerun()
