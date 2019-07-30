import twint

searchParameters = twint.Config()

# referTo: https://github.com/twintproject/twint/wiki/Module)

searchParameters.Username = ""
searchParameters.Output = "../dumps/" + searchParameters.Username
searchParameters.Stats = True
searchParameters.Store_csv = True
searchParameters.User_full = True
searchLog = ""

print("Running search...")

twint.run.Search(searchParameters)

print("Search finished.")
