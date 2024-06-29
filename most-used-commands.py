# key 'q' to abort
print("Hello git!\n");
# git -h
# git --help
print("Configuracion global de git en el equipo local");
# git config --global user.name "Juan"
# git config --global user.email "juanjosecavila@gmail.com"
print("Cambio de nombre opcional de la rama master a main")
# git config --global init.defaultBranch main 
print("Commandos por default con alias");
# git config --global alias.tree "log --graph --decorate --all --oneline"
# git tree

print("Crear carpeta .git en carpeta del proyecto");
# git init
print("Renombrar la rama si se desea")
# git branch -m main
print("Con las excepciones en la carpeta .gitignore");
# **/ignored.txt

print("Ver el estado actual del git para modificar");
# git status
print("Ver el historial del git para modificar");
# git log
# git log --graph
# git log --graph --pretty=oneline
# git log --graph --decorate --all --oneline
# git reflog
print("Ver diferencias o cambios especificos");
#git diff

print("Añadir fichero o todos los ficheros");
# git add hellogit2.py
# git add .
print("Captura de version");
# git commit -m "Version"
# GIT_COMMITTER_DATE="<DATE>" git commit -m "Version" --date="<DATE>"

print("Regresar a version capturada");
# git checkout
# git checkout hellogit2.py
# git checkout HEAD
print("Nombrar capturas")
# git tag DIA_1

print("Crear rama, eliminar y cambiar rama");
# git branch login
# git branch -d login
# git switch login
print("Fusionar la rama");
# git merge login

print("Hacer borrador, ver la lista, recuperar y eliminar");
# git stash
# git stash list
# git stash pop
# git stash drop

print("Github");
# git remote add origin https://github.com/juanjosecavila/git-course.git
# git push -u origin main
