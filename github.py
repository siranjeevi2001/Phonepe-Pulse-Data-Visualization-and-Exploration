import git

repository_url='https://github.com/phonepe/pulse.git'

destination_data= r"test"
git.Repo.clone_from(repository_url,destination_data)

