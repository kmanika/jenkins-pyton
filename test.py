for_each   = {
for ecr-key, ecr-value in var.ecr_repos_list :
ecr-key => ecr-value
if lookup(ecr-value, "attach_ecr_repo_policy", false) }