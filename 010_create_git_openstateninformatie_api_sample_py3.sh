# Filenaam: 010_create_git_openstateninformatie_api_sample_py3.sh
# Functie: create centrale remote git repository van de commandline
#          tbv script mbt python3 script tbv ophalen van Open Raads en Staten informatie obv een API sample
#
# Opmerking: 

# Tbv Ubuntu
# curl -u 'cx1964@gmail.com' https://api.github.com/user/repos -d '{"name":"openstateninformatie_api_sample_py3"}'

# tbv mingw64 onder windows
# letop vul voor <PASSWORD> een password waarde in
curl -d '{"name":"openstateninformatie_api_sample_py3"}' -u cx1964@gmail.com:<PASSWORD> https://api.github.com/user/repos

# maak een lege repository
git init

# Voeg readme.md toe onder versie beheer plaats het in staging
# Iedere keer als men een file wilt committen, moet het eerst met add in staging gezet worden
# ook voor files die al een keer zijn gecommit.
git add readme.md
git add .gitignore

# set de identity
git config --global user.email "cx1964@gmail.com"
git config --global user.name "cx1964"

# commit de file
git commit readme.md -m "Commit de readme.md file"

# maak wat voorbeeld sources files
git add *.sh
git commit *.sh -m "Commit de shell script sources files"


# Voeg een remote repository toe
git remote add origin https://github.com/cx1964/openstateninformatie_api_sample_py3.git

# Schrijf de  wijzgingen van local repository naar master branch van de remote repository
# Gebruik username cx1964@gmail.com
git push -u origin master
